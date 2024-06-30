import sys
input = sys.stdin.readline

N = int(input())
ns = [0]+sorted([int(input()) for _ in range(N)], reverse=True)

ans = sum([ns[i] for i in range(1, N+1) if i % 3 != 0])
print(ans)