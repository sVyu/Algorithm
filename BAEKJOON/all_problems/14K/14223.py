import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    xys = [list(map(int, input().split())) for _ in range(n)]

    mx = int(1e10)
    ans = mx*mx

    for i in range(n-1):
        for j in range(i+1, n):
            new_xys = [xys[k] for k in range(n) if k not in [i, j]]
            # print(new_xys)

            min_x, min_y = mx, mx
            max_x, max_y = -mx, -mx
            for x, y in new_xys:
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)

            # print(min_x, min_y, max_x, max_y)
            ans = min(ans, (max(max_x-min_x, max_y-min_y)+2)**2)

    print(ans)

solve()