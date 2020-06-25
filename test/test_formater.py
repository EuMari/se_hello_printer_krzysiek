import unittest
from hello_world import app
import hello_world.formater as FT


class TestFormater(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_plain_uppercase(self):
        r = FT.plain_text_upper_case("dfdfTest", "ddfeSSSetest")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())

    def test_plain_lowercase(self):
        r = FT.plain_text_lower_case("SSStest", 'NUUsdtest')
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.islower())
        self.assertTrue(msg.islower())

    def test_plain_text(self):
        r = FT.plain_text("MSG", "IMIE")
        r2 = "IMIE MSG"
        self.assertEquals(r, r2)

    def test_format_to_json(self):
        r = FT.format_to_json("msg", "imie")
        r2 = '{"imie": "imie", "msg": "msg"}'
        self.assertEquals(r, r2)

    def test_format_to_xml(self):
        r = FT.format_to_xml("msg", "imie")
        r2 = '<greetings>\n  <name>imie</name>\n  <msg>msg</msg>\n</greetings>\n' # noqa
        self.assertEquals(r, r2)
