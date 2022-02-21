from unittest import TestCase

from maakmeervoud import maakmeervoud


class Test(TestCase):
    def test_maakmeervoud(self):
        # self.assertEqual(maakmeervoud('wind'), 'winden')
        # self.assertEqual(maakmeervoud('aai'), 'aaien')
        # self.assertEqual(maakmeervoud('boer'),'boeren')
        # self.assertEqual(maakmeervoud('boom'),'bomen')
        # self.assertEqual(maakmeervoud('bom'),'bommen')
        # self.assertEqual(maakmeervoud('beer'),'beren')
        # self.assertEqual(maakmeervoud('baas'),'bazen')
        # self.assertEqual(maakmeervoud('muis'), 'muizen')
        # self.assertEqual(maakmeervoud('slaaf'), 'slaven')
        # self.assertEqual(maakmeervoud('bier'), 'bieren')
        # self.assertEqual(maakmeervoud('nep'), 'neppen')
        # self.assertEqual(maakmeervoud('aai'), 'aaien')
        # self.assertEqual(maakmeervoud('roos'), 'rozen')
        # self.assertEqual(maakmeervoud('wagen'), 'wagens')
        # self.assertEqual(maakmeervoud('jongen'), 'jongens')
        # self.assertEqual(maakmeervoud('meisje'), 'meisjes')
        self.assertEqual(maakmeervoud('tand'), 'tanden')

        self.assertEqual(maakmeervoud('gans'), 'ganzen')
        self.assertEqual(maakmeervoud('kind'), 'kinderen')

        # abcdefghijklmnopqrstuvwxyz


        self.assertEqual(maakmeervoud(''),'???')

