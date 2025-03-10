import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    dts = [list(map(int, input().split())) for _ in range(n)]
    dts = sorted(dts, key=lambda x:(-x[1]))
    # print(dts)

    ans = int(1e10)
    for d, t in dts:
        ans = min(ans, t)
        ans -= d

    print(ans)

if __name__ == "__main__":
    solve()