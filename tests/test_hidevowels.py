from unittest import TestCase

from wordmanipulations.hidevowels import hidevowels


class Test(TestCase):
    def test_hidevowels(self):
        self.assertEqual(hidevowels("abeedfghiii"),".b..dfgh...")
        self.assertEqual(hidevowels("abedfghiiiou"),".b.dfgh.....")
        self.assertEqual(hidevowels("bdf"),"bdf")
