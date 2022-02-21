from unittest import TestCase

from strongletter import strongletter


class Test(TestCase):
    def test_strongletter(self):
       self.assertEqual(strongletter('baas'),'baaz')
       self.assertEqual(strongletter('boom'),'boom')
       self.assertEqual(strongletter('slaaf'),'slaav')




