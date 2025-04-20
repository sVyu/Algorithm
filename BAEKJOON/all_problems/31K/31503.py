import sys
input = sys.stdin.readline

def cal_lis_and_dp(n, zs):
    dp = [0]*(n+1)
    # lis - O(NlogN)
    lis = [-3_000_000_000]*(int(3e5)+1)
    max_lis_idx = 0

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

    return dp

def solve():
    n, q = map(int, input().split())
    base_zs = list(map(int, input().split()))

    zs = [0] + base_zs[:]
    dp1 = cal_lis_and_dp(n, zs)
    # print(dp1)

    zs = [0] + [-z for z in base_zs[:][::-1]]
    dp2 = [0] + cal_lis_and_dp(n, zs)[::-1]
    # print(dp2)

    for _ in range(q):
        t = int(input())
        print(dp1[t]+dp2[t]-1)

solve()