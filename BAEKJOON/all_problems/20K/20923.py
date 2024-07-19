import sys
input = sys.stdin.readline
from collections import deque

def check_win(do:deque, su:deque, gdo:deque, gsu:deque):
    if (gdo and gdo[0] == 5) or (gsu and gsu[0] == 5):
        while gsu: do.append(gsu.pop())
        while gdo: do.append(gdo.pop())
    elif gdo and gsu and (gdo[0]+gsu[0] == 5):
        while gdo: su.append(gdo.pop())
        while gsu: su.append(gsu.pop())

def solve():
    N, M = map(int, input().split())
    do, su = deque(), deque()
    for _ in range(N):
        a, b = map(int, input().split())
        do.appendleft(a)
        su.appendleft(b)
    # print(do, su)

    # g: ground
    gdo, gsu = deque(), deque()
    while do and su:
        gdo.appendleft(do.popleft())
        if not do: break
        check_win(do, su, gdo, gsu)
        M -= 1
        if M == 0: break

        gsu.appendleft(su.popleft())
        if not su: break
        check_win(do, su, gdo, gsu)
        M -= 1
        if M == 0: break

    if len(do) > len(su):   print("do")
    elif len(do) < len(su): print("su")
    else:                   print("dosu")

solve()