#!/usr/bin/python3
# -*- coding:utf-8 -*-
from sqlalchemy import Column, INT, VARCHAR, Text, Boolean, text, TIMESTAMP

from app.base.extensions import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(INT, primary_key=True, autoincrement=True)
    email = Column(VARCHAR(255))
    username = Column(VARCHAR(255))
    admin = Column(INT, default=0)
    ban = Column(INT, default=0)
    nickname = Column(VARCHAR(255))
    sex = Column(INT, default=0)
    password = Column(VARCHAR(255))
    avatar = Column(VARCHAR(255), default='0')
    channel_name = Column(VARCHAR(255))
    create_time = Column(TIMESTAMP(True), nullable=False, server_default=text('NOW()'))
