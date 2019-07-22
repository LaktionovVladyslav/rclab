from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI: str = 'sqlite:///labrc.db'
db = create_engine(DATABASE_URI)

Base = declarative_base()
Session: sessionmaker = sessionmaker(bind=db)

# create a Session
session = Session()


class Theme(Base):
    __tablename__ = 'themes'
    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True)
    title = Column(String)
    tags = Column(String)
    text = Column(String)
    date = Column(String)
    author = Column(String)


Base.metadata.create_all(db)
