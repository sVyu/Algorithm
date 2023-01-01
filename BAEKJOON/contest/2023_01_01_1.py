# SciOI 2022 Open Contest

# A번 카드 뽑기
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# N = int(input())
# A = list(map(int, input().split()))

# dd = defaultdict(int)

# for a in A:
#     dd[a] += 1
# # print(dd)

# ans = 1
# for val in dd.values():
#     ans *= (val+1)

# print((ans-1)%(int(1e9)+7))


# B번 - 최대 점수
# from collections import deque

# N, s = map(int, input().split())
# A = list(map(int, input().split()))

# q = deque([[s-1, 0]])
# # max_score = 0
# max_score = [0]*2
# visited = [False]*N
# visited[s-1] = True

# while q:
#     # print(q)
#     # print(visited)
#     a, score = q.popleft()

#     for px in [-1, 1]:
#         if 0 <= a+px < N :
#             if score + A[a+px] >= 0 and not visited[a+px]:
#                 # print(a+px, score + A[a+px])
#                 q.append([a+px, score + A[a+px]])
#                 visited[a+px] = True

#                 if px == -1:
#                     max_score[0] = max(max_score[0], score + A[a+px]) 
#                 else:
#                     max_score[1] = max(max_score[1], score + A[a+px]) 

# # print(max_score)
# print(sum(max_score))

'''
5 3   
100 -10 0 3 7
'''
# import sys
# input = sys.stdin.readline
# from collections import deque

# N, s = map(int, input().split())
# A = list(map(int, input().split()))

# q = deque([[s-1, s-1, 0]])
# p_set = set()
# p_set.add(tuple([s-1, s-1]))
# max_score = 0

# while q:
#     p1, p2, score = q.popleft()
#     # print(p1, p2, score)
#     max_score = max(max_score, score)

#     for px in [-1, 1]:
#         if px == -1 and 0 <= p1+px and score + A[p1+px] >= 0:
#             if tuple([p1+px, p2]) not in p_set:
#                 p_set.add(tuple([p1+px, p2]))
#                 q.append([p1+px, p2, score + A[p1+px]])

#         elif px == 1 and p2+px < N and score + A[p2+px] >= 0:
#             if tuple([p1, p2+px]) not in p_set:
#                 p_set.add(tuple([p1, p2+px]))
#                 q.append([p1, p2+px, score + A[p2+px]])

# print(max_score)


# D번 - 직육면체
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     A, B, C, p = map(int, input().split())
#     cnt = 0

#     for k in [A, B, C]:
#         if k % p == 0:
#             cnt += 1

#     print(1 if cnt >= 2 else 0)