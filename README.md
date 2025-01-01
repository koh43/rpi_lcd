# Raspberry Pi Waveshare 2-inch LCD

## Before you start...
The LCD module best works with **32-bit** Raspberry Pi OS!
For Bookworm OS, install the following
```
sudo apt-get install libraspberrypi-dev
```

## Official Docs
[Waveshare 2inch LCD Module](https://www.waveshare.com/wiki/2inch_LCD_Module#FBCP_Porting)

## FBCP
The code and nice documentation are available at:
[fbcp-ili9341](https://github.com/juj/fbcp-ili9341)

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
