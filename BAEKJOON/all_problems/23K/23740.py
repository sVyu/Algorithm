import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    # print(lines)

    lines.sort(key=lambda x:(x[0], -x[1]))
    # print(lines)

    pre_s = -1
    pre_e = -1
    pre_c = -1
    ans = []

    for s, e, c in lines:
        # print(s, e, c)
        if(s > pre_e):
            ans.append([pre_s, pre_e, pre_c])
            pre_s = s
            pre_e = e
            pre_c = c
        else:
            pre_e = max(pre_e, e)
            pre_c = min(pre_c, c)

    ans.append([pre_s, pre_e, pre_c])
    print(len(ans)-1)
    for line in ans[1:]:
        print(*line)

solve()