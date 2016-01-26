#!/usr/bin/python3



def mergesort(tosort):
    '''Merge sort works by splitting list into two until in single units
    and merging them back together'''
    if len(tosort) == 1:
        return tosort


    lhs = mergesort(tosort[:len(tosort)//2])
    rhs = mergesort(tosort[len(tosort)//2:])
    
    merged = []
    lhsi, rhsi = 0,0

    while lhsi < len(lhs) and rhsi < len(rhs):
        if lhs[lhsi] < rhs[rhsi]:
            merged.append( lhs[lhsi] )
            lhsi += 1
        else:
            merged.append( rhs[rhsi] )
            rhsi += 1
    # Put back remaining
    merged.extend( rhs[rhsi:] if rhsi < len(rhs) else lhs[lhsi:] )
    return merged


if __name__ == "__main__":
    assert(mergesort([3,4,2,7,5,8,5,9,0,1,6]) == [0,1,2,3,4,5,5,6,7,8,9])
