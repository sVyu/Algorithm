import sys
input = sys.stdin.readline
import math

def prime_check(n):
    if n==1: return False
    elif n==2: return True
    elif n%2 == 0: return False
    else:
        for k in range(3, math.isqrt(n)+1, 2):
            if n%k == 0:
                return False
        return True

for _ in range(int(input())):
    case, n = map(int, input().split())
    n_backup = n
    nset = set()

    if not prime_check(n):
        print(case, n, "NO")
        continue

    while n not in nset:
        nset.add(n)
        if n == 1:
            break
    
        new_n = 0
        ns = list(map(int, str(n)))
        for k in ns:
            new_n += k**2
            n = new_n

    if 1 in nset:
        print(case, n_backup, "YES")
    else:
        print(case, n_backup, "NO")