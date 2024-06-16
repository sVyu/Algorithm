cmds = list(input())
swaps = [[0, 1], [1, 2], [0, 2]]
ans = [1, 0, 0]

for c in cmds:
    l, r = swaps[ord(c)-65]
    ans[l], ans[r] = ans[r], ans[l]
# print(ans)

for i in range(3):
    if ans[i]:
        print(i+1)