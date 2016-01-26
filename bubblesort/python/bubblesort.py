#!/usr/bin/python3


def bubblesort(tosort):
    found_sort = True
    while found_sort:
        found_sort = False
        for i,k in zip(range(len(tosort)-1), range(1,len(tosort))):
            if tosort[i] > tosort[k]:
                tosort[i], tosort[k] = tosort[k], tosort[i]
                found_sort = True

    return tosort

if __name__ == "__main__":
    assert(bubblesort([1,4,3,6,6,7,8,2,5,9,0]) == [0,1,2,3,4,5,6,6,7,8,9])
