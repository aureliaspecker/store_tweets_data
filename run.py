from stream import Stream
from services.get_tweet import Tweet
from services.get_user import User
import time
from models.db_base import Base, get_db_sessionmaker
from services.credentials_service import CredentialsService

def main():
    
    """Read in user detail"""
    credentials = CredentialsService().from_yaml_file("credentials.yml")

    db_sessionmaker = get_db_sessionmaker(credentials.local_db)

    """Initialise stream"""
    stream = Stream(db_sessionmaker, credentials.twitter_api)

    """Get Tweet and store in DB"""
    # Yet to do

    """Get User and store in DB"""
    # Yet to do

if __name__ == "__main__":
    main()