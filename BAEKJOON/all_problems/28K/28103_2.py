N, M, X = map(int, input().split())
vals = sorted(list(map(int, input().split())), reverse=True)

cnts = [0]*M
# X >= k*vals[i] + (N-k)*vals[M-1]
# (X-N*vals[M-1]) >= k*vals[i] - k*vals[M-1]
# (X-N*vals[M-1])//(vals[i]-vals[M-1]) -> k

for i in range(M-1):
    cnts[i] = min(N, (X-N*vals[-1])//(vals[i]-vals[-1]))
    N -= cnts[i]
    X -= cnts[i]*vals[i]

cnts[-1] = min(N, X//vals[-1])
print(*cnts)