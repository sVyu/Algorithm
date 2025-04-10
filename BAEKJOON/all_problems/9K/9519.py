import sys
input = sys.stdin.readline

def solve():
    x = int(input())
    s = list(input().rstrip())

    base_s = s
    len_s = len(s)
    # print(len_s)

    one_cycle_cnt = 0
    while(True):
        one_cycle_cnt += 1

        ts = ['_']*len_s
        front_base_idx = ((len_s//2)+(len_s%2))
        for i in range(front_base_idx):
            ts[i] = s[i*2]
        for i in range(len_s//2):
            ts[front_base_idx+i] = s[len_s-1-(len_s%2)-i*2]
        s = ts
        if(base_s == ts):
            break

    s = base_s
    for _ in range(x%one_cycle_cnt):
        ts = ['_']*len_s
        front_base_idx = ((len_s//2)+(len_s%2))
        for i in range(front_base_idx):
            ts[i] = s[i*2]
        for i in range(len_s//2):
            ts[front_base_idx+i] = s[len_s-1-(len_s%2)-i*2]
        s = ts

    print(''.join(s))

solve()