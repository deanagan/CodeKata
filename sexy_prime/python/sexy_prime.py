#!/usr/bin/python3
'''
Sexy primes are pairs of two primes that are 6 apart. 
In this kata, your job is to complete the 
function sexy_prime(x, y) which returns true if x & y are sexy, false otherwise. 
'''

def sexy_prime(x, y):
    ''' This uses fermat's theorem to test primality of p
     Pick a number 1 <= n < p, then do n**p-1 % p, if result is not 1, then p is not prime 
    '''
    return all([is_prime for is_prime in map(lambda n: all([rand_num**(n-1) % n == 1 if n > 1 else False 
        for rand_num in range(1, n-1 if n < 100 else 100)] or [False]), [x,y])] + [abs(x-y) == 6])


if __name__ == "__main__":
    assert(sexy_prime(5,11) == True)
    assert(sexy_prime(5, 11) == True)
    assert(sexy_prime(13, 19) == True)
    assert(sexy_prime(83, 89) == True)
    assert(sexy_prime(1, 11) == False)
    assert(sexy_prime(7, 13) == True)
    assert(sexy_prime(1, 7) == False)
