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

    def test_name_output(self):
        rv = self.app.get('/?name=Apolonia')
        op = 'Apolonia'
        self.assertEquals(op, rv.data.split(" ")[0])

    def test_msg_with_output_json(self):
        rv = self.app.get('/?output=json')
        op = '{"imie": "Krzysiek", "msg": "Aplikacja testowa!"}'
        self.assertEquals(op, rv.data)

    def test_msg_with_output_xml(self):
        rv = self.app.get('/?output=xml')
        op = '<greetings>\n  <name>Krzysiek</name>\n  <msg>Aplikacja testowa!</msg>\n</greetings>\n' # noqa
        self.assertEquals(op, rv.data)
