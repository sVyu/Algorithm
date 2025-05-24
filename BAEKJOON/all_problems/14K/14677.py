import sys
input = sys.stdin.readline
from collections import deque

def solve():
    _ = int(input())
    base_s = tuple(input().rstrip())
    # print(s)

    target_alpha = "BLD"
    target_alpha_idx = 0

    q = deque({base_s})
    # print(q.popleft())

    ans = 0
    while(q):
        check = False

        target = target_alpha[target_alpha_idx]
        len_q = len(q)

        s_set = set()
        for _ in range(len_q):
            s = q.popleft()
            if(len(s) == 0): break

            if(s[0] == target):
                new_s = s[1:]
                if(new_s not in s_set):
                    s_set.add(new_s)
                    q.append(new_s)
                    check = True
            if(s[-1] == target):
                new_s = s[:-1]
                if(new_s not in s_set):
                    s_set.add(new_s)
                    q.append(new_s)
                    check = True

        if(check): ans += 1
        target_alpha_idx = (target_alpha_idx+1)%3

    print(ans)

solve()