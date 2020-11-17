#!/usr/bin/python3
# -*- coding:utf-8 -*-
from sqlalchemy import Column, INT, VARCHAR, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.base.extensions import Base


class TopicArticle(Base):
    __tablename__ = 'topic_article'
    id = Column(INT, primary_key=True, autoincrement=True)
    topic_id = Column(INT, ForeignKey("topic.id"))
    title = Column(Text)
    content = Column(Text)
    sum = Column(Text)
