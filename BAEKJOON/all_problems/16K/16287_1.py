'''
799994 4
200000 200000 200000 200000
'''

# index error ?
# 그리고 로직 자체도 고쳐야 한다..

import sys
input = sys.stdin.readline

def solve():
    w, n = map(int, input().split())
    ns = list(map(int, input().split()))
    half_n = n//2

    limit = int(4e5)
    arrs = [ns[:half_n], ns[half_n:]]
    dps = [[False]*(limit+1), [False]*(limit+1)]

    for k in range(2):
        arr = arrs[k]
        len_arr = len(arr)

        for i in range(len_arr-1):
            for j in range(i+1, len_arr):
                dps[k][arr[i]+arr[j]] = True
    # print("arr", arrs)

    for i in range(min(w, limit)):
        j = w-i

        if dps[0][i] and dps[1][j]:
            print("YES")
            return

    print("NO")

solve()