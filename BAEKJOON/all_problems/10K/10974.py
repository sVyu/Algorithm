def btr(checks, idx, N, ans):
    for n in range(1, N+1):
        if not checks[n]:
            checks[n] = True
            ans[idx] = n

            if idx < N:
                btr(checks, idx+1, N, ans)
            else:
                print(*ans[1:])

            checks[n] = False

def solve():
    N = int(input())
    checks = [False]*(N+1)
    ans = [-1]*(N+1)

    btr(checks, 1, N, ans)

solve()