#!/usr/bin/python3

def quicksort(tosort):

    if not len(tosort):
        return []

    median = [i for i in tosort if i == tosort[0]]
    less = quicksort([ i for i in tosort if i < tosort[0] ])
    more = quicksort([ i for i in tosort if i > tosort[0] ])
    print(less + median + more)
    return less + median + more
#    return [0,1,2,3,4,5,5,6,7,8,9]

if __name__ == "__main__":
    assert(quicksort([3,4,2,7,6,8,9,1,5,0,5]) == [0,1,2,3,4,5,5,6,7,8,9])
