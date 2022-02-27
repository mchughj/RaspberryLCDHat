# RaspberryLCDHat

![Picture of LCD on top of the PI](/Lcd-On-Pi.jpg)

This is a simple repository to get the [Waveshare 1.44 inch LCD Hat](https://www.waveshare.com/wiki/1.44inch_LCD_HAT) working.

## Configure device

### Enabling SPI
After seating the LCD hat onto the Raspberry PI you need to ensure that the PI is setup to support SPI.  If you are using Raspbian then getting this setup is trivial.  Just follow this:
   ```
   sudo raspi-config
   Choose Interfacing Options -> SPI -> Yes  to enable SPI interface
   sudo reboot
   ```
Otherwise, if you are using Ubuntu for example, then it is a bit more involved.  For Ubuntu, follow this https://askubuntu.com/questions/1273700/enable-spi-and-i2c-on-ubuntu-20-04-raspberry-pi.  

### Install Necessary Libraries
For most Raspberry PI OSes you don't need to install the SPI python libraries.  But in case your installation doesn't have it then use this:
   ```
   sudo apt-get update
   sudo apt-get install python-pip 
   sudo pip install RPi.GPIO
   sudo pip install spidev
   ```

Next you need to install the BCM2835 libraries.
   ```
   wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.68.tar.gz
   tar zxvf bcm2835-1.68.tar.gz 
   cd bcm2835-1.68/
   sudo ./configure && sudo make && sudo make check && sudo make install
   cd ..
   ```
## Sample program

This repo contains a python library, originally part of a larger distribution from Waveshare specific to this device.  That larger zip file can be found here:  https://www.waveshare.com/w/upload/f/fa/1.44inch-LCD-HAT-Code.7z.  Note that the examples in that zip will not compile without modifications.  It was written for a much older version of things.

Try the simple python program here.  
   ```
   sudo python showIP.py
   ```
