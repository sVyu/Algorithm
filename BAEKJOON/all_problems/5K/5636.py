import sys
input = sys.stdin.readline

# prime check (sieve of Eratosthenes)
size = int(1e5)
primes = [False, False]+[True]*(size+1)
for i in range(2, size):
    if primes[i]:
        for ii in range(2*i, size, i):
            primes[ii] = False

# find max prime number
ss = input().rstrip()
while ss != '0':
    len_ss = len(ss)

    ans = -1
    for partial_length in range(min(len_ss, 5), 0, -1):
        for base_idx in range(0, len_ss-partial_length+1):
            n = int(ss[base_idx:base_idx+partial_length])
            if primes[n]:
                ans = max(ans, n)

    print(ans)
    ss = input().rstrip()