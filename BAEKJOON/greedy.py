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
#     print(que.queue)

# print(total_count)
# # # for _ in range(n_card_num - 1):
    
# #     # print(card_num_list)
# #     # card_num_list.sort()
# #     # total_count += card_num_list[0] + card_num_list[1]
# #     # card_num_list.append(card_num_list[0] + card_num_list[1])
# #     # del card_num_list[1], card_num_list[0]

# # # print(total_count)


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


# 1439 뒤집기
# import math

# num = list(map(int, input()))
# # print(num)

# # 앞, 뒤 index 재서 할 수도 있음

# check = 0
# number_statement = num[0]
# for i in range(1, len(num)):
#     if(num[i] != number_statement):
#         check += 1
#         number_statement = num[i]

# print(math.ceil(check/2))


# 16953 A → B

# A, B = map(int, input().split())
# cnt = 0

# while B > A:
#     units_B = B % 10
#     if(units_B % 2 == 0):
#         # print(B)
#         B //= 2
#         cnt += 1
#     elif(units_B == 1):
#         # print(B)
#         B //= 10
#         cnt += 1
#     else:   # 끝자리가 2의 배수나 1이 아닌 경우
#         # print(B)
#         break

# if(B == A): print(cnt + 1)
# else: print(-1)

# 1449 수리공 항승
# hole_num, tape_length = map(int, input().split())
# hole_list = list(map(int, input().split()))
# hole_list.sort()

# cnt_tape = 1
# rest_tape_length = tape_length - 1


# for i in range(1, len(hole_list)):

#     # 현재 테이프로 커버가 되는 경우
#     if(hole_list[i] - hole_list[i-1]) <= rest_tape_length:
#         rest_tape_length -= (hole_list[i] - hole_list[i-1])

#     # 안 되는 경우
#     else:
#         # print(rest_tape_length)
#         rest_tape_length = tape_length -1
#         cnt_tape += 1

# print(cnt_tape)


# 1202 보석 도둑

# 1049 기타줄
# n, m = map(int, input().split())
# string_list = [list(map(int, input().split())) for _ in range(m)]
# # print(string_list)

# min_string6, min_string1 = string_list[0][0], string_list[0][1]

# for i in range(len(string_list)):
#     if(string_list[i][0] < min_string6):
#         min_string6 = string_list[i][0]
#     if(string_list[i][1] < min_string1):
#         min_string1 = string_list[i][1]
# # print(min_string6, min_string1)

# if(min_string6 < (min_string1 * 6)):
#     if(min_string6 < min_string1 * (n%6)):
#         print(min_string6 * ((n//6)+1))
#     else: print(min_string6 * (n//6) + min_string1 * (n%6))
# else:
#     print(min_string1 * n)

# 11000 강의실 배정
# while - for문 : 시간 초과
# 우선순위 큐?
# class_num = int(input())
# class_list = [list(map(int, input().split())) for _ in range(class_num)]
# class_list.sort(key=lambda x:(x[0], x[1]))
# # print(class_list)

# check_list = [0] * class_num
# room_num = 0

# while sum(check_list) != class_num:
#     start_minute = 0
#     room_num += 1
#     for i in range(class_num):
#         if(check_list[i] == 0) & (start_minute <= class_list[i][0]):
#             start_minute = class_list[i][1]
#             check_list[i] = 1

# print(room_num)


# 2720 세탁소 사장 동혁
# num = int(input())
# num_list = [int(input()) for _ in range(num)]

# for i in range(len(num_list)):
#     value = num_list[i]
#     print(value//25, end=' ')
#     value %= 25
#     print(value//10, end=' ')
#     value %= 10
#     print(value//5, end=' ')
#     value %= 5
#     print(value//1)


# 15904 UCPC는 무엇의 약자일까?
# string_list = list(str(input()))
# # print(string_list)

# check = 0
# for i in string_list:
#     if(i == 'U') & (check == 0):
#         check += 1
#     elif(i == 'C') & (check == 1):
#         check += 1
#     elif(i == 'P') & (check == 2):
#         check += 1
#     elif(i == 'C') & (check == 3):
#         check += 1
#         break
    
# if(check == 4): print("I love UCPC")
# else: print("I hate UCPC")


# 2012 등수 매기기
# input() → sys.stdin.readline()
# import sys

# num = int(input())
# num_list = [int(sys.stdin.readline()) for _ in range(num)]
# num_list.sort()
# # print(num_list)

# unsatisfied_point = 0
# for i in range(len(num_list)):
#     unsatisfied_point += abs((i+1) - num_list[i])

# print(unsatisfied_point)


# 1543 문서 검색
# s = input()
# check = input()
# step = 0
# count = 0

# for i in range(len(s)):
#     if((step+1 > len(s)) or (step+len(check)+1 > len(s))):
#     # if(i + len(check) > len(s)):
#         break

#     else:
#         if(s[step+i:step+len(check)+i] == check[0:]):
#             step += len(check)-1   # i가 증가해서 -1
#             count += 1

# print(count)


# 9237 이장님 초대
# num = int(input())
# tree_list = list(map(int, input().split()))
# tree_list.sort(reverse=True)

# max = 0
# for i in range(len(tree_list)):
#     if(max < (tree_list[i] + i + 1)):
#         max = (tree_list[i] + i + 1)
#     else: continue

# print(max + 1)


# 1461 도서관
# n, m = map(int, input().split())
# num_list = list(map(int, input().split()))
# num_list.sort()

# sum = 0

# print(num_list)
# for i in range(num_list):


# 14487 욱제는 효도쟁이야
# num = int(input())
# num_list = list(map(int, input().split()))
# num_list.sort()

# print(sum(num_list[:-1]))


# 1246 온라인 판매
# n, m = map(int, input().split())
# mentioned_price_list = [int(input()) for _ in range(m)]
# mentioned_price_list.sort()

# start_index = 0
# total_price = 0
# max_price = 0
# egg_price = 0

# if(n < m): start_index = m-n

# for i in range(start_index, m):
#     total_price = mentioned_price_list[i] * (m - i)
#     if(max_price < total_price):
#         max_price = total_price
#         egg_price = mentioned_price_list[i]

# print(egg_price, max_price)


# 19539 사과나무
# 시간 초과
# num = int(input())
# num_list = sorted(list(map(int, input().split())))

# for i in range(num - 1):
#     num_list[i] %= 3

# num_list[num-1] = (num_list[num-1] % 3) + 3

# # print(num_list)

# if(sum(num_list)) == 0 :
#     # print("YES")
#     yes_check = True
# elif((sum(num_list) == 1) | (sum(num_list) ==2)):
#     # print("NO")
#     yes_check = False

# not_zero_index = 0
# while sum(num_list) != 0:
#     yes_check = False
#     # 5, 4, 3, 2
#     if ((num_list[not_zero_index] // 2) >= 1):
#         # print(num_list, "2")
#         num_list[not_zero_index] -= 2
#         for j in range(not_zero_index, num):
#             if(num_list[j] >= 1):
#                 num_list[j] -= 1
#                 yes_check = True
#                 break
#         # 사과나무를 조건에 맞게 키울 수 없음
#         if(yes_check == False):
#             # print("NO")
#             break
    
#     elif (num_list[not_zero_index] == 1):
#         # print(num_list, "1")
#         num_list[not_zero_index] -= 1
#         for j in range(not_zero_index, num):
#             if(num_list[j] >= 2):
#                 num_list[j] -= 2
#                 yes_check = True
#                 break
#         if(yes_check == False):
#             break

#     if(num_list[not_zero_index] == 0):
#         not_zero_index += 1

# if(yes_check == True): print("YES")
# else: print("NO")

# num = int(input())
# num_list = sorted(list(map(int, input().split())))

# if(sum(num_list) % 3) != 0:
#     print("NO")
# else:
#     odd_number_count = 0
#     for i in range(num):
#         odd_number_count += (num_list[i] // 2)

#     if(odd_number_count >= (sum(num_list)//3)):
#         print("YES")
#     else: print("NO")

#     # print(odd_number_count)


# 13164 행복 유치원
# n, k  = map(int, input().split())
# num_list = list(map(int, input().split()))

# gap_list = []
# for i in range(n-1):
#     gap_list.append([(num_list[i+1] - num_list[i]), i+1])
# # print(gap_list)
# gap_list.sort(key = lambda x:(-x[0]))
# # print(gap_list)

# top_gap_index_list = []
# for i in gap_list[:k-1]:
#     # print(gap_list[i])
#     top_gap_index_list.append(i[1])
# # print(top_gap_index_list)
# top_gap_index_list.sort()
# # print(top_gap_index_list)

# total_sum = 0
# sum_start_index, sum_end_index = 0, 0

# for i in top_gap_index_list:
#     # print(i)
#     sum_end_index = i
#     total_sum += (num_list[sum_end_index-1] - num_list[sum_start_index])
#     sum_start_index = sum_end_index

# if(sum_end_index != (n-1)):
#     total_sum += num_list[-1] - num_list[sum_end_index]

# print(total_sum)


# 13414 수강신청 dictionary
# https://www.acmicpc.net/problem/13414

# 출력 초과
# 시간 초과
# 틀렸습니다

# import sys

# k, list_len = map(int, sys.stdin.readline().rstrip().split())
# number_list = [str(sys.stdin.readline().rstrip()) for _ in range(list_len)]
# # number_list = [int(sys.stdin.readline().rstrip()) for _ in range(list_len)]

# # 길이 8 체크 코드(추가)
# # new_number_list = []
# for i in number_list:
#     # new_number_list.append(list(str(i)))
#     if(len(list(str(i))) != 8):
#         quit()
# # print(new_number_list[i])

# # dictionary에 하나씩 입력
# register_dict = {}
# for i in range(list_len):
#     register_dict[number_list[i]] = i
# # print(register_dict)

# # 등록 dictionary 의 key, value 거꾸로
# register_dict = dict(map(reversed, register_dict.items()))
# # print(register_dict)
# # print(register_dict.keys(), register_dict.values())

# # 0부터 시작해서 k명 만큼 수강 신청 → print
# count = 0
# for i in range(list_len):
#     if(i in register_dict):
#         # print('{0:08d}'.format(register_dict[i]))   # int
#         print(register_dict[i])                     # str
#         count += 1
#     else: continue
#     if(count == k): break

# import sys

# input = sys.stdin.readline

# K, L = map(int, input().split())

# queue_list = {}

# for i in range(L):
#     studentId = input().rstrip()
#     queue_list[studentId] = i
# print(queue_list)
# print(sorted(queue_list.items(), key=lambda x: x[1]))

# cnt = 0
# for x in sorted(queue_list.items(), key=lambda x: x[1]):
#     cnt += 1
#     if cnt > K:
#         break
#     print(x[0])



# 11509 풍선 맞추기
# 시간 초과
# num = int(input())
# num_list = list(map(int, input().split()))

# # 화살 count 0부터
# arrow_count = 0
# for k in range(num):
#     # 풍선 높이가 다 0이면 (다 터졌으면) break
#     if(sum(num_list) == 0): break

#     # 최고 높이 인덱스 찾기
#     max_height_index = 0
#     for i in range(num):
#         if(num_list[i] > num_list[max_height_index]): max_height_index = i
#     # print(max_height_index)

#     # 최고 높이 인덱스부터 시작해서 풍선이 맞으면 화살 높이 1씩 감소하면서 검사
#     arrow_height = num_list[max_height_index]
#     for j in range(max_height_index, num):
#         if(num_list[j] == arrow_height):
#             num_list[j] = 0
#             arrow_height -= 1
    
#     # 화살 count 증가
#     arrow_count += 1

# print(arrow_count)

# 5% 에서 시간 초과
# import sys

# num = int(sys.stdin.readline())
# num_list = list(map(int, sys.stdin.readline().split()))

# # 화살 카운트, 시작 index 0으로 초기화
# arrow_count = 0
# arrow_start_index = 0

# # 풍선이 다 터지면 (sum의 값이 0이면) break, 아닐 경우 계속 진행
# while True:
#     if(max(num_list) == 0): break

#     # arrow_start_index 조정, 풍선이 없으면(이미 터졌으면) 다음 index
#     while True:
#         if(num_list[arrow_start_index] == 0): arrow_start_index += 1
#         else: break
    
#     # 화살에 맞으면 0을 대입하고 화살 높이 -1
#     arrow_height = num_list[arrow_start_index]
#     for i in range(arrow_start_index, num):
#         if(num_list[i] == arrow_height):
#             num_list[i] = 0
#             arrow_height -= 1
#             # 화살 높이가 0인 경우, for문은 무의미하므로 break
#             if(arrow_height == 0): break

#     # 인덱스, 카운트 증가
#     arrow_start_index += 1
#     arrow_count += 1

# print(arrow_count)

# import sys

# num = int(sys.stdin.readline())
# num_list = list(map(int, sys.stdin.readline().split()))

# # arrow(의 높이)를 저장하는 list와 확인용 index
# arrow_list = []
# i = 0
# # i는 0부터 num-1 까지 1번만, O(n)
# arrow_count = 0
# while True:
#     if(num_list[i] not in arrow_list):
#         arrow_list.append(num_list[i]-1)
#         # print("[1] ,", i, arrow_list)
#         arrow_count += 1
#         i += 1
#     else:
#         wanted_index = arrow_list.index(num_list[i])
#         arrow_list[wanted_index] -= 1
#         # print("[2] ,", i, arrow_list)
#         i += 1
#         if(arrow_list[wanted_index] == 0):
#             del arrow_list[wanted_index]

#     if(i == (num)):
#         break

# print(arrow_count)
# # print(len(arrow_list))


# import sys

# num = int(sys.stdin.readline())
# num_list = list(map(int, sys.stdin.readline().split()))
# num_list.insert(0, 0)

# # 0부터 n까지, index 편의를 위해 크기 1만큼 더 크게 초기화
# arrow_list = [0] * (max(num_list) + 1)
# arrow_count = 0
# for i in range(1, num + 1):
#     if(arrow_list[num_list[i]] == 0):
#         arrow_list[num_list[i] - 1] += 1
#         arrow_count += 1
#     else:
#         arrow_list[num_list[i]] -= 1
#         arrow_list[num_list[i]-1] += 1
#     # print(arrow_list)

# print(arrow_count)


# 23742 Player-based Team Distribution
# 6퍼
# 84퍼
# Done
# import sys
# input = sys.stdin.readline

# # score_list 정렬
# num = int(input())
# score_list = sorted(list(map(int, input().split())))
# # print(score_list)

# # 처음으로 0 이상이 되는 인덱스를 찾음
# # zero_plus_index = 0
# zero_plus_index = -1
# for i in range(num):
#     if(score_list[i] >= 0):
#         zero_plus_index = i
#         break
# # print("zero_plus_index : ", zero_plus_index)

# # 0이상의 값을 모은 plus_list의 sum과 len 계산
# plus_list_sum = sum(score_list[zero_plus_index:])
# plus_list_len = len(score_list[zero_plus_index:])
# # print(plus_list_sum, plus_list_len)

# # zero_plus_index-1 부터 시작해서 (0에 가장 가까운 음수부터) 이 값을 넣었을 때 점수 합의 최대값이 더 높으면 넣음
# minus_list_limit_index = zero_plus_index
# for i in range(zero_plus_index-1, -1, -1):
#     if((score_list[i] + (plus_list_len * plus_list_sum)) <= ((plus_list_len + 1) * (plus_list_sum + score_list[i])) ):
#         plus_list_sum += score_list[i]
#         plus_list_len += 1
#         minus_list_limit_index = i
#     else: break

# # plus 리스트의 점수 합 + 음수 각각 팀들의 합 (음수는 1씩 팀이어야 전체 점수가 높음)
# # print(plus_list_len, plus_list_sum, score_list[:minus_list_limit_index])
# print((plus_list_len * plus_list_sum) + sum(score_list[:minus_list_limit_index]))

'''
# 84퍼 보완
# zero_plus_index = 0 일 경우
# 4
# -4 -3 -2 -1
# -40

# zero_plus_index = -1 일 경우
# 4
# -4 -3 -2 -1
# -10
'''