import sys
input = sys.stdin.readline

N, C = map(int, input().split())
xs = sorted([int(input()) for _ in range(N)])
# print(xs)

lo, hi = 1, xs[N-1]-xs[0]
ans = 1

while lo <= hi:
    mid = (lo+hi)//2

    # üũ
    cnt, px = 1, xs[0]
    for x in xs[1:]:
        if (x-px) >= mid:
            cnt += 1
            px = x

    pos = True if cnt >= C else False
    # print(pos, lo, hi, mid)

    if pos:
        ans = mid
        lo = mid+1
    else:
        hi = mid-1

print(ans)