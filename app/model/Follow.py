#!/usr/bin/python3
# -*- coding:utf-8 -*-
from sqlalchemy import Column, INT
from app.base.extensions import Base


class Follow(Base):
    __tablename__ = 'following'
    id = Column(INT, primary_key=True, autoincrement=True)
    user_id = Column(INT)
    channel_user_id = Column(INT)
    topic_id = Column(INT)
    status = Column(INT)
