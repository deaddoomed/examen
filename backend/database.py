from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.automap import automap_base
# from pymongo import MongoClient
from typing import Annotated
import os
from dotenv import load_dotenv

load_dotenv(".env")

mysql_url = create_engine(os.getenv('DB_MYSQL'))

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=mysql_url)

mysql_database = automap_base()
mysql_database.prepare(mysql_url, schema='ferremas')

Base = automap_base()
Base.metadata.create_all(bind=mysql_url)

def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

db_dependency = Annotated[Session, Depends(get_db)]