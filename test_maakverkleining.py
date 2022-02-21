from unittest import TestCase

from maakverkleining import maakverkleining


class Test(TestCase):
    def test_maakverkleining(self):
        # laatste m

        self.assertEqual(maakverkleining('boom'),'boompje')
        # laatste t
        self.assertEqual(maakverkleining('kast'), 'kastje')
        self.assertEqual(maakverkleining('huis'), 'huisje')
        # self.assertEqual(maakverkleining('ship'), 'scheepje')
        # self.assertEqual(maakverkleining('glas'), 'glaasje')
        # self.assertEqual(maakverkleining('groen'), 'groentje')
        # self.assertEqual(maakverkleining('blauw'), 'blauwtje')
        # self.assertEqual(maakverkleining('ton'), 'tonnetje')
        # self.assertEqual(maakverkleining('spion'), 'spionnetje')
        # self.assertEqual(maakverkleining('slang'), 'slangetje')
        # self.assertEqual(maakverkleining('stroming'), 'strominkje')
        # self.assertEqual(maakverkleining('beer'), 'beertje')
        #






