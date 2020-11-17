#!/usr/bin/python3
# -*- coding:utf-8 -*-
from sqlalchemy import Column, INT, TIMESTAMP

from app.base.extensions import Base


class Reference(Base):
    __tablename__ = 'reference'
    id = Column(INT, primary_key=True)
    user_id = Column(INT)
    channel_id = Column(INT)
    topic_id = Column(INT)
    topic_article_id = Column(INT)
    is_read = Column(INT)
    create_time = Column(TIMESTAMP)
    status = Column(INT)
