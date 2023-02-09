# 베스트 앨범
# from collections import defaultdict
# def solution(genres, plays):
#     ans = []

#     gp = defaultdict(list)
#     gp_idx = defaultdict(int)
#     for i in range(len(genres)):
#         gp[genres[i]].append(plays[i])
#         gp_idx[(genres[i], plays[i])] = i
#     # print(gp_idx)

#     gp = sorted(gp.items(), key=lambda x:(-sum(x[1])))
#     # print(gp)

#     for g, ns in gp:
#         cnt = 0
#         ns = sorted(ns, reverse=True)
#         for n in ns:
#             ans.append((gp_idx[(g, n)]))
#             cnt += 1
#             if cnt >= 2:
#                 break

#     return ans

# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
# print(solution(["classic", "pop"], [500, 600]))

'''
3번 조건 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
를 놓쳐서 수정
'''

# from collections import defaultdict
# def solution(genres, plays):
#     ans = []

#     gp_sum = defaultdict(int)
#     gp_info = defaultdict(list)
#     for i in range(len(genres)):
#         gp_sum[genres[i]] += plays[i]
#         gp_info[genres[i]].append([plays[i], i])
#     # print(gp_idx)

#     gp_sum = sorted(gp_sum.items(), key=lambda x:(-x[1]))
#     # print(gp)

#     for gp, _ in gp_sum:
#         table = sorted(gp_info[gp], key=lambda x:(-x[0], x[1]))
#         # print(table)
#         cnt = 0
#         for record in table:
#             ans.append(record[1])
#             cnt += 1
#             if cnt >= 2:
#                 break

#     return ans

# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
# # print(solution(["classic", "pop"], [500, 600]))


# test
# from collections import defaultdict

# g = defaultdict(list)

# g['k'].append([1, 3, 3])
# g['k'].append([0, 2, 2])

# g = sorted(g.items(), key=lambda x:(x[1]))
# print(g)