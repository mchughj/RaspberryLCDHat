import LCD_1in44
import LCD_Config

import RPi.GPIO as GPIO
import socket
from PIL import Image,ImageDraw,ImageFont,ImageColor

def getLocalIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # Doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        result = s.getsockname()[0]
    except Exception:
        result = '127.0.0.1'
    finally:
        s.close()
    return result

localIPAddress = getLocalIP()

KEY_UP_PIN     = 6 
KEY_DOWN_PIN   = 19
KEY_LEFT_PIN   = 5
KEY_RIGHT_PIN  = 26
KEY_PRESS_PIN  = 13
KEY1_PIN       = 21
KEY2_PIN       = 20
KEY3_PIN       = 16

# Init GPIO
GPIO.setmode(GPIO.BCM) 

# Setup all of the keys - including the 'joystick' - to be in pull up mode.
GPIO.setup(KEY_UP_PIN,      GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY_DOWN_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY_LEFT_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY_RIGHT_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY_PRESS_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY1_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY2_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY3_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 240x240 display with hardware SPI:
disp = LCD_1in44.LCD()
Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
disp.LCD_Init(Lcd_ScanDir)
disp.LCD_Clear()

# Create blank image for drawing.
width = 128
height = 128
image = Image.new('RGB', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Create font and put the IP address on the image
print ("Local IP Address: {}".format(localIPAddress))
font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf', 14) 
draw.text((5, 100), str(localIPAddress), font = font, align ="left") 

disp.LCD_ShowImage(image,0,0)

# Forever loop.  This is just here to show you how to handle the 
# keypresses.  You should debounce the key presses and distinguish
# between 'on down' and 'on up' if appropriate.  But it will depend
# on your use case.
while 1:
    # with canvas(device) as draw:
    if GPIO.input(KEY_UP_PIN) == 0: # button is released       
        draw.polygon([(25, 30), (35, 12), (45, 30)], outline=255, fill=0xff00)  #Up        
    else: # button is pressed:
        draw.polygon([(25, 30), (35, 12), (45, 30)], outline=255, fill=0)  #Up filled
        
    if GPIO.input(KEY_LEFT_PIN) == 0: # button is released
        draw.polygon([(5, 40), (23, 31), (23, 51)], outline=255, fill=0xff00)  #left
    else: # button is pressed:       
        draw.polygon([(5, 40), (23, 31), (23, 51)], outline=255, fill=0)  #left filled
        
    if GPIO.input(KEY_RIGHT_PIN) == 0: # button is released
        draw.polygon([(65, 40), (47, 31), (47, 51)], outline=255, fill=0xff00) #right
    else: # button is pressed:
        draw.polygon([(65, 40), (47, 31), (47, 51)], outline=255, fill=0) #right filled       
        
    if GPIO.input(KEY_DOWN_PIN) == 0: # button is released
        draw.polygon([(35, 70), (45, 52), (25, 52)], outline=255, fill=0xff00) #down
    else: # button is pressed:
        draw.polygon([(35, 70), (45, 52), (25, 52)], outline=255, fill=0) #down filled
        
    if GPIO.input(KEY_PRESS_PIN) == 0: # button is released
        draw.rectangle((27, 34,43,48), outline=255, fill=0xff00) #center 
    else: # button is pressed:
        draw.rectangle((27, 34,43,48), outline=255, fill=0) #center filled
        
    if GPIO.input(KEY1_PIN) == 0: # button is released
        draw.ellipse((70,10,90,30), outline=255, fill=0xff00)
    else: # button is pressed:
        draw.ellipse((70,10,90,30), outline=255, fill=0)
        
    if GPIO.input(KEY2_PIN) == 0: # button is released
        draw.ellipse((100,30,120,50), outline=255, fill=0xff00)
    else: # button is pressed:
        draw.ellipse((100,30,120,50), outline=255, fill=0)
        
    if GPIO.input(KEY3_PIN) == 0: # button is released
        draw.ellipse((70,50,90,70), outline=255, fill=0xff00)
    else: # button is pressed:
        draw.ellipse((70,50,90,70), outline=255, fill=0)

    disp.LCD_ShowImage(image,0,0)
