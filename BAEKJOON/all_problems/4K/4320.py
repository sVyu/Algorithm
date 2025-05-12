import sys
input = sys.stdin.readline
import math

def solve():
    x = int(input())
    while(x):
        ans = 1
        minus = True if x < 0 else False
        x = abs(x)
        base = math.isqrt(x)

        for k in range(2, base+1):
            if(x%k == 0):
                cnt = 0
                tx = x
                while(tx%k == 0):
                    tx //= k
                    cnt += 1
                if(tx == 1):
                    if(minus and (cnt%2 == 0)):
                        continue
                    ans = cnt
                    break

        print(ans)
        x = int(input())

solve()