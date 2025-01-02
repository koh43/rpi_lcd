# Raspberry Pi Waveshare 2-inch LCD (320x240)

## Before you start...
The LCD module best works with **32-bit** Bullseye Raspberry Pi OS!

## Official Docs (Not recommended)
[Waveshare 2inch LCD Module](https://www.waveshare.com/wiki/2inch_LCD_Module#FBCP_Porting)

## FBCP (Recommended)
The original repository has a nice documentation and it is available at:
[fbcp-ili9341](https://github.com/juj/fbcp-ili9341)

### Required Modifications

Please follow this [modification](https://github.com/juj/fbcp-ili9341/issues/248#issuecomment-982675699) so Pi can access the LCD module.

Here are the CMake options I used for my Raspberry Pi 3B+:
```
cmake -DST7789VW=ON \
-DGPIO_TFT_DATA_CONTROL=25 \
-DGPIO_TFT_RESET_PIN=27 \
-DGPIO_TFT_BACKLIGHT=18 \
-DSPI_BUS_CLOCK_DIVISOR=20 \
-DARMV8A=ON \
-DBACKLIGHT_CONTROL=ON \
-DSTATISTICS=0 ..
```

The details of all CMake options are described at: [fbcp-ili9341](https://github.com/juj/fbcp-ili9341)
