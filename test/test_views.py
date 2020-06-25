# -*- coding: utf-8 -*-
import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        app.config['TESTING'] = False

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data

    def test_name_output(self):
        rv = self.app.get('/formaty?name=Ania')
        op = 'Ania'
        self.assertEquals(op, rv.data.split(" ")[0])

    def test_msg_with_output_json(self):
        rv = self.app.get('/formaty?output=json')
        op = '{"imie": "Krzysiek", "msg": "Aplikacja testowa!"}'
        self.assertEquals(op, rv.data)

    def test_msg_with_output_xml(self):
        rv = self.app.get('/formaty?output=xml')
        op = '<greetings>\n  <name>Krzysiek</name>\n  <msg>Aplikacja testowa!</msg>\n</greetings>\n' # noqa
        self.assertEquals(op, rv.data)

    def test_error404page_display(self):
        r = self.app.get('404')
        self.assertEqual(r.status_code, 404)
        self.assertIn('Przepraszam, nie ma takiej strony.', r.data)

    def test_login_display(self):
        r = self.app.get('/login')
        self.assertEqual(r.status_code, 200)
        self.assertIn('Zaloguj', r.data)

    def test_index_no_access_redirect_to_login_page(self):
        r = self.app.get('/index')
        self.assertEqual(r.status_code, 302)
        self.assertIn('/login', r.data)

    def test_registration_display(self):
        r = self.app.get('/register')
        self.assertEqual(r.status_code, 200)
        self.assertIn('Zarejestruj', r.data)

    def test_resetpassword_request_display(self):
        r = self.app.get('/reset_password_request')
        self.assertEqual(r.status_code, 200)
        self.assertIn('Zresetuj hasło', r.data)
