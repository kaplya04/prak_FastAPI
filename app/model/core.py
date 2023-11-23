from sqlalchemy import Column, Integer, String, MetaData, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.model.database import Base

metadata = MetaData()

comic_publishing = Table(
    'comic_publishing',
    metadata,
    Column('comic_id', ForeignKey("publishing.id"), primary_key=True),
    Column("publishing_id", ForeignKey("comic.id"), primary_key=True),
)


class comic(Base):
    __tablename__ = "comic"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    after = Column(String, index=True)
    year = Column(String, index=True)
    publishing = relationship('publishing', secondary=comic_publishing, back_populates="comic")


class publishing(Base):
    __tablename__ = "publishing"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class genre(Base):
    __tablename__ = "genre"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class series(Base):
    __tablename__ = "series"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class hero(Base):
    __tablename__ = "hero"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
