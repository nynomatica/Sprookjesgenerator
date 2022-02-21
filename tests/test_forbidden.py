from unittest import TestCase

from wordmanipulations.forbidden import forbidden, IsUnspeakable


class Test(TestCase):
    def test_forbidden(self):
        self.assertEqual(IsUnspeakable("brar"),True)
        self.assertEqual(IsUnspeakable("bluul"),True)
        self.assertEqual(IsUnspeakable("bruur"),True)
        self.assertEqual(IsUnspeakable("bror"),True)


