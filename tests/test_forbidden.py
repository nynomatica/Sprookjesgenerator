from unittest import TestCase

from wordmanipulations.forbidden import forbidden


class Test(TestCase):
    def test_forbidden(self):
        self.assertEqual(forbidden("brar"),"")
