#!/usr/bin/python3
from collections import Counter

def countvowels(data):
    return sum([v for k,v in Counter(data).items() if k in 'aeiouAEIOU'] )

def countvowels2(data):
    return sum ( data.count(i) for i in 'aeiouAEIOU' )


if __name__ == "__main__":
    print(countvowels("hello"))

    assert(countvowels('abracadabra') == countvowels2('abracadabra'))
