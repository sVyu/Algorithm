import sys
input = sys.stdin.readline

'''
ans[10_000_000] -> 31373
'''

def solve():
    mx = int(4e4)+1
    check_prime = [True]*mx
    check_prime[0] = False
    check_prime[1] = False

    for i in range(2, mx):
        if(check_prime[i]):
            for j in range(i*2, mx, i):
                check_prime[j] = False

    ans = [-1]*mx
    for i in range(100, mx):
        t = str(i) # target
        ans[i] = ans[i-1]
        if(check_prime[i]): continue
        if(i >= 31374): continue

        len_t = len(t)
        isPrime = True
        for s in range(len_t-1):
            for e in range(s+1, len_t):
                if((e-s) == (len_t-1)): continue
                isPrime &= check_prime[int(t[s:e+1])]
                if(not isPrime): break
            if(not isPrime): break

        if(isPrime):
            ans[i] = i

    n = int(input())
    for _ in range(n):
        target = int(input())
        if(target >= 31373):
            print(31373)
            continue
        else:
            print(ans[target])

solve()