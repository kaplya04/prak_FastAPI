from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.model.core import *
from app.model.database import db

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/comics')
def create_comics():
    comics = db.query(Comics).all()
    return comics

@app.get('/personaj')
def create_personaj():
    personaj = db.query(Personajs).all()
    return personaj
