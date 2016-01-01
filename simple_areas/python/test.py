#!/usr/bin/python3

from math import pi, sqrt
from operator import mul
from functools import reduce

def simple_areas(*args):
    numparams = len(args)
    if numparams == 2:
        return round( args[1] * args[0], 2)
    
    elif numparams == 1:
        return round(pi * ((args[0]/2)**2), 2)
    
    elif numparams == 3:
        # using heron's formula
        parameter = sum(args) / 2
        radicand = reduce(mul, [(parameter-e) for e in args], parameter)
        return round(sqrt(radicand), 2)
    
    return 0

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"

    print("Earn cool rewards by using the 'Check' button!")

