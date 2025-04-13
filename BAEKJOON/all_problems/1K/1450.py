import sys
input = sys.stdin.readline

def calculate_all_ws(len_arr:int, ws:list):
    # len_arr >= 0
    len_result_arr = 2**len_arr
    result_arr = [0]*len_result_arr

    for i in range(len_arr):
        base = 1 << i
        for ti in range(base, 2*base):
            result_arr[ti] = result_arr[ti-base]+ws[i]

    return result_arr

def solve():
    n, c = map(int, input().split())
    ws = list(map(int, input().split()))

    ti = n//2
    ws1, ws2 = calculate_all_ws(ti, ws[:ti]), calculate_all_ws(n-ti, ws[ti:])
    ws1.sort()
    ws2.sort()

    idx_ws1 = len(ws1)-1
    ans = 0

    for w in ws2:
        while((w + ws1[idx_ws1]) > c):
            idx_ws1 -= 1
            if(idx_ws1 < 0): break

        if(idx_ws1 < 0): break
        ans += idx_ws1+1

    print(ans)

solve()

# print(1 << 0)