#!/usr/bin/python3
#from itertools import accumulate
from functools import reduce

def isValidWalk(walk):
    
    if len(walk) != 10:
        return False
 
    mapdict = {'n':(1,0), 's':(-1,0), 'e':(0,1), 'w':(0,-1)}

    dr = ([mapdict[x] for x in walk])

    # add starting point
    dr.insert(0, [0, 0])


    #return [total for total in accumulate(dr, lambda p,x: [p[0]+x[0],p[1]+x[1]])][-1] == [0,0]
        
    ret = reduce(lambda p,x: [p[0]+x[0],p[1]+x[1]], dr)
    print (ret)
    return ret == [0,0]

if __name__ == "__main__":
    assert(isValidWalk(['e','e', 'e', 's', 's', 'w', 'n', 'n', 'w', 'w']) == True)
    assert(isValidWalk(['e','w', 'e']) == False)
