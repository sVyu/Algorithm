import sys

def solve():
    n, k = map(int, input().split())

    cnt_a = n//2
    cnt_b = n-cnt_a
    if(k > cnt_a*cnt_b):
        print(-1)
        return

    quo = k // cnt_b
    mod = k % cnt_b

    for _ in range(quo):
        print("A", end='')
        n -= 1

    for res in range(cnt_b, 0, -1):
        if(res == mod):
            print("A", end='')
            n -= 1
        print("B", end='')
        n -= 1

    for _ in range(n):
        print("A", end='')

solve()