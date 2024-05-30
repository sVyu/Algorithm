N, A, B = map(int, input().split())
aa = sorted(list(map(int, input().split())), reverse=True)
bb = [0]+sorted(list(map(int, input().split())), reverse=True)

bidx = min(N//2, B)
aidx = N-2*bidx

while aidx < (A-1) and bidx:
    if sum(aa[aidx:aidx+2]) > bb[bidx]:
        aidx += 2
        bidx -= 1
    else:
        break

# print(aidx, bidx)
print(sum(aa[:aidx])+sum(bb[:bidx+1]))