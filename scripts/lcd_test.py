import time
import logging
from glob import glob
import cv2

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

try:
    # display with hardware SPI:
    ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
    disp = LCD_2inch.LCD_2inch()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()
    #Set the backlight to 100
    disp.bl_DutyCycle(50)

    # load image paths
    img_paths = glob("../pics/xmas/*.jpg")
    img_paths.sort()
    while True:
        for img_path in img_paths:
            img = cv2.imread(img_path)
            disp.ShowImageCV(img, rot_ang=90)
            time.sleep(5)
except IOError as e:
    logging.info(e)
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()