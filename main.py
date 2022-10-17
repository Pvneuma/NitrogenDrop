import uvicorn
from config import Config

if __name__ == '__main__':
    SERVER = Config().get('server')
    uvicorn.run(
        app="server:app",
        host=SERVER['host'],
        port=SERVER['port'],
        workers=SERVER['workers'],
        reload=False
    )
