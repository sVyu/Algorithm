# 전력망을 둘로 나누기
# from collections import defaultdict, deque
# def solution(n, wires):
#     answer = n

#     g = defaultdict(list)
#     for u, v in wires:
#         g[u].append(v)
#         g[v].append(u)

#     for std_u, std_v in wires:
#         g[u].remove(v)
#         g[v].remove(u)

#         que = deque()
#         que.append(1)
#         visited = [False] * (n+1)
#         visited[1] = True
#         cnt = 1

#         while que:
#             now_v = que.popleft()
#             # print(now_v)
#             for next_u in g[now_v]:
#                 # if now_v in [std_v, std_u] and u in [std_v, std_u]:
#                 #     continue

#                 if next_u != std_u and not visited[next_u]:
#                     cnt += 1
#                     visited[next_u] = True
#                     que.append(next_u)

#         answer = min(answer, abs(cnt-(n-cnt)))
#         print(std_u, std_v, answer)

#         g[u].append(v)
#         g[v].append(u)

#     return answer

# print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
# print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
# print(solution(8, [[1,2], [2,3], [3, 4], [1, 5], [1, 6],[5, 7], [6, 8]])) # this_case

# clear
# from collections import defaultdict, deque
# def solution(n, wires):
#     answer = n

#     g = defaultdict(list)
#     for u, v in wires:
#         g[u].append(v)
#         g[v].append(u)

#     for std_u, std_v in wires:
#         que = deque()
#         que.append(std_v)
#         visited = [False] * (n+1)
#         visited[std_v] = True
#         cnt = 1

#         while que:
#             now_v = que.popleft()
#             for next_u in g[now_v]:
#                 if next_u != std_u and not visited[next_u]:
#                     cnt += 1
#                     visited[next_u] = True
#                     que.append(next_u)

#         answer = min(answer, abs(cnt-(n-cnt)))

#     return answer

# print(solution(8, [[1,2], [2,3], [3, 4], [1, 5], [1, 6],[5, 7], [6, 8]]))


# 모의고사
# def solution(answers):
#     answer = []

#     w = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
#     len_w = [len(w[0]), len(w[1]), len(w[2])]
#     cnt_w = [0, 0, 0]
#     p = [0, 0, 0]

#     for a in answers:
#         for idx in range(3):
#             if w[idx][p[idx]] == a:
#                 cnt_w[idx] += 1
#             p[idx] = (p[idx]+1) % len_w[idx]
#         # print(p)
#     # print(cnt_w)

#     max_val = max(cnt_w)
#     for idx in range(3):
#         if cnt_w[idx] == max_val:
#             answer.append(idx+1)

#     return answer

# print(solution([1,2,3,4,5]))
# print(solution([1,3,2,4,2]))


# 소수 찾기
# import itertools
# def solution(numbers):
#     answer = 0
#     len_numbers = len(numbers)

#     sieves = [False, False] + [True]*(10**len_numbers)
#     for k in range(2, len(sieves)):
#         if sieves[k]:
#             for kk in range(2*k, len(sieves), k):
#                 sieves[kk] = False

#     num_set = set()
#     for num_len in range(1, len_numbers+1):
#         for ns in itertools.permutations([i for i in range(len_numbers)], num_len):
#             # print(ns)
#             this_n = int("".join(numbers[n] for n in ns))
#             # print(this_n)
#             if sieves[this_n] and this_n not in num_set:
#                 num_set.add(this_n)
#                 answer += 1

#     return answer

# print(solution("17"))
# print(solution("011"))
# print(solution("1234567"))


# 최소직사각형
# def solution(sizes):
#     w, h = 0, 0
#     for s in sizes:
#         s = sorted(s)
#         w = max(w, s[0])
#         h = max(h, s[1])

#     return w * h

# print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))


# 카펫
# def solution(brown, yellow):
#     for yw in range(yellow, 0, -1):
#         if yellow % yw == 0:
#             yh = yellow // yw
#             if (yw+2)*(yh+2)-yw*yh == brown:
#                 return [yw+2, yh+2]

# print(solution(10, 2))


# 효율 개선
# def factorization(n):
#     l = []
#     while n % 2 == 0:
#         l.append(2)
#         n //= 2
#         if n == 1:
#             return l

#     for i in range(3, n+1, 2):
#         while n % i == 0:
#             l.append(i)
#             n //= i
#             if n == 1:
#                 return l

# def all_divisors(l:list):
#     if not l: #yellow가 1인 경우
#         return {1}

#     n_set = set({1})
#     for a in l:
#         tmp_set = set()
#         for n in n_set:
#             if a*n not in n_set:
#                 tmp_set.add(a*n)

#         for n in tmp_set:
#             n_set.add(n)

#     return n_set

# def solution(brown, yellow):
#     for yw in sorted(all_divisors(factorization(yellow)), reverse=True):
#         if yellow % yw == 0:
#             yh = yellow // yw
#             if (yw+2)*(yh+2)-yw*yh == brown:
#                 return [yw+2, yh+2]

# print(solution(10, 2))
# print(solution(8, 1))


# 피로도
# import itertools
# def solution(k, dungeons):
#     ans = 0
#     n = len(dungeons)
    
#     for idxs in itertools.permutations([i for i in range(n)], n):
#         # print(idxs)
#         now_k = k
#         now_cnt = 0

#         for i in idxs:
#             if now_k >= dungeons[i][0]:
#                 now_k -= dungeons[i][1]
#                 now_cnt += 1

#         if now_cnt == n:
#             return n

#         ans = max(ans, now_cnt)

#     return ans

# print(solution(80, [[80,20],[50,40],[30,10]]))



# 모음사전
# pm 09:57 ~ 10:12
# btr(word, ["A", "E", "I", "O", "U"], ['','','','',''], 0, 5, 0)
# def btr(word, vowels, now_list, idx, n, cnt):
#     # alphabet : apb
#     for apb in vowels:
#         now_list[idx] = apb
#         cnt[0] += 1
#         # print(''.join(now_list))
#         if word == ''.join(now_list):
#             return cnt

#         elif idx+1 < n:
#             ans = btr(word, vowels, now_list, idx+1, n, cnt)
#             if ans != None:
#                 return ans

#     now_list[idx] = ''

# def solution(word):
#     return btr(word, ["A","E","I","O","U"], ['','','','',''], 0, 5, [0])[0]

# print(solution("AAAAE"))
# print(solution("AAAE"))
# print(solution("I"))