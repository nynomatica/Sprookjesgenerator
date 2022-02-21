from unittest import TestCase

from wordmanipulations.doublelast import doublelast


class Test(TestCase):
    def test_doublelastconsonant(self):
        self.assertEqual(doublelast('dik'),'dikk')
        self.assertEqual(doublelast('gans'), 'gans')
