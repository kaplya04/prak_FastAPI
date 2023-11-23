from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

metadata = MetaData()
comic = Table(
    "comic",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('autor', String, nullable=False),
    Column('year', String, nullable=False),
    Column('permissions', JSON),
)

publishing = Table(
    "publishing",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
)

genre = Table(
    "genre",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
)

series = Table(
    "serie",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
)

hero = Table(
    "hero",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
)

users = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('name', String, nullable=False),
    Column('password', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
    Column('hashed_password', String, nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=True, nullable=False),
    Column('is_verified', Boolean, default=True, nullable=False),
)
