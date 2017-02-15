#!/usr/bin/python

import unittest

from brackets import checkio

class TestCase(unittest.TestCase):
    def test_bracket_validity(self):
        self.assertTrue(  checkio("((5+3)*2+1)") )
        self.assertTrue(  checkio("{[(3+1)+2]+}") )
        self.assertFalse( checkio("(3+{1-1)}") )
        self.assertTrue(  checkio("[1+1]+(2*2)-{3/3}") )
        self.assertFalse( checkio("(({[(((1)-2)+3)-3]/3}-3)") )
        self.assertTrue(  checkio("2+3") )
        self.assertFalse( checkio("(((([[[{{{3}}}]]]]))))") )

if __name__ == "__main__":
    unittest.main()

