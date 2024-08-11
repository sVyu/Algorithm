N = int(input())
ns = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for s in range(1, 4):
    find = [False]*4
    find[s] = True
    right_cnt = 0

    for a, b, g in ns:
        find[a], find[b] = find[b], find[a]
        if find[g]:
            right_cnt += 1

    ans = max(ans, right_cnt)

print(ans)