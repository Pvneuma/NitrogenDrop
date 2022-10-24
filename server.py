import uvicorn
import socket
from fastapi import FastAPI, UploadFile
from config import Config

app = FastAPI()
config = Config()


@app.post("/")
async def download(file: UploadFile):

    def file_iterator():
        size = eval(config.get('size'))
        return file.file.read(size)

    with open(f"{config.get('directory')}{file.filename}", 'wb') as f:
        for i in iter(file_iterator, b''):
            f.write(i)
    await file.close()
    return f'Uploaded successfully: {file.filename}'


def get_host_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))  # 114.114.114.114也是dns地址
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


if __name__ == '__main__':
    SERVER = config.get('server')
    print("IP: "+get_host_ip())
    uvicorn.run(
        app="server:app",
        host=SERVER['host'],
        port=SERVER['port'],
        workers=SERVER['workers'],
        reload=False
    )
