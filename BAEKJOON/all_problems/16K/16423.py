import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    ns = [list(map(int, input().split())) for _ in range(n)]
    for k in range(n, 0, -1):
        cnt = 0
        for a, b in ns:
            if a <= k <= b:
                cnt += 1

        if k == cnt:
            print(k)
            return

    print(-1)

solve()