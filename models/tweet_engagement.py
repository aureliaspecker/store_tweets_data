# -*- coding: UTF-8 -*-

import sys
import datetime
from models.db_base import Base
from sqlalchemy import Table, Column, MetaData, ForeignKey, Boolean, DATETIME, BIGINT

class BaseTweetEngagement():
    start_time = Column(DATETIME)
    end_time = Column(DATETIME)
    total_impressions = Column(BIGINT, nullable=True)
    unique_impressions = Column(BIGINT, nullable=True)
    total_engagements = Column(BIGINT, nullable=True)
    unique_engagements = Column(BIGINT, nullable=True)
    replies_count = Column(BIGINT, nullable=True)
    unreplies_count = Column(BIGINT, nullable=True)
    retweets_count = Column(BIGINT, nullable=True)
    unretweets_count = Column(BIGINT, nullable=True)
    quotes_count = Column(BIGINT, nullable=True)
    unquotes_count = Column(BIGINT, nullable=True)
    favorites_count = Column(BIGINT, nullable=True)
    unfavorites_count = Column(BIGINT, nullable=True)
    url_clicks = Column(BIGINT, nullable=True)
    hashtag_clicks = Column(BIGINT, nullable=True)
    detail_clicks = Column(BIGINT, nullable=True)
    permalink_clicks = Column(BIGINT, nullable=True)
    app_install_attempts = Column(BIGINT, nullable=True)
    app_opens = Column(BIGINT, nullable=True)
    email_tweet = Column(BIGINT, nullable=True)
    user_follows = Column(BIGINT, nullable=True)
    user_profile_clicks = Column(BIGINT, nullable=True)
    media_clicks = Column(BIGINT, nullable=True)
    video_starts = Column(BIGINT, nullable=True)
    video_viewed_25 = Column(BIGINT, nullable=True)
    video_viewed_50 = Column(BIGINT, nullable=True)
    video_viewed_75 = Column(BIGINT, nullable=True)
    video_viewed_95 = Column(BIGINT, nullable=True)
    video_viewed_100 = Column(BIGINT, nullable=True)
    video_views_total = Column(BIGINT, nullable=True)

class TweetEngagement(Base, BaseTweetEngagement): 
    __tablename__ = "engagements"

    tweet_id = Column(BIGINT, primary_key=True) 

class TimeSeries(Base, BaseTweetEngagement): 
    __tablename__ = "time_series"

    id = Column(BIGINT, primary_key=True)
    tweet_id = Column(BIGINT) 
