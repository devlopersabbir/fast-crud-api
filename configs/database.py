import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


DB_USERNAME = os.environ.get("DB_USERNAME")
DB_NAME = os.environ.get("DB_NAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

engine = create_engine(
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost:3306/{DB_NAME}")

SessionLocal = sessionmaker(autocommit=False, bind=engine, autoflush=False)

base = declarative_base()
