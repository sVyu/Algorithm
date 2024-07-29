import sys
input = sys.stdin.readline

def btr_lotus(N, lotus_xs, lotus_idx, lotus_fill, tunnels, favs):
    for x in lotus_xs[lotus_idx]:
        if lotus_fill[x] == -1:
            lotus_fill[x] = lotus_idx

            if lotus_idx < (N-1):
                if btr_lotus(N, lotus_xs, lotus_idx+1, lotus_fill, tunnels, favs):
                    return True
            else:
                pos = True
                for tx1, tx2, n in tunnels:
                    # if favs[tx1][n] != favs[tx2][n]:
                    if favs[lotus_fill[tx1]][n] != favs[lotus_fill[tx2]][n]:
                        pos = False
                        break

                if pos:
                    print("YES")
                    print(*[k+1 for k in lotus_fill])
                    return True

            lotus_fill[x] = -1
    return False

def solve():
    N, M = map(int, input().split())
    favs = [list(map(int, input().split())) for _ in range(N)]
    lotus_xs = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        x1, x2 = lotus_xs[i]
        lotus_xs[i] = [x1-1, x2-1]

    tunnels = [list(map(int, input().split())) for _ in range(M)]
    for i in range(M):
        x1, x2, n = tunnels[i]
        tunnels[i] = [x1-1, x2-1, n-1]
    # print(tunnels)

    lotus_fill = [-1]*N
    if not btr_lotus(N, lotus_xs, 0, lotus_fill, tunnels, favs):
        print("NO")

solve()
