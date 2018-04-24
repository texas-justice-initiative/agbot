import requests


class Gmaps:
    def __init__(self, settings):
        self.api_key = settings['api_key']

    def geocode(self, address):
        url = f'https://maps.googleapis.com/maps/api/geocode/json'

        params = {
            'address': address,
            'key': self.api_key,
        }

        r = requests.get(url, params=params)
        if r.status_code != 200:
            print(f'Failed to geocode {address}')
            r.raise_for_status()

        coordinates = r.json()['results'][0]['geometry']['location']

        return coordinates['lat'], coordinates['lng']
