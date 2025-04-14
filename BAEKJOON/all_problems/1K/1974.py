def solve():
    n = int(input())
    zs = [-1] + list(map(int, input().split()))

    # lis - O(NlogN)
    lis = [-1]*(10001)
    max_lis_idx = 0

    # ans dp
    dp = [-1]*(n+1)

    for i in range(1, n+1):
        z = zs[i]
        if(z > lis[max_lis_idx]):
            max_lis_idx += 1
            lis[max_lis_idx] = z
            dp[i] = max_lis_idx
            continue

        l, r = 1, max_lis_idx
        ti = -1
        while(l <= r):
            mid = (l+r)//2

            if(z <= lis[mid]):
                r = mid-1
                ti = mid
            else:
                l = mid+1
        # print(i, ti)

        lis[ti] = z
        dp[i] = ti

    ans = []
    target_dp_val = max(dp)
    for i in range(n, 0, -1):
        if(dp[i] == target_dp_val):
            ans.append(i)
            target_dp_val -= 1

    print(len(ans))
    print(*ans[::-1])

for _ in range(int(input())):
    solve()