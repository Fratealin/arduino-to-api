# Gets data from Arduino and sends it to Adafruit Api

import serial
import adafruit_api
import time

adafruit_api_manager = adafruit_api.AdafruitApi()
arduino_serial_data = serial.Serial('/dev/ttyACM0', baudrate = 9600, timeout = 1)

while True:

    if arduino_serial_data.in_waiting > 0:
        myData = arduino_serial_data.readline()
        light = float(myData.decode().rstrip())
        adafruit_api_manager.send_data(light)
        time.sleep(10)
