n, m = map(int, input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = sorted(map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

# print(g)
pos = [[True]*5 for _ in range(n+1)]
# print(pos)

ans = [0]*(n+1)
for x in range(1, n+1):
    for y in range(1, 5):
        if(pos[x][y]):
            ans[x] = y
            for nx in g[x]:
                pos[nx][y] = False
            break

print(*ans[1:], sep='')