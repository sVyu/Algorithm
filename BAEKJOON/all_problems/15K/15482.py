s1, s2 = input(), input()
len_s1, len_s2 = len(s1), len(s2)

dp = [0]*len_s2
for i in range(len_s1):
    cnt = 0
    for j in range(len_s2):
        if cnt < dp[j]:         cnt = dp[j]
        elif s1[i] == s2[j]:    dp[j] = cnt+1
    # print(i, dp)

print(max(dp))