import sys
input = sys.stdin.readline

def solve():
    t = int(input())

    # sieve -> primes
    mx = 1299709+1
    sieve = [True]*mx
    for i in range(2, mx):
        if(sieve[i]):
            for j in range(2*i, mx, i):
                sieve[j] = False
    primes = [i for i in range(2, mx) if sieve[i]]
    len_primes = len(primes)
    # print(len_primes)

    for _ in range(t):
        k = int(input())
        lower, upper = -1, -1

        # find lower limit
        lo, hi = 0, len_primes-1
        while(lo <= hi):
            mid = (lo+hi)//2

            if(primes[mid] <= k):
                lo = mid+1
                lower = mid
            elif(primes[mid] > k):
                hi = mid-1

        # find upper limit
        lo, hi = 0, len_primes-1
        while(lo <= hi):
            mid = (lo+hi)//2

            if(primes[mid] < k):
                lo = mid+1
            elif(primes[mid] >= k):
                upper = mid
                hi = mid-1

        # print(lower, upper)
        print(max(0, primes[upper]-primes[lower]))

solve()