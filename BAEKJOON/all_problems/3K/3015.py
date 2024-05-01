# solved
import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    n = int(input())
    ans = 0
    s = []
    len_s = 0
    h = -1
    d = defaultdict(int)

    for _ in range(n):
        h = int(input())
        if(s):
            if(s[-1]<h):
                while(s and s[-1]<h):
                    ans += 1
                    d[s.pop()] -= 1
                    len_s -= 1

        if(s and s[-1]==h):
            ans += d[h]
        if(len_s > d[h]):
            ans += 1

        s.append(h)
        len_s += 1
        d[h] += 1

    print(ans)

solve()