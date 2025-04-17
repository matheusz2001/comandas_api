from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import STR_DATABASE

#Matheus Felipe Ribeiro Cruz de Mello

engine = create_engine(STR_DATABASE, echo=True)

Session = sessionmaker(bind=engine, autocommit=False, autoflush=True)

Base = declarative_base()

async def criaTabelas():
    Base.metadata.create_all(engine)