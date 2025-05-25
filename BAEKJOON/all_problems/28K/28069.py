import sys
input = sys.stdin.readline
from collections import deque

def solve():
    n, k = map(int, input().split())
    if(n <= k):
        print("minigimbob")
        return

    q = deque({0})
    visited = [False]*(n+1)
    visited[0] = True

    for _ in range(k):
        len_q = len(q)
        for _ in range(len_q):
            v = q.popleft()

            for nv in [v+1, v+(v//2)]:
                if(nv > n): continue
                if(visited[nv]): continue
                visited[nv] = True

                q.append(nv)
                if(nv == n):
                    print("minigimbob")
                    return

    print("water")

solve()