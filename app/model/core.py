from sqlalchemy import Column, Integer, String, MetaData, ForeignKey, Text
from app.model.database import Base

metadata = MetaData()


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)


class Comics(Base):
    __tablename__ = "comics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, index=True)
    autor = Column(Text, index=True)
    year = Column(String, index=True)
    image = Column(String, index=True)
    comics_id = Column(Integer, ForeignKey("category.id"))


class Publishings(Base):
    __tablename__ = "publishings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, index=True)


class Personajs(Base):
    __tablename__ = "personajs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, index=True)
