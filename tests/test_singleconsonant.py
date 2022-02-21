from unittest import TestCase

from wordmanipulations.singleconsonant import singleconsonant


class Test(TestCase):
    def test_singleconsonant(self):
        self.assertEqual(singleconsonant("akkker"),'aker')
        self.assertEqual(singleconsonant("akkkeer"),'akeer')
        self.assertEqual(singleconsonant("akkkerrrr"),'aker')
        self.assertEqual(singleconsonant("knast"), 'knast')
        self.assertEqual(singleconsonant("kklak"), 'klak')

