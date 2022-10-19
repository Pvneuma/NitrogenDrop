import httpx
import sys
from config import Config

config = Config()
base_url = config.get('base_url')


def upload_file(file_path):
    with open(file_path, 'rb') as f:
        files = {'file': f}
        res = httpx.post(base_url, files=files)
        print(res.json())


if __name__ == '__main__':
    file_path = sys.argv[1]
    upload_file(file_path)
