import sys
input = sys.stdin.readline

def hanoi(dep, s, tmp, e):
    if(dep == 1):
        print(s, e)
        return

    hanoi(dep-1, s, e, tmp)
    hanoi(1, s, tmp, e)
    hanoi(dep-1, tmp, s, e)

def solve():
    n = int(input())
    print(2**n-1)
    if(n > 20): return
    hanoi(n, 1, 2, 3)

solve()