from math import floor

def sundaram(N):
    if N < 2:
        return []
    flags = [True] * (N + 1)
    primes = [2]

    for j in range(1, N + 1):
        for i in range(1, j + 1):
            k = i + j + 2 * i * j
            if k <= N:
                flags[k] = False
    
    for i in range(1, floor((N - 1) / 2) + 1):
        if flags[i]:
            primes.append(2 * i + 1)

    return primes

def test_sundaram():
    if sundaram(10) == [2, 3, 5, 7]:
        print("Test 1: passed")
    else:
        print("Test 1: failed")
    
    if sundaram(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        print("Test 2: passed")
    else:
        print("Test 2: failed")

    if sundaram(-1) == []:
        print("Test 3: passed")
    else:
        print("Test 3: failed")

test_sundaram()