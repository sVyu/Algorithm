import sys
input = sys.stdin.readline
from itertools import permutations

def cal_switch(s):
    base = s[0]
    cnt = 0

    for c in s[1:]:
        if(base != c):
            base = c
            cnt += 1

    return cnt

def solve():
    n = int(input().rstrip())
    arr = list(input().rstrip() for _ in range(n))

    base_cnt = sum([cal_switch(el) for el in arr])
    arr = [el[0]+el[-1] for el in arr]
    # print(arr)

    ans = 2000
    for idxs in permutations([i for i in range(n)], n):
        # print(idxs)
        connect_diff_cnt = 0
        for i in range(n-1):
            if(arr[idxs[i]][-1] !=  arr[idxs[i+1]][0]):
                connect_diff_cnt += 1

        ans = min(ans, base_cnt + connect_diff_cnt)

    print(ans)

solve()