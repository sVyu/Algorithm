# dp 초기값 0 or -1 ,, 차이가 없어야 하는데?
# math.sqrt, math.isqrt

import sys
input = sys.stdin.readline
import math

n = int(1e6)
mod = int(1e6)
dp = [-2]*(n+1) # 
dp[0] = 1

for i in range(1, n+1):
    if 100 <= i <= 200:
        print("i", i, int(i-math.sqrt(i)), int(math.log(i)), int(i*math.sin(math.radians(i))*math.sin(math.radians(i))))
    # dp[i] = (dp[int(i-math.sqrt(i))]+dp[int(math.log(i))]+dp[int(i*((math.sin(math.radians(i)))**2))])%mod

k = int(input())
while k != -1:
    print(dp[k])
    k = int(input())