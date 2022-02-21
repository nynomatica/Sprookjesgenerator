from unittest import TestCase

from wordmanipulations.uniquelist import uniquelist


class Test(TestCase):
    def test_makeunique(self):
        self.assertEqual(uniquelist(['a','a','a','b','b']),['a','b'])
