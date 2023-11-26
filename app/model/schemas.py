from datetime import date
from typing import List

from pydantic import BaseModel


class ComicsShemas(BaseModel):
    name: str
    after: str
    year: str


class PublishingsShemas(BaseModel):
    name: str


class GenresShemas(BaseModel):
    name: str


class SeriesShemas(BaseModel):
    name: str


class PersonajsShemas(BaseModel):
    name: str


class CategoryShemas(BaseModel):
    categories: str
