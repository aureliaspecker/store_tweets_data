# -*- coding: UTF-8 -*-

import sys
import datetime
from models.db_base import Base
from sqlalchemy import Table, Column, MetaData, ForeignKey, Boolean, DATETIME, BIGINT, TEXT

class Users(Base): 
    __tablename__ = "users"

    user_id = Column(BIGINT, primary_key=True) 
    name = Column(TEXT)
    handle = Column(TEXT)
    location = Column(TEXT, nullable=True)
    bio = Column(TEXT, nullable=True)
    verified = Column(Boolean, nullable=True)
    protected = Column(Boolean, nullable=True)
    followers_count = Column(BIGINT, nullable=True)
    friends_count = Column(BIGINT, nullable=True)
    listed_count = Column(BIGINT, nullable=True)
    favorites_count = Column(BIGINT, nullable=True)
    statuses_count = Column(BIGINT, nullable=True)
    lang = Column(TEXT, nullable=True)
    timezone = Column(TEXT, nullable=True)
    utc_offset = Column(BIGINT, nullable=True)
    country_code = Column(TEXT, nullable=True)
    region = Column(TEXT, nullable=True)
    sub_region = Column(TEXT, nullable=True)
    locality = Column(TEXT, nullable=True)
    geo_full_name = Column(TEXT, nullable=True)
    latitude = Column(BIGINT, nullable=True)
    longitude = Column(BIGINT, nullable=True)
    created_at = Column(DATETIME, nullable=True)
    updated_at = Column(DATETIME, nullable=True)