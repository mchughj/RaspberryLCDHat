# RaspberryLCDHat

![Picture of LCD on top of the PI](/Lcd-On-Pi.jpg)

This is a simple repository to get the Waveshare 1.44 inch LCD Hat working.

## Configure device

After seating the LCD hat onto the Raspberry PI you need to ensure that the PI is setup to support SPI.

   sudo raspi-config
   Choose Interfacing Options -> SPI -> Yes  to enable SPI interface
   sudo reboot

Next you need to install the BCM2835 libraries.

   wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.68.tar.gz
   tar zxvf bcm2835-1.68.tar.gz 
   cd bcm2835-1.68/
   sudo ./configure && sudo make && sudo make check && sudo make install
   cd ..

## Sample program

This repo contains a python library, originally part of a larger distribution from Waveshare specific to this device.  That larger zip file can be found here:  https://www.waveshare.com/w/upload/f/fa/1.44inch-LCD-HAT-Code.7z.  Note that the examples in that zip will not compile without modifications.  It was written for a much older version of things.

Try the simple python program here.  

sudo python showIP.py

