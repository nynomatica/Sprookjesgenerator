from unittest import TestCase

from generators import MaleNameRND


class Test(TestCase):
    def test_malename(self):
        self.assertTrue(MaleNameRND(),True)
