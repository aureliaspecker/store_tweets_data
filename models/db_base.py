from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def get_db_sessionmaker(db_credentials):
    """Setting up database"""
    db_engine = create_engine('mysql://{0}:{1}@{2}:{3}/{4}'.format(
        db_credentials.db_user, 
        db_credentials.db_password, 
        db_credentials.db_host, 
        db_credentials.db_port, 
        db_credentials.db_name
    ), echo=True)

    Base.metadata.create_all(db_engine)
    return sessionmaker(bind=db_engine)