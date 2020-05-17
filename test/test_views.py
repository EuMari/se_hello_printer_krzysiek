import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data

    def test_msg_with_output_json(self):
        rv = self.app.get('/?output=json')
        self.assertEquals('{"imie":"Krzysiek", "mgs":"Hello World!"}', rv.data)

    def test_msg_with_output_xml(self):
        rv = self.app.get('/?output=xml')
        op = '<greetings>\n\t<name>Krzysiek</name>\n\t<msg>Hello World!</msg>\n</greetings>\n'
        self.assertEquals(op, rv.data)
