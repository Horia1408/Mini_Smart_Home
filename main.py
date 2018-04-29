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

#loop
while True:
    if button_read() == 1:
        show_temp(1)
        turn_off_led()
    if button_read() == 2:
        show_humidity(1)
        turn_off_led()
    if button_read() == 3:
        show_temp(2)
    if button_read() == 4:
        show_humidity(2)
    if read_water() == True:
        turn_on_led()
    else:
        turn_off_led()
    time.sleep(0.2)