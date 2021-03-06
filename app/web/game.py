#!/usr/bin/python3
# -*- coding:utf-8 -*-
from flask import render_template, session

from app.base.function import is_login
from app.web import web
from app.base.extensions import DBSession
from app.model.User import User


@web.route('/game_check/')
def game_check():
    return render_template('game_check.html', login=is_login())


@web.route('/game/')
def game():
    return render_template('game.html', login=is_login())


