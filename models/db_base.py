from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def get_db_sessionmaker(credentials):
    """Setting up database"""
    db_engine = create_engine('mysql://aspecker:{0}@127.0.0.1:{1}/storetweetslocal'.format(credentials["local_password"], credentials["local_port"]), echo=True)

    Base.metadata.create_all(db_engine)
    return sessionmaker(bind=db_engine)