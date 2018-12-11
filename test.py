import unittest


def fun(x):
    return x + 1


def strip_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join([x for x in string if x.lower() not in vowels])


class MyTest(unittest.TestCase):
    def test_fun(self):
        self.assertEqual(fun(3), 4)

    def test_strip_vowels_lcase(self):
        self.assertEqual(strip_vowels('abcdefghijlkmnopqrtuvwxyz'), 'bcdfghjlkmnpqrtvwxyz')

    def test_strip_vowels_ucase(self):
        self.assertEqual(strip_vowels('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'BCDFGHJKLMNPQRSTVWXYZ')
