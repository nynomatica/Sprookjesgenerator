from unittest import TestCase

from wordmanipulations.maxconsonant import maxconsonant


class Test(TestCase):
    def test_maxconsonant(self):
        self.assertEqual(maxconsonant("abbe"),2)
