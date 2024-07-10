import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    square_N = N**2
    board = [list(map(int, input().split())) for _ in range(square_N)]
    limit = int(1e6)

    # sieve
    checks = [i for i in range(limit)]
    for i in range(2, limit):
        if checks[i]:
            for j in range(i*2, limit, i):
                checks[j] = False
    primes = [i for i in range(2, limit) if checks[i]]
    # print(primes[:20])

    rows = [set() for _ in range(square_N)]
    cols = [set() for _ in range(square_N)]
    areas = [[set() for _ in range(N)] for _ in range(N)]

    for x in range(square_N):
        for y in range(square_N):
            if board[x][y]:
                rows[x].add(board[x][y])
                cols[y].add(board[x][y])
                areas[x//N][y//N].add(board[x][y])

    for x in range(square_N):
        for y in range(square_N):
            if board[x][y] == 0:
                for p in primes:
                    can_put = True
                    for arr in [rows[x], cols[y], areas[x//N][y//N]]:
                        for n in arr:
                            if (n%p)*(p%n) == 0:
                                can_put = False

                    if can_put:
                        board[x][y] = p
                        rows[x].add(board[x][y])
                        cols[y].add(board[x][y])
                        areas[x//N][y//N].add(board[x][y])
                        break

    for x in range(square_N):
        print(*board[x])

solve()