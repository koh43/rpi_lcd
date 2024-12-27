import time
import logging
import cv2
from picamera2 import Picamera2, MappedArray
import traceback

import sys
sys.path.append("..")
from lcd import LCD_2inch

# Raspberry Pi pin configuration:
RST = 13
DC = 22
BL = 12
bus = 0
device = 0
logging.basicConfig(level=logging.DEBUG)

# for writing fps
font = cv2.FONT_HERSHEY_SIMPLEX
prev_ts = 0
cur_ts = 0
fps = 0
frame_duration = 1e6/60

# display with hardware SPI:
disp = LCD_2inch.LCD_2inch()
# Initialize library.
disp.Init()
# Clear display.
disp.clear()
#Set the backlight to 100
disp.bl_DutyCycle(50)

def draw_fps(request):
    with MappedArray(request, 'main') as m:
        cv2.putText(m.array, f"Expected FPS: {1e6/frame_duration:02f}", (10, 30), font, 0.5, (100, 255, 0), 1, cv2.LINE_AA)
        cv2.putText(m.array, f"Current FPS: {fps:02f}", (10, 60), font, 0.5, (100, 255, 0), 1, cv2.LINE_AA)
        disp.ShowImageCV(m.array)

try:
    # You can check the initial camera settings by
    # rpicam-hello --list-cameras -v
    # Connect to camera
    cap = Picamera2()
    cap.set_logging(Picamera2.INFO)
    cap.configure(
        cap.create_preview_configuration(
            main={
                "format": "RGB888",
                "size": (320, 240)
            }
        )
    )
    cap.set_controls({
        "FrameRate": 60,
        "AeEnable": True,
    })
    cap.pre_callback = draw_fps
    cap.start()
    prev_ts = cap.capture_metadata()["SensorTimestamp"]
    frame_duration = cap.capture_metadata()["FrameDuration"]

    # load image paths
    while True:
        cur_ts = cap.capture_metadata()["SensorTimestamp"]
        fps = 1e9/(cur_ts - prev_ts)
        prev_ts = cur_ts

except:
    disp.module_exit()
    logging.info("quit:")
    traceback.print_exc()
    exit()