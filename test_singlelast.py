from unittest import TestCase

from wordmanipulations.singlelast import singlelast


class Test(TestCase):
    def test_singlelast(self):
        self.assertEqual(singlelast('dik'),'dik')
        self.assertEqual(singlelast('dikk'),'dik')
        self.assertEqual(singlelast('gans'),'gans')
        self.assertEqual(singlelast('ganss'),'ganss')

