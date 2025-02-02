import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ns = set(map(int, input().split()))
ms = set(map(int, input().split()))
ans = sorted(ns-ms)

print(len(ans))
if(ans):
    print(*ans)