#!/usr/bin/python3
# -*- coding:utf-8 -*-
from .Channel import Channel
from .User import User
from .Follow import Follow
from .Image import Image
from .Like import Like
from .Reference import Reference
from .Topic import Topic
from .TopicArticle import TopicArticle

from app.base.extensions import Base
from app.base.extensions import engine

# Init for creating tables
Base.metadata.create_all(engine)
