# Sends data to Google Sheets Api

from googleapiclient.discovery import build
import os
from google.oauth2 import service_account
from datetime import datetime
import json

class api_class:
    def __init__(self):
        with open('config.json') as json_file:
            data = json.load(json_file)

        self.my_data = [['9','3', '20','312'],['11','4','23','295']]
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        # create and download credential json file from console.cloud.google.com
        self.SERVICE_ACCOUNT_FILE = 'tutorial_keys.json'
        self.pwd = os.getcwd()
        self.filename = os.path.join(self.pwd, "tutorial_keys.json")

        self.creds = None
        self.creds = service_account.Credentials.from_service_account_file(
                self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)

        # The ID and range of a sample spreadsheet.
        # create sheets spreadsheet and share
        # get email address from console.cloud.google.com Service account details
        # get id from url
        self.SPREADSHEET_ID = data["SHEETS_SPREADSHEET_ID"]
        self.RANGE_NAME = 'sensor!A1:D'

        self.service = build('sheets', 'v4', credentials=self.creds)
        # Call the Sheets API
        self.sheet = self.service.spreadsheets()

    def main(self):
        """Shows basic usage of the Sheets API.
        """ 
        self.write_data()
        self.my_data = self.get_new_data("2 2".split(" "))
        self.append_data(self.my_data)

    def read_data(self):
        result = self.sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                    range=self.RANGE_NAME).execute() # in json format
        
        values = result.get('values', []) # list of lists
        return values

    def  write_data(self):
        request = self.sheet.values().update(spreadsheetId=self.SPREADSHEET_ID, 
                                    range='sensor!A5', valueInputOption='USER_ENTERED', body={'values':self.my_data})
        response = request.execute()
        print("finished overwriting data")


    def append_data(self, my_data):
        request = self.sheet.values().append(spreadsheetId=self.SPREADSHEET_ID, 
                                    range='sensor!A5', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={'values':my_data})
        response = request.execute()
        print("finished appending data:")
        print(my_data)

    def get_new_data(self, new_data = "2 2".split(" ")):
        # datetime object containing current date and time
        now = datetime.now()
        # dd-mm-YY H:M:S
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
        new_data.insert(0, dt_string)

        current_data = self.read_data()
        last_id = current_data[-1][0]
        if not last_id:
            this_id = 1
        else: 
            this_id = str(int(last_id)+1)
        new_data.insert(0, this_id) 

        # convert to list of lists as necessary
        my_data = [new_data]
        return  my_data

if __name__ == '__main__':
    api_manager = api_class()
    api_manager.main()
        