from unittest import TestCase

from woorden import vowelcount, countvowellist, isvowel


class Test(TestCase):
    def test_vowelcount2(self):
        # only vowels
        self.assertEqual(vowelcount("lal"), ['l', 'a', 'l'])
        self.assertEqual(vowelcount("laal"), ['l', 'aa', 'l'])
        self.assertEqual(vowelcount("l"), ['l'])
        self.assertEqual(vowelcount("a"), ['a'])
        self.assertEqual(vowelcount(""), [])
        self.assertEqual(vowelcount("a"), ['a'])
        self.assertEqual(vowelcount("x"), ['x'])
        self.assertEqual(vowelcount("laauloo"), ['l', 'aau', 'l', 'oo'])
        self.assertEqual(vowelcount("oee"), ['oee'])


class Test2(TestCase):
    def test_isvowel(self):
        self.assertTrue(isvowel('aa'))
        self.assertFalse(isvowel('l'))
        self.assertTrue(isvowel('a'))
        self.assertFalse(isvowel('m'))
        self.assertTrue(isvowel('oe'))
        self.assertTrue(isvowel(''))


# #
#
#
class Test3(TestCase):
    def test_countvowel(self):
        # adic = {
        # "aacaaa": 1,
        # "a": 1,
        # "b": 0
        # }
        # for x, y in adic.items():
        #     self.assertEqual(countvowellist(x), y)

        self.assertEqual(countvowellist('aacaaa'), 2)
        self.assertEqual(countvowellist('a'), 1)
        self.assertEqual(countvowellist('b'), 0)
        self.assertEqual(countvowellist('abc'), 1)
        self.assertEqual(countvowellist('bcd'), 0)
        self.assertEqual(countvowellist('bacad'), 2)
        self.assertEqual(countvowellist('bacaad'), 2)
        self.assertEqual(countvowellist('acaadaa'), 3)
        self.assertEqual(countvowellist('ccaaccii'), 2)
        self.assertEqual(countvowellist('ccaacci'), 2)
        self.assertEqual(countvowellist('a'), 1)
        self.assertEqual(countvowellist('b'), 0)
        self.assertEqual(countvowellist('ba'), 1)
        self.assertEqual(countvowellist('bb'), 0)
        self.assertEqual(countvowellist('abceeff'), 2)


class Test(TestCase):
    def test_randomletters(self):
        self.fail()
