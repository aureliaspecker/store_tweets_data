# -*- coding: UTF-8 -*-

import sys
import datetime
from models.db_base import Base
from sqlalchemy import Table, Column, MetaData, ForeignKey, Boolean, DATETIME, BIGINT, TEXT, LONGTEXT

class Tweets(Base): 
    __tablename__ = "tweets"

    tweet_id = Column(BIGINT, primary_key=True)
    text = Column(TEXT)
    posted_at = Column(DATETIME)
    truncated = Column(Boolean, nullable=True)
    source = Column(TEXT, nullable=True)
    lang = Column(TEXT, nullable=True)
    favorite_count = Column(BIGINT, nullable=True)
    reply_count = Column(BIGINT, nullable=True)
    retweet_count = Column(BIGINT, nullable=True)
    place_name = Column(BIGINT, nullable=True)
    country_code = Column(BIGINT, nullable=True)
    latitude = Column(BIGINT, nullable=True)
    longitude = Column(BIGINT, nullable=True)
    lat_box = Column(BIGINT, nullable=True)
    long_box = Column(BIGINT, nullable=True)
    tweet_json = Column(LONGTEXT)
