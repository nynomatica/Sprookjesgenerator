from unittest import TestCase

from wordmanipulations.captallist import capitallist


class Test(TestCase):
    def test_capitallist(self):
        self.assertEqual(capitallist(['aak', 'aalst', 'aamelo', 'aamen']),['Aak', 'Aalst', 'Aamelo', 'Aamen'])