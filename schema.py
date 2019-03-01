# -*- coding: UTF-8 -*-

import sys
import datetime

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData, ForeignKey, Boolean, DATETIME, BIGINT
from sqlalchemy.dialects.mysql import TEXT, LONGTEXT

engine = create_engine('mysql://aspecker:password@127.0.0.1:3306/storetweetslocal', echo=True) #PORT:3306
print(engine)

metadata = MetaData(engine)

tweet_engagements = Table('engagements', metadata,
    Column('id', BIGINT, primary_key=True), 
    Column('tweet_id', BIGINT), 
    Column('start_time', DATETIME),
    Column('end_time', DATETIME),
    Column('total_impressions', BIGINT, nullable=True),
    Column('unique_impressions', BIGINT, nullable=True),
    Column('total_engagements', BIGINT, nullable=True),
    Column('unique_engagements', BIGINT, nullable=True),
    Column('replies_count', BIGINT, nullable=True),
    Column('retweets_count', BIGINT, nullable=True),
    Column('unretweets_count', BIGINT, nullable=True),
    Column('quotes_count', BIGINT, nullable=True),
    Column('unquotes_count', BIGINT, nullable=True),
    Column('favorites_count', BIGINT, nullable=True),
    Column('unfavorites_count', BIGINT, nullable=True),
    Column('url_clicks', BIGINT, nullable=True),
    Column('hashtag_clicks', BIGINT, nullable=True),
    Column('detail_clicks', BIGINT, nullable=True),
    Column('permalink_clicks', BIGINT, nullable=True),
    Column('app_install_attempts', BIGINT, nullable=True),
    Column('app_opens', BIGINT, nullable=True),
    Column('email_tweet', BIGINT, nullable=True),
    Column('user_follows', BIGINT, nullable=True),
    Column('user_profile_clicks', BIGINT, nullable=True),
    Column('media_clicks', BIGINT, nullable=True),
    Column('video_starts', BIGINT, nullable=True), 
    Column('video_viewed_25', BIGINT, nullable=True),
    Column('video_viewed_50', BIGINT, nullable=True),
    Column('video_viewed_75', BIGINT, nullable=True),
    Column('video_viewed_95', BIGINT, nullable=True),
    Column('video_viewed_100', BIGINT, nullable=True),
    Column('video_views_total', BIGINT, nullable=True)
)

time_series = Table('time_series', metadata,
    Column('id', BIGINT, primary_key=True), 
    Column('tweet_id', BIGINT), 
    Column('start_time', DATETIME),
    Column('end_time', DATETIME),
    Column('total_impressions', BIGINT, nullable=True),
    Column('unique_impressions', BIGINT, nullable=True),
    Column('total_engagements', BIGINT, nullable=True),
    Column('unique_engagements', BIGINT, nullable=True),
    Column('replies_count', BIGINT, nullable=True),
    Column('retweets_count', BIGINT, nullable=True),
    Column('unretweets_count', BIGINT, nullable=True),
    Column('quotes_count', BIGINT, nullable=True),
    Column('unquotes_count', BIGINT, nullable=True),
    Column('favorites_count', BIGINT, nullable=True),
    Column('unfavorites_count', BIGINT, nullable=True),
    Column('url_clicks', BIGINT, nullable=True),
    Column('hashtag_clicks', BIGINT, nullable=True),
    Column('detail_clicks', BIGINT, nullable=True),
    Column('permalink_clicks', BIGINT, nullable=True),
    Column('app_install_attempts', BIGINT, nullable=True),
    Column('app_opens', BIGINT, nullable=True),
    Column('email_tweet', BIGINT, nullable=True),
    Column('user_follows', BIGINT, nullable=True),
    Column('user_profile_clicks', BIGINT, nullable=True),
    Column('media_clicks', BIGINT, nullable=True),
    Column('video_starts', BIGINT, nullable=True), 
    Column('video_viewed_25', BIGINT, nullable=True),
    Column('video_viewed_50', BIGINT, nullable=True),
    Column('video_viewed_75', BIGINT, nullable=True),
    Column('video_viewed_95', BIGINT, nullable=True),
    Column('video_viewed_100', BIGINT, nullable=True),
    Column('video_views_total', BIGINT, nullable=True)
)

tweets = Table('tweets', metadata,
    Column('id', BIGINT, primary_key=True), 
    Column('tweet_id', BIGINT), 
    Column('text', TEXT),
    Column('posted_at', DATETIME),
    Column('truncated', Boolean),
    Column('source', TEXT),
    Column('lang', TEXT),
    Column('favorite_count', BIGINT),
    Column('reply_count', BIGINT),
    Column('retweet_count', BIGINT),
    Column('place_name', TEXT, nullable=True),
    Column('country_code', TEXT, nullable=True),
    Column('lat', BIGINT, nullable=True),
    Column('long', BIGINT, nullable=True),
    Column('lat_box', BIGINT, nullable=True),
    Column('long_box', BIGINT, nullable=True),
    Column('tweet_json', LONGTEXT)
)

users = Table('users', metadata,
    Column('id', BIGINT, primary_key=True), 
    Column('user_id', BIGINT), 
    Column('name', TEXT),
    Column('handle', TEXT),
    Column('location', TEXT),
    Column('bio', TEXT, nullable=True),
    Column('verified', Boolean),
    Column('protected', Boolean),
    Column('followers_count', BIGINT),
    Column('friends_count', BIGINT),
    Column('listed_count', BIGINT),
    Column('favorites_count', BIGINT),
    Column('statuses_count', BIGINT),
    Column('lang', TEXT),
    Column('timezone', TEXT, nullable=True), 
    Column('utc_offset', BIGINT, nullable=True),
    Column('country_code', TEXT, nullable=True),
    Column('region', TEXT, nullable=True),
    Column('sub_region', TEXT, nullable=True), 
    Column('locality', TEXT, nullable=True), 
    Column('geo_full_name', TEXT, nullable=True), 
    Column('lat', BIGINT, nullable=True),
    Column('long', BIGINT, nullable=True),
    Column('created_at', DATETIME),
    Column('updated_at', DATETIME)
)

metadata.create_all()
