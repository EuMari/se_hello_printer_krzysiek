import unittest
from hello_world import app, db
from hello_world.models import User, Post # noqa
from datetime import datetime, timedelta # noqa


class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='JanTester')
        u.set_password('testowe')
        self.assertFalse(u.check_password('nieprawidlowe'))
        self.assertTrue(u.check_password('testowe'))
