import sys
input = sys.stdin.readline
import itertools

def solve():
    n, k = map(int, input().split())
    zs = list(map(int, input().split()))
    # print(zs)

    ans = 0
    for nums in itertools.permutations(zs, n):
        w = 500

        pos = True
        for n in nums:
            w += n
            w -= k

            if(w < 500):
                pos = False
                break

        if(pos):
            ans += 1
    print(ans)

solve()