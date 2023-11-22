from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.model.database import Base


class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    email = Column(String, unique=True)


class Comic(Base):
    __tablename__ = "comics"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    after = Column(String, index=True)
    year = Column(String, index=True)

    owners = relationship("owner", back_populates="comics")


class Publishing(Base):
    __tablename__ = "publishings"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    owners = relationship("publishings", back_populates="owner")


class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    owners = relationship("genres", back_populates="owner")


class Series(Base):
    __tablename__ = "series"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    owners = relationship("series", back_populates="owner")


class Hero(Base):
    __tablename__ = "heros"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    owners = relationship("heros", back_populates="owner")
