from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.model.schemas
from app.controllers.crud import get_comic
from app.model.database import get_db

router = APIRouter()


@router.get('/', responses_model=list[app.model.schemas.Comic])
def read_comics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comics = get_comic(db, skip=skip, limit=limit)
    return comics
