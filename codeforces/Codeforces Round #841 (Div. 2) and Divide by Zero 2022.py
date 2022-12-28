# A. Joey Takes Money
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     t = int(input())
#     a = sorted(list(map(int, input().split())))
    
#     ans = 1
#     for idx in range(t):
#         ans *= a[idx]
#     ans += (t-1)

#     print(ans * 2022)


# B. Kill Demodogs
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     # print(((n*(n+1)*(4*n-1)//6)*2022)%((1e9)+7))
#     print(((n*(n+1)*(4*n-1)//6)*2022)%(int(1e9)+7))