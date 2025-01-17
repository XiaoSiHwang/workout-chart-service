import uvicorn

from fastapi import FastAPI

from api.v1 import poster
app = FastAPI(title="workout-chart-service",
              description="workout-chart-service",
              version="v1.0.0")
app.include_router(poster.router)


# if __name__ == '__main__':
#     uvicorn.run('main:app')