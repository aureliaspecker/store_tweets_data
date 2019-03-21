from models.db_base import get_db_sessionmaker
from services.credentials_service import CredentialsService
import numpy as np
from models.tweet_engagement import TimeSeries
from services.get_tweet import TweetService
from services.get_user import UserService

import matplotlib.pyplot as py

def main():
    credentials = CredentialsService().from_yaml_file("credentials.yml")

    tweet_service = TweetService(credentials.twitter_api)
    
    user_service = UserService(credentials.twitter_api)

    db_sessionmaker = get_db_sessionmaker(credentials.local_db)

    session = db_sessionmaker()

    tweet_id = "1108499416611061761" # Replace with Tweet ID from database that you want to run analysis on

    print(tweet_service.get_tweet(tweet_id))

    user_id = "1062705508400971776" # Replace with User ID from database that you want to run analysis on

    print(user_service.get_user(user_id))

    records = session.query(TimeSeries).filter_by(tweet_id=tweet_id).order_by(TimeSeries.end_time).all()

    print(records)

    end_times = list(map(lambda record: record.end_time, records))
    total_engagements = list(map(lambda record: record.total_engagements, records)) 

    print(end_times)
    print(total_engagements)

    py.plot(end_times, total_engagements)

    py.show()

if __name__ == "__main__":
    main()