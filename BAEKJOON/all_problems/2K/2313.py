tot_val = 0
tot_ans_idxs = []

for _ in range(int(input())):
    L = int(input())
    ns = list(map(int, input().split()))
    # print(ns)

    max_val = ns[0]
    base_idx = 0
    ans_idx_gap = 0
    ans_idxs = [0, 0]

    dp = [0]*L
    dp[0] = ns[0]
    for i in range(1, L):
        dp[i] = ns[i]
        if dp[i-1] <= 0:
            base_idx = i
        else:
            dp[i] += dp[i-1]

        if max_val <= dp[i]:
            if max_val == dp[i] and ans_idx_gap <= (i-base_idx):
                continue
            max_val = dp[i]
            ans_idx_gap = i-base_idx
            ans_idxs = [base_idx, i]

    tot_val += dp[ans_idxs[1]]
    tot_ans_idxs.append([ans_idxs[0]+1, ans_idxs[1]+1])

print(tot_val)
for idxs in tot_ans_idxs:
    print(*idxs)