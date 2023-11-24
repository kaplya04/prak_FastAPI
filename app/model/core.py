from sqlalchemy import Column, Integer, String, MetaData, Table, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.model.database import Base

metadata = MetaData()

Comics_Publishings = Table(
    'comics_publishings',
    metadata,
    Column('comics_id', ForeignKey("publishings.id"), primary_key=True),
    Column("publishings_id", ForeignKey("comics.id"), primary_key=True),
)


class Comics(Base):
    __tablename__ = "comics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, index=True)
    autor = Column(Text, index=True)
    year = Column(String, index=True)
    publishing = relationship('publishings', secondary="comics_publishings", back_populates="comic")


class Publishings(Base):
    __tablename__ = "publishings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, index=True)


class Genres(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, index=True)


class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, index=True)


class Personajs(Base):
    __tablename__ = "personajs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, index=True)
