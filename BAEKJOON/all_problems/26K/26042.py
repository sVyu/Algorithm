import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque()
max_q_len = 0
now_q_len = 0
ans = int(1e10)

for _ in range(n):
    zs = list(map(int, input().split()))
    if(zs[0] == 1):
        q.append(zs[1])
        now_q_len += 1
        if(max_q_len == now_q_len):
            if(ans > zs[1]):
                ans = zs[1]
        elif(max_q_len < now_q_len):
            max_q_len = now_q_len
            ans = zs[1]
    else:
        q.popleft()
        now_q_len -= 1

print(max_q_len, ans)