#!/usr/bin/python

import unittest
from count_vowels import countvowels



class TestCase(unittest.TestCase):
    def test_correct_vowel_count(self):
        self.assertEqual( countvowels("hello"), 2 )
        self.assertEqual( countvowels("eo"),    2 )
        self.assertEqual( countvowels("hll"),   0 )

    def test_empty_string(self):
        self.assertEqual(countvowels(""), 0)

if __name__ == "__main__":
    unittest.main()
