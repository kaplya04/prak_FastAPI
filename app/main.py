from typing import Union
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.model.schemas import ComicsCreate

app = FastAPI()

comics = []
publishings = []
personajs = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create
app.post('/comics')


async def create_comics(comics: ComicsCreate):
    comics.append(comics)
    return {'massage': 'Ваш комикс создан'}


# receiving
@app.get("/comics/")
async def get_comics():
    return {"comics": comics}


# receiving id
@app.get("/comics/{comics_id}")
async def git_comics(comics_id: int):
    if comics_id < len(comics):
        return {"comics": comics[comics_id]}
    else:
        return {"error": "Комикс не найден"}


# delete
@app.delete("/comics/{comics_id}")
async def delete_comics(comics_id: int):
    if comics_id < len(comics):
        comics.pop(comics_id)
        return {"message": "Комикс удалён"}
    else:
        return {"error": "Комикс не найден"}
