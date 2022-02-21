from unittest import TestCase

from compresslastvowel import compresslastvowel


class Test(TestCase):
    def test_compresslastvowel(self):
       self.assertEqual(compresslastvowel('boomen'),'bomen')
       self.assertEqual(compresslastvowel('boemen'),'boemen')
       self.assertEqual(compresslastvowel('aaboomen'),'aabomen')

