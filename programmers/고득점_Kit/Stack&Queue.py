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
#     ans = 0

#     truck_que = deque(truck_weights)
#     # print(truck_que)
#     bridge_que = deque()

#     remain_w = weight
#     while truck_que:
#         # 무게 되는 선에서 계속 추가
#         while truck_que and remain_w >= truck_que[0]:
#             remain_w -= truck_que[0]

#             ans += 1
#             for idx in range(len(bridge_que)):
#                 bridge_que[idx][1] -= 1
#             bridge_que.append([truck_que.popleft(), bridge_length])

#             if bridge_que[0][1] == 0:
#                 remain_w += bridge_que.popleft()[0]
#         # print("[1]", bridge_que, truck_que, ans)

#         # 제일 앞에 있는 트럭 빼기, 새 트럭 들여올 수 있으면 추가
#         # while bridge_que:
#         if bridge_que:
#             remain_w += bridge_que[0][0]
#             val = bridge_que.popleft()[1]

#             ans += val
#             for idx in range(len(bridge_que)):
#                 bridge_que[idx][1] -= val

#             if truck_que and remain_w >= truck_que[0]:
#                 remain_w -= truck_que[0]
#                 bridge_que.append([truck_que.popleft(), bridge_length])
#         # print("[2]", bridge_que, truck_que, ans)

#     # 나머지 처리
#     if bridge_que:
#         ans += bridge_que.pop()[1]

#     return ans

# print(solution(2, 10, [7,4,5,6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
# print(solution(1, 10, [1, 1]))

# print(solution(2, 4, [10,10,10,10,10,10]))
# print(solution(5, 5, [2,2,2,2,1,1,1,1,1]))
# print(solution(10, 10, [10, 9, 8, 7, 6, 5, 4, 3]))

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     # [0, 0, 7, 4, 5, 6]
#     bridge = [0 for _ in range(bridge_length)] + truck_weights
#     while bridge:
#         # 앞에서부터 하나씩 제거하면서
#         bridge.pop(0)
#         # 다리 길이 만큼의 트럭 무게가 
#         # 다리가 견딜 수 있는 무게보다 큰 경우
#         if sum(bridge[:bridge_length]) > weight:
#             # 대기
#             bridge.insert(bridge_length-1, 0)
#         # 반복마다 시간 증가
#         answer += 1
#         print(bridge)
#     return answer

# print(solution(10, 10, [7,4,5,6]))


# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     ans, now_w = 0, 0
#     q_bridge, q_truck = deque([0]*bridge_length), deque(truck_weights)
#     # print(q_bridge)

#     while q_truck:
#         now_w -= q_bridge.popleft()

#         if (weight - now_w) >= q_truck[0]:
#             val = q_truck.popleft()
#             now_w += val
#             q_bridge.append(val)
#         else:
#             q_bridge.append(0)

#         ans += 1

#     return ans + bridge_length

# print(solution(2, 10, [7,4,5,6]))