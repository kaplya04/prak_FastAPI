from fastapi import APIRouter
from sqlalchemy.orm import joinedload
from app.model.core import Comics, Publishings
from app.model.database import db
from app.model.schemas import ComicsCreate, PublishingsCreate
from fastapi import HTTPException, status

comicsRouter = APIRouter(prefix='',
                         tags=['ComicsContRouter'],
                         responses={404: {'description': 'Not found'}})


@comicsRouter.get("/")
async def get_comics():
    comics = db.query(Comics).all()
    return comics


@comicsRouter.post('/newcomics/', response_model=ComicsCreate)
async def newcomics(comic: ComicsCreate):
    comic = ComicsCreate(
        name=comic.name,
        author=comic.autor,
        year=comic.year
    )
    try:
        db.add(comic)
        db.commit()
    except:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Try again'
        )
    return comic


@comicsRouter.get('/publishings/{publishings_id})/', response_model=PublishingsCreate)
async def comFilms(publishings_id: int):
    pubcomic = db.query(Publishings).join(Comics, Publishings.comics).filter(Publishings.id == publishings_id).one()
    return {'comics': pubcomic.comics, 'publishings_id': publishings_id}
