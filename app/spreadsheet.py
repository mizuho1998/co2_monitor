from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class Spreadsheet:
    def __init__(self):
        # If modifying these scopes, delete the file token.pickle.
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        cur_dir = os.path.dirname(__file__)
        self.token_path = os.environ.get("TOKEN_PATH") 
        self.token_path = os.path.join(cur_dir, self.token_path) 
        self.credentials_path = os.environ.get("CREDENTIALS_PATH")  
        self.credentials_path = os.path.join(cur_dir, self.credentials_path) 
        self.spreadsheet_id = os.environ.get("SPREADSHEET_ID") 

        self.service = self.Auth()


    def Auth(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(self.token_path):
            with open(self.token_path, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_path, self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.token_path, 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)

        return service


    def getValue(self, range_):
        """
        sample:
        range_ = 'Sheet1!A1:B5'

        """

        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.spreadsheet_id,
                                    range=range_).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')


    def appendValue(self, values, range_='Sheet1!A1'):
        value_input_option = 'RAW' 
        insert_data_option = 'INSERT_ROWS'
        value_range_body = {
            # "range": '',
            "majorDimension": "ROWS",
            "values": values
            }

        request = self.service.spreadsheets().values().append(spreadsheetId=self.spreadsheet_id, 
                range=range_, 
                valueInputOption=value_input_option, 
                insertDataOption=insert_data_option, 
                body=value_range_body)
        response = request.execute()

        if not response:
            print('No data found.')


if __name__ == '__main__':
    # test
    spreadsheet = Spreadsheet()
    spreadsheet.getValue('Sheet1!A2:B6')
    spreadsheet.appendValue([[33,44], [55,66], [77,77]])


