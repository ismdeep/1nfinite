#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    HOSTNAME = os.environ.get('DB_HOST')
    PORT = os.environ.get('DB_PORT')
    DATABASE = os.environ.get('DB_NAME')
    USERNAME = os.environ.get('DB_USER')
    PASSWORD = os.environ.get('DB_PASS')
    DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}'.format(username=USERNAME, password=PASSWORD,
                                                                               host=HOSTNAME, port=PORT, db=DATABASE)

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 设置session 7天过期。
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    DEBUG = True

    SECRET_KEY = os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass
