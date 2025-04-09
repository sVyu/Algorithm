import sys
input = sys.stdin.readline
import itertools

def check_pos(arr:list, n:int, s:int):
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if(arr[i] < arr[j]):
                cnt += 1

    return 1 if cnt == s else 0

def solve():
    n, s = map(int, input().split())
    zs = list(map(int, input().split()))

    idxs = []
    for i in range(n):
        if(zs[i] == 0):
            idxs.append(i)
    # print(idxs)

    res_nums = set([i for i in range(1, n+1)])
    for z in zs:
        if(z in res_nums):
            res_nums.remove(z)
    res_nums = list(res_nums)

    if(len(res_nums) == 0):
        print(check_pos(zs, n, s))
        return

    ans = 0
    len_idxs = len(idxs)
    for tis in itertools.permutations(idxs, len_idxs):
        for i in range(len_idxs):
            zs[tis[i]] = res_nums[i]
        ans += check_pos(zs, n, s)

    print(ans)

solve()