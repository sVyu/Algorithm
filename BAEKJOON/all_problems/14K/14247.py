n = int(input())
hs = list(map(int, input().split()))
ns = sorted(list(map(int, input().split())))

ans = sum(hs)+sum([i*ns[i] for i in range(n)])
print(ans)