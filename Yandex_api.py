import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def create_folder(self, path):
        create_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": f'{path}'}
        request_code = requests.put(create_url, headers=headers, params=params).status_code
        return request_code


if __name__ == '__main__':
    ya_token = ...
    uploader = YaUploader(ya_token)
    print(uploader.create_folder('testing'))