import sys
input = sys.stdin.readline
import math

def gcd(a, b):
    while(b):
        a, b = b, a%b
    return a

def solve():
    a, b = map(int, input().split())
    # print(a, b)

    mx = math.isqrt(max(a, b))
    sieves = [i for i in range(mx+1)]
    # print(sieves)

    for i in range(2, mx+1):
        if(sieves[i]):
            for j in range(2*i, mx+1, i):
                sieves[j] = False

    primes = [i for i in range(2, mx+1) if sieves[i]]
    # print(primes)

    pia, pib = 0, 0
    while(a != b):
        if(gcd(a, b) == 1):
            print(1)
            return

        if(a > b):
            while(a % primes[pia]):
                pia += 1
            a //= primes[pia]
        else:
            while(b % primes[pib]):
                pib += 1
            b //= primes[pib]

    print(a)

solve()