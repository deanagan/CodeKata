#!/usr/bin/python3


class test(object):
    def assert_equals(outp, param):
        print(outp)
        assert(outp == param)

def group_by_commas(arg):
    return '{:,}'.format(arg)
           
def group_by_commas_long(arg):
    argstr = str(arg)
    argstrlen = len(argstr)

    init = argstrlen % 3
    chunk = [argstr[s:s+3] for s in range(init, argstrlen,3)]
    if init:
        chunk.insert(0,argstr[:init])
    return ','.join(chunk) 

if __name__ == "__main__":
    test.assert_equals(group_by_commas(1), '1')
    test.assert_equals(group_by_commas(10), '10')
    test.assert_equals(group_by_commas(100), '100')
    test.assert_equals(group_by_commas(1000), '1,000')
    test.assert_equals(group_by_commas(10000), '10,000')
    test.assert_equals(group_by_commas(100000), '100,000')
    test.assert_equals(group_by_commas(1000000), '1,000,000')
    test.assert_equals(group_by_commas(35235235), '35,235,235')
