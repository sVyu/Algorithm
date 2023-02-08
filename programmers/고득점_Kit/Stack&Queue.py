# 올바른 괄호
# def solution(s):
#     cnt = 0
#     for a in s:
#         if a == '(':
#             cnt += 1
#         else:
#             if cnt == 0:
#                 return False
#             else:
#                 cnt -= 1

#     return True if cnt == 0 else False

# print(solution("()()"))


# 기능개발
# def solution(progresses, speeds):
#     answer = []
#     n = len(progresses)
#     std_idx = 0

#     while std_idx < n:
#         while progresses[std_idx] < 100:
#             for i in range(std_idx, n):
#                 progresses[i] += speeds[i]

#         cnt = 0
#         for i in range(std_idx, n):
#             if progresses[i] >= 100:
#                 cnt += 1
#             else:
#                 break

#         answer.append(cnt)
#         std_idx += cnt
#         # print(std_idx, progresses)

#     return answer

# print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))


# 주식 가격
# def solution(prices):
#     n = len(prices)
#     stack, answer = [], [0]*n

#     for idx in range(n):
#         while stack and prices[stack[-1]] > prices[idx]:
#             k = stack.pop()
#             answer[k] = idx-k
#         stack.append(idx)

#     while stack:
#         k = stack.pop()
#         answer[k] = idx-k

#     return answer
# print(solution([1,2,3,2,3]))

# 프린터
# from collections import deque
# from heapq import heappush, heappop
# def solution(priorities, location):
#     heap = []
#     for p in priorities:
#         heappush(heap, -p)

#     # que = deque()
#     # for i, p in enumerate(priorities):
#     #     que.append([p, i])
#     que = deque([[p, i] for i, p in enumerate(priorities)])
#     # print(que)

#     cnt = 1
#     while que:
#         while que[0][0] != -heap[0]:
#             que.append(que.popleft())

#         while que[0][0] == -heap[0]:
#             if que[0][1] == location:
#                 return cnt

#             cnt += 1
#             que.popleft()
#             heappop(heap)

# print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))



# 다리를 지나는 트럭
# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     answer = 1

#     que = deque()
#     for t in truck_weights:
#         que.append(t)

#     while que:
#         # print(que)
#         remain_w = weight
#         while que and que[0] <= remain_w:
#             remain_w -= que[0]
#             que.popleft()
#             answer += 1

#         answer = answer -1 + bridge_length

#     return answer

# print(solution(2, 10, [7,4,5,6]))
# print(solution(3, 100, [100, 50]))
# print(solution(3, 100, [100, 100, 100]))


# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     answer = 1

#     truck_que = deque()
#     for t in truck_weights:
#         truck_que.append(t)

#     bridge_que = deque()

#     remain_w = weight
#     while truck_que:
#         cnt = 0
#         while truck_que and truck_que[0] <= remain_w:
#             t = truck_que.popleft()
#             remain_w -= t
#             # answer += 1

#             cnt += 1
#             # bridge_que.append([bridge_t])

#         # answer = answer -1 + bridge_length
#         answer = answer + bridge_length - cnt +1
#         remain_w += bridge_que.popleft()
#         print(bridge_que, truck_que, answer)

#     answer += len(bridge_que)

#     return answer


# print(solution(2, 10, [7,4,5,6]))

