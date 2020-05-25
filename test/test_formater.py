import unittest
import hello_world.formater as FT


class TestFormater(unittest.TestCase):
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
