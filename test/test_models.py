# -*- coding: utf-8 -*-
import unittest
from hello_world import app, db
from hello_world.models import User, Post
from datetime import datetime, timedelta


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

    def test_get_and_reset_password_token(self):
        u = User(username='JanTester')
        u2 = User(username='AniaTesterka')
        db.session.add_all([u, u2])
        db.session.commit()
        token = u.get_reset_password_token()
        token2 = u2.get_reset_password_token()
        #  sprawdza czy tokeny userów są różne
        self.assertNotEqual(token, token2)
        # sprawdza czy token pasuje do usera
        self.assertEqual(u.verify_reset_password_token(token), u)
        self.assertNotEqual(u2.verify_reset_password_token(token2), u)

    def test_avatar(self):
        u = User(username='tester2', email='tester2@testy.pl')
        self.assertEqual(u.avatar(70), ('https://www.gravatar.com/avatar/'
                                        'cc49fbb9790fe0823efda45ccb9b5a59'
                                        '?d=identicon&s=70'))

    def test_follow(self):
        u1 = User(username='JanTester', email='jantester@test.pl')
        u2 = User(username='Zuzia', email='zuzia@test.pl')
        db.session.add(u1)
        db.session.add(u2)
        db.session. commit()

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'Zuzia')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'JanTester')

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followed.count(), 0)

    def test_follow_posts(self):
        # tworzymy czterech userów
        u1 = User(username='Jan', email='jan@test.pl')
        u2 = User(username='Zuzia', email='zuzia@test.pl')
        u3 = User(username='Asia', email='asia@test.pl')
        u4 = User(username='Kasia', email='kasia@test.pl')
        db.session.add_all([u1, u2, u3, u4])

        # tworzymy czetery posty
        now = datetime.utcnow()
        p1 = Post(body='post od Jana', author=u1,
                  timestamp=now + timedelta(seconds=1))
        p2 = Post(body='post od Zuzi', author=u2,
                  timestamp=now + timedelta(seconds=4))
        p3 = Post(body='post od Asi', author=u3,
                  timestamp=now + timedelta(seconds=3))
        p4 = Post(body='post od Jana', author=u4,
                  timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        # przygotowanie followers
        u1.follow(u2)  # user 1 obserwuje usera 2
        u1.follow(u4)
        u2.follow(u3)
        u3.follow(u4)
        db.session.commit()

        # sprawdza posty obserwowanych userów
        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])
