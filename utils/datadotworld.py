import requests

BASE_URL = 'https://api.data.world/v0'


class Datadotworld:
    def __init__(self, settings):
        self.api_key = settings['api_key']
        self.dataset_slug = settings['dataset_slug']

    def sync(self):
        url = f'{BASE_URL}/datasets/{self.dataset_slug}/sync'
        headers = {'Authorization': f'Bearer {self.api_key}'}

        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            print(f'Failed to sync {self.dataset_slug}')
            r.raise_for_status()
