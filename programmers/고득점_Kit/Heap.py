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