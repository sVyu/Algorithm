import sys
input = sys.stdin.readline
import itertools
import math

def prime_check(n):
    if(n <= 1):       return False
    elif(n == 2):     return True
    elif(n % 2 == 0): return False
    else:
        for k in range(3, math.isqrt(n)+1, 2):
            if(n % k == 0):
                return False
        return True

def cal_cnt(mx, zs):
    length = len(zs)
    visited = [False]*mx
    cnt = 0

    for l in range(1, length+1):
        for k in itertools.permutations(zs, l):
            val = int(''.join(map(str, k)))
            if(prime_check(val) and not visited[val]):
                visited[val] = True
                cnt += 1

    return cnt

def solve():
    mx = int(1e7)

    n = int(input())
    for _ in range(n):
        zs = list(map(int, input().rstrip()))
        # print(zs)

        cnt = cal_cnt(mx, zs)
        print(cnt)

solve()