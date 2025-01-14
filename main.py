import uvicorn

from fastapi import FastAPI

from api.v1 import poster

app = FastAPI()
app.include_router(poster.router)


if __name__ == '__main__':
    uvicorn.run('main:app')