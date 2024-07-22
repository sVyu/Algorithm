import itertools

N = int(input())
ns = list(map(int, input().split()))

ans = 0
for tns in itertools.permutations(ns, N):
    sums = [0]*N
    sums[0] = tns[0]
    for i in range(1, N):
        sums[i] = sums[i-1]+tns[i]
    # print(set(sums))

    tmp = 0
    for n in sums:
        if (n+50) in sums:
            tmp += 1

    ans = max(ans, tmp)

print(ans)