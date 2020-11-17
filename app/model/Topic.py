#!/usr/bin/python3
# -*- coding:utf-8 -*-
from sqlalchemy import Column, INT, VARCHAR, Text, Boolean, ForeignKey

from app.base.extensions import Base


class Topic(Base):
    __tablename__ = 'topic'
    id = Column(INT, primary_key=True, autoincrement=True)
    user_id = Column(INT, ForeignKey("user.id"))
    title = Column(Text)
    sum = Column(Text)
