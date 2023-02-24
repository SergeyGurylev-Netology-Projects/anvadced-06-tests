import requests
from config import ya_token


class YaUploader:
    def __init__(self, token: str):
        self.base_host = 'https://cloud-api.yandex.net:443/'
        self.base_headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'}

    def create_folder(self, upload_folder):
        url = self.base_host + 'v1/disk/resources'
        params = {'path': upload_folder}
        response = requests.put(url, params=params, headers=self.base_headers)
        return response


if __name__ == '__main__':
    pass
