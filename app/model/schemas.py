from datetime import date
from typing import List

from pydantic import BaseModel


class ComicsCreate(BaseModel):
    name: str
    after: str
    year: str


class PublishingsCreate(BaseModel):
    name: str


class GenresCreate(BaseModel):
    name: str


class SeriesCreate(BaseModel):
    name: str


class PersonajsCreate(BaseModel):
    name: str


class Comicsq(BaseModel):
    id: int
    name: str
    after: str
    year: str


class publishingsq(BaseModel):
    comics: List[Comicsq]
    publishings_id: int