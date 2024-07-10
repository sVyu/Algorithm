import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    square_N = N**2
    board = [list(map(int, input().split())) for _ in range(square_N)]
    limit = int(1e6)+1

    # sieve
    checks = [True]*limit
    for i in range(2, limit):
        if checks[i]:
            for j in range(i*2, limit, i):
                checks[j] = False

    # 기존 수들 빼주기
    for x in range(square_N):
        for y in range(square_N):
            if board[x][y] > 0:
                checks[board[x][y]] = False

    primes = [i for i in range(500001, limit) if checks[i]]
    primes_idx = 0

    for x in range(square_N):
        for y in range(square_N):
            if board[x][y] == 0:
                board[x][y] = primes[primes_idx]
                primes_idx += 1

    for x in range(square_N):
        print(*board[x])

solve()
