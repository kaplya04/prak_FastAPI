from datetime import date
from typing import List

from pydantic import BaseModel


class ComicsShemas(BaseModel):
    name: str
    autor: str
    year: str
    image: str


class PublishingsShemas(BaseModel):
    name: str


class PersonajsShemas(BaseModel):
    name: str


class CategoryShemas(BaseModel):
    categories: str
