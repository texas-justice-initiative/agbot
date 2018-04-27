import requests

BASE_URL = 'https://www.documentcloud.org/api'


class DocumentCloud:
    def __init__(self, settings):
        self.auth = (settings['email'], settings['password'])

    # 'project_id' can be gotten by running list_projects()
    # 'source' is optional
    def upload(self, title, file_url, project_id, source=None, access='public'):
        url = f'{BASE_URL}/upload.json'

        body = {
            'title': title,
            'file': file_url,
            'project': project_id,
            'access': access,
        }
        if source:
            body['source'] = source

        r = requests.post(url, auth=self.auth, json=body)
        if r.status_code != 200:
            print(f'Failed to upload {file_url}')
            r.raise_for_status()

    def list_projects(self):
        url = f'{BASE_URL}/projects.json'

        r = requests.get(url, auth=self.auth)
        if r.status_code != 200:
            print(f'Failed to list the projects owned')
            r.raise_for_status()

        return [{'id': p['id'], 'title': p['title']} for p in r.json()['projects']]
