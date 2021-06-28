# Gets data from Arduino and sends it to Google sheets Api
import os
import google_sheets_api
import serial

arduino_serial_data = serial.Serial('/dev/ttyACM0', baudrate = 9600, timeout = 1)

while True:

    if arduino_serial_data.in_waiting > 0:
        myData = arduino_serial_data.readline()
        light = float(myData.decode().rstrip())
        api_object = google_sheets_api.api_class()
        new_data = api_object.get_new_data([light])
        api_object = api_object.append_data(new_data)
