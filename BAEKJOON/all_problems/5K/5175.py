import sys
input = sys.stdin.readline
import itertools

def solve(k:int):
    M, N = map(int, input().split())
    problems_list = [list(map(int, input().split())) for _ in range(N)]
    problems_list = [[1<<p for p in problems_list[x]] for x in range(N)]
    for x in range(N):
        now = 0
        for p in problems_list[x]:
            now |= p
        problems_list[x] = now
    # print(problems_list)

    target = (1<<(M+1))-2
    base = [i for i in range(N)]
    for cnt in range(1, N+1):
        for comb in itertools.combinations(base, cnt):
            now = 0
            for el in comb: #element
                now |= problems_list[el]
            # print(now)

            if now == target:
                print(f'Data Set {k}: ', end='')
                for el in comb:
                    print(chr(el+65), end=' ')
                return

K = int(input())
for k in range(1, K+1):
    solve(k)
    if k < K:
        for _ in range(2):
            print()