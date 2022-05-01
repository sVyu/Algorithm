# # 2839 설탕 배달
# num = int(input())
# num_5kg = 0
# backup_num = num

# for i in range(num//5, -1, -1):
#     num_5kg = i
#     num = backup_num - num_5kg * 5
#     if(num % 3 == 0):
#         print(num_5kg + (num//3))
#         quit()
#     else: continue

# print(-1)


# 11399 ATM
# num = int(input())
# num_list = list(map(int, input().split()))
# num_list.sort()
# total_min, certain_index_min = 0, 0

# for i in range(len(num_list)):
#     certain_index_min += num_list[i]
#     total_min += certain_index_min

# print(total_min)


# 1931 회의실 배정
# num = int(input())
# num_list = [list(map(int, input().split())) for _ in range(num)]
# meeting_end_time = 0
# count = 0
# # 예시 데이터는 정렬한 걸 줬는데, 설명에는 정렬 데이터를 준다는 말이 없다
# num_list.sort(key=lambda x: (x[1], x[0]))

# for i in range(len(num_list)):
#     if(num_list[i][0] >= meeting_end_time):
#         meeting_end_time = num_list[i][1]
#         count += 1

# print(count)


# 1026 보물
# num = int(input())
# a_list = list(map(int, input().split()))
# b_list = list(map(int, input().split()))

# new_a_list = [0] * num
# c_list = [0] * num

# a_list.sort(reverse=True)
# # print(a_list)

# # 조건 : b_list는 재배열하면 안 됨 → 하면 되게 쉬워짐
# # 제일 작은 b_list index를 찾을 것
# # 거기서부터 제일 큰 a_list 값을 할당할 것

# for i in range(num):
#     min = 101
#     min_index = 0

#     for j in range(len(b_list)):
#         if(b_list[j] < min) & (c_list[j] == 0):
#             min = b_list[j]
#             min_index = j
    
#     c_list[min_index] = 1
#     new_a_list[min_index] = a_list[i]

# sum = 0
# for i in range(num):
#     sum += new_a_list[i] * b_list[i]

# # print(new_a_list)
# print(sum)


# 1946 사원
# 시간 초과
# 출력 초과
# 출력 초과
# 시간 초과
# import sys

# num_test_case = int(input())
# ans_list = []

# for _ in range(num_test_case):
#     num_applicant = int(input())
#     applicant_score_list = [list(map(int, sys.stdin.readline().split())) for _ in range(num_applicant)]
#     # print(applicant_score_list)

#     applicant_score_list.sort(key=lambda x:(x[0]))
#     # print(applicant_score_list)

#     count = 1
#     col2_min = applicant_score_list[0][1]
#     for i in range(1, len(applicant_score_list)):
#         if(applicant_score_list[i][1] < col2_min):
#             col2_min = applicant_score_list[i][1]
#             count += 1
#         else: continue # (applicant_score_list[i][1] > col2_min)
    
#     print(count)


# 1715 카드 정렬하기
# 출력 초과
# 시간 초과
# 우선순위 큐

# import sys
# from queue import PriorityQueue

# n_card_num = int(input())
# card_num_list = [int(sys.stdin.readline()) for _ in range(n_card_num)]
# total_count = 0

# que = PriorityQueue()   # size default : infinite

# for i in range(n_card_num):
#     que.put(card_num_list[i])

# # for _ in range(n_card_num):
# #     print(que.get())

# for _ in range(n_card_num - 1):
#     new_card_num = que.get() + que.get()
#     total_count += new_card_num
#     que.put(new_card_num)

# print(total_count)
# # for _ in range(n_card_num - 1):
    
#     # print(card_num_list)
#     # card_num_list.sort()
#     # total_count += card_num_list[0] + card_num_list[1]
#     # card_num_list.append(card_num_list[0] + card_num_list[1])
#     # del card_num_list[1], card_num_list[0]

# # print(total_count)


# 1339 단어 수학
# from queue import PriorityQueue

# num = int(input())
# num_list = [list(str(input())) for _ in range(num)]
# # print(num_list)
# # value_list = [[0] * 10 for _ in range(2)]
# value_list = [0] * 10

# que = PriorityQueue()

# for i in range(num):
#     value = 1
#     for j in range(len(num_list[i])-1, -1, -1):
#         value_list[(ord(num_list[i][j]))-65] += value   # A : 65
#         value *= 10

# # print(value_list)

# # for i in range(10):
# #     value = 9 - i
# #     max_index = i
# #     for j in range(i, 10):
# #         if(value_list[0][j] > value_list[0][max_index]):
# #             max_index = j
# #     value_list[1][max_index] = value

# for i in range(10):
#     que.put(value_list[i])

# value = 0
# sum = 0
# for _ in range(10):
#     sum += que.get() * value
#     value += 1

# print(sum)

# 런타임 에러(Index Error)

# num = int(input())
# num_list = [list(str(input())) for _ in range(num)]
# value_list = [0] * 26
# # value_list = [0] * 10     # 이게 낚시였네
# # print(num_list)

# for i in range(num):
#     value = 1
#     for j in range(len(num_list[i])-1, -1, -1):
#         value_list[(ord(num_list[i][j]))-65] += value   # A : 65
#         value *= 10

# # print(value_list)

# # for i in range(10):
# #     que.put(value_list[i])

# # value = 0
# # sum = 0
# # for _ in range(10):
# #     sum += que.get() * value
# #     value += 1

# sum = 0
# value_list.sort(reverse=True)
# for i in range(10):
#     if(value_list[i] == 0): break 
#     else: sum += value_list[i] * (9 - i)

# # print(value_list)
# print(sum)
