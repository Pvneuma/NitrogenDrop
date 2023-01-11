import mimetypes
import sys
import requests
import typing
from config import Config
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from pathlib import Path
from rich.progress import Progress, TaskProgressColumn, BarColumn, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn, TextColumn, SpinnerColumn

config = Config()
base_url = config.get('base_url')


def create_callback(progress: Progress, task):

    def callback(monitor):
        progress.update(task, completed=monitor.bytes_read)

    return callback


def guess_content_type(filename: typing.Optional[str]) -> typing.Optional[str]:
    if filename:
        return mimetypes.guess_type(filename)[0] or "application/octet-stream"
    return None


def get_file_name(file):
    return Path(str(getattr(file, "name", "upload"))).name


def upload_file(file_path: str):
    with open(file_path, 'rb') as f:
        file_name = get_file_name(f)
        data = MultipartEncoder(
            fields={'file': (file_name, f, guess_content_type(file_name))})
        with Progress(
            TaskProgressColumn(),
            BarColumn(),
            DownloadColumn(),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
        ) as progress:
            upload_task = progress.add_task("Upload", total=data.len)
            callback = create_callback(progress, upload_task)
            monitor = MultipartEncoderMonitor(data, callback)
            try:
                res = requests.post(base_url, data=monitor,
                                    headers={'Content-Type': monitor.content_type})
                print(res.json())
            except requests.exceptions.ConnectionError:
                print('Connection Error')


if __name__ == '__main__':
    file_path = sys.argv[1]
    upload_file(file_path)
