from sqlalchemy.orm import Session

from app.model import core


def get_comic(db: Session, skip: int = 0, limit: int = 100):
    return db.query(core.Comic).offset(skip).limit.all()
