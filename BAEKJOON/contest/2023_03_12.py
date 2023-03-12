# AI Network Scholarium I이 개최됩니다!

# B
# 시간 초과...
# 공지 중 C 외의 언어로 풀 수 있음이 보장 되지 않음..
# import sys
# input = sys.stdin.readline

# def init(tree):
#     tree = [0]*(len(tree))

# def show(s, e, nd, l, r, tree):
#     if (e < l) or (r < s): return 0;
#     elif (l <= s) and (e <= r): return tree[nd];

#     mid = (s+e)//2
#     return max(show(s, mid, nd*2, l, r, tree), show(mid+1, e, nd*2+1, l, r, tree))

# def update(s, e, nd, idx, val, tree):
#     if not (s <= idx <= e):
#         return;

#     tree[nd] = max(tree[nd], val)
#     if s == e:
#         tree[nd] = val;
#         return;

#     mid = (s + e) // 2
#     update(s, mid, nd*2, idx, val, tree)
#     update(mid+1, e, nd*2+1, idx, val, tree)

# def cal_tree_len(N):
#     tl = 1
#     while tl < N:
#         tl *= 2
#     tl *= 2
#     return tl

# def solve():
#     N, Q = map(int, input().split())
#     nums = [0] + list(map(int, input().split()))
#     sums = [0]
#     for i in range(1, N+1):
#         sums.append(nums[i]+sums[i-1])
#     # print(sums)

#     tree = [0 for _ in range(cal_tree_len(N))]
#     init(tree)
#     # print(tree)

#     for _ in range(Q):
#         # a, b, c
#         cmds = list(map(int, input().split()))

#         if cmds[0] == 1:
#             update(0, N-1, 1, cmds[1], cmds[1], tree)
#         else: # 2
#             if cmds[1] == cmds[2]:
#                 print(nums[cmds[2]])
#             else:
#                 # 마지막날 제외하고 가장 빠른 날(cmds[2]-1)
#                 needed_day = max(cmds[1]-1, show(0, N-1, 1, cmds[1], cmds[2]-1, tree))
#                 print(sums[cmds[2]] - sums[needed_day])
#         # print(tree)

# solve()