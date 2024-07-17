N, M, X = map(int, input().split())
vals = sorted(list(map(int, input().split())), reverse=True)

cnts = [0]*M
for i in range(M):
    lo, hi = 0, N
    while lo <= hi:
        mid = (lo+hi)//2
        tot_val = mid*vals[i] + (N-mid)*vals[-1]

        if tot_val <= X:
            lo = mid+1
            cnts[i] = mid
        else:
            hi = mid-1

    N -= cnts[i]
    X -= cnts[i]*vals[i]

print(*cnts)