import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    ns = sorted(list(map(int, input().split())))

    tot = sum(ns)
    find = False
    for n in ns[::-1]:
        rest_tot = tot-n
        if n < rest_tot:
            print(tot)
            find = True
            break

        tot = rest_tot

    if not find:
        print(0)