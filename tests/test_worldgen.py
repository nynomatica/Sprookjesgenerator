from unittest import TestCase
from world import worldmapsize,citycount


class Test(TestCase):
    def test_initworld(self):
        self.assertEqual(worldmapsize,10000)
        self.assertEqual(citycount, 1200)
