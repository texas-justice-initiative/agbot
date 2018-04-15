import requests

BASE_URL = 'https://sheets.googleapis.com/v4'


class Gsheets:
    def __init__(self, settings):
        self.api_key = settings['api_key']

    def fetch(self, sheet_id, sheet_range):
        url = f'{BASE_URL}/spreadsheets/{sheet_id}/values/{sheet_range}?key={self.api_key}&majorDimension=COLUMNS'

        r = requests.get(url)

        if r.status_code == 200:
            return r.json()['values']
        else:
            print(f'Failed to fetch from Google Sheets: Error {r.status}')
            r.raise_for_status()
