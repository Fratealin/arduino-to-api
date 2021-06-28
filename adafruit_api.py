# Uploads data to Adafruit AdafruitApi
# Limit is 30 uploads a minute


import json
#pip3 install adafruit-io
from Adafruit_IO import Client, Feed

class AdafruitApi():
    def __init__(self):

        with open('config.json') as json_file:
            data = json.load(json_file)
            # (go to https://accounts.adafruit.com to find your username)
            ADAFRUIT_IO_USERNAME = data['ADAFRUIT_IO_USERNAME']
            ADAFRUIT_IO_KEY = data['ADAFRUIT_IO_KEY']
            self.feed_name = 'light-data'

            # Create an instance of the Adafruit IO Client and set up the feed we created earlier.
            self.aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

    def send_data(self, this_data):
        self.aio.send(self.feed_name, this_data)
        print("data sent to adafruit")
    
if __name__ == '__main__':
    adafruit_api_manager = AdafruitApi()
    adafruit_api_manager.send_data(50)
