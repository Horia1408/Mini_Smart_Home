import sys
sys.path.insert(0, '/var/fpwork/hcostina/proiect/trunk/lcdPrint/')
sys.path.insert(0, '/var/fpwork/hcostina/proiect/trunk/temperature/')
import I2C_LCD_driver
import dht11
from time import *
import RPi.GPIO as GPIO
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.IN)

# init libs
instance_of_temp = dht11.DHT11(pin=14)
mylcd = I2C_LCD_driver.lcd()
positionY = 0
positionX = 0
mesajePosition = 0
inundatiiFlag = 0
doNothing = 0
#functions

def button_read():
    input_state_dreapta = GPIO.input(17)
    if input_state_dreapta == True:
        return 1
    input_state_jos = GPIO.input(27)
    if input_state_jos == True:
        return 2
    input_state_sus = GPIO.input(22)
    if input_state_sus == True:
        return 3
    input_state_stanga = GPIO.input(10)
    if input_state_stanga == True:
        return 4
    return 0

def read_water():
    return GPIO.input(11)

def turn_on_led():
    GPIO.output(9,GPIO.HIGH)

def turn_off_led():
    GPIO.output(9,GPIO.LOW)

def show_temp(pos):
    result_temp = instance_of_temp.read()
    if result_temp.is_valid():
        mylcd.lcd_display_string("Temperatura " + str(result_temp.temperature) + "C", pos)

def show_humidity(pos):
    result_temp = instance_of_temp.read()
    if result_temp.is_valid():
        mylcd.lcd_display_string("Umiditate   " + str(result_temp.humidity) + "%", pos)

def displayThis(posx, posy, prior):
    global mesajePosition
    if prior == 0 and posx == 0:
        if posy == 0:
            mylcd.lcd_display_string("Mesaje          ", 2)
        if posy == 1:
            mylcd.lcd_display_string("Control         ", 2)
        if posy == 2:
            show_temp(2)
        if posy == 3:
            mylcd.lcd_display_string("Inundatii       ", 2)
    if prior == 1 and posx == 0:
        if posy == 0:
            mylcd.lcd_display_string("Mesaje         <", 1)
        if posy == 1:
            mylcd.lcd_display_string("Control        <", 1)
        if posy == 2:
            show_temp(1)
        if posy == 3:
            mylcd.lcd_display_string("Inundatii      <", 1)
    if prior == 2 and posx == 1:
        f = open("mesaje.txt" , "r")
        lines = f.readlines()
        if len(lines) > mesajePosition:
            mylcd.lcd_display_string(lines[mesajePosition][:-1] + "                ", 1)
        if len(lines) > (mesajePosition +1):
            mylcd.lcd_display_string(lines[mesajePosition + 1][:-1] + "                ", 2)
        else:
            mylcd.lcd_display_string("                ", 2)
        if len(lines) <= mesajePosition:
            mesajePosition = -1
        f.close()

def select_to_display(posx, posy):
    if posy == 0 and posx == 0:
        displayThis(0, 0, 1)
        displayThis(0, 1, 0)
    if posy == 1 and posx == 0:
        displayThis(0, 1, 1)
        displayThis(0, 2, 0)
    if posy == 2 and posx == 0:
        displayThis(0, 2, 1)
        displayThis(0, 3, 0)
    if posy == 3 and posx == 0:
        displayThis(0, 3, 1)
        displayThis(0, 0, 0)

    if posy == 0 and posx == 1:
        displayThis(1, 0, 2)

#loop
while True:
    if button_read() == 1:
        if positionX == 0:
            positionY += 1
        if positionX == 1 and positionY == 0:
            mesajePosition += 1
    if button_read() == 2:
        positionX += 1
    if button_read() == 3:
        positionX -= 1
    if button_read() == 4:
        if positionX == 0:
            positionY -= 1
        if positionX == 1 and positionY == 0:
            mesajePosition -= 1
    if read_water() == True:
        turn_on_led()
        if inundatiiFlag == 0:
            now = datetime.datetime.now()
            takeTime = '{:%d/%m/%y %H:%M:%S}'.format(now)
            fr = open("inundatii.txt", "r+")
            for line in fr.readlines():
                doNothing = 0;
            fr.write(takeTime + "\n")
            fr.close()
            inundatiiFlag = 1;
    else:
        turn_off_led()
        inundatiiFlag = 0;
    if positionY > 3:
        positionY = 0
    if positionY < 0:
        positionY = 3

    if positionX < 0:
        positionX = 0
    if positionX > 1:
        positionX = 1

    if mesajePosition < 0:
        mesajePosition = 0
    select_to_display(positionX ,positionY)

    time.sleep(0.2)
