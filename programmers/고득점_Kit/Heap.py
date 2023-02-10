# 더 맵게 
# from heapq import heapify, heappush, heappop
# def solution(scoville, K):
#     heap = scoville
#     len_heap = len(heap)

#     ans = 0
#     heapify(scoville)
#     while heap and heap[0] < K:
#         # heappush()
#         if len_heap < 2:
#             break
#         f, s = heappop(heap), heappop(heap)
#         heappush(heap, (f+2*s))

#         ans += 1
#         len_heap -= 1

#     if heap[0] < K:
#         ans = -1

#     return ans

# solution([1,2,3,9,10,12], 7)


# 이중 우선순위 큐
# from heapq import heappush, heappop
# def solution(operations):
#     min_heap, max_heap = [], []
#     exec_check = [False] * len(operations)

#     for idx in range(len(operations)):
#         cmd, val = operations[idx].split()
#         val = int(val)

#         if cmd == 'I':
#             heappush(min_heap, [val, idx])
#             heappush(max_heap, [-val, idx])
#         else: # D
#             if val == -1:
#                 while min_heap and exec_check[min_heap[0][1]]:
#                     heappop(min_heap)
#                 if min_heap:
#                     exec_check[min_heap[0][1]] = True
#                     heappush(max_heap, [-min_heap[0][0], min_heap[0][1]])
#                     heappop(min_heap)

#             else:
#                 while max_heap and exec_check[max_heap[0][1]]:
#                     heappop(max_heap)
#                 if max_heap:
#                     exec_check[max_heap[0][1]] = True
#                     heappush(min_heap, [-max_heap[0][0], max_heap[0][1]])
#                     heappop(max_heap)

#     while min_heap and exec_check[min_heap[0][1]]: heappop(min_heap)
#     while max_heap and exec_check[max_heap[0][1]]: heappop(max_heap)

#     return [-max_heap[0][0], min_heap[0][0]] if min_heap else [0,0]

# print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
# print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))


# 디스크 컨트롤러
# from collections import deque
# from heapq import heappush, heappop
# def solution(jobs):
#     ans, now_time = 0, 0

#     # heap이 빌 경우를 가정해서 x[1]까지 정렬해야 함
#     que = deque(sorted(jobs, key=lambda x:(x[0], x[1])))
#     # print(que)
#     heap = []

#     while que or heap:
#         # 현재 시간 기점으로 처리 가능한 모든 작업들 heap에 넣음
#         # [실행시간, 작업요청시간]으로 순서 변경
#         while que and now_time >= que[0][0]:
#             heappush(heap, [que[0][1], que[0][0]])
#             que.popleft()
#         # heap이 비었을 경우 (하드디스크에 작업이 없을 경우)
#         if not heap: # and que
#             heappush(heap, [que[0][1], que[0][0]])
#             que.popleft()

#         if now_time > heap[0][1]:
#             ans += now_time - heap[0][1]
#         else:
#             now_time = heap[0][1]

#         ans += heap[0][0]
#         now_time += heap[0][0]
#         heappop(heap)

#     return ans // len(jobs)

# print(solution([[0, 3], [1, 9], [2, 6]]))