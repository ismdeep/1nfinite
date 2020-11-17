#!/usr/bin/python3
# -*- coding:utf-8 -*-
from sqlalchemy import Column, INT, Text

from app.base.extensions import Base


class Image(Base):
    __tablename__ = 'image'
    id = Column(INT, primary_key=True, autoincrement=True)
    url = Column(Text)
