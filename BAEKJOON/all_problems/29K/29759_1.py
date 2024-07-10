import math

def find_divisors(n):
    divs = set()
    for k in range(1, math.isqrt(n)+1):
        if n % k == 0:
            divs.add(k)
            divs.add(n//k)

    return divs

def solve():
    N = int(input())
    square_N = N*N
    board = [list(map(int, input().split())) for _ in range(square_N)]

    limit = int(1e6)
    ns = [True]*limit

    deletes = sorted([board[x][y] for x in range(square_N) for y in range(square_N) if board[x][y]])
    # print(deletes)

    # divisors(약수들) 확인
    divs_set = set({1})
    for d in deletes:
        for divisor in find_divisors(d):
            divs_set.add(divisor)
    divs_set.remove(1)

    # divs 기반 sieve, d값 자체도 False 처리
    for d in sorted(divs_set):
        if ns[d]:
            for i in range(d, limit, d):
                ns[i] = False

    # sieve
    for i in range(2, limit):
        if ns[i]:
            for j in range(2*i, limit, i):
                ns[j] = False

    # board에 값 넣어주기
    primes = [i for i in range(2, limit) if ns[i]]
    primes_idx = 0
    for x in range(square_N):
        for y in range(square_N):
            if board[x][y] == 0:
                board[x][y] = primes[primes_idx]
                primes_idx += 1

    # 출력
    for x in range(square_N):
        print(*board[x])

solve()
