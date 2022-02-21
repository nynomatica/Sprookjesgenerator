from unittest import TestCase

from wordmanipulations.plural import plural, pluralword
from wordmanipulations.vowelconsonantpairs import vowelconsonantpairs


class Test(TestCase):
    def test_plural(self):
        self.assertEqual(pluralword('gans'), 'ganzen')
        # self.assertEqual(pluralword('dak'), 'ganzen')

        self.assertEqual(pluralword('boom'),'bomen')
        # self.assertEqual(pluralword('bom'),'bommen')
        # self.assertEqual(pluralword('glas'),'glazen')


