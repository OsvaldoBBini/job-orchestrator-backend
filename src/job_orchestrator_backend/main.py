from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}