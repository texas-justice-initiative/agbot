import requests

BASE_URL = 'https://www.documentcloud.org/api'


class DocumentCloud:
    def __init__(self, settings):
        self.auth = (settings['email'], settings['password'])

    def upload(self, title, file_url, project_id, source=None, access='public'):
        """
        Uploads a new document to DocumentCloud.

        Run list_projects() to get the project ids.

        :param str title: Name of the document
        :param str file_url: URL where the file will be downloaded from
        :param str project_id: Project to upload the document to
        :param str source: Source of the document (optional)
        :param str access: Visibility of the document (default='public')
        """
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
        """
        Lists the projects owned.

        :return: A list of dictionaries with the keys: (id, title)
        """
        url = f'{BASE_URL}/projects.json'

        r = requests.get(url, auth=self.auth)
        if r.status_code != 200:
            print(f'Failed to list the projects owned')
            r.raise_for_status()

        return [{'id': p['id'], 'title': p['title']} for p in r.json()['projects']]
