from models.db_base import get_db_sessionmaker
from services.credentials_service import CredentialsService
import numpy as np
from models.tweet_engagement import TimeSeries

import matplotlib.pyplot as py

def main():
    credentials = CredentialsService().from_file("credentials.txt")

    db_sessionmaker = get_db_sessionmaker(credentials)

    session = db_sessionmaker()

    tweet_id = "1107084711317385216" # Replace with Tweet ID from database that you want to run analysis on

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