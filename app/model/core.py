from sqlalchemy import Column, Integer, String, MetaData, Table, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.model.database import Base

metadata = MetaData()


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    medicine = relationship("Comics", back_populates="categorys")


class Comics(Base):
    __tablename__ = "comics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, index=True)
    autor = Column(Text, index=True)
    year = Column(String, index=True)
    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", backref="comics")


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
