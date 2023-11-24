from typing import Union
from fastapi import FastAPI

from app.model import core
from model.database import engine
from routers.router import router as comic_router

core.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router=comic_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
