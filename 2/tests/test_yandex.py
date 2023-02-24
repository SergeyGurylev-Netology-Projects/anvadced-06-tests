import requests
from config import ya_token
from unittest import TestCase
from main import YaUploader


class TestYaUploader(TestCase):
    def setUp(self):
        self.uploader = YaUploader(ya_token)
        self.url = self.uploader.base_host + 'v1/disk/resources'
        self.headers = self.uploader.base_headers

    def test_create_folder(self):
        folder_name = '__test_folder__'
        params = {'path': folder_name}

        result = self.uploader.create_folder(folder_name)
        self.assertEqual(result.status_code, 201, result.reason)

        response = requests.get(self.url, params=params, headers=self.headers)
        self.assertEqual(response.status_code, 200, response.reason)

        requests.delete(self.url, params=params, headers=self.headers)
