from math import sqrt

def eratosthenes(N):
    flags = [True] * (N + 1)
    primes = []

    i = 2
    while i <= sqrt(N):
        if flags[i]:
            j = i * i
            while j <= N:
                flags[j] = False
                j += i
        i += 1
    
    for i in range(2, N + 1):
        if flags[i]:
            primes.append(i)
    
    return primes

def test_erat():
    if eratosthenes(10) == [2, 3, 5, 7]:
        print("Test 1: passed")
    else:
        print("Test 1: failed")
    
    if eratosthenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        print("Test 2: passed")
    else:
        print("Test 2: failed")

test_erat()