from google.oauth2 import service_account
from googleapiclient import discovery


class Gsheets:
    def __init__(self, settings):
        self.sheet_id = settings['sheet_id']

        credentials = service_account.Credentials.from_service_account_info(settings['auth_params']) \
            .with_scopes(['https://www.googleapis.com/auth/spreadsheets'])
        self.service = discovery.build('sheets', 'v4', credentials=credentials)

    def append(self, sheet_range, rows):
        body = {
            'range': sheet_range,
            'majorDimension': 'ROWS',
            'values': [rows],
        }
        self.service.spreadsheets().values().append(
            spreadsheetId=self.sheet_id, range=sheet_range, body=body, valueInputOption='USER_ENTERED'
        ).execute()
