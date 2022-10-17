import uvicorn
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


if __name__ == '__main__':
    SERVER = config.get('server')
    uvicorn.run(
        app="server:app",
        host=SERVER['host'],
        port=SERVER['port'],
        workers=SERVER['workers'],
        reload=False
    )
