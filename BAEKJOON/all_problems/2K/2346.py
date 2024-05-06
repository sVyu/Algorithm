from collections import deque

N = int(input())
ns = list(map(int, input().split()))

q = deque([i for i in range(1,N+1)])
while(q):
    b = q.popleft()
    print(b, end=' ')

    if not q: break
    move = ns[b-1]

    if move > 0:
        for _ in range(move-1):
            q.append(q.popleft())
    else:
        for _ in range(-move):
            q.appendleft(q.pop())

    # print(q)