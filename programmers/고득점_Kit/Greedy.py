# def solution(name):
#     answer = 0
#     name = list(name)
#     # print(name)

#     # cleared -> 처리했거나 할 필요 없는 곳 (0 : not yet, 1 : done)
#     cleared, len_name = [0]*len(name), len(name)
#     # print(len_name)

#     for idx in range(1, len_name):
#         if name[idx] == "A":
#             cleared[idx] = 1
#     idx = 0

#     while sum(cleared) != len_name:
#         if name[idx] != 'A':
#             answer += min(ord(name[idx])-65, 91-ord(name[idx])) 
#         cleared[idx] = 1
#         print(cleared, idx, answer)

#         if sum(cleared) == len_name:
#             break

#         l, r = (idx-1)%len_name, (idx+1)%len_name
#         answer += 1
#         while cleared[l] and cleared[r] and (l != idx):
#             l, r = (l-1)%len_name, (r+1)%len_name
#             answer += 1

#         # 더 이상 처리할 필요가 없는 경우 (ex. 남은 게 모두 A)
#         if l == idx:
#             break

#         # if name[l] != "A":
#         if not cleared[l]:
#             idx = l
#         else:
#             idx = r

#     return answer

# # print(solution("JEROEN"))
# # print(solution("JAN"))
# # print(solution("ABAB"))
# # print(solution("GRAADY"))
# print(solution(input()))

'''
BABAAAAAABAB
'''


# 구명보트
# def solution(people, limit):
#     answer = 0

#     pp = sorted(people)
#     l, r = 0, len(pp)-1
#     left_p = len(pp)
#     while l < r:
#         if pp[l] + pp[r] <= limit:
#             answer += 1
#             left_p -= 2
#             l += 1
#             r -= 1
#         else:
#             r -= 1

#     return answer + left_p

# solution([70, 50, 80, 50], 100)


# 42861 섬 연결하기
# pm 08:44 ~ 09 : 16
# from collections import defaultdict
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])

#     return parent[x]

# def union_parents(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a

# def solution(n, costs):
#     ans = 0
#     parent = [i for i in range(n+1)]
#     costs = sorted(costs, key=lambda x:(x[2]))

#     for a, b, c in costs:
#         if find_parent(parent, a) != find_parent(parent, b):
#             union_parents(parent, a, b)
#             ans += c

#     return ans

# print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))