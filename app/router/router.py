from fastapi import APIRouter
from sqlalchemy.orm import joinedload

from app.model.core import Comics, Publishings

from app.model.database import db
from app.model.schemas import ComicsCreate, publishingsq
from fastapi import HTTPException, status

comicsRouter = APIRouter(prefix="",
                         tags=["Comics"],
                         responses={404: {"description": "Not found"}})


@comicsRouter.get('/')
async def catalog():
    comics = db.query(Comics).all()
    return comics


@comicsRouter.post('/newcomics/', response_model=ComicsCreate)
async def newcomics(comics: ComicsCreate):
    comics = Comics(
        name=comics.name,
        after=comics.after,
        year=comics.year,
    )
    try:
        db.add(comics)
        db.commit()
    except:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Try again'
        )
    return comics


@comicsRouter.get('/publishings/{publishings_id}/', response_model=publishingsq)
async def get_comicsq(publishings_id: int):
    comicsq = db.query(Publishings).join(Comics, Publishings.comics).filter(Publishings.id == publishings_id).one()
    return {'comics': comicsq.comics, 'publishings_id': publishings_id}