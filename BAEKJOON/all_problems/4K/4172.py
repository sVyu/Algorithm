import sys
input = sys.stdin.readline
import math

n = int(1e6)
mod = int(1e6)
dp = [0]*(n+1)
dp[0] = 1

for i in range(1, n+1):
    dp[i] = (dp[int(i-math.sqrt(i))]+dp[int(math.log(i))]+dp[int(i*(math.sin(i)**2))])%mod

k = int(input())
while k != -1:
    print(dp[k])
    k = int(input())