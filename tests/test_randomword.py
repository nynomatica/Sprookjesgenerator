from unittest import TestCase

from generators.randomword import randomword


class Test(TestCase):
    def test_randomword(self):
        self.assertEqual(randomword(10), randomword(10))
        self.assertEqual(randomword(20), randomword(20))
