import requests


class DocumentCloud:
    def __init__(self, settings):
        self.username = settings['email']
        self.password = settings['password']

    def upload(self):
        pass
