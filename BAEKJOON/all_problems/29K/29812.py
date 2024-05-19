N = int(input())
ss = list(input())
D, M = map(int, input().split())

ans_cost, ans_cnt = 0, 0
pre = -1
t = "HYU"
freq = [0]*26

for i in range(N):
    c = ss[i]
    if c in t:
        ans_cost += min((i-1-pre)*D, M+D)
        pre = i
        freq[ord(c)-65] += 1

ans_cost += min((N-1-pre)*D, M+D)
ans_cnt = min(freq[ord(c)-65] for c in t)

print(ans_cost if ans_cost else "Nalmeok")
print(ans_cnt if ans_cnt else "I love HanYang University")