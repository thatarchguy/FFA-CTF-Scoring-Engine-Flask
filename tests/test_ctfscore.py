#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This runs unittests so we know if our program breaks
The database is run in memory.
It utilizes the nose module.

ex. python manage.py test
"""

import urllib2
from flask import Flask
from flask.ext.testing import LiveServerTestCase
from ctfscore import app, db, models
import config

class Testctfscores(LiveServerTestCase):

    TESTING = app.config['TESTING']
    def create_app(self):
        app.config.from_object('config.TestConfiguration')
        SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI']
        print SQLALCHEMY_DATABASE_URI

        return app

    def setUp(self):
        print "CREATING DB"
        db.create_all()
        db.session.commit()

    def tearDown(self):
        print "TEARING DOWN!"
        db.session.remove()
        db.drop_all()

    def test_server_is_up_and_running(self):
        u = models.Flags(flag="Flag-test",points=20)
        db.session.add(u)
        db.session.commit()
        print "DATA ADDED!"

        print "QUERYING DATABASE"
        flagID = models.Flags.query.filter_by(flag="Flag-test").one().id
        print flagID

        response = urllib2.urlopen(self.get_server_url() + "/")
        self.assertEqual(response.code, 200)

