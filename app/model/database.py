from sqlalchemy import create_enginefrom sqlalchemy.ext.declarative import declarative_basefrom sqlalchemy.orm import sessionmakerSQLALCHEMY_DATABASE_URL = "sqlite:///./comics"# SQLALCHEMY_DATABASE_URL = "postgresql://postgresql:123@localhost:5432/comics"engine = create_engine(    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)Base = declarative_base()