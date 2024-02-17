# 10869 사칙연산

# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(int(a/b)) # 아니 ㅋㅋㅋ
# print(a%b)


# 10430 나머지
# A, B, C = map(int, input().split())
# print((A+B)%C)
# print(((A%C)+(B%C))%C)
# print((A*B)%C)
# print((A%C)*(B%C)%C)

# 2558 A + B -2
# a = int(input())
# b = int(input())
# print(a+b)
# a, b = map(int, input().split())
# print(a+b)

# 2588 곱셈
"""
a = int(input())
b = int(input())
b_temp = b
c = []
while b_temp > 1:
    # print(b_temp)
    c.append(int(b_temp%10))
    b_temp /= 10

# print(c)
# c.reverse()
# print(c)

while len(c):
    # print(c[0])
    print(a*c[0])
    del c[0]

print(a*b)
# 머리 속에 로직은 그려지는데 코드 문법이..
# for문으로 뒤에서부터 10 → 100 으로 나누어서 각 자리수의 숫자로 분리
# 이를 순서대로 하나씩 출력, 최종적으로는 단순 곱셈값 혹은 더한값 출력
# I did it !
"""

# 3046 R2

# S = (R1 + R2)/2
# R2 = 2S -R1

# a, b = map(int, input().split())
# print(2*b - a)

# 2163 초콜릿 자르기
# logical thinking problem
# a, b = map(int, input().split())
# if a > b:
#     a, b = b, a
# print((b-1)+((a-1)*b))

# 11021 A+B-7
# 11022 A+B - 8

# row_num = int(input())
# num_list = []
# check = 0

# while check < row_num:
#     num_list.append([])
#     a, b = map(int, input().split())
#     num_list[check].extend([a, b])
#     check += 1

# # print(num_list)

# check = 0
# while check < row_num:
#     # print("Case #{0}: {1}" .format(check+1, num_list[check][0] + num_list[check][1]))
#     print("Case #{0}: {1} + {2} = {3}" .format(check+1, num_list[check][0], \
#             num_list[check][1], num_list[check][0]+num_list[check][1]))
#     check += 1


# 10699 오늘 날짜

# YYYY-MM-DD
# 채점 서버는 시간대 UTC+0, 즉 9시간을 빼야 함
# import datetime
# from datetime import date

# # 2022-04-25
# # today = date.today()
# # print(today)
# # 이게 정답..? 9시간 연산을 안 넣었는데..
# # 안 넣는 게 맞는 답

# # 2022-04-25 16:13:07.465844
# # d = datetime.datetime.now()
# # print(d)

# # 07:00:00
# # test1 = datetime.time(7)
# # print(test1)

# # 시간 연산 → timedelta
# """
# # d = date.today()
# # print(d)

# # td = datetime.timedelta(hours=23)
# # print(d + td)
# """

# now = datetime.datetime.now()
# td = datetime.timedelta(hours=10)

# ans = now + td
# # print(now+td)
# print(ans)


# 7287 등록 - 크롤링
# print("14")
# print("vyu")

# 2525 오븐 시계
# a, b = map(int, input().split())
# gap = int(input())

# b += gap
# while b >= 60:
#     b -= 60
#     a += 1

# if a >= 24:
#     a -= 24

# print(a, b)


# 2530 인공지능 시계
# a, b, c = map(int, input().split())
# gap = int(input())

# c += gap
# if c >= 60:
#     # b += int(c/60)
#     b += c//60
#     c %= 60

# if b >= 60:
#     a += b//60
#     b %= 60

# if a >= 24:
#     a %= 24
#     # a -= 24

# print(a, b, c)


# 2914 저작권
# a, b = map(int, input().split())
# print(a*(b-1)+1)


# 5355 화성 수학
# 조금 더 효율적인 코드 작성이 가능하지 않을까..

# num = int(input())
# exp_list = []
# row_check = 0

# while row_check < num:
#     exp_list.append(input().split())

#     # exp_list.append([])
#     # exp_list[row_check].extend(input().split())
#     # 이 쉬운 걸 놓쳤네

#     row_check += 1
#     # char = num(input())
#     # exp_list[row_check].append(char)

# # print(exp_list)

# row_check = 0
# ans = 0

# while row_check < num:
#     col_check = 1
#     ans = float(exp_list[row_check][0])
#     # print(ans)
#     # print("len : {0}", len(exp_list[row_check]))

#     while col_check < len(exp_list[row_check]):
#         if exp_list[row_check][col_check] == '@':
#             ans *= 3
#         elif exp_list[row_check][col_check] == '%':
#             ans += 5
#         elif exp_list[row_check][col_check] == '#':
#             ans -= 7
#         else:
#             print("error\n")

#         col_check += 1

#     print("{0:.2f}".format(ans))
#     row_check += 1


# 2675 문자열 반복

# # a = [input().split()]
# # print(a)

# line_num = int(input())

# s_list = [input().split() for _ in range(line_num)]
# # print(s_list)

# for num in range(len(s_list)):
#     out_array = list(s_list[num][1])
#     # print(out_array)
#     # print("haha")

#     for num2 in range(len(out_array)):
#         # for k in s_list[num][0]:
#         for k in range(int(s_list[num][0])):
#             # print("{0}, {1}" .format(num2, k))
#             print(out_array[num2], end='')

#     print()

############################# 2022/04/26
# 2935 소음
# list_a = [input() for _ in range(3)]
# # print(list_a) # 이 부분 주석처리 하는 것 까먹음

# if list_a[1] == '+':
#     print(int(list_a[0])+int(list_a[2]))
# elif list_a[1] == '*':
#     print(int(list_a[0])*int(list_a[2]))
# else:
#     print("not supported operator")

# 9498 시험 성적
# test_score = int(input())

# if test_score >= 90:
#     print("A")
# elif test_score >= 80:
#     print("B")
# elif test_score >= 70:
#     print("C")
# elif test_score >= 60:
#     print("D")
# else:
#     print("F")

# 10817 세 수
# num_list = list(map(int, input().split()))
# # print(num_list)
# num_list.sort()
# # print(num_list)
# print(num_list[-2])

# 11653 소인수분해
# num = int(input())

# if num == 1:
#     exit()

# div = 2 # 나누는 수, divisor
# num_list = []

# while num > 1:
#     if num % div == 0:
#         num_list.append(div)
#         num /= div
#         continue

#     elif num < div:
#         break

#     else:
#         div += 1

# # print([num_list[i] for i in range(len(num_list))])
# for i in range(len(num_list)):
#     print(num_list[i])

# 1789 수들의 합
# num = int(input())

# sum = 0
# ans = 0

# while num >= sum:   # 등호가 있어야 함
#     ans += 1
#     sum += ans

# ans -= 1
# print(ans)

# 2753 윤년
# year = int(input())
# # if year % 4 == 0 & (((year % 100) != 0) | ((year % 400) == 0)):
# if (year % 4 == 0) & ((year % 100 != 0) | ((year % 400) == 0)):
#     print(1)

# else: print(0)

# 10039 평균 점수
# num_list = [int(input()) for _ in range(5)]
# for x in range(5):
#     if(num_list[x] < 40):
#         num_list[x] = 40

# print(int(sum(num_list)/5))


# 1934 최소공배수
# num = int(input())
# num_list = [input().split() for _ in range(num)]

# # print(num_list)
# # 유클리드 호제법
# def gcd (a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# def lcm (a,b):
#     return int(a * b / gcd(a,b))

# for x in range(num):
#     print(lcm(int(num_list[x][0]), int(num_list[x][1])))


# 2480 주사위 세 개

# num_list = list(map(int, input().split()))
# num_list.sort()

# if (num_list[0] == num_list[1]) & (num_list[1] == num_list[2]):
#     print(10000 + num_list[0]*1000)
# elif (num_list[0] == num_list[1]) | (num_list[1] == num_list[2]):
#     print(1000 + num_list[1]*100)
# else:
#     print(num_list[2]*100)


# 4101 크냐?
# num_list = []
# count = 0

# while True:
#     num_list.append(list(map(int, input().split())))
#     if (num_list[count][0] == 0) & (num_list[count][1] == 0):
#         del num_list[count]
#         break
#     count += 1

# # print(num_list)
# for i in range(len(num_list)):
#     if(num_list[i][0] > num_list[i][1]):
#         print("Yes")
#     else:
#         print("No")


# 10156 과자
# num_list = list(map(int, input().split()))
# needed_money = num_list[0] * num_list[1] - num_list[2]

# if(needed_money < 0):
#     print(0)
# else:
#     print(needed_money)


# 3009 네 번째 점
# num_list = [list(map(int, input().split())) for _ in range(3)]
# # print(num_list)
# ans_list =[]

# for i in range(2):
#     if num_list[0][i] == num_list[1][i]:
#         ans_list.append(num_list[2][i])

#     elif num_list[0][i] == num_list[2][i]:
#         ans_list.append(num_list[1][i])

#     else:
#         ans_list.append(num_list[0][i])

# print(ans_list[0], ans_list[1])


# 2476 주사위 게임
# num = int(input())
# num_list = [list(map(int, input().split())) for _ in range(num)]
# # print(num_list)
# reward_list = []

# for i in range(num):
#     num_list[i].sort()
#     if (num_list[i][0] == num_list[i][1]) & (num_list[i][1] == num_list[i][2]):
#         reward_list.append(10000 + num_list[i][0] * 1000)
#     elif (num_list[i][0] == num_list[i][1]) | (num_list[i][1] == num_list[i][2]):
#         reward_list.append(1000 + num_list[i][1] * 100)
#     else:
#         reward_list.append(num_list[i][2]*100)

# # print(reward_list)
# reward_list.sort()
# print(reward_list[-1])


# 2754 학점계산
# grade_dict = {  "A+":"4.3", "A0": "4.0", "A-": "3.7",\
#                 "B+":"3.3", "B0": "3.0", "B-": "2.7",\
#                 "C+":"2.3", "C0": "2.0", "C-": "1.7",\
#                 "D+":"1.3", "D0": "1.0", "D-": "0.7",\
#                 "F" :"0.0"}

# # print(type(grade_dict))
# # print(grade_dict)

# grade = input()
# print(grade_dict[grade])


# 2884 알람 시계
# h, m = map(int, input().split())
# # print(h, m)

# if m >= 45:
#     m -= 45
# else:
#     if(h == 0):
#         h = 24

#     h -= 1
#     m += 15

# print(h, m)


# 7567 그릇
# # dishes = [input()]
# dishes = input()
# dishes_list = []
# # 그릇을 하나씩 분리해서 list로
# for i in range(len(dishes)):
#     dishes_list.append(dishes[i])
# # print(dishes_list)

# height = 10

# for i in range(len(dishes_list)-1):
#     print(i)
#     if(dishes_list[i+1] == dishes_list[i]):
#         height += 5
#     else:
#         height += 10

# print(height)


# 5063 TGN
# num = int(input())
# num_list = [list(map(int, input().split())) for _ in range(num)]
# # print(num_list)
# ad_str_list = []

# for i in range(len(num_list)):
#     benefit = (num_list[i][1] - num_list[i][0] - num_list[i][2])
#     if benefit > 0:
#         print("advertise")
#     elif benefit == 0:
#         print("does not matter")
#     else:
#         print("do not advertise")

# 10102 개표
# num = int(input())
# vote = list(input())

# # print(vote)
# if vote.count('A') > (num/2):
#     print("A")
# elif vote.count('B') > (num/2):
#     print("B")
# else:
#     print("Tie")


# 10886     0 = not cute/ 1 = cute
# num = int(input())
# num_list = [int(input()) for _ in range(num)]

# check = 0
# for i in range(len(num_list)):
#     if(num_list[i] == 1):
#         check += 1

# # 조건) num 은 홀수
# if check > (num/2):
#     print("Junhee is cute!")
# else:
#     print("Junhee is not cute!")


# 10988 팰린드롬인지 확인하기
# word_list = list(input())
# # print(word_list)

# check = 1
# for i in range(int(len(word_list)/2)):
#     if(word_list[i] != word_list[-(i+1)]):
#         check = 0
#         break
#     else:
#         continue

# print(check)


# 5086 배수와 약수
# result_list = []
# while True:
#     data_list = list(map(int, input().split()))

#     if (data_list[0] == 0) & (data_list[1] == 0):
#         break
#     elif(data_list[1] % data_list[0] == 0):
#         result_list.append("factor")
#     elif(data_list[0] % data_list[1] == 0):
#         result_list.append("multiple")
#     else:
#         result_list.append("neither")

# for i in range(len(result_list)):
#     print(result_list[i])


# 5717 상근이의 친구들
# result_list = []
# while True:
#     data_list = list(map(int, input().split()))
#     if (data_list[0] == 0) & (data_list[1] == 0):
#         break
#     else:
#         result_list.append(data_list[0]+data_list[1])

# for i in range(len(result_list)):
#     print(result_list[i])


# 9610 사분면
# num = int(input())
# point_list = [list(map(int,input().split())) for _ in range(num)]
# # print(point_list)
# # result_list = [0]*5     # index : Q1, Q2, Q3, Q4, AXIS
# result_list = [0 for _ in range(5)]
# # print(result_list)

# for i in range(num):
#     if(point_list[i][1] > 0):
#         if(point_list[i][0] > 0):
#             result_list[0] += 1     # 1사분면
#         elif(point_list[i][0] < 0):
#             result_list[1] += 1     # 2사분면
#         else:
#             result_list[4] += 1     # AXIS

#     elif(point_list[i][1] < 0):
#         if(point_list[i][0] < 0):
#             result_list[2] +=1      # 3사분면
#         elif(point_list[i][0] > 0):
#             result_list[3] += 1     # 4사분면
#         else:
#             result_list[4] += 1     # AXIS

#     else:
#         result_list[4] += 1         # AXIS

# for i in range(num):  이 부분 실수
# for i in range(5):
#     if(i == 4):
#         print("AXIS: {0}".format(result_list[i]))
#     else:
#         print("Q{0}: {1}".format((i+1), result_list[i]))


# 8958 OX퀴즈
# num = int(input())
# score_list = []
# for i in range(num):
#     o_score = 0
#     ones_score_sum = 0
#     ans_list = list(str(input()))
#     for j in range(len(ans_list)):
#         if(ans_list[j] == 'O'):
#             o_score += 1
#             ones_score_sum += o_score
#         else:           # 'X'
#             o_score = 0
#     score_list.append(ones_score_sum)

# for i in range(num):
#     print(score_list[i])


# 9506 약수들의 합
# num_list = []
# while True:
#     num = int(input())
#     if(num == -1):
#         break
#     num_list.append(num)
# # print(num_list)

# def check_perfect_number(num):
#     div_list = [1]
#     div = 1
#     while True:
#         div += 1
#         if (num % div == 0) & (num != div):
#             div_list.append(div)
#             # print("test2, {0}, {1}" .format(num, div))
#         elif num <= div :
#             break
#         else:
#             continue

#     if(num == sum(div_list)):
#         print("{0} = ".format(num), end='')
#         for i in range(len(div_list)-1):
#             print("{0} + ".format(div_list[i]), end='')
#         print(div_list[-1])
#     else:
#         print("{0} is NOT perfect.".format(num))
#     # print("{0}의 약수 : {1}, sum:{2}".format(num, div_list, sum(div_list)))

# for i in range(len(num_list)):
#     check_perfect_number(num_list[i])


# 10162 전자레인지
# cooking_time = int(input())
# hms_list = [0]*3

# if cooking_time % 10 != 0:
#     print(-1)
#     exit()
# else:
#     if(cooking_time >= 300):
#         hms_list[0] = cooking_time // 300
#         cooking_time %= 300

#     if(cooking_time >= 60):
#         hms_list[1] = cooking_time // 60
#         cooking_time %= 60

#     hms_list[2] = cooking_time // 10

# print("{0} {1} {2}".format(hms_list[0], hms_list[1], hms_list[2]))


# 10103 주사위 게임
# num = int(input())
# dice_list = [list(map(int, input().split())) for _ in range(num)]
# score_list = [100] * 2

# for i in range(num):
#     gab = dice_list[i][0] - dice_list[i][1]
#     if gab > 0:
#         score_list[1] -= dice_list[i][0]

#     elif gab < 0:
#         score_list[0] -= dice_list[i][1]

#     else:
#         continue

# print(str(score_list[0])+'\n'+str(score_list[1]))


# 10214 Baseball
# import os

# num = int(input())
# sum_list = [0] * 2
# check = 0
# while check < (num*9):
#     score_list = list(map(int, input().split()))
#     for i in range(2):
#         sum_list[i] += score_list[i]

#     if( (check+1) % 9 == 0):
#         if(sum_list[0] > sum_list[1]):
#             print("Yonsei")
#         elif(sum_list[0] < sum_list[1]):
#             print("Korea")
#         else:
#             print("Draw")
#             # os.system("pause")

#         sum_list = [0] * 2
#     check += 1

# 11557 Yangjojang of The Year

# num_of_test_case = int(input())
# winner_list = []

# for i in range(num_of_test_case):
#     num_of_col = int(input())
#     col_list = [input().split() for _ in range(num_of_col)]

#     winner = col_list[0][0]
#     for j in range(len(col_list)-1):
#         if(int(col_list[j][1]) < int(col_list[j+1][1])):
#             winner = col_list[j+1][0]

#     # print(winner)
#     winner_list.append(winner)

# for i in range(len(winner_list)):
#     print(winner_list[i])


# 10757 큰 수 A+B
# a, b = map(int, input().split())
# print(a+b)


# 2562 최댓값
# num_list = [int(input()) for _ in range(9)]

# max_value = max(num_list)
# for i in range(len(num_list)):
#     if(max_value == num_list[i]):
#         print(max_value)
#         print(i+1)


# 13333 Q-인덱스
# (개선 전)
# num = int(input())
# num_list = list(map(int, input().split()))
# num_list.sort()

# index = 0
# # k 번 이상 인용된 논문 k편 이상, k는 0부터 num까지
# for k in range(num, -1, -1):
#     count1 = 0
#     count2 = 0

#     # k번 이상 인용된 논문 count1
#     for i in range(num-1, -1, -1):
#         if(num_list[i] >= k):
#             count1 += 1
#             index = i
#         else: break

#     # k번 이하의 논문 수 count2, range범위를 index-1까지
#     for j in range(index):
#         if(num_list[i] <= k):
#             count2 += 1
#         else: break

#     # if( (k <= count1) & ( k >= count2) ):
#     if((k <= count1) & ((num-k) >= count2)):
#         print(k, count1, count2)
#     if(k <= count1):
#         print(k)
#         break

# 개선 코드
# num = int(input())
# num_list = sorted(list(map(int, input().split())))

# # k번 이상 인용된 논문 k편 이상, k는 0부터 num까지
# for k in range(num, -1, -1):
#     count1 = 0
#     # k번 이상 인용된 논문 count1
#     for i in range(num-1, -1, -1):
#         if(num_list[i] >= k):
#             count1 += 1
#         else: break

#     # count1 이 k편 이상임을 검사, 나머지 n-k편의 논문들의 인용횟수는 당연히 k번 이하(정확히는 미만)
#     # 위 for문의 검사 조건이 (인용횟수) k 이상인 논문들을 count하기 때문
#     if(k <= count1):
#         print(k)
#         break

# 2023/02/07 개선 코드
# N = int(input())
# qs = sorted(list(map(int, input().split())))

# def solve():
#     idx = -1
#     len_qs = len(qs)
#     max_k = 0

#     for k in range(0, qs[-1]+1):
#         while idx < len_qs-1 and qs[idx+1] < k:
#             idx += 1

#         # k 번 이상 인용된 논문 수
#         upper_k = len_qs - (idx+1)

#         if upper_k >= k:
#             max_k = k

#     print(max_k)

# solve()

# 더 개선
# N = int(input())
# qs = sorted(list(map(int, input().split())))

# def solve():
#     len_qs = len(qs)
#     idx = len_qs-1

#     for k in range(qs[-1], -1, -1):
#         while idx > 0 and qs[idx-1] >= k:
#             idx -= 1

#         # k 번 이상 인용된 논문 수
#         if (len_qs - idx) >= k:
#             print(k)
#             break

# solve()

# 더 더 개선
# N = int(input())
# qs = sorted(list(map(int, input().split())))

# def solve():
#     len_qs = len(qs)
#     for k in range(len_qs):
#         if qs[k] >= len_qs-k:
#             return len_qs-k
#     return 0

# print(solve())


# 1929 소수 구하기
# 시간 초과
# import math

# m, n = map(int, input().split())

# def prime_check(num):
#     if num == 1: return False

#     for i in range(2, int(math.sqrt(num))+1):
#         if num % i == 0 : return False

#     return True

# for i in range(m, n+1):
#     if prime_check(i):
#         print(i)

# for i in range(m, n+1):
#     prime_number_check = 1
#     for j in range(2, int(math.sqrt(i))+1):
#         if(i % j == 0):
#             prime_number_check = 0
#             break

#     if(prime_number_check == 1):
#         print(i)


# 4344 평균은 넘겠지

# c = int(input())
# score = []         # score 리스트 안에 또 각각의 리스트를 만들 것이다.
# sum_score = []     # score 리스트 안에 있는 각 리스트의 점수들의 합을 모아둘 것이다.
# average = []       # score 리스트 안에 있는 각 리스트의 평균들을 모아둘 것이다.
# count = [0] * c    # 한 리스트에서 평균 넘는 애들 숫자 세기

# for i in range(c):                                        # 각 리스트의 점수 입력 및 평균까지 구하기
#     score.append(list(map(int, input().split())))         # 한 리스트의 점수들을 입력해서 score 리스트에 추가하기
#     sum_score.append(sum(score[i][1:(score[i][0]+1)]))    # 그 리스트 안에 있는 점수들 합해서 sum_score 리스트 안에 추가하기
#     average.append(sum_score[i] / score[i][0])            # 그 sum_score에 합한 값을 점수 개수로 나누어서 average 리스트에 추가하기

# # 평균 넘는 애들을 카운트해서 비율 구하기
#     for k in range(1, score[i][0] + 1):
#         if score[i][k] > average[i]:
#             count[i] += 1
#     # print(f'{round(count[i] / score[i][0] * 100, 3)}%')
#     print('{0:.3f}%'.format(round(count[i] / score[i][0] * 100, 3)))

# num = int(input())
# num_list = [list(map(int, input().split())) for _ in range(num)]
# print(num_list)

# # 0행부터 num-1 행까지
# for i in range(num):
#     avg = sum(num_list[i][1:])/num_list[i][0]   # 각 행마다 평균(avg) 계산
#     # print(avg)

#     count = 0
#     for j in range(1, num_list[i][0]+1):
#         if(num_list[i][j] > avg): count += 1    # 평균보다 크면 count+1

#     print('{0:.3f}%'.format(round((count/num_list[i][0]) * 100, 3)))    # 형식에 맞게 출력

# 10757
# p, q = input().split()

# d= max(len(p), len(q))
# p = p.zfill(d+1)
# q = q.zfill(d+1)
# r = ''
# # print(d, p, q)

# c = 0
# # 1 부터 d+1 까지
# for i in range(1, d+2):
#     t = int(p[-i]) + int(q[-i])
#     r = str(t % 10 + c) + r
#     c = t // 10 # 다음 자리 수 +c 만큼
#     # print(t, r, c)

#     # t = int(p[-i]) + int(q[-i]) + c
#     # r = str(t % 10) + r
#     # c = t // 10
#     # print(t, r, c)

# print(r.lstrip('0'))


# for class ~
# 1152 단어의 개수
# print(len(list(map(str, input().split()))))

# 1157 단어 공부
# print(ord('A'))
# print(chr(65))

# str_input = list(input())
# # print(str_input)
# # 각 알파벳을 카운트 할 list
# count_list = [0] * 26

# for i in range(len(str_input)):
#     # 대문자 A(65) ~ Z
#     if(65 <= ord(str_input[i]) <= 90):
#         count_list[ord(str_input[i])-65] += 1
#     # 소문자 a(97) ~ z
#     else:
#         count_list[ord(str_input[i])-97] += 1
# # print(count_list)

# # count_list의 최대값을 이용해서 그 최대값이 몇 개(max_value_count) 있고 index는 몇인지
# max_value = max(count_list)
# max_value_count, max_value_index = 0, 0
# # print(count_list.index(max_value))
# for i in range(26):
#     if(count_list[i] == max_value):
#         max_value_count += 1
#         max_value_index = i
# # print(max_value_count)

# if(max_value_count == 1): print(chr(65 + max_value_index))
# else: print("?") # 2개 이상


# 1546 평균
# num = int(input())
# num_list = list(map(int, input().split()))
# # print(num_list)

# # 새로운 점수 : num_list[index] / max(num_list) * 100 이므로 아래는 평균
# print(sum(num_list)/(max(num_list)*num) * 100)


# 11720 숫자의 합
# list_len = int(input())
# int_list = list(map(str, input()))

# sum = 0
# for i in range(list_len):
#     sum += int(int_list[i])

# print(sum)


# 1110 더하기 사이클
# num = int(input())

# # 10의 자리, 1의 자리
# tens_place, ones_place = num // 10, num % 10
# # print(tens_place, ones_place)

# # 새로 만든 숫자 : -1로 초기화
# new_number = -1 # new_number = 0
# count = 0
# while num != new_number:
#     new_number = (ones_place * 10) + (tens_place + ones_place) % 10
#     count += 1
#     tens_place, ones_place = new_number // 10, new_number % 10
#     # print(new_number, count)

# print(count)


# 4690 완전 세제곱
# a;b;c;d;i;j;k;l;main()
# for(i=2;100>i;i++){
#     for(j=2;100>j;j++){
#         for(k=j;100>k;k++){
#             for(l=k;100>l;l++){
#                 if(i*i*i==j*j*j+k*k*k+l*l*l){
#                     printf("Cube = %d, Triple = (%d,%d,%d)\n",i,j,k,l);
#                 }
#             }
#         }
#     }
# }

# for i in range(2, 101):
#     for j in range(2, i):
#         for k in range(j, i):
#             for m in range(k, i):
#                 # if(i**3 == ((j**3) + (k**3) + (m**3))):
#                 if((i*i*i) == ((j*j*j) + (k*k*k) + (m*m*m))):
#                     print("Cube = {0}, Triple = ({1},{2},{3})".format(i, j, k, m))


# 2805 나무 자르기
# 시간 초과
# 틀렸습니다..?
# 또 시간 초과 ㅡㅡ
# 이제는 그냥 푼다 ㅎㅎ
# import sys

# n, m = map(int, sys.stdin.readline().rstrip().split())
# tree_height_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
# # print(tree_height_list)

# if(n != len(tree_height_list)):
#     print("haha")
#     quit()

# # 이분 탐색
# top, bot = tree_height_list[n-1], 0
# while top >= bot:
#     cutting_height = (top+bot)//2
#     # print(cutting_height)

#     sum = 0
#     for i in range(n-1, -1, -1):
#         if(tree_height_list[i] > cutting_height):
#             sum += tree_height_list[i] - cutting_height
#         else: break

#     if(sum == m): break
#     elif(sum > m): bot = cutting_height+1
#     else: top = cutting_height-1

# if(top < bot): print(top)
# else: print(cutting_height)

# python3 통과 ~
# import sys
# input = sys.stdin.readline

# def tree_binary_search(tree_height_list, top, bot, n, m):
#     if(top < bot):
#         return top

#     cutting_height = (top + bot) // 2
#     sum = sum_cut_tree(tree_height_list, cutting_height, n)
#     # print(cutting_height, sum)

#     # 각 경우에 대해서 return 달아줘야 된다 ~ 안 그러면 print()로 None이 나옴
#     if(sum > m): return tree_binary_search(tree_height_list, top, cutting_height+1, n, m)
#     elif(sum < m): return tree_binary_search(tree_height_list, cutting_height-1, bot, n, m)
#     else: return cutting_height

# def sum_cut_tree(tree_height_list, cutting_height, n):
#     sum = 0
#     for i in range(n):
#         if(tree_height_list[i] > cutting_height):
#             sum += tree_height_list[i] - cutting_height
#     return sum

# n, m = map(int, input().split())
# tree_height_list = list(map(int, input().split()))
# print(tree_binary_search(tree_height_list, max(tree_height_list), 0, n, m))


# https://www.acmicpc.net/source/43783824
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# li = list(map(int, input().split()))

# if n == 1 :
#     ans = li[0] - m

# else :
#     li.sort(reverse=True)

#     if li[0] == li[n-1] :
#         ans = li[0] - (m+1)//n

#     else :

#         wood = 0
#         ans = 0
#         for i in range(1, n) :
#             wood += (li[i-1] - li[i]) * i
#             if wood >= m :
#                 ans = li[i]
#                 break

#         if wood > m :
#             ans += (wood - m)//i

# print(ans)


# brute force
# # 1씩 줄이면서 계산
# # 제일 높은 나무의 높이를 기점으로 cutting_height 변수 초기화
# cutting_height = max(tree_height_list)
# for i in range(cutting_height, -1, -1):
#     sum = 0
#     # 큰 나무부터 cutting을 해서 남는 값이 있으면 sum에 합산
#     for j in range(n):
#         if((tree_height_list[j] - i) > 0):
#             sum += tree_height_list[j] - i
#             # print(i, j, sum)
#         # 0이하의 값 → cutting 기준 이하의 나무 길이 → 정렬돼있으므로 확인 할 필요 없음
#         else:
#             break

#     # sum의 값이 m 이상이 되면 조건 충족이므로 break
#     if(sum >= m):
#         cutting_height = i
#         break

# print(cutting_height)


# 2869 달팽이는 올라가고 싶다
# 시간 초과
# import math
# import sys

# a, b, v = map(int, sys.stdin.readline().split())
# v -= a

# print(math.ceil(v/(a-b)) + 1)

# gab = a - b
# days = math.ceil(v / gab)
# minus_days = 0
# min_days = 0

# while True:
#     minus_days += 1
#     if((gab * (days - minus_days) + a) >= v): continue
#         # print(gab, days, minus_days, a, v)
#     else: break
# min_days = days - minus_days
# print(min_days + 2)


# 두 수 비교하기 1330
# a, b = map(int, input().split())
# if(a > b): print(">")
# elif(a < b): print("<")
# else: print("==")


# 팰린드롬수 1259

# while True:
#     num_input = input()
#     if(num_input == '0'): break
#     else:
#         num_list = list(map(int, num_input))
#         # print(num_list)

#         palindrome_check = True
#         for i in range(len(num_list) // 2):
#             if(num_list[i] == num_list[len(num_list)-1-i]): continue
#             else: palindrome_check = False

#         if(palindrome_check): print("yes")
#         else: print("no")


# 1018 체스판 다시 칠하기
# import sys
# m, n = map(int, input().split())
# checkboard_list = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
# # print(checkboard_list)

# # m, n은 각각 8이상이므로 check 필요 X
# # i, j : 시작돌 위치
# # 바꿔야 하는 돌의 최대 개수는 64개이므로 min을 64로 설정
# min_count = 64
# for i in range(m-7):
#     for j in range(n-7):
#         count = 0
#         go_stone = {0:'W', 1:'B'}
#         for x in range(0, 8):
#             for y in range(0, 8):
#                 # 시작 돌이 White
#                 if(checkboard_list[i+x][j+y] == go_stone[(x+y)%2]): count += 0
#                 else: count += 1
#         # print(i, j, count, 'W')
#         if(count < min_count): min_count = count

#         count = 0
#         for x in range(8):
#             for y in range(8):
#                 # 시작 돌이 Black
#                 if(checkboard_list[i+x][j+y] == go_stone[(x+y+1)%2]): count += 0
#                 else: count += 1
#         # print(i, j, count, 'B')
#         if(count < min_count): min_count = count

# print(min_count)

# go_stone = {0:'W', 1:'B'}
# print(go_stone[0])
# print(go_stone[2])
# print(go_stone[1])


# 2747 피보나치 수
# 2748 피보나치 수 2
# 2749 피보나치 수 3
# 10826 피보나치 수 4
# 10870 피보나치 수 5

# 11444 피보나치 수 6
# 행렬을 이용한 계산

# num_input = int(input())
# fibonacci_list = [0, 1]
# for i in range(2, num_input + 1):
#     fibonacci_list.append((fibonacci_list[i-1] + fibonacci_list[i-2]))

# print(fibonacci_list[num_input])


# 9471 피사노 주기
# case_num = int(input())
# case_list = [list(map(int, input().split())) for _ in range(case_num)]
# # print(case_list)

# for k in range(case_num):
#     fibonacci_list = [0, 1]
#     i = 1
#     while True:
#         # i : index (i번째 fibonacci 수)
#         i += 1
#         fibonacci_list.append((fibonacci_list[i-1]+fibonacci_list[i-2]) % case_list[k][1])
#         # print(fibonacci_list)
#         if((fibonacci_list[-1] + fibonacci_list[-2]) == 1):
#             break

#     print(k + 1, i)
#     # print(i, fibonacci_list)


# 2749 피보나치 수 3
# 9471 피사노 주기를 먼저 풀어야 가능
# num = int(input())
# fibonacci_list = [0, 1]

# for i in range(2, 1500001):
#     fibonacci_list.append((fibonacci_list[i-1] + fibonacci_list[i-2]) % 1000000)

# print(fibonacci_list[num % 1500000])


# 11444
# num = int(input())
# fibonacci_list = [0, 1]

# for i in range(2, 1500001):
#     fibonacci_list.append((fibonacci_list[i-1] + fibonacci_list[i-2]) % 1000000)

# print(fibonacci_list[num % 1500000])


# 5522 카드 게임
# print(sum([int(input()) for _ in range(5)]))


# 14754 Pizza Boxes
# import sys

# n, m = map(int, sys.stdin.readline().rstrip().split())
# pizza_boxes = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
# # print(pizza_boxes)
# check_pizza_list = [[0] * m  for _ in range(n)]

# # 각 행의 최대 boxes 좌표 check
# for i in range(0, n):
#     max_index = 0
#     for j in range(1, m):
#         if(pizza_boxes[i][j] > pizza_boxes[i][max_index]): max_index = j
#     check_pizza_list[i][max_index] = 1

# # 각 열의 최대 boxes 좌표 check
# for j in range(0, m):
#     max_index = 0
#     for i in range(1, n):
#         if(pizza_boxes[i][j] > pizza_boxes[max_index][j]): max_index = i
#     check_pizza_list[max_index][j] = 1

# # pizza 합계 계산
# sum = 0
# for i in range(n):
#     for j in range(m):
#         # if ([i, j] not in max_index_list): sum += pizza_boxes[i][j]
#         if(check_pizza_list[i][j] == 0): sum += pizza_boxes[i][j]

# # print(max_index_list)
# print(sum)


# 10718 We love kriii
# print("강한친구 대한육군\n강한친구 대한육군")


# 1181 단어 정렬
# num = int(input())

# word_dict = {}
# for i in range(num):
#     word = input()
#     word_dict[word] = len(word)

# # word_dict = sorted(word_dict.items(), key=lambda x:(x[1], x[0]))
# # print(word_dict)

# # 1. 길이순(x[1]), 2.(같은 길이인 경우)사전순(x[0])
# for i in sorted(word_dict.items(), key=lambda x:(x[1], x[0])):
#     print(i[0])


# 1764 듣보잡
# import sys
# n, m = map(int, input().split())

# # 듣잡 dict
# not_heard_dict = {}
# for i in range(n):
#     name = sys.stdin.readline().rstrip()
#     not_heard_dict[name] = i
# # 정렬
# not_heard_dict = sorted(not_heard_dict.items(), key=lambda x:(x[0]))

# # 보잡 dict
# not_seen_dict = {}
# for i in range(m):
#     name = sys.stdin.readline().rstrip()
#     not_seen_dict[name] = i

# # 듣보잡 list
# not_heard_seen_list = []
# for i in range(min([n, m])):
#     if(not_heard_dict[i][0] in not_seen_dict):
#         not_heard_seen_list.append(not_heard_dict[i][0])

# # 듣보잡의 수와 그 명단을 사전순으로 출력(위에서 이미 정렬을 했으므로 사전순으로 출력됨)
# print(len(not_heard_seen_list))
# for i in range(len(not_heard_seen_list)): print(not_heard_seen_list[i])


# 4949 균형잡힌 세상
# import sys

# while True:
#     str_list = list(sys.stdin.readline().rstrip())
#     # print(str_list)

#     if((len(str_list) == 1) & (str_list[0] == '.')):
#         break

#     stack_list = []

#     symmetry_check = True
#     for i in range(len(str_list)):
#         if (str_list[i] == '('): stack_list.append('(')
#         elif (str_list[i] == '['): stack_list.append('[')

#         elif (str_list[i] == ')'):
#             if(len(stack_list) == 0):
#                 symmetry_check = False
#                 break
#             elif(stack_list.pop() == '('): continue
#             else:
#                 symmetry_check = False
#                 break
#         elif (str_list[i] == ']'):
#             if(len(stack_list) == 0):
#                 symmetry_check = False
#                 break
#             elif(stack_list.pop() == '['): continue
#             else:
#                 symmetry_check = False
#                 break
#         else: continue

#     # if(len(stack_list) == 0): print("yes")
#     # else: print("no")

#     # 출력초과 테스트용 코드
#     # 테스트결과, 한 string에 .이 2개 이상인 경우는 없었음
#     dot_count = 0
#     for i in range(len(str_list)):
#         if(str_list[i] == '.'):
#             dot_count += 1
#     if(dot_count > 1):
#         print("haha")

#     if((len(stack_list) == 0) & (symmetry_check == True)): print("yes")
#     else: print("no")


# 2108 통계학
# import math
# import sys

# num = int(input())
# num_list = [int(sys.stdin.readline().rstrip()) for _ in range(num)]
# num_list.sort()

# # 평균
# print(round(sum(num_list)/len(num_list)))

# # 중앙값
# # 길이가 홀수인 경우
# if((len(num_list) % 2) == 1): print(num_list[len(num_list)//2])
# # 짝수인 경우
# else: print(num_list[len(num_list)//2] + num_list[(len(num_list)//2)-1])

# # 최빈값
# num_count_set = {}
# for i in range(len(num_list)):
#     if(num_list[i] not in num_count_set): num_count_set[num_list[i]] = 1
#     else: num_count_set[num_list[i]] += 1

# # -x[1] : 카운트 수로 정렬, x[0] : 같은 카운트에 대해 기존 숫자 오름차순 정렬
# num_count_set = sorted(num_count_set.items(), key=lambda x:(-x[1], x[0]))
# if(len(num_count_set) == 1): print(num_count_set[0][0])
# elif(num_count_set[0][1] == num_count_set[1][1]): print(num_count_set[1][0])
# else: print(num_count_set[0][0])
# # print(num_count_set)

# # 범위
# print(num_list[-1] - num_list[0])


# 2609 최대공약수와 최소공배수
# n, m = map(int, input().split())

# # 최대공약수 - 유클리드 호제법
# def gcd(a, b):
#     while(b!= 0): a, b = b, a % b
#     return a

# # 최소공배수
# def lcm(a, b):
#     return a * b // gcd(a,b)

# print(gcd(n, m))
# print(lcm(n, m))

# 10944 랜덤 게임~~
# from random import *
# print(randint(1, 10000))


# 빠른 A+B
# import sys

# num = int(sys.stdin.readline().rstrip())
# for _ in range(num):
#     num_list = list(map(int, sys.stdin.readline().rstrip().split()))
#     print(sum(num_list))


# 16120 PPAP
# 시간 초과
# str_list = list(input().rstrip())
# # print(str_list)

# while True:
#     if(len(str_list) < 4):
#         print("NP")
#         break
#     elif(str_list == ['P', 'P', 'A', 'P']):
#         print('PPAP')
#         break
#     # 길이 4이상에 PPAP가 아닌 경우
#     else:
#         new_str_list = []
#         # 7인 경우 3까지 검사 range(4)
#         # for i in range(len(str_list)-3):
#         i = 0
#         while True:
#             # index가 str_list 범위를 벗어나면 break
#             if(i >= len(str_list)): break
#             # print(i)
#             # 남은 str_list 길이가 3이하면 PPAP 검사 할 필요가 없으므로 new_str_list에 .extend()
#             if(len(str_list[i:]) <= 3):
#                 new_str_list.extend(str_list[i:])
#                 break
#             # PPAP 검사
#             elif((str_list[i] == 'P') & (str_list[i+1] == 'P') & (str_list[i+2] == 'A') & (str_list[i+3] == 'P')):
#                 new_str_list.append('P')
#                 i += 4
#             # PPAP가 아닌 경우 단순하게 append 추가
#             else:
#                 new_str_list.append(str_list[i])
#                 i += 1

#         # 새로운 str_list랑 기존 str_list랑 같은 경우 → 무한 루프 → NP
#         if(new_str_list == str_list):
#             print("NP")
#             break
#         # 아닌 경우, 다음 step 진행
#         else:
#             # print(new_str_list)
#             str_list = new_str_list


# 15881 Pen Pineapple Apple Pen
# str_len = int(input())
# str_list = list(input())

# p_index = []
# for i in range(str_len):
#     if(str_list[i] == 'p'): p_index.append(i)
# # print(p_index)

# count = 0
# for i in p_index:
#     if((i + 3) >= str_len): break
#     elif(str_list[i:i+4] == ['p','P','A','p']):
#         count += 1
#         str_list[i+3] = 'v' # pPApPAp 일 때 1개만 체크하기 위함
#     else: continue
#     # print(str_list)
# print(count)


# 16692 Greedy Scheduler
# n, c = map(int, input().split())
# cart_list = list(map(int, input().split()))

# cashier_number_list = [0] * c

# # 0 ~ n-1 인덱스 까지는 오는 순서대로 받을 수 있음
# for i in range(n):
#     cashier_number_list[i] = i + 1

# # 그 이후의 인덱스에 대해서는 기존 n 까지의 범위 중 최소 값을 가지는 cashier의 index 값을 이용
# for i in range(n, c):
#     min_seconds_index = 0
#     for j in range(1, n):
#         if(cart_list[min_seconds_index] > cart_list[j]): min_seconds_index = j
#     cart_list[min_seconds_index] += cart_list[i]
#     cashier_number_list[i] = min_seconds_index + 1

# for i in range(c):
#     print(cashier_number_list[i], end= ' ')
# # print(cashier_number_list)


# 18787 Mad Scientist
# num = int(input())
# string_A = list(input())
# string_B = list(input())

# flipinator_3000_on = False
# count = 0
# for i in range(num):
#     if(string_A[i] != string_B[i]):
#         # if(~flipinator_3000_on): # 이건 numpy 식
#         if(not flipinator_3000_on):
#             flipinator_3000_on = True
#             count += 1
#         else: continue
#     else:
#         flipinator_3000_on = False
#         continue
#     # print(i, flipinator_3000_on, count)

# print(count)


# 10859 뒤집어진 소수
# 4퍼 13퍼 16퍼 91퍼 → 틀렸습니다
# 4퍼 5퍼 시간 초과
# import math
# import sys

# input_value = sys.stdin.readline().rstrip()
# num_list = list(map(int, input_value))
# list_len = len(num_list)
# new_num_list = [0] * list_len

# # # 2의 배수나 5의 배수인지 혹은 3의 배수인지 check
# # def multiple_check(list):
# #     if( ((list[-1]%2) == 0) | (list[-1] == 5) | (sum(list) % 3 == 0)):
# #         print("no")
# #         # quit()
# #         sys.exit(0)

# # 소수 체크 함수
# def prime_num_check(num):
#     if num == 1: return False
#     elif num == 2: return True
#     elif num % 2 == 0: return False # 2가 아닌 2의 배수

#     # 3부터 루트(num)까지 check
#     prime_check = True
#     for i in range(3, int(math.sqrt(num))+1, 2):
#         if(num % i == 0):
#             prime_check = False
#             break

#     return(prime_check)

# # list를 숫자로 만드는 함수
# def list_to_num(list):
#     num = 0
#     multiple_value = 1
#     for i in range(list_len-1, -1, -1):
#         num += list[i] * multiple_value
#         multiple_value *= 10
#     return num

# # multiple_check(num_list)
# # 3, 4, 7은 (뒤집으면, 180도 돌리면) 숫자가 아니다, 확인하면서 숫자 돌림(new_num_list)
# for i in range(list_len):
#     if((num_list[i] == 3) | (num_list[i] == 4) | (num_list[i] == 7)):
#         print("no")
#         # quit()
#         sys.exit(0)
#     elif(num_list[i] == 6): new_num_list[list_len-1-i] = 9
#     elif(num_list[i] == 9): new_num_list[list_len-1-i] = 6
#     else: new_num_list[list_len-1-i] = num_list[i]
# # print(num_list)
# # print(new_num_list)
# # multiple_check(new_num_list)

# new_value = list_to_num(new_num_list)

# # 뒤집어진(new) 숫자와 기존 숫자를 체크해서 둘 다 소수면 yes 아니면 no
# # print(input_value, new_value)
# if(prime_num_check(new_value) & prime_num_check(int(input_value))): print("yes")
# else: print("no")

# 1712 손익분기점
# a, b, c = map(int, input().split())
# if((c-b) <= 0): print(-1)
# else: print((a//(c-b)) +1)


# 2798 블랙잭
# import sys
# input = sys.stdin.readline

# # n은 제시되는 카드 개수, m은 합
# n, m = map(int, input().split())
# num_list = list(map(int, input().split()))
# # print(n, m, num_list)

# sum = 0
# for i in range(n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             # print(i, j, k)
#             if(sum < (num_list[i] + num_list[j] + num_list[k]) <= m):
#                 sum = num_list[i] + num_list[j] + num_list[k]
#                 # print("sum : ", sum)
# print(sum)


# 1977 완전제곱수
# import math

# m = int(input())
# n = int(input())

# sum = 0
# for i in range(math.ceil(math.sqrt(m)), math.floor(math.sqrt(n))+1):
#     sum += i ** 2

# if(sum == 0): print(-1)
# else:
#     print(sum)
#     print(math.ceil(math.sqrt(m)) ** 2)


# 1966 프린터 큐
# import sys
# from queue import Queue
# input = sys.stdin.readline

# # 입력 데이터로 for 문, 중요도 높은 문서를 확인하기 위해 sorted list 추가
# case_num = int(input())
# for i in range(case_num):
#     n, m = map(int, input().split())
#     test_case = list(map(int, input().split()))
#     test_case_sorted= sorted(test_case.copy())
#     # print(test_case_sorted)

#     # test_case 값에 index를 추가로 포함하는 리스트를 que에 put()
#     que = Queue()
#     count = 0
#     for j in range(n):
#         que.put([test_case[j], j])
#     # print(que.queue)

#     # que가 비어있지 않는 한 get()을 반복하면서 확인
#     while que.qsize():
#         get_value = que.get()
#         # print(get_value)
#         # 우선도가 가장 높은 수일 경우, sorted[-1] pop(), count 증가
#         if(get_value[0] == test_case_sorted[-1]):
#             test_case_sorted.pop()
#             count += 1
#             # 원하는 index의 값까지 get()에 성공했을 경우 count 출력하고 종료
#             if(get_value[1] == m):
#                 print(count)
#                 break
#         # 우선도가 떨어지는 수일 경우, 다시 que에 추가
#         else: que.put(get_value)

# 큐 10845
# 양방향 큐 사용
# from collections import deque
# import sys

# input = sys.stdin.readline
# num = int(input())

# queue = deque()
# # queue = deque([])
# # print(queue)
# for _ in range(num):
#     command_list = list(map(str, input().split()))
#     # print("command_list :", command_list)
#     if(command_list[0] == 'push'):
#         queue.append(int(command_list[1]))
#         # print(command_list[1])
#     elif(command_list[0] == 'pop'):
#         if(len(queue) == 0): print(-1)
#         else:
#             pop_value = queue.popleft()
#             print(pop_value)
#     elif(command_list[0] == 'size'):
#         print(len(queue))
#     elif(command_list[0] == 'empty'):
#         if(len(queue) == 0): print(1)
#         else: print(0)
#     elif(command_list[0] == 'front'):
#         if(len(queue) == 0): print(-1)
#         else:
#             # pop_value = queue.popleft()
#             # print(pop_value)
#             # queue.appendleft(pop_value)
#             print(queue[0])
#     else: # back
#         if(len(queue) == 0): print(-1)
#         else:
#             # pop_value = queue.pop()
#             # print(pop_value)
#             # queue.append(pop_value)
#             print(queue[-1])


# 영화감독 숌
# from itertools import combinations

# num = int(input())
# i = 1
# while True:
#     i += 1
#     com = list(combinations())

# 비효율적이지만 10000 이하의 input이면 충분히 가능..할 듯
# 어떻게 하면 더 효율적으로 만들 수 있을까
# num = int(input())
# count = 0
# value = 665
# while True:
#     value += 1

#     if('666' in str(value)):
#         count += 1
#     if(count == num):
#         print(value)
#         break


# 요세푸스 11866
# from queue import Queue

# n, k = map(int, input().split())
# que = Queue()
# count = 0

# # 1부터 n까지 queue에 put()
# for i in range(1, n+1):
#     que.put(i)
# # print(que.queue)

# # 요세푸스 순열 list 생성
# Josephus_permutation_list = []
# while que.qsize():
#     count += 1
#     get_value = que.get()
#     if(count % k) == 0:
#         # print(get_value)
#         Josephus_permutation_list.append(get_value)
#     else: que.put(get_value)

# # 출력
# print("<", end= '')
# for i in range(n-1):
#     print("{0}, ".format(Josephus_permutation_list[i]), end= '')
# print(Josephus_permutation_list[-1], end='')
# print(">", end= '')


# 10828 스택
# import sys
# input = sys.stdin.readline

# command_num = int(input())
# # command_num 만큼의 명령어 입력받음
# stack_list = []
# for _ in range(command_num):
#     command_list = list(map(str, input().split()))
#     if(command_list[0] == 'push'):
#         stack_list.append(command_list[1])
#     elif(command_list[0] == 'pop'):
#         if(len(stack_list) == 0): print(-1)
#         else: print(stack_list.pop())
#     elif(command_list[0] == 'size'):
#         print(len(stack_list))
#     elif(command_list[0] == 'empty'):
#         if(len(stack_list) == 0): print(1)
#         else: print(0)
#     else: # top
#         if(len(stack_list) == 0): print(-1)
#         else: print(stack_list[-1])

#     # print("stack_list : ", stack_list)


# 10866 덱
# from collections import deque
# import sys
# input = sys.stdin.readline

# que = deque()

# command_num = int(input())
# for i in range(command_num):
#     command_list = list(map(str, input().split()))
#     if(command_list[0] == 'push_front'): que.appendleft(int(command_list[1]))
#     elif(command_list[0] == 'push_back'): que.append(int(command_list[1]))
#     elif(command_list[0] == 'pop_front'):
#         if(len(que) == 0): print(-1)
#         else: print(que.popleft())
#     elif(command_list[0] == 'pop_back'):
#         if(len(que) == 0): print(-1)
#         else: print(que.pop())

#     elif(command_list[0] == 'size'): print(len(que))
#     elif(command_list[0] == 'empty'):
#         if(len(que) == 0): print(1)
#         else: print(0)
#     elif(command_list[0] == 'front'):
#         if(len(que) == 0): print(-1)
#         else: print(que[0])
#     elif(command_list[0] == 'back'):
#         if(len(que) == 0): print(-1)
#         else: print(que[-1])


# 2775 부녀회장이 될테야
# import sys
# input = sys.stdin.readline

# # 입력 처리
# test_case_num = int(input())
# test_case_list = []
# for i in range(test_case_num):
#     k = int(input())
#     n = int(input())
#     test_case_list.append([k, n])
# # print(test_case_list)

# # 제일 높은 층 (안 구해도 구현 가능)(∴ k, n 이 14 이하)
# highest_floor = sorted(test_case_list, key=lambda x:-x[0])[0][0]
# # print(highest_floor)

# # 제일 높은 호수 (안 구해도 구현 가능)
# highest_room_num = sorted(test_case_list, key=lambda x:-x[1])[0][1]

# # 최대 방 호수 크기만큼 최고 층까지 0으로 초기화
# residents_num_list = [[0] * highest_room_num for _ in range(highest_floor+1)]
# for i in range(highest_room_num):
#     residents_num_list[0][i] = i+1
# # print(residents_num_list)

# # 거주민 수 계산
# for i in range(1, highest_floor + 1):
#     residents_num_list[i][0] = 1
#     for j in range(1, highest_room_num):
#         residents_num_list[i][j] = residents_num_list[i][j-1] + residents_num_list[i-1][j]
# # print(residents_num_list)

# # 출력
# for i in range(test_case_num):
#     print(residents_num_list[test_case_list[i][0]][test_case_list[i][1]-1])


# 2164 카드2
# from collections import deque

# num = int(input())
# que = deque()

# for i in range(1, num+1):
#     que.append(i)
# # print(que)

# throw_away_check = True
# while len(que) > 1:
#     if(throw_away_check == True):
#         # print("버리기 : ", que.popleft())
#         que.popleft()
#         throw_away_check = False
#     else: # False
#         value = que.popleft()
#         # print("아래로 옮기기", value)
#         que.append(value)
#         throw_away_check = True
#     # print(que)

# print(que[0])


# 5430 AC
# 시간초과 x 2
# https://www.acmicpc.net/board/view/89276
# 33퍼 틀렸습니다 x 2
# 결국 성공 ㅎㅎㅎ

# import sys
# # from collections import deque

# input = sys.stdin.readline
# test_case_num = int(input())

# for i in range(test_case_num):
#     # rstrip()으로 개행(\n) 제거
#     func_p = list(input().rstrip())
#     # print(func_p)

#     # que = deque()
#     que = []
#     array_num = int(input())
#     # print("array_num : ", array_num)

#     array_num_str = input().rstrip()
#     # print("array_num_str : ", array_num_str, "!")
#     if(array_num_str == '[]'): array_num_list = []
#     else:
#         # print(array_num_str[1:-1])
#         # ValueError: invalid literal for int() with base 10: '' 때문에 else로 처리
#         # array_num_list = list(map(int, array_num_str[1:-1].split(',')))
#         que.extend(list(map(int, array_num_str[1:-1].split(','))))

#     # for j in range(array_num):
#     #     que.append(array_num_list[j])

#     start_index = 0
#     end_index = len(que)-1
#     reverse_check = False

#     error_check = False
#     if(func_p.count('D') > len(que)):
#         error_check = True
#     else:
#         for j in range(len(func_p)):
#             if(func_p[j] == 'R'):
#                 # que.reverse()
#                 # print(que)
#                 if(reverse_check == False): reverse_check = True
#                 else: reverse_check = False
#                 # print("R", que, start_index, end_index)

#             else: #'D'
#                 # if(len(que) == 0):
#                 #     error_check = True
#                 #     break
#                 # else:
#                 # que.popleft()
#                     # print("len(que) == ", len(que))
#                 if(reverse_check == False): start_index += 1
#                 else: end_index -= 1
#                 # print("D", que, start_index, end_index)

#     if(start_index > end_index):
#         que = []
#     else:
#         if(reverse_check == False):
#             if(end_index == len(que)-1):
#                 que = que[start_index:]
#             else:
#                 que = que[start_index:end_index+1]

#         else:
#             que.reverse()
#             # print("reverse", que)
#             if(start_index == 0):
#                 que = que[-end_index-1:]
#             else:
#                 que = que[-end_index-1:(-start_index)]

#     if(error_check): print("error")
#     else:
#         # print(que)
#         print('[', end='')
#         for j in range(len(que)-1):
#             print('{0},'.format(que[j]), end = '')
#         if(len(que) > 0): print(que[-1], end = '')
#         print(']')

# input()으로 str을 받는 부분은 readline().rstrip()으로 처리해주는 게 좋고
# int(input())으로 처리하는 부분은 rstrip() 없이 다루는 게 좋다

# list_as = [1,2,3]
# print(list_as[2:])
# print('{0}, '.format(" 1 "))
# print(list_as.count(-2))


# 11654 아스키코드
# print(ord(input()))

# # https://www.acmicpc.net/board/view/90920
# def lower_bound(a, t):
#     lo, hi=0, len(a)
#     while lo<hi:
#         mid=(lo+hi)//2
#         if t<=a[mid]:
#             hi=mid
#         else:
#             lo=mid+1
#     return lo

# def upper_bound(ar, tt):
#     lo, hi=0, len(ar)
#     while lo<hi:
#         mid=(lo+hi)//2
#         if tt>=ar[mid]:
#             lo=mid+1
#         else:
#             hi=mid
#     return lo

# N=int(input())
# ns=list(map(int, input().split()))
# M=int(input())
# ms=list(map(int, input().split()))
# ans=[]
# ns.sort()
# for i in ms:
#     if not lower_bound(ns, i):
#         print(ns, i, lower_bound(ns, i))
#         ans.append(0)
#         print("(1) i : ", i, "ans : ", ans)
#     else:
#         ans.append(upper_bound(ns, i)-lower_bound(ns, i))
#         print("(2) i : ", i, "ans : ", ans)
# # print(*ans)
# print(ans)


# import sys
# input = sys.stdin.readline

# n=int(input())
# a=[]
# b=[]
# for i in range(n):
#     A, B = map(int,input().split())
#     a.append(A)
#     b.append(B)
# a.sort()
# b.sort()
# for i in range(n):
#     print(a[i], b[i])


# 11650 좌표 정렬하기
# import sys
# input = sys.stdin.readline

# num = int(input())
# num_list = [list(map(int, input().split())) for _ in range(num)]
# num_list = sorted(num_list, key=lambda x:(x[0], x[1]))

# for i in range(num):
#     print(num_list[i][0], num_list[i][1])


# 10773 제로
# 이거 제출해야됨 ~
# import sys
# input = sys.stdin.readline
# num = int(input())
# num_list = []

# for _ in range(num):
#     plus_num = int(input())
#     if(plus_num) == 0: num_list.pop()
#     else: num_list.append(plus_num)

# print(sum(num_list))


# 2872 우리집엔 도서관이 있어
# import sys
# input = sys.stdin.readline

# num = int(input())
# num_list = [int(input()) for _ in range(num)]

# comp_num = max(num_list)
# count = num

# for i in range(num-1, -1, -1):
#     if(num_list[i] == comp_num):
#         count -= 1
#         comp_num -= 1

# print(count)


# 1978 소수 찾기
# 1 15 1 ?? math.floor() 뒤에 +1을 해주었어야 됐음
# import math

# num = int(input())
# num_list = list(map(int, input().split()))

# def prime_check(value):
#     # print(value)
#     if(value == 1): return False
#     elif(value == 2): return True
#     elif(value % 2 == 0): return False
#     else:
#         for i in range(3, math.floor(math.sqrt(value))+1, 2):
#             if(value % i == 0):
#                 # print(value, i, value%i)
#                 return False
#         return True

# count = 0
# for i in range(num):
#     if(prime_check(num_list[i]) == True):
#         count += 1

# print(count)


# 10818 최소, 최대
# num = int(input())
# num_list = list(map(int, input().split()))
# print(min(num_list), max(num_list))

# while True:
#     # 입력받기
#     dot_list = list(map(float,input().split()))
#     if len(dot_list) <= 0:
#         break
#     # 각 점의 좌표를 구하는 모습
#     dot1 = [dot_list[0],dot_list[1]]
#     dot2 = [dot_list[2],dot_list[3]]
#     dot3 = [dot_list[4],dot_list[5]]
#     dot4 = [dot_list[6],dot_list[7]]
#     # 2번째 3번째 좌표를 같게 만드는 모습
#     while True:
#         if dot2 == dot3:
#             break
#         dot2,dot1 = dot1,dot2
#         if dot2 == dot3:
#             break
#         # 한번 바꾼 것을 다시 돌려놓는 모습
#         dot2,dot1 = dot1,dot2
#         dot3,dot4 = dot4,dot3

#     # 공통된 점을 제외하고 다른 두점의 중간 지점을 구함
#     tmp = [(dot1[0] + dot4[0])/2,(dot1[1] + dot4[1])/2]

#     # 공통된 점을 중간 지점을 기준으로 반전
#     result = [0.000,0.000]
#     for i in range(2):
#         if tmp[i] > dot2[i]:
#             result[i] = dot2[i] + (tmp[i] - dot2[i]) * 2
#         else:
#             result[i] = dot2[i] - (dot2[i] - tmp[i]) * 2
#     print(f"{result[0]:.3f} {result[1]:.3f}")


# import sys

# # EOF(파일 끝)까지 한 꺼번에 읽어서 처리
# lines = sys.stdin.readlines()
# # print(lines)
# for line in lines:
#     dot_number_list = list(map(float, line.split()))
#     # print(dot_number_list)

#     # 각 line의 dots들 저장 dot_list에 저장
#     dot_list = [[0] * 2 for _ in range(4)]
#     for i in range(4):
#         dot_list[i] = [dot_number_list[i*2], dot_number_list[i*2 + 1]]
#     # print(dot_list)

#     # 한 개만 있는 점들(odd_dots)과 중복되는 점(overlapped_dot)을 따로 저장
#     odd_dots = []
#     overlapped_dot = []
#     for i in range(4):
#         if(dot_list.count(dot_list[i]) == 1): odd_dots.append(dot_list[i])
#         else: overlapped_dot = dot_list[i]
#     # print(odd_dots)
#     # print(overlapped_dot)

#     # 한 개만 있는 점들을 가지고 중앙점을 구함
#     standard_dot = [(odd_dots[0][0] + odd_dots[1][0])/2, (odd_dots[0][1] + odd_dots[1][1])/2]

#     # required_dot : standard_dot 기준 overlapped_dot의 반대편을 구함
#     required_dot = []
#     for i in range(2):
#         required_dot.append(2 * standard_dot[i] - overlapped_dot[i])

#     # 답 출력
#     # print(required_dot)
#     print("{0:.3f} {1:.3f}".format(required_dot[0], required_dot[1]))


# while True:
#     try:
#         line = input()
#     # except:
#     except EOFError:
#         break

#     dot_number_list = list(map(float, line.split()))
#     # print(dot_number_list)

#     # 각 line의 dots들 저장 dot_list에 저장
#     dot_list = [[0] * 2 for _ in range(4)]
#     for i in range(4):
#         dot_list[i] = [dot_number_list[i*2], dot_number_list[i*2 + 1]]
#     # print(dot_list)

#     # 한 개만 있는 점들(odd_dots)과 중복되는 점(overlapped_dot)을 따로 저장
#     odd_dots = []
#     overlapped_dot = []
#     for i in range(4):
#         if(dot_list.count(dot_list[i]) == 1): odd_dots.append(dot_list[i])
#         else: overlapped_dot = dot_list[i]
#     # print(odd_dots)
#     # print(overlapped_dot)

#     # 한 개만 있는 점들을 가지고 중앙점을 구함
#     standard_dot = [(odd_dots[0][0] + odd_dots[1][0])/2, (odd_dots[0][1] + odd_dots[1][1])/2]

#     # required_dot : standard_dot 기준 overlapped_dot의 반대편을 구함
#     required_dot = []
#     for i in range(2):
#         required_dot.append(2 * standard_dot[i] - overlapped_dot[i])

#     # 답 출력
#     # print(required_dot)
#     print("{0:.3f} {1:.3f}".format(required_dot[0], required_dot[1]))


# 11718 그대로 출력하기
# import sys
# lines = sys.stdin.readlines()

# for line in lines:
#     print(line.rstrip())

# while True:
#     try:
#         line = input()
#     except EOFError:
#         break

#     print(line)


# 10814 나이순 정렬
# normal input() → 4192 ms / sys.stdin.readline → 336 ms
# import sys
# input = sys.stdin.readline

# num = int(input())
# num_list = [list(map(str, input().split())) for _ in range(num)]
# # print(num_list)

# for i in range(num):
#     num_list[i][0] = int(num_list[i][0])

# for i in sorted(num_list, key=lambda x:x[0]):
#     print(*i)


# 22993 서든어택3
# import sys
# input = sys.stdin.readline

# num = int(input())
# num_list = list(map(int, input().split()))

# junwons_power = num_list[0]
# survive_check = True

# sorted_power_list = sorted(num_list[1:])
# # print(sorted_power_list)

# # 준원이 제외 1명 이상이면
# if(num >= 2):
#     for i in range(0, num-1):
#         if(junwons_power > sorted_power_list[i]): junwons_power += sorted_power_list[i]
#         else:
#             survive_check = False
#             break
#         # print(junwons_power)

# # print(survive_check)
# if(survive_check): print("Yes")
# else: print("No")


# 2920 음계
# num_list = list(map(int, input().split()))
# num_list_copy = num_list.copy()

# if(num_list_copy == sorted(num_list)): print("ascending")
# elif(num_list_copy == sorted(num_list, reverse=True)): print("descending")
# else: print("mixed")


# 2739 구구단
# num = int(input())
# for i in range(1, 10):
#     print("{0} * {1} = {2}".format(num, i, num*i))


# 17298 오큰수
# 요새 출력 형식을 정확히 안 맞춰서 틀리는 경우가 종종 있네
# 자중할 필요가 있다 !
# 시간 초과...
# 힌트가 스택 ?

# 1st try
# import sys
# input = sys.stdin.readline

# num = int(input())
# num_list = list(map(int, input().split()))

# NGE_list = []
# # # 0부터 n-2번까지
# for i in range(num-1):
#     for j in range(i+1, num):
#         if(num_list[i] < num_list[j]):
#             NGE_list.append(num_list[j])
#             # print(i, j, NGE_list)
#             break
#         # 끝 index까지 비교해봤는데 오큰수가 없는 경우, -1 추가
#         if(j == (num-1)):
#             NGE_list.append(-1)
# # n-1번째는 오른쪽이 없으므로 -1
# NGE_list.append(-1)

# print(*NGE_list)

# 2nd try
# import sys
# input = sys.stdin.readline

# num = int(input())
# num_list = list(map(int, input().split()))

# # 스택을 쓴다면..
# NGE_list = [-1] * num
# stack_list = []

# # i번째 인덱스 : 0부터 num -1 까지
# for i in range(0, num):
#     # stack_list에 저장된 값을 중에서 num_list[i]보다 작은 값이 있으면
#     # 해당하는 인덱스(stack_list[j][0])의 NGE_list에 num_list[i] 값을 넣고 stack_list[j] 삭제
#     for j in range(len(stack_list)-1, -1, -1):
#         if(num_list[i] > stack_list[j][1]):
#             NGE_list[stack_list[j][0]] = num_list[i]
#             del stack_list[j]

#     # i번째 인덱스 값을 stack_list에 추가
#     stack_list.append([i, num_list[i]])
# print(*NGE_list)

# 3rd try
# import sys
# input = sys.stdin.readline

# num = int(input())
# num_list = list(map(int, input().split()))
# if(num != len(num_list)):
#     quit()

# NGE_list = [-1] * num
# # stack_list에는 index를 저장
# stack_list = []

# # num_list[i]가 stack_list의 가장 마지막 요소 이하의 값이면 append(), 아닐 경우 오큰수를 만족하는 index까지 pop()
# for i in range(0, num):
#     if(len(stack_list) == 0): stack_list.append(i)
#     elif(num_list[stack_list[-1]] >= num_list[i]): stack_list.append(i)
#     else:
#         # while (len(stack_list) != 0) & (num_list[stack_list[-1]] < num_list[i]):
#         #     NGE_list[stack_list.pop()] = num_list[i]
#         while True:
#             if(len(stack_list) == 0): break
#             elif(num_list[stack_list[-1]] < num_list[i]):
#                 NGE_list[stack_list.pop()] = num_list[i]
#             else: break
#         stack_list.append(i)

# print(*NGE_list)


# 9012 괄호
# import sys
# input = sys.stdin.readline

# num = int(input())
# for _ in range(num):
#     line = list(input().rstrip())
#     # print(line)
#     stack_list = []

#     YES_check = True
#     for i in range(len(line)):
#         if(line[i] == '('): stack_list.append(line[i])
#         elif(line[i] == ')'):
#             if(len(stack_list) == 0):
#                 YES_check = False
#                 break
#             else: stack_list.pop()
#         # print(i, stack_list)

#     if((len(stack_list) == 0) & YES_check): print("YES")
#     else: print("NO")

# 24051 알고리즘 수업 - 삽입 정렬 1
# 90퍼 시간 초과
# Python 3로 통과한 사람이 없음(ㄷㄷ) → PyPy3로 하니까 통과

# import sys
# input = sys.stdin.readline

# def insertion_sort(numbers, val):
#     n = len(numbers)
#     cnt = 0
#     num = 0

#     # n 길이의 최대 cnt 보다 val이 큰 경우
#     if(val > (n*(n-1))//2):
#         return -1

#     for i in range(1, n):
#         now = numbers[i]
#         j = i - 1
#         # 0부터 i-1까지는 정렬 되어있는 상태
#         while j >= 0 and numbers[j] > now:
#             numbers[j + 1] = numbers[j]
#             cnt += 1
#             j -= 1

#             # num = numbers[j + 1]
#             if cnt == val:
#                 num = numbers[j + 1]
#                 return num

#         # 기존 (오름차순) 정렬에 1번이라도 변화가 있었다면, now가 들어갈 자리에 저장
#         if((j+1) != i):
#             numbers[j + 1] = now
#             cnt += 1
#             if (cnt == val):
#                 num = numbers[j + 1]
#                 return num
#     # cnt가 val에 도달하지 못한 경우
#     return -1

# A, B = map(int, input().split())
# numbers = list(map(int, input().split()))
# print(insertion_sort(numbers, B))

# 1010 다리 놓기
# 1st code
# import sys
# import math
# input = sys.stdin.readline

# for _ in range(int(input())):
#     num_list = list(map(int, input().split()))
#     print(math.factorial(num_list[1])//(math.factorial(num_list[0]) * math.factorial(num_list[1]-num_list[0])))

# 2nd code
# import sys
# input = sys.stdin.readline

# def factorial(num):
#     if num > 1: return num * factorial(num-1)
#     else: return 1

# for _ in range(int(input())):
#     num_list = list(map(int, input().split()))
#     print(factorial(num_list[1])//(factorial(num_list[0]) * factorial(num_list[1]-num_list[0])))

# import sys
# input = sys.stdin.readline

# input()
# list_A = list(map(int, input().split()))
# list_B = list(map(int, input().split()))
# list_A += list_B

# print(*sorted(list_A))


# 2018 수들의 합 5
# 메모리.. 초과..
# PyPy3 로 통과.. 했는데 슈퍼 간단한 코드가 있다
# import sys

# def solve():
#     num = int(sys.stdin.readline())
#     num_list = [i for i in range(1, (num//2)+2)]
#     # print(num_list)

#     cnt = 0
#     if(num >= 3):
#         first_index = 0
#         second_index = 1
#         len_num_list = len(num_list)
#         while True:
#             list_sum = (((first_index +1) + (second_index+1)) * (second_index - first_index +1)) // 2
#             if(list_sum < num):
#                 if(second_index < (len_num_list-1)): second_index += 1
#                 else: break
#             elif(list_sum > num) :
#                 if(first_index < (len_num_list-1)): first_index += 1
#                 else: break
#             else: # 조건에 부합하는 경우, 원하는 sum 원소들을 찾은 경우
#                 cnt += 1
#                 # print(num_list[first_index:second_index+1])
#                 if(second_index == (len_num_list-1)): break
#                 else: second_index += 1
#             # print(first_index, second_index)
#     # 해당 숫자 그대로인 숫자도 포함해서 +1 (ex. 15면 15)
#     print(cnt+1)
# solve()


# 생각해보니 굳이 list를 쓸 필요가 없다
# sum을 그 때마다 구할 필요도 없다 한 개의 원소 값을 더하거나 빼기만 하면 되네..

# 2nd try : 참고해서 진행
# import sys

# n = int(sys.stdin.readline())
# s, e = 1, 1
# cnt = 0
# sum = 1
# while s < (n // 2 + 1):
#     if sum < n:
#         e += 1
#         sum += e
#     elif sum == n:
#         cnt += 1
#         e += 1
#         sum += e
#         sum -= s
#         s += 1
#     else:
#         sum -= s
#         s += 1
# print(cnt + 1)


# 1920 수 찾기
# import sys
# input = sys.stdin.readline

# # 이분 탐색
# def binary_search(list, num):
#     bot = 0
#     top = len(list)-1
#     while bot <= top:
#         mid = (bot + top)//2
#         if num < list[mid] : top = mid - 1
#         elif num > list[mid] : bot = mid + 1
#         else:
#             print(1)
#             return
#     print(0)

# n = input()
# n_list = sorted(list(map(int, input().split())))
# m = input()
# m_list = list(map(int, input().split()))

# for i in m_list:
#     binary_search(n_list, i)


# 2751 수 정렬하기 2
# import sys
# input = sys.stdin.readline

# num = int(input())
# num_list = sorted([int(input()) for _ in range(num)])
# for i in range(num):
#     print(num_list[i])


# 17122 체스
# import sys
# input = sys.stdin.readline

# num = int(input())
# for _ in range(num):
#     A, B = map(str, input().split())
#     B = int(B)

#     # ord(A) → 65, (B-1) // 8 은 각각의 줄 인덱스
#     # 표기법1(A)에서 A1 → 66, 여기에 %2 적용하면 0, 표기법2(B)에서 1 → 0
#     if((ord(A[0]) + int(A[1]))%2 == (((B-1) // 8) + (B%2) +1)%2): print("YES")
#     else: print("NO")


# 2840 행운의 바퀴
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# str_list = ['?'] * n
# alpha_list = [-1] * 26
# index = 0
# normal_check = True

# for _ in range(k):
#     s, letter = map(str, input().split())
#     s = int(s)
#     index = (index + s) % n

#     # 현재 index의 글자가 '?'이 아니면서 입력받은 글자와 다른 경우 (1인덱스 2글자)
#     if(str_list[index] != '?') & (str_list[index] != letter):
#         normal_check = False
#         break
#     # 하나의 글자가 두 개 이상의 index에서 나타나는 경우 (1글자 2인덱스)
#     elif(alpha_list[(ord(letter)-65)] != -1) and (alpha_list[(ord(letter)-65)] != index):
#         normal_check = False
#         break
#     else: str_list[index] = letter
#     alpha_list[ord(letter)-65] = index

# if(normal_check == True):
#     # for i in range(index, -1, -1): print(str_list[i], end='')
#     # for i in range(n-1, index, -1): print(str_list[i], end='')
#     for i in range(n, 0, -1):
#         print(str_list[(i+index)%n], end = '')
# else: print("!")


# 11726 2xn 타일링
# 런타임 에러(RecursionError)
# 틀렸습니다 → 결과값이 10007로 나눈 나머지 값이어야함 -_-
# RecursionError → return 재귀로 안 하고 아래와 같이 for문으로 치환
# def factorial(num):
#     value = 1
#     for i in range(num, 1, -1):
#         value *= i
#     return value

# sum = 0
# num = int(input())
# for i in range(num//2 +1):
#     a = num - i*2
#     # a + i 개의 땅 중에 a개를 선택하는 조합의 수
#     sum += factorial(a+i)//(factorial(a)*factorial(i))

# print(sum % 10007)

# RecursionError 해결2번째
# import sys
# sys.setrecursionlimit(10**6)

# def factorial(num):
#     if(num >= 2): return num * factorial(num-1)
#     else: return 1

# sum = 0
# num = int(sys.stdin.readline())
# for i in range(num//2 +1):
#     a = num - i*2
#     # a + i 개의 땅 중에 a개를 선택하는 조합의 수
#     sum += factorial(a+i)//(factorial(a)*factorial(i))

# print(sum % 10007)


# # 14405 피카츄
# import sys
# str_list = list(sys.stdin.readline().rstrip())

# len_str_list = len(str_list)
# index = 0
# pos_check = True

# while True:
#     # pi ka chu 로 index를 len_str_list까지 채웠다면 True / break
#     if(index == len_str_list): break
#     elif (len_str_list - index) >= 3 and str_list[index:index+3] == ['c','h','u']:
#         index += 3
#     elif (len_str_list - index) >= 2 and str_list[index:index+2] == ['p','i']:
#         index += 2
#     elif (len_str_list - index) >= 2 and str_list[index:index+2] == ['k','a']:
#         index += 2
#     # pi ka chu 로 발음할 수 없는 문자열이면 False / break
#     else:
#         pos_check = False
#         break

# if(pos_check): print("YES")
# else: print("NO")


# 17509 And the Winner Is... Ourselves!
# 시간이 적게 드는 순서부터 많이 드는 순서까지 정렬 → 합산하면 끝
# import sys

# def cal_sum(num_list):
#     sum = 0
#     time = 0
#     for i in range(11):
#         time += num_list[i][0]
#         sum += time + num_list[i][1]*20
#     return sum

# num_list = sorted([list(map(int, input().split())) for _ in range(11)], key=lambda x:x[0])
# # print(num_list)
# print(cal_sum(num_list))


# 2231 분해합
# try 1
# import sys
# num = int(sys.stdin.readline())

# def find_creator_num(num):
#     for i in range(10):
#         for j in range(10):
#             for k in range(10):
#                 for a in range(10):
#                     for b in range(10):
#                         for c in range(10):
#                             if(100001 * i + 10001*j + 1001*k + 101*a + 11*b + 2*c) == num:
#                                 return(100000 * i + 10000 * j + 1000*k + 100*a + 10*b + c)
#                             elif(100000 * i + 10000 * j + 1000*k + 100*a + 10*b + c) > num:
#                                 break
#     return 0

# print(find_creator_num(num))

# try 2
# import sys
# num = int(sys.stdin.readline())

# def find_creator_num(num):
#     if(num == 1000000): return 0

#     for i in range(10):
#         for j in range(10):
#             for k in range(10):
#                 for a in range(10):
#                     for b in range(10):
#                         for c in range(10):
#                             if(100001 * i + 10001*j + 1001*k + 101*a + 11*b + 2*c) == num:
#                                 return(100000 * i + 10000 * j + 1000*k + 100*a + 10*b + c)
#                             elif(100000 * i + 10000 * j + 1000*k + 100*a + 10*b + c) >= num:
#                                 return 0

# print(find_creator_num(num))


# 17478 재귀함수가 뭔가요?
# import sys
# input = sys.stdin.readline

# num = int(input())
# count = 0

# def recursion_func(count):
#     print('{0}"재귀함수가 뭔가요?"'.format(count*'_'*4))
#     if(count == num):
#         print('{0}"재귀함수는 자기 자신을 호출하는 함수라네"'.format(count*'_'*4))
#     else:
#         print('''\
# {0}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# {0}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# {0}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'''.format(count*'_'*4))
#         count += 1
#         recursion_func(count)
#         count -= 1
#     print("{0}라고 답변하였지.".format(count*'_'*4))

# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# recursion_func(count)


# 1074 Z
# 1st try → 시간 초과
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# N, r, c = map(int, input().split())
# array_dist = 2**N
# count = 0
# # num_list = [[0] * array_dist for _ in range(array_dist)]

# def recursion_Z(N, x, y):
#     global count
#     gap = 2**(N-1)
#     # print(gap, N, x, y)
#     if(N == 1):
#         if(x == r and y == c): print(count)
#         else: count += 1
#             # print(count)
#         if(x == r and y+1 == c): print(count)
#         else: count += 1
#         if(x+1 == r and y == c): print(count)
#         else: count += 1
#         if(x+1 == r and y+1 == c): print(count)
#         else: count += 1
#     else:
#         N -= 1
#         recursion_Z(N, x, y)
#         recursion_Z(N, x, y+gap)
#         recursion_Z(N, x+gap, y)
#         recursion_Z(N, x+gap, y+gap)

# recursion_Z(N, 0, 0)

# 1074 Z
# import sys
# input = sys.stdin.readline
# # RecursionError 방지
# sys.setrecursionlimit(10**6)

# # 입력 처리
# N, r, c = map(int, input().split())
# gap = 2**N
# count = 0
# # 기준 점을 잡아서 위쪽 좌우 / 아래쪽 좌우를 나누기 위한 변수
# standard_x, standard_y = gap//2, gap//2

# def recursion_Z(N, x, y):
#     global count, standard_x, standard_y, gap
#     # print("standard: ", standard_x, standard_y)
#     # print(gap, N, x, y, count)
#     if(N == 1):
#         if(x == r and y == c): print(count)
#         else: count += 1
#             # print(count)
#         if(x == r and y+1 == c): print(count)
#         else: count += 1
#         if(x+1 == r and y == c): print(count)
#         else: count += 1
#         if(x+1 == r and y+1 == c): print(count)
#         else: count += 1
#     else:
#         N -= 1
#         gap //= 2
#         gap_div_2 = gap // 2
#         # 좌상단 (standard 좌표를 기준으로 (r, c)의 위치)
#         if(r < standard_x and c < standard_y):
#             standard_x -= gap_div_2
#             standard_y -= gap_div_2
#             recursion_Z(N, x, y)
#         # 우상단
#         elif(r < standard_x and c >= standard_y):
#             standard_x -= gap_div_2
#             standard_y += gap_div_2
#             count += gap ** 2
#             recursion_Z(N, x, y+gap)
#         # 좌하단
#         elif(r >= standard_x and c < standard_y):
#             standard_x += gap_div_2
#             standard_y -= gap_div_2
#             count += (gap ** 2) * 2
#             recursion_Z(N, x+gap, y)
#         # 우하단
#         else:
#             standard_x += gap_div_2
#             standard_y += gap_div_2
#             count += (gap ** 2) * 3
#             recursion_Z(N, x+gap, y+gap)

# recursion_Z(N, 0, 0)


# 다른 사람 코드
# https://www.acmicpc.net/source/43877252
# import sys
# input = sys.stdin.readline

# N, r, c = map(int, input().split())

# def D(row,col):

#     if row == 0 and col == 0:
#         return 0
#     else:
#         pass

#     return 2 * (row % 2) + col % 2 + 4 * D(row//2,col//2)

# print(D(r,c))


# 7568 덩치
# import sys
# input = sys.stdin.readline

# num = int(input())
# num_list = [list(map(int, input().split())) for _ in range(num)]
# rate_list = []

# for i in range(num):
#     count = 1
#     for j in range(num):
#         if i == j : continue
#         else:
#             if num_list[i][0] < num_list[j][0] and num_list[i][1] < num_list[j][1]:
#                 count += 1
#             else: continue
#     rate_list.append(count)

# print(*rate_list)


# 9020 골드바흐의 추측
# 1. 소수를 찾아야 함
# 2. 두 소수의 차가 가장 적은 골드바흐 파티션 → 정렬로 구현 (더 좋은 방법이 있을 듯?)
# 1st try → 시간 초과
# import sys
# import math
# input = sys.stdin.readline
# num = int(input())

# # 소수 체크 함수
# def prime_check(num):
#     if(num == 1): return False
#     elif(num == 2): return True
#     elif(num % 2 == 0): return False
#     else:
#         for i in range(3, math.floor(math.sqrt(num))+1, 2):
#             if(num % i == 0):
#                 return False
#         return True

# def solve():
#     for _ in range(num):
#         n = int(input())
#         prime_list = []
#         ans_list = []
#         if n == 4:
#             ans_list.append([2, 2, 0])
#         else:
#             for i in range(3, n-1, 2):
#                 if(prime_check(i) == True):
#                     prime_list.append(i)

#             len_prime_list = len(prime_list)
#             for i in range(len_prime_list):
#                 for j in range(i, len_prime_list):
#                     if(prime_list[i] + prime_list[j] == n):
#                         ans_list.append([prime_list[i], prime_list[j], prime_list[j] - prime_list[i]])

#         ans_list.sort(key=lambda x:x[2])
#         print(ans_list[0][0], ans_list[0][1])
#         # print(prime_list)

# solve()


# 9퍼.. 또 시간 초과
# import sys
# import math
# import os
# input = sys.stdin.readline
# num = int(input())

# # 소수 체크 함수
# def prime_check(num):
#     if(num == 1): return False
#     elif(num == 2): return True
#     elif(num % 2 == 0): return False
#     else:
#         for i in range(3, math.floor(math.sqrt(num))+1, 2):
#             if(num % i == 0):
#                 return False
#         return True

# def solve():
#     for _ in range(num):
#         n = int(input())
#         prime_list = []
#         if n == 4:
#             print(2, 2)
#         else:
#             for i in range(3, n-2, 2):
#                 if(prime_check(i) == True):
#                     prime_list.append(i)
#             # print(prime_list)

#             # 찾았는지 체크
#             find_check = False
#             index = 0
#             # n//2 에 가장 가까우면서도 작은 소수의 인덱스를 찾아야 함
#             for i in range(n//2, 2, -1):
#                 if(i in prime_list):
#                     index = prime_list.index(i)
#                     break

#             # len_prime_list = len(prime_list)
#             # index_1은 index 포함 왼쪽, index_2는 index포함 오른쪽
#             index_2 = index
#             for index_1 in range(index, -1, -1):
#                 # for index_2 in range(index_1, len(prime_list), 1):
#                 while True :
#                     # 숫자 조합을 찾은 경우
#                     if(prime_list[index_1] + prime_list[index_2] == n):
#                         print(prime_list[index_1], prime_list[index_2])
#                         find_check = True
#                         break
#                     # 두 숫자의 합이 n보다 커진 경우
#                     elif(prime_list[index_1] + prime_list[index_2] > n):
#                         index_2 -= 1
#                         break
#                     # 못 찾았는데 index_2가 아직 len_prime_list-1보다 작은 경우
#                     # elif (index_2 < len_prime_list-1): index_2 += 1
#                     else: index_2 += 1
#                     # 못 찾았는데 두 숫자의 합이 n보다 작으면서 index_2가 len_prime_list-1인 경우
#                     # else:
#                     #     print("check", index_1, prime_list[index_1], index_2, prime_list[index_2])
#                     #     os.system("pause")
#                     #     break

#                 if(find_check): break

# solve()

# # for i in range(4, 10001, 2):
# #     print(i, end= ' ')
# #     solve(i)


# 4th try → clear
# import sys
# import math
# input = sys.stdin.readline
# num = int(input())

# # 소수 체크 함수
# def prime_check(num):
#     if(num == 1): return False
#     elif(num == 2): return True
#     elif(num % 2 == 0): return False
#     else:
#         for i in range(3, math.floor(math.sqrt(num))+1, 2):
#             if(num % i == 0):
#                 return False
#         return True

# def solve():
#     for _ in range(num):
#         n = int(input())
#         if n == 4:
#             print(2, 2)
#         else:
#             # 찾았는지 체크용 변수
#             find_check = False
#             index = 0
#             # n//2 랑 같거나 작으면서 가장 가까운 소수의 인덱스를 찾아야 함
#             for i in range(n//2, 2, -1):
#                 if(i in prime_list):
#                     index = prime_list.index(i)
#                     break

#             # index_1은 index 포함 왼쪽, index_2는 index포함 오른쪽
#             index_2 = index
#             for index_1 in range(index, -1, -1):
#                 # for index_2 in range(index_1, len(prime_list), 1):
#                 while True :
#                     # 숫자 조합을 찾은 경우
#                     if(prime_list[index_1] + prime_list[index_2] == n):
#                         print(prime_list[index_1], prime_list[index_2])
#                         find_check = True
#                         break
#                     # 두 숫자의 합이 n보다 커진 경우
#                     elif(prime_list[index_1] + prime_list[index_2] > n):
#                         index_2 -= 1
#                         break
#                     # 아직 못 찾은 경우
#                     else: index_2 += 1

#                 if(find_check): break

# # 소수 list를 구해놓고 체크를 하면 되는데 바보같이 num 받을때마다 소수 list를 구하게 했네..
# prime_list = []
# for i in range(3, 10000-2, 2):
#     if(prime_check(i) == True):
#         prime_list.append(i)
# solve()
# # for i in range(4, 10001, 2):
# #     solve(i)


# 2577
# import sys
# input = sys.stdin.readline

# count_check = [0] * 10

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num = num1 * num2 * num3
# num_list = list(str(num1 * num2 * num3))

# for i in range(len(num_list)):
#     count_check[num % 10] += 1
#     num //= 10

# # print(count_check)
# for i in range(10):
#     print(count_check[i])


# 3190 뱀
# 23퍼 틀렸습니다 → 사과를 먹은 다음 해당 인덱스를 0으로 처리해주지 않았음 즉 무한 사과여서 틀렸음 ㄷㄷ
# import sys
# from collections import deque
# input = sys.stdin.readline

# que = deque()
# que.append([0, 0]) # 뱀의 위치

# n = int(input())
# k = int(input())

# board = [[0] * n for _ in range(n)]

# for _ in range(k):
#     apple_x, apple_y = map(int, input().split())
#     apple_x -= 1
#     apple_y -= 1

#     board[apple_x][apple_y] += 1

# snake_direction = {0:'right', 1:'down', 2:'left', 3:'up'}
# now_d = 0

# # board 확인 이상 무
# # for i in range(n):
# #     for j in range(n):
# #         print(board[i][j], end= ' ')
# #     print()

# now_x = 0
# now_y = 0
# total_distance = 0

# dist_direct_list = []
# dist_direct_index = 0
# # L : 뱀의 방향 정보
# for _ in range(int(input())):
#     distance, direction = map(str, input().split())
#     distance = int(distance)
#     dist_direct_list.append([distance, direction])
# # print(dist_direct_list)

# def check_que(now_x, now_y):
#     # 뱀이 자기 몸이랑 만나면 True 반환
#     if([now_x, now_y] in que): return True
#     # 사과가 없는 자리면 꼬리 부분 pop()
#     elif(board[now_x][now_y] != 1): que.pop()
#     elif(board[now_x][now_y] == 1): board[now_x][now_y] = 0
#     que.appendleft([now_x, now_y])

# def solve(snake_direction, now_d, now_x, now_y, total_distance, dist_direct_list, dist_direct_index):
#     # print(now_d)
#     while True:
#         total_distance += 1
#         # 이동 수행
#         if(snake_direction[now_d] == 'right'):
#             if(now_y < n-1):
#                 now_y += 1
#                 if(check_que(now_x, now_y)): break
#             else: break
#         elif(snake_direction[now_d] == 'down'):
#             if(now_x < n-1):
#                 now_x += 1
#                 if(check_que(now_x, now_y)): break
#             else: break
#         elif(snake_direction[now_d] == 'left'):
#             if(now_y > 0):
#                 now_y -= 1
#                 if(check_que(now_x, now_y)): break
#             else: break
#         elif(snake_direction[now_d] == 'up'):
#             if(now_x > 0):
#                 now_x -= 1
#                 if(check_que(now_x, now_y)): break
#             else: break

#         # 제시된 거리만큼 이동 한 다음에 방향 조정
#         if(total_distance == dist_direct_list[dist_direct_index][0]):
#             if(dist_direct_list[dist_direct_index][1] == 'L'):  # 왼쪽으로 90도
#                 if(now_d == 0): now_d = 3
#                 else: now_d -= 1
#             else: # D, 오른쪽으로 90도
#                 now_d = (now_d+1) % 4

#             if dist_direct_index < len(dist_direct_list)-1:
#                 dist_direct_index += 1
#         # print(total_distance, que, snake_direction[now_d])
#     return(total_distance)

# print(solve(snake_direction, now_d, now_x, now_y, total_distance, dist_direct_list, dist_direct_index))


# 2741 N 찍기
# for i in range(1, int(input())+1): print(i)

# 10250 ACM호텔
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     h, w, n = map(int, input().split())
#     print(((n-1)%h +1)*100 +((n-1)//h +1))


# 3553 Dragon’s Question
# n, d = map(int, input().split())

# def solve():
#     for i in range(10**(n-1), 10**n):
#         if(i % d ==0):
#             return i
#     return "No solution"

# print(solve())


# 18108 1998년생인 내가 태국에서는 2541년생?!
# print(int(input())-543)


# 1267 핸드폰 요금
# import sys
# import math
# input = sys.stdin.readline

# def yeong_sik(num):
#     return math.ceil((num+1)/30)*10

# def min_sik(num):
#     return math.ceil((num+1)/60)*15

# def solve():
#     sum_yeong_sik, sum_min_sik = 0, 0
#     n = int(input())
#     talk_time_list = list(map(int, input().split()))

#     for i in range(n):
#         sum_yeong_sik += yeong_sik(talk_time_list[i])
#         sum_min_sik += min_sik(talk_time_list[i])

#     print("sum_yeong_sik :", sum_yeong_sik)
#     print("sum_min_sik :", sum_min_sik)

#     if(sum_yeong_sik < sum_min_sik):
#         print("Y", sum_yeong_sik)
#     elif(sum_yeong_sik > sum_min_sik):
#         print("M", sum_min_sik)
#     else:
#         print("Y M", sum_yeong_sik)

# solve()


# 1541 잃어버린 괄호
# def sum_list(now_str):
#     num_list = list(map(int, now_str.split('+')))
#     # print(num_list)
#     return sum(num_list)

# def solve():
#     str_input = input().split('-')
#     # print(str_input)

#     # 마이너스 나오기 전 값들은 다 더할 수 밖에 없음
#     total_sum = sum_list(str_input[0])

#     # 첫 번째 마이너스 이후의 값들은 모두 마이너스 처리
#     for i in range(1, len(str_input)):
#         total_sum -= sum_list(str_input[i])

#     return total_sum

# print(solve())


# 2953 나는 요리사다
# import sys
# input = sys.stdin.readline

# def solve():
#     max_index = -1
#     max_sum = 0
#     for i in range(5):
#         list_sum = sum(list(map(int, input().split())))
#         if(max_sum < list_sum):
#             max_index = i
#             max_sum = list_sum
#     return max_index+1, max_sum

# print(*solve())


# 10799 쇠막대기
# def solve():
#     pipe_list = list(input())
#     # print(pipe_list)
#     pipe_stack, sum = 0, 0
#     pre_pipe = '('

#     for i in range(len(pipe_list)):
#         if(pipe_list[i] == '('):
#             pipe_stack += 1
#             pre_pipe = '('
#         else: # pipe_list[i] == ')'
#             if(pre_pipe == '('):
#                 pipe_stack -= 1
#                 sum += pipe_stack
#                 pre_pipe = ')'
#             else:
#                 sum += 1
#                 pipe_stack -= 1
#     return sum

# print(solve())


# 2812 크게 만들기
# try 1
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# num_list = list(map(int, input().rstrip()))
# # print(num_list)

# new_num_list = []
# for i in range(n):
#     new_num_list.append([num_list[i], i])
# # print(new_num_list)

# new_num_list.sort(key=lambda x:(-x[0], -x[1]))
# # print(new_num_list[:k])

# new_num_list = sorted(new_num_list[:(n-k)], key=lambda x:x[1])
# # .sort(key=lambda x:x[1])
# print(new_num_list)

# for i in range(n-k):
#     print(new_num_list[i][0], end='')


# try 2
# import sys
# input = sys.stdin.readline

# def solve():
#     n, k = map(int, input().split())
#     num_list = list(map(int, input().rstrip()))
#     # print(num_list)
#     num_stack = []

#     for i in range(n):
#         if k > 0 : # 아직 지울 수 있다면
#             if(not num_stack):
#                 num_stack.append(num_list[i])
#             else:
#                 # 기존 num_stack의 마지막 수보다 num_list[i]가 클 때 k가 0보다 크다면 pop()
#                 while num_stack and k > 0:
#                     if num_stack[-1] < num_list[i] :
#                         num_stack.pop()
#                         k -= 1
#                     else: # num_stack[-1] >= num_list[i]
#                         break
#                 num_stack.append(num_list[i])
#         else: # k == 0, 더 이상 지울 수 없음
#             num_stack.append(num_list[i])

#     # k가 남아있는 경우도 계산해야 함, 예를 들면 내림차순의 형태를 띄는 수
#     # print(k, num_stack)
#     if k > 0: num_stack = num_stack[:-k]
#     return num_stack

# for i in solve():
#     print(i, end='')


# 18258 큐2
# from collections import deque
# import sys
# input = sys.stdin.readline

# def solve():
#     que = deque()

#     for _ in range(int(input())):
#         command_list = list(map(str, input().split()))
#         if(command_list[0] == 'push'):
#             que.append(command_list[1])
#         elif(command_list[0] == 'pop'):
#             if(not que): print("-1")
#             else: print(que.popleft())
#         elif(command_list[0] == 'size'):
#             print(len(que))
#         elif(command_list[0] == 'empty'):
#             if(not que): print("1")
#             else: print("0")
#         elif(command_list[0] == 'front'):
#             if(not que): print("-1")
#             else: print(que[0])
#         else: # back
#             if(not que): print("-1")
#             else: print(que[-1])

# solve()


# 1300 K번째 수
# 1st try : 메모리 초과
# import sys
# input = sys.stdin.readline

# n = int(input())
# k = int(input())

# b_list = []
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         b_list.append(i*j)
# b_list.sort()
# print(b_list[k-1])


# 1489 대결
# 어떻게 풀까..
# import sys
# input = sys.stdin.readline

# len_list = int(input())
# team_a = sorted(list(map(int, input().split())), reverse=True)
# team_b = sorted(list(map(int, input().split())), reverse=True)
# # print(team_a)
# # print(team_b)
# # check_b = [0] * team_b
# index_b = 0

# score = 0
# for index_a in range(len_list):
#     while team_a[index_a] < team_b[index_b]:
#         if index_b == len_list -1:
#             break
#         else:
#             index_b += 1

#     if(team_a[index_a] > team_b[index_b]): score += 2
#     elif(team_a[index_a] == team_b[index_b]): score += 1
#     print(team_a[index_a], team_b[index_b])
#     if(index_b < len_list-1): index_b += 1

# print(score)


# 2437 저울
# 메모리 초과
# import sys
# input = sys.stdin.readline

# def solve():
#     n = int(input())
#     weight_list = list(map(int, input().split()))
#     # print(weight_list)
#     # weight_set = {}
#     weight_set = set()

#     for i in range(n):
#         # 추 자기 자신의 무게를 temp_weight_set에 추가
#         temp_weight_set = {weight_list[i]}
#         # 기존 weight_set에 현재 추 무게만큼 더한 값을 temp_weight_set에 추가
#         for j in weight_set:
#             temp_weight_set.add(weight_list[i] + j)

#         # 기존 weight_set과 temp_weight_set을 union
#         weight_set = weight_set.union(temp_weight_set)
#         # print(weight_set)

#     # 1부터 증가시켜서 없는 숫자가 있으면 print하고 break
#     i = 1
#     while True:
#         if i in weight_set:
#             i += 1
#             continue
#         else: return i

# print(solve())


# try2
# 71% 틀렸습니다
# weight_list[0] 일 때 print(1)로 해버렸네 아 ㅋㅋ
# import sys
# input = sys.stdin.readline

# n = int(input())
# weight_list = sorted(list(map(int, input().split())))
# # print(weight_list)

# def solve():
#     if(weight_list[0] != 1): return 1
#     else:
#         max_limit = 1
#         for i in range(1, n):
#             if(weight_list[i] > max_limit + 1): return max_limit+1
#             else: # weight_list[i] <= max_limit +1
#                 max_limit += weight_list[i]
#         # 제일 무거운 추까지 연속적으로 무게를 잴 수 있는 경우
#         return max_limit+1

# print(solve())


# 1158 요세푸스 문제
# from collections import deque
# n, k = map(int, input().split())

# que = deque(i for i in range(1, n+1))
# # for i in range(1, n+1):
# #     que.append(i)
# Josephus_list = []
# count = 1

# while que:
#     if count % k == 0: Josephus_list.append(que.popleft())
#     else: que.append(que.popleft())
#     count += 1

# print('<{0}>'.format(', '.join(map(str, Josephus_list))))


# 2438 별 찍기 - 1
# for i in range(1, int(input())+1):
#     print('*' * i)

# 2439 별 찍기 - 2
# num = int(input())
# for i in range(1, num+1):
#     print(" " * (num-i),end='')
#     print("*" * i)

# 2442 별 찍기 - 5
# num = int(input())
# for i in range(1, num+1):
#     print(" " * (num-i),end='')
#     print("*" * i, end='')
#     print("*" * (i-1))


# 1927 최소 힙
# from queue import PriorityQueue
# import sys
# input = sys.stdin.readline

# def solve():
#     que = PriorityQueue()

#     for i in range(int(input())):
#         num = int(input())
#         if num == 0:
#             if que.qsize() == 0: print(0)
#             else: print(que.get())
#         else: que.put(num)

# solve()


# 11279 최대 힙
# from queue import PriorityQueue
# import sys
# input = sys.stdin.readline

# def solve():
#     que = PriorityQueue()

#     for i in range(int(input())):
#         num = int(input())
#         if num == 0:
#             if que.qsize() == 0: print(0)
#             else: print(-que.get())
#         else: que.put(-num)

# solve()


# N과 M (1)
# from itertools import permutations

# n, m = map(int, input().split())
# num_list = [i for i in range(1, n+1)]
# # print(num_list)
# for i in list(permutations(num_list, m)):
#     print(*i)
#     # for j in range(len(i)):
#     #     print(i[j], end=' ')
#     # print()


# 15779 Zigzag
# import sys
# input = sys.stdin.readline

# num = int(input())
# num_list = list(map(int, input().split()))
# gap_list = [0] * (num-1)
# zigzag_list = [2] * (num-1)

# for i in range(num-1):
#     gap_list[i] = num_list[i+1] - num_list[i]
# # print(num_list)
# # print(gap_list)

# zigzag_count = 0
# for i in range(1, num-1):
#     if gap_list[i] > 0:
#         if gap_list[i-1] < 0: zigzag_count += 1
#         else: zigzag_count = 0
#     elif gap_list[i] < 0:
#         if gap_list[i-1] > 0: zigzag_count += 1
#         else: zigzag_count = 0
#     else: zigzag_count = 0
#     zigzag_list[i] += zigzag_count

# # print(zigzag_list)
# print(max(zigzag_list))


# 5622 다이얼
# str_list = list(input())

# sum = 0
# for i in range(len(str_list)):
#     ord_value = ord(str_list[i])

#     if ord_value <= 67 : sum += 3       # ABC
#     elif ord_value <= 70 : sum += 4     # DEF
#     elif ord_value <= 73 : sum += 5     # GHI
#     elif ord_value <= 76 : sum += 6     # JKL
#     elif ord_value <= 79 : sum += 7     # MNO
#     elif ord_value <= 83 : sum += 8     # PQRS
#     elif ord_value <= 86 : sum += 9     # TUV
#     else: sum += 10                     # WXYZ

# print(sum)


# 10872
# def factorial(num):
#     value = 1
#     for i in range(num, 0, -1):
#         value *= i
#     return value

# print(factorial(int(input())))


# 11651 좌표 정렬하기 2
# key=lambda
# import sys
# input = sys.stdin.readline

# def solve():
#     num = int(input())
#     num_list = [list(map(int, input().split())) for _ in range(num)]
#     # print(*num_list)

#     for i in sorted(num_list, key=lambda x:(x[1], x[0])):
#         print(i[0], i[1])

# solve()


# 10816 숫자카드2
# 10815 숫자카드

# 2
# 10 11
# 2
# 10 14
# index_binary_search 값 넘겨줄 때 top으로 n값을 넘겨줘서 IndexError
# 지금 보니 두 숫자카드가 같은 경우는 없다.. 이런..

# import sys
# input = sys.stdin.readline

# def index_binary_search(n_list, num, top, bot):
#     while bot <= top:
#         mid = (top+bot) // 2
#         if n_list[mid] == num:
#             max, min = find_max_min_index(n_list, num, mid)
#             return max - min + 1
#         elif num > n_list[mid]: return index_binary_search(n_list, num, top, mid+1)
#         else: return index_binary_search(n_list, num, mid-1, bot)
#     return 0

# def find_max_min_index(n_list, num, index):
#     max, min = index, index
#     while min > 0:
#         if n_list[min-1] == num: min -= 1
#         else: break
#     while max < len(n_list)-1:
#         if n_list[max+1] == num: max += 1
#         else: break
#     return max, min

# def solve():
#     n = int(input())
#     n_list = sorted(list(map(int, input().split())))
#     # print(n_list)
#     m = int(input())
#     m_list = list(map(int, input().split()))

#     for i in range(m):
#         # print("m_list[i]:", m_list[i])
#         print(index_binary_search(n_list, m_list[i], n-1, 0), end=' ')

# solve()


# 10989 수 정렬하기3
# python3, PyPy3 메모리 초과
# import sys
# input = sys.stdin.readline

# num = int(input())
# num_list = [int(input()) for _ in range(num)]

# for i in sorted(num_list):
#     print(i)

# 검색 참고
# import sys
# input = sys.stdin.readline

# num = int(input())
# num_list = [0] * 10001

# for _ in range(num):
#     num_list[int(input())] += 1

# # 0부터 10000까지
# for i in range(10001):
#     if num_list[i] != 0:
#         for j in range(num_list[i]):
#             print(i)


# N과 M(3)
# from itertools import product

# m, n = map(int, input().split())
# for i in product(range(1, m+1), repeat=n):
#     print(*i)


# 숫자 카드 2
# import sys
# input = sys.stdin.readline

# n = int(input())
# n_list = list(map(int, input().split()))
# m = int(input())
# m_list = list(map(int, input().split()))

# m_set = dict()
# for i in range(n):
#     if n_list[i] in m_set.keys():
#         m_set[n_list[i]] += 1
#     else: m_set[n_list[i]] = 1
# # print(m_set)

# for i in range(m):
#     if m_list[i] in m_set.keys():
#         print(m_set[m_list[i]], end = ' ')
#     else: print(0, end = ' ')


# 9935 문자열 폭발
# 시간 초과
# 문자열을 다시 잡아주는 것보다 pop이 훨씬 빠름
# import sys
# input = sys.stdin.readline

# def solve():
#     list_a = list(input().rstrip())
#     boom_str = list(input().rstrip())
#     stack_list = []
#     # print(list_a, boom_str)
#     len_boom_str = len(boom_str)

#     for i in range(len(list_a)):
#         stack_list.append(list_a[i])

#         if len(stack_list) >= len_boom_str:
#             # print(stack_list[-len_boom_str:])
#             if stack_list[-len_boom_str:] == boom_str:
#                 # stack_list = stack_list[:-len_boom_str]
#                 for _ in range(len_boom_str):
#                     stack_list.pop()

#     if stack_list: print(''.join(stack_list))
#     else: print("FRULA")

# solve()


# 시간 초과
# import sys
# input = sys.stdin.readline

# list_a = list(input().rstrip())
# boom_str = list(input().rstrip())
# len_list_a = len(list_a)
# len_boom_str = len(boom_str)

# check_list = [1] * len_list_a
# check_index_list = []

# for i in range(len_list_a):
#     if(list_a[i] == boom_str[0]): check_index_list.append(i)
# # print(list_a, boom_str)
# # print(check_index_list)
# # count = 0

# while True:
#     is_it_bombed = False

#     # 인덱스 별로 확인
#     for i in check_index_list:
#         # print(count, i, check_list)
#         stack_list = []
#         stack_index_list = []
#         if(check_list[i] == 0): continue

#         for j in range(i, len_list_a):
#             # 해당 index에 대해서 폭발이 일어나지 않은 경우만
#             if(check_list[j] != 0):
#                stack_list.append(list_a[j])
#                stack_index_list.append(j)
#                if len(stack_list) == len_boom_str:
#                     if stack_list == boom_str:
#                         is_it_bombed = True
#                         for k in stack_index_list:
#                             check_list[k] = 0
#                     else: break
#     # count += 1

#     if is_it_bombed == False:
#         break

# # print(check_list)  if check_list[i] != 0
# if sum(check_list) == 0: print("FRULA")
# else:
#     for i in range(len_list_a):
#         if check_list[i] != 0:
#             print(list_a[i], end='')


# 1302 베스트셀러
# import sys
# input = sys.stdin.readline

# book_dict = {}
# for _ in range(int(input())):
#     book_name = input().rstrip()
#     if book_name in book_dict: book_dict[book_name] += 1
#     else: book_dict[book_name] = 1

# print(sorted(book_dict.items(), key=lambda x:(-x[1], x[0]))[0][0])


# 3273 두 수의 합
# indexError, left > right 일때 조건을 달아서 해결
# import sys
# input = sys.stdin.readline

# n = int(input())
# num_list = sorted(list(map(int, input().split())))
# x = int(input())

# p_left, p_right = 0, n-1
# count = 0
# # print(num_list)

# while p_left != p_right:
#     if num_list[p_left] + num_list[p_right] > x:
#         p_right -= 1
#     elif num_list[p_left] + num_list[p_right] < x:
#         p_left += 1
#     else:
#         count += 1
#         p_left += 1
#         p_right -= 1
#         if(p_left >= p_right): break

# print(count)


# 16120 PPAP
# input_list = list(input())
# ppap_stack = []
# ppap_list = list('PPAP')

# for i in range(len(input_list)):
#     ppap_stack.append(input_list[i])

#     # ppap_stack의 길이가 4(PPAP)이상일 때
#     if(len(ppap_stack) >= 4):
#         if ppap_stack[-4:] == ppap_list:
#             for _ in range(3):
#                 ppap_stack.pop()
#     # print(i, ppap_stack)

# if ppap_stack == ['P'] : print("PPAP")
# else: print("NP")


# 25285 심준의 병역판정검사
# import sys
# input = sys.stdin.readline

# def check_physical_class(h, w):
#     bmi = w / (h/100)**2
#     if h < 140.1: return 6
#     elif 140.1 <= h < 146: return 5
#     elif 146 <= h < 159: return 4
#     elif 159 <= h < 161:
#         if 16.0 <= bmi < 35.0 : return 3
#         else: return 4
#     elif 161 <= h < 204:
#         if 20.0 <= bmi < 25.0 : return 1
#         elif 18.5 <= bmi < 20.0 or 25.0 <= bmi < 30.0: return 2
#         elif 16.0 <= bmi < 18.5 or 30.0 <= bmi < 35.0: return 3
#         else: return 4
#     else: return 4

# for _ in range(int(input())):
#     h, w = map(int, input().split())
#     print(check_physical_class(h, w))


# 18870 좌표 압축
# import sys
# input = sys.stdin.readline

# def solve():
#     n = int(input())
#     num_list = list(map(int, input().split()))
#     new_num_list = sorted(num_list)

#     # 좌표 순서를 담은 dict
#     seq_dict = {}
#     seq_num = 0
#     # print(type(seq_dict))

#     for i in range(n):
#         if new_num_list[i] in seq_dict: continue
#         else:
#             seq_dict[new_num_list[i]] = seq_num
#             seq_num += 1

#     for i in range(n):
#         print(seq_dict[num_list[i]], end= ' ')

# solve()


# 18111 마인크래프트
# 값은 잘 나오는데 시간초과네 아 ~
# PyPy3로 제출했더니 틀렸습니다.. 왜 틀렸지 ?
"""
2 2 0
1 3
2 2
정답 : 3 2
출력 : 8 1
why? 블록이 모자란 경우가 아닌데 모자라다고 판별해버렸음
"""
# import sys
# input = sys.stdin.readline

# n, m, b = map(int, input().split())
# land_list = [list(map(int, input().split())) for _ in range(n)]
# # print(land_list)

# min_height, max_height = 256, 0
# for i in range(n):
#     for j in range(m):
#         if land_list[i][j] < min_height : min_height = land_list[i][j]
#         if land_list[i][j] > max_height : max_height = land_list[i][j]
# # print("min :", min_height, "max :", max_height)

# # min_time_sum = 500 * 500 * 256 * 2
# min_time_sum = sys.maxsize
# result_height = 0
# # 최소 시간, 같은 시간일 경우 최대 높이이므로 높은 경우부터 계산
# for i in range(max_height, min_height-1, -1):
#     time_sum = 0
#     temp_b = b

#     b_pos_check = True
#     for j in range(n):
#         for k in range(m):
#             # 높을 경우 제거한 블록은 인벤토리에, 제거는 블록당 2초
#             if land_list[j][k] > i:
#                 temp_b += land_list[j][k] - i
#                 time_sum += (land_list[j][k] - i) * 2
#             # 낮을 경우 블록이 모자라다면 False와 break, 아닐 경우 추가는 블록당 1초
#             elif land_list[j][k] < i:
#                 if i - land_list[j][k] > temp_b:
#                     b_pos_check = False
#                     break
#                 else:
#                     temp_b -= i - land_list[j][k]
#                     time_sum += i - land_list[j][k]
#             else: continue
#             # print(i, j, k, time_sum)
#         if b_pos_check == False: break
#     if b_pos_check == False: continue
#     # print("i:", i, "time_sum:", time_sum)

#     if min_time_sum > time_sum:
#         min_time_sum = time_sum
#         result_height = i

# print(min_time_sum, result_height)


# try 2
# 보완 : 2차원 배열이 아닌 1차원 배열로 정의, sort
# PyPy3 : 통과, Python3 시간 초과
# import sys
# input = sys.stdin.readline
# n, m, b = map(int, input().split())
# land_list = [0] * (n * m)
# # print(land_list)

# for i in range(n):
#     temp_list = list(map(int, input().split()))
#     for j in range(m):
#         land_list[i*m+j] = temp_list[j]
#         # print(i*m+j)
# # print(land_list)
# len_land_list = n*m
# min_sum_time = sys.maxsize
# max_height = 256

# # 정답은 땅에 있는 범위 내의 값일 수밖에 없으므로 범위는 이하와 같음
# land_list.sort()
# for i in range(land_list[-1], land_list[0]-1, -1):
#     sum_time = 0
#     temp_b = b
#     b_pos_check = True
#     for j in range(len_land_list-1, -1, -1):
#         # 고르게 설정하고자 하는 땅의 높이보다 높은 경우
#         if land_list[j] > i:
#             temp_b += land_list[j] - i
#             sum_time += (land_list[j] - i)*2
#         # (높이가) 낮은 경우
#         elif land_list[j] < i:
#             gap = i - land_list[j]
#             if gap > temp_b:
#                 b_pos_check = False
#                 break
#             else:
#                 temp_b -= gap
#                 sum_time += gap
#         # (높이가) 동일한 경우
#         else: continue
#     if b_pos_check == False: continue
#     elif min_sum_time > sum_time:
#         min_sum_time = sum_time
#         max_height = i

# print(min_sum_time, max_height)

# try3
# 높이 별로 수를 책정해서 더 효율적으로 처리
# import sys
# input = sys.stdin.readline

# n, m, b = map(int, input().split())
# land_list = [0] * (n * m)
# # print(land_list)
# for i in range(n):
#     temp_list = list(map(int, input().split()))
#     for j in range(m):
#         land_list[i*m+j] = temp_list[j]
# # print(land_list)

# # 높이별로 count한 list 생성
# height_count_list = [0] * 257
# for i in range(n*m): #len(land_list)
#     height_count_list[land_list[i]] += 1
# # print(height_count_list)

# min_sum_time = sys.maxsize
# max_height = 256

# # 최종 높이는 land_list 내의 원소 값일 수밖에 없으므로 범위는 이하와 같음
# land_list.sort()
# for i in range(land_list[-1], land_list[0]-1, -1):
#     sum_time = 0
#     temp_b = b

#     for j in range(257):
#         if height_count_list[j] == 0 or i == j: continue
#         else:
#             if j > i:
#                 temp_b += height_count_list[j] * (j - i)
#                 sum_time += height_count_list[j] * (j - i)*2
#             else: # j < i
#                 temp_b -= height_count_list[j] * (i - j)
#                 sum_time += height_count_list[j] * (i - j)
#     if temp_b < 0: continue
#     else:
#         if min_sum_time > sum_time:
#             min_sum_time = sum_time
#             max_height = i

# print(min_sum_time, max_height)


# 1874 스택수열
# import sys
# input = sys.stdin.readline

# n = int(input())
# stack_list = []
# check_list = [0] * (n+1)
# pos_check = True

# pre_num = -1
# for _ in range(n):
#     num = int(input())
#     # 처음 값을 넣는 경우, push
#     if pre_num == -1:
#         for i in range(1, num+1):
#             check_list[i] = 1
#             stack_list.append('+')
#         check_list[num] = -1
#         stack_list.append('-')
#     else:
#         # 더 큰 값이 들어온 경우, push
#         if num > pre_num:
#             for i in range(pre_num+1, num+1):
#                 if(check_list[i] == -1): continue
#                 else:
#                     check_list[i] = 1
#                     stack_list.append('+')
#             check_list[num] = -1
#             stack_list.append('-')

#         # pop, 여기서 가능/불가능 체크
#         else: # num < pre_num
#             # pop 하고자 하는 값이 이미 pop된 경우
#             if check_list[num] == -1:
#                 pos_check = False
#                 break
#             else: # check_list[num] == 1
#                 # num 값 전에, 먼저 pop 되야할 값들이 있는 경우
#                 for i in range(pre_num-1, num, -1):
#                     if check_list[i] == 1:
#                         pos_check = False
#                         break
#                     else: # check_list[i] == -1
#                         continue
#                 check_list[num] = -1
#                 stack_list.append('-')
#     pre_num = num
#     # print(num, check_list, stack_list)

# if pos_check : print('\n'.join(stack_list))
#     # for i in range(len(stack_list)):
#     #     print(stack_list[i])
# else: print("NO")


# try 2
# 좀 더 효율적으로, 다른 사람의 코드를 참고했음
# import sys
# input = sys.stdin.readline

# n = int(input())
# num_list = [int(input()) for _ in range(n)]
# num_for_stack = list(range(1, n+1))[::-1]

# def solve():
#     tmp, operator = [0], []
#     for t in num_list:
#         if t < tmp[-1]:
#             print('NO')
#             return
#         while t > tmp[-1]:
#             tmp.append(num_for_stack.pop())
#             operator.append('+')
#         tmp.pop()
#         operator.append('-')
#     print(*operator, sep='\n')

# solve()


# 1655 가운데를 말해요
# from queue import PriorityQueue

# que = PriorityQueue()
# for _ in range(int(input())):
#     que.put(int(input()))
#     # if que.qsize() % 2 == 0: print(que[que.qsize()//2 -1])
#     # else: print(que[que.qsize()//2])
#     print(que[0])

# # print(que.queue)

# 우선순위 큐 세 개로 구현하는 것 같은데..
# import sys
# input = sys.stdin.readline

# num_list = []
# for _ in range(int(input())):
#     num_list.append(int(input()))
#     num_list.sort()

#     if len(num_list) % 2 == 0 : print(num_list[len(num_list)//2 -1])
#     else: print(num_list[len(num_list)//2])


# 1980 햄버거 사랑
# import sys
# input = sys.stdin.readline

# n, m, t = map(int, input().split())
# if n >= m: max_nm, min_nm = n, m
# else: max_nm, min_nm = m, n

# min_time = 10000
# max_hamburger = 10000

# # i : 먹는 시간이 적게 드는 햄버거의 개수
# for i in range(t//min_nm, -1, -1):
#     sum_hamburger = 0
#     res_t = t - i * min_nm

#     # other_hamburger : 다른(시간이 많이 드는) 햄버거의 개수
#     other_hamburger = res_t // max_nm
#     res_t %= max_nm
#     sum_hamburger = i + other_hamburger

#     if min_time > res_t:
#         min_time = res_t
#         max_hamburger = sum_hamburger

# print(max_hamburger, min_time)


# import sys
# input = sys.stdin.readline

# # n, m, t = map(int, input().split())
# for n in range(1, 10):
#     for m in range(1, 10):
#         for t in range(1, 10):

#             if n >= m: max_nm, min_nm = n, m
#             else: max_nm, min_nm = m, n

#             min_time = 10000
#             max_hamburger = 10000

#             # i : 먹는 시간이 적게 드는 햄버거의 개수
#             for i in range(t//min_nm, -1, -1):
#                 sum_hamburger = 0
#                 res_t = t - i * min_nm

#                 # other_hamburger : 다른(시간이 많이 드는) 햄버거의 개수
#                 other_hamburger = res_t // max_nm
#                 res_t %= max_nm
#                 sum_hamburger = i + other_hamburger

#                 if min_time > res_t:
#                     min_time = res_t
#                     max_hamburger = sum_hamburger

#             hamberger = 0
#             cola = 0

#             t_2 = t
#             if n + m > t_2:
#                 hamberger += (t_2 // min_nm)
#                 cola += min(t_2 % min_nm, t_2 % max_nm)

#             else:
#                 while t_2 > 0:
#                     if t_2 % min_nm == 0:
#                         hamberger += (t_2 // min_nm)
#                         break

#                     t_2 -= max_nm
#                     hamberger += 1

#             if t_2 < 0:
#                 hamberger -= 1
#                 t_2 += max_nm
#                 cola += t_2

#             # print(hamberger, cola)
#             if max_hamburger != hamberger or min_time != cola:
#                 print(n, m, t)
#                 print("[ 정답 ]", max_hamburger, min_time)
#                 print("[ 출력 ]", hamberger, cola)
#                 print()


# 5397 키로거
# (헷갈리는 표현) 만약 커서의 위치가 줄의 마지막이 아니라면,
# 커서 및 커서 오른쪽에 있는 모든 문자는 오른쪽으로 한 칸 이동한다.

# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     word_list = list(input().rstrip())
#     pw_stack, temp_stack = [], []

#     for i in range(len(word_list)):
#         if word_list[i] == '<':
#             if not pw_stack: continue
#             else: temp_stack.append(pw_stack.pop())
#         elif word_list[i] == '>':
#             if not temp_stack: continue
#             else: pw_stack.append(temp_stack.pop())
#         elif word_list[i] == '-':
#             if not pw_stack: continue
#             else: pw_stack.pop()
#         else: pw_stack.append(word_list[i])

#     while temp_stack:
#         pw_stack.append(temp_stack.pop())

#     print(*pw_stack, sep='')


# 2167 2차원 배열의 합
# 시간초과
# PyPy3로 통과
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# l_n = [list(map(int, input().split())) for _ in range(n)]

# for _ in range(int(input())):
#     i, j, x, y = map(int, input().split())
#     total_sum = 0

#     for i in range(i-1, x):
#         total_sum += sum(l_n[i][j-1:y])

#     print(total_sum)


# 합계 dp


# 10926 ??!
# print(input()+'??!')


# 14652 나는 행복합니다~
# n, m, k = map(int, input().split())
# print(k//m, k%m)


# 유기농 배추
# RecursionError 고치고 바로 통과 ㄷㄷ
# 아예 안 보고 풀었음 ~ 기분 좋아 ~~~

# import sys
# from collections import deque

# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline
# que = deque()

# def check_bfs(graph, check_graph, nx, ny, m, n):
#     x = [1, 0, -1, 0]
#     y = [0, 1, 0, -1]

#     if(graph[nx][ny] == 1 and check_graph[nx][ny] == 0):
#         check_graph[nx][ny] = 1

#         for i in range(4):
#             if 0 <= nx + x[i] < m and 0 <= ny + y[i] < n:
#                 check_bfs(graph, check_graph, nx+x[i], ny+y[i], m, n)
#         return True

#     else: return False


# for _ in range(int(input())):
#     m, n, k = map(int, input().split())

#     # 입력값에 맞춰서 초기화
#     # graph = [[0] * m for _ in range(n)]
#     # check_graph = [[0] * m for _ in range(n)]

#     graph = [[0] * n for _ in range(m)]
#     check_graph = [[0] * n for _ in range(m)]

#     for _ in range(k):
#         dot_x, dot_y = map(int, input().split())
#         graph[dot_x][dot_y] = 1

#     total_area = 0
#     for nx in range(m):
#         for ny in range(n):
#             if check_bfs(graph, check_graph, nx, ny, m, n):
#                 total_area += 1

#     print(total_area)


# 1620 나는야 포켓몬 마스터 이다솜
# import sys
# input = sys.stdin.readline

# def solve():
#     n, m = map(int, input().split())
#     pokemon_dict_1 = dict()
#     for i in range(1, n+1):
#         pokemon_dict_1[input().rstrip()] = i
#     # print(pokemon_dict_1)
#     pokemon_dict_2 = {v:k for k,v in pokemon_dict_1.items()}
#     # print(pokemon_dict_2)

#     for i in range(1, m+1):
#         input_value = input().rstrip()
#         if 65 <= ord(input_value[0]) <= 90 : print(pokemon_dict_1[input_value])
#         else: print(pokemon_dict_2[int(input_value)])

# solve()


# 연구소 14502
# 1st try clear

# import sys
# import copy
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# def virus_bfs(virus_graph, check_graph, nx, ny, n, m, plus_x, plus_y):
#     if virus_graph[nx][ny] == 2 and check_graph[nx][ny] == 0:
#         check_graph[nx][ny] = 1
#         for idx in range(4):
#             new_x, new_y = nx + plus_x[idx], ny + plus_y[idx]
#             if 0 <= new_x < n and 0 <= new_y < m and virus_graph[new_x][new_y] != 1:
#                 virus_graph[new_x][new_y] = 2
#                 virus_bfs(virus_graph, check_graph, new_x, new_y, n, m, plus_x, plus_y)

# def solve():
#     n, m = map(int, input().split())
#     graph = [list(map(int, input().split())) for _ in range(n)]
#     # print(graph)

#     # 0은 빈 칸, 1은 벽, 2가 바이러스
#     # 빈 칸의 개수는 3개 이상
#     blank_dot = []
#     virus_dot = []

#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0 : blank_dot.append([i, j])
#             elif graph[i][j] == 2: virus_dot.append([i, j])

#     len_blank_dot = len(blank_dot)
#     # print(len_blank_dot)
#     max_count = 0

#     for i in range(0, len_blank_dot-2):
#         for j in range(i+1, len_blank_dot-1):
#             for k in range(j+1, len_blank_dot):
#                 # 바이러스 퍼졌을 때 상태
#                 new_graph = copy.deepcopy(graph)

#                 for x in [i, j, k]:
#                     new_graph[blank_dot[x][0]][blank_dot[x][1]] = 1
#                 # print(i,j,k)
#                 # print(new_graph)
#                 check_graph = [[0] * m for _ in range(n)]

#                 plus_x = [1, 0, -1, 0]
#                 plus_y = [0, 1, 0, -1]

#                 # for nx in range(n):
#                 #     for ny in range(m):
#                 for nx, ny in virus_dot:
#                        virus_bfs(new_graph, check_graph, nx, ny, n, m, plus_x, plus_y)

#                 # for nx in range(n):
#                 #     print(new_graph[nx])

#                 count = 0
#                 for nx in range(n):
#                     for ny in range(m):
#                         if new_graph[nx][ny] == 0: count += 1

#                 if max_count < count: max_count = count
#     return max_count

# print(solve())


# 위 코드 개선
# import sys
# from collections import deque
# # sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# que = deque()

# def virus_dfs(virus_graph, nx, ny, n, m, plus_x, plus_y):
#     for idx in range(4):
#         new_x, new_y = nx + plus_x[idx], ny + plus_y[idx]
#         if 0 <= new_x < n and 0 <= new_y < m and virus_graph[new_x][new_y] == 0:
#             virus_graph[new_x][new_y] = 2
#             virus_dfs(virus_graph, new_x, new_y, n, m, plus_x, plus_y)

# def virus_bfs(virus_graph, n, m, plus_x, plus_y):
#     nx, ny = que.popleft()
#     for idx in range(4):
#         new_x, new_y = nx + plus_x[idx], ny + plus_y[idx]
#         if 0 <= new_x < n and 0 <= new_y < m and virus_graph[new_x][new_y] == 0:
#             virus_graph[new_x][new_y] = 2
#             que.append([new_x, new_y])
#     if que: virus_bfs(virus_graph, n, m, plus_x, plus_y)

# def reset_graph(graph, blank_dot, wall_dot, virus_dot):
#     # for nx, ny in blank_dot: graph[nx][ny] = 0
#     # for nx, ny in wall_dot: graph[nx][ny] = 1
#     # for nx, ny in virus_dot: graph[nx][ny] = 2
#     new_list = [blank_dot, wall_dot, virus_dot]
#     for i in range(3):
#         for x, y in new_list[i]:
#             graph[x][y] = i

# def solve():
#     n, m = map(int, input().split())
#     graph = [list(map(int, input().split())) for _ in range(n)]
#     # print(graph)

#     # 0은 빈 칸, 1은 벽, 2가 바이러스
#     # 빈 칸의 개수는 3개 이상
#     blank_dots, wall_dots, virus_dots = [], [], []
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0 : blank_dots.append([i, j])
#             elif graph[i][j] == 1: wall_dots.append([i, j])
#             else: virus_dots.append([i, j])

#     len_blank_dots = len(blank_dots)
#     # print(len_blank_dot)
#     max_count = 0

#     for i in range(0, len_blank_dots-2):
#         for j in range(i+1, len_blank_dots-1):
#             for k in range(j+1, len_blank_dots):
#                 # graph 초기화
#                 reset_graph(graph, blank_dots, wall_dots, virus_dots)
#                 for x in [i, j, k]:
#                     graph[blank_dots[x][0]][blank_dots[x][1]] = 1
#                 # print(i,j,k)
#                 # print(new_graph)
#                 # check_graph = [[0] * m for _ in range(n)]

#                 plus_x = [1, 0, -1, 0]
#                 plus_y = [0, 1, 0, -1]

#                 # for nx in range(n):
#                 #     for ny in range(m):
#                 for nx, ny in virus_dots:
#                     virus_dfs(graph, nx, ny, n, m, plus_x, plus_y)
#                     # que.append([nx, ny])
#                     # virus_bfs(graph, n, m, plus_x, plus_y)

#                 # for nx in range(n):
#                 #     print(graph[nx])

#                 count = 0
#                 for nx in range(n):
#                     for ny in range(m):
#                         if graph[nx][ny] == 0: count += 1
#                 if max_count < count: max_count = count
#     return max_count

# print(solve())

"""
dfs/bfs
1. check_graph가 별도로 필요한 경우가 있으니 필요하다 싶으면 바로 확인
2. 브루트포스로 각 index에 접근할 때 for문 안에 dfs/bfs 함수를 넣어서 구현해야 함,
    dfs/bfs 함수 안에서 브루트포스로 접근 X
3. 재귀 limit 풀기 sys.setrecursionlimit(10**6)

빠른 건 dfs가 더 빠른 듯, 대신 좌표 값을 넘겨주어야 함 (nx, ny)
"""


# 2477 참외밭
# import sys
# input = sys.stdin.readline

# n = int(input())
# # sq_info = [[] for _ in range(5)]
# sq_info = []
# count_list = [0] * 5

# for _ in range(6):
#     temp_list = list(map(int, input().split()))
#     sq_info.append(temp_list)
#     count_list[temp_list[0]] += 1
# # print(sq_info)
# # print(count_list)

# # # 모든 경우의 수 -> 동쪽/서쪽 중 1방향 2번, 남쪽/북쪽 중 1방향 2번으로 나눌 수 있음
# count_1_list = [i for i in range(1, 5) if count_list[i] == 1]
# k = 0 # 처음으로 1번 카운트된 숫자가 나올 때의 인덱스를 체크하는 변수
# for i in range(5):
#     if sq_info[i][0] in count_1_list:
#         if sq_info[i+1][0] in count_1_list: k = i # %6 안 해도 됨
#         else: k = 5 # sq_info[0][0], sq_info[5][0]이 0인 경우
#         break
# # print(first_count_1_index)

# field_area = sq_info[k][1]*sq_info[(k+1)%6][1] - sq_info[(k+3)%6][1]*sq_info[(k+4)%6][1]
# print(field_area * n)


# 2206 벽 부수고 이동하기
# import sys
# from collections import deque
# input = sys.stdin.readline

# def move_bfs(graph, que, n, m, plus_x, plus_y):
#     nx, ny, move_count, wall_distroy_check = que.popleft()
#     move_count += 1

#     for i in range(4):
#         new_x, new_y = nx + plus_x[i], ny + plus_y[i]
#         if 0 <= new_x < n and 0 <= new_y < m:
#             # print(new_x, new_y)
#             if new_x == n-1 and new_y == m-1: return move_count
#             if graph[new_x][new_y] == 0:
#                 graph[new_x][new_y] = 2
#                 que.append([new_x, new_y, move_count, wall_distroy_check])
#             elif graph[new_x][new_y] == 1:
#                 if wall_distroy_check == 0:
#                     que.append([new_x, new_y, move_count, 1])

#     if que: return move_bfs(graph, que, n, m, plus_x, plus_y)

# def solve():
#     n, m = map(int, input().split())
#     # graph = [list(map(int, input().split())) for _ in range(n)]
#     graph = [list(map(int, input().rstrip())) for _ in range(n)]
#     # print(graph)
#     # nx, ny, move_count, wall_distroy_check
#     que = deque([[0, 0, 1, 0]])
#     # que = deque()
#     # que.append([0, 0, move_count, wall_distroy_check])
#     # print(que)

#     plus_x = [1, 0, -1, 0]
#     plus_y = [0, 1, 0, -1]

#     result = move_bfs(graph, que, n, m, plus_x, plus_y)
#     if result is not None: print(result)
#     else: print(-1)

# solve()


# 21퍼 틀렸습니다
# 1개의 graph만 공유해서 풀려고 하면 문제가 생김
# import sys
# from collections import deque
# # sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# def move_bfs(graph, que, n, m, plus_x, plus_y):
#     global result
#     nx, ny, move_count, wall_distroy_check = que.popleft()
#     move_count += 1

#     for i in range(4):
#         new_x, new_y = nx + plus_x[i], ny + plus_y[i]
#         if 0 <= new_x < n and 0 <= new_y < m:
#             # print(new_x, new_y)
#             if new_x == n-1 and new_y == m-1:
#                 result = move_count
#                 # print(move_count)
#             if graph[new_x][new_y] == 0:
#                 graph[new_x][new_y] = 2
#                 que.append([new_x, new_y, move_count, wall_distroy_check])
#             elif graph[new_x][new_y] == 1:
#                 if wall_distroy_check == 0:
#                     que.append([new_x, new_y, move_count, 1])
#     # if que: move_bfs(graph, que, n, m, plus_x, plus_y)

# def solve():
#     n, m = map(int, input().split())
#     graph = [list(map(int, input().rstrip())) for _ in range(n)]
#     # nx, ny, move_count, wall_distroy_check
#     que = deque([[0, 0, 1, 0]])

#     plus_x = [1, 0, -1, 0]
#     plus_y = [0, 1, 0, -1]
#     # result = move_bfs(graph, que, n, m, plus_x, plus_y)
#     global result
#     result = -1

#     while que:
#         move_bfs(graph, que, n, m, plus_x, plus_y)

#     # if result is : print(result)
#     # else: print(-1)
#     print(result)

# solve()


# 시간 초과
# import sys
# import copy
# from collections import deque
# input = sys.stdin.readline

# def move_bfs(graph, que, n, m, plus_x, plus_y):
#     global result
#     nx, ny, move_count, wall_distroy_check, visited = que.popleft()
#     # print(nx, ny, move_count, wall_distroy_check)

#     # print("visited :", visited, "0")
#     # print(type(visited), len(visited))
#     # print(visited[i] for i in range(len(visited)))
#     # print(new_visited[i] for i in range(len(new_visited)))

#     move_count += 1

#     for i in range(4):
#         new_x, new_y = nx + plus_x[i], ny + plus_y[i]
#         if 0 <= new_x < n and 0 <= new_y < m:
#             # print(new_x, new_y)
#             if [new_x, new_y] in visited: continue
#             else:
#                 if new_x == n-1 and new_y == m-1:
#                     result = move_count
#                     que.clear()
#                     return
#                 if graph[new_x][new_y] == 0:
#                     new_visited = copy.deepcopy(visited)
#                     new_visited.append([new_x, new_y])
#                     # print("haha", new_visited)
#                     que.append([new_x, new_y, move_count, wall_distroy_check, new_visited])
#                 elif graph[new_x][new_y] == 1:
#                     if wall_distroy_check == 0:
#                         new_visited = copy.deepcopy(visited)
#                         new_visited.append([new_x, new_y])
#                         # print("haha", new_visited)
#                         que.append([new_x, new_y, move_count, 1, new_visited])
#     # print("move_count :", move_count)

# def solve():
#     n, m = map(int, input().split())
#     graph = [list(map(int, input().rstrip())) for _ in range(n)]
#     # nx, ny, move_count, wall_distroy_check
#     # visited = [[0, 0]]
#     # que = deque([[0, 0, 1, 0, [[0, 0]]]])
#     que = deque([[0, 0, 1, 0, [[0, 0]]]])

#     plus_x = [1, 0, -1, 0]
#     plus_y = [0, 1, 0, -1]

#     global result
#     result = -1

#     if n == 1 and m == 1: print(1)
#     else:
#         while que:
#             move_bfs(graph, que, n, m, plus_x, plus_y)
#             # print("que:", que)
#     print(result)

# solve()


# finally i solved it
# import sys
# from collections import deque
# input = sys.stdin.readline

# def move_bfs(graph, que, n, m, plus_x, plus_y):
#     global result
#     nx, ny, move_count, wall_distroy_val = que.popleft()
#     # print(nx, ny, move_count, wall_distroy_val)
#     move_count += 1

#     for i in range(4):
#         new_x, new_y = nx + plus_x[i], ny + plus_y[i]
#         if 0 <= new_x < n and 0 <= new_y < m:
#             # print(new_x, new_y)
#             if new_x == n-1 and new_y == m-1:
#                 result = move_count
#                 que.clear()
#                 return
#             # 빈 공간
#             if graph[new_x][new_y] == 0:
#                 graph[new_x][new_y] = move_count * wall_distroy_val
#                 que.append([new_x, new_y, move_count, wall_distroy_val])
#             # 벽인 경우, 한 번도 벽을 부순적 없으면 distroy
#             elif graph[new_x][new_y] == 1:
#                 if wall_distroy_val == 1:
#                     que.append([new_x, new_y, move_count, -1])
#             # 벽을 부수면서 왔던 칸에 벽을 부수지 않고 도착한 경우 (단, 여기서 도착한 칸은 벽이 아님)
#             elif graph[new_x][new_y] < 0:
#                 if wall_distroy_val == 1:
#                     graph[new_x][new_y] = move_count * 1
#                     que.append([new_x, new_y, move_count, 1])
#     # print("move_count :", move_count)

# def solve():
#     n, m = map(int, input().split())
#     graph = [list(map(int, input().rstrip())) for _ in range(n)]
#     # nx, ny, move_count, wall_distroy_val(1 : yet, -1 : done)
#     que = deque([[0, 0, 1, 1]])

#     plus_x = [1, 0, -1, 0]
#     plus_y = [0, 1, 0, -1]

#     global result
#     result = -1

#     if n == 1 and m == 1: print(1)
#     else:
#         graph[0][0] = 2
#         while que:
#             move_bfs(graph, que, n, m, plus_x, plus_y)
#             # print(que)
#         print(result)

# solve()


# 4999 아!
# import sys
# input = sys.stdin.readline

# if len(input()) < len(input()): print("no")
# else: print("go")


# 2583 영역 구하기 bfs

# import sys
# from collections import deque
# input = sys.stdin.readline

# def area_bfs(que, inc_xy, graph, check_graph, m, n, area_num):
#     nx, ny = que.popleft()
#     graph[ny][nx] = area_num
#     check_graph[ny][nx] = 1
#     for i in range(4):
#         new_x, new_y = nx + inc_xy[i][0], ny + inc_xy[i][1]
#         if 0 <= new_x < n and 0 <= new_y < m and graph[new_y][new_x] == 0 and check_graph[new_y][new_x] == 0:
#             que.append([new_x, new_y])

# def solve():
#     m, n, k = map(int, input().split())
#     graph = [[0] * n for _ in range(m)]
#     check_graph = [[0] * n for _ in range(m)]
#     # area_graph = [0] * 10003

#     for _ in range(k):
#         x1, y1, x2, y2 = map(int, input().split())
#         for y in range(y1, y2):
#             for x in range(x1, x2):
#                 # print(x, y) # x y 축 확인
#                 graph[y][x] = 1
#     # for i in range(m):
#     #     print(graph[i])

#     que = deque()
#     inc_xy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#     area_num = 1

#     for ny in range(m):
#         for nx in range(n):
#             if graph[ny][nx] == 0:
#                 area_num += 1
#                 que.append([nx, ny])
#                 # print(que)
#                 while que: area_bfs(que, inc_xy, graph, check_graph, m, n, area_num)

#     # for i in range(m):
#     #     print(graph[i])
#     # print()

#     # for i in range(m):
#     #     print(check_graph[i])

#     area_list = [0] * (area_num-1)
#     for y in range(m):
#         for x in range(n):
#             if graph[y][x] > 1: area_list[graph[y][x]-2] += 1

#     print(len(area_list))
#     print(*sorted(area_list))

# solve()


# 시간 초과
# 같은 칸을 여러 번 체크하고 있었음
# import sys
# from collections import deque
# input = sys.stdin.readline

# def area_bfs(que, inc_xy, graph, m, n):
#     nx, ny = que.popleft()
#     graph[ny][nx] = 1
#     for i in range(4):
#         new_x, new_y = nx + inc_xy[i][0], ny + inc_xy[i][1]
#         if 0 <= new_x < n and 0 <= new_y < m and graph[new_y][new_x] == 0 :
#             graph[new_y][new_x] = 1
#             # print(nx, ny, new_x, new_y)
#             que.append([new_x, new_y])

# def solve():
#     m, n, k = map(int, input().split())
#     graph = [[0] * n for _ in range(m)]

#     for _ in range(k):
#         x1, y1, x2, y2 = map(int, input().split())
#         for y in range(y1, y2):
#             for x in range(x1, x2):
#                 graph[y][x] = 1
#     # for i in range(m):
#     #     print(graph[i])

#     que = deque()
#     inc_xy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#     area_list = []

#     for ny in range(m):
#         for nx in range(n):
#             if graph[ny][nx] == 0:
#                 area_num = 0
#                 que.append([nx, ny])
#                 # print(que)
#                 while que:
#                     area_bfs(que, inc_xy, graph, m, n)
#                     area_num += 1
#                 area_list.append(area_num)

#     print(len(area_list))
#     print(*sorted(area_list))

# solve()


# 1037 약수
# import sys
# input = sys.stdin.readline

# n = int(input())
# num_list = sorted(list(map(int, input().split())))
# print(num_list[0] * num_list[n -1])


# 7569 토마토
# import sys
# from collections import deque
# input = sys.stdin.readline

# def tomato_bfs(que, check_graph, graph, inc_xyz, h, n, m):
#     nh, nn, nm = que.popleft()
#     graph[nh][nn][nm] = 1
#     for i in range(6):
#         new_h, new_n, new_m = nh + inc_xyz[i][2], nn + inc_xyz[i][1], nm + inc_xyz[i][0]
#         # print(new_h, new_n, new_m)
#         if 0 <= new_h < h and 0 <= new_n < n and 0 <= new_m < m :
#             if graph[new_h][new_n][new_m] == 0 and check_graph[new_h][new_n][new_m] == 0:
#                 que.append([new_h, new_n, new_m])
#                 check_graph[new_h][new_n][new_m] = 1

# def solve():
#     m, n, h = map(int, input().split())
#     tomato_graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
#     check_graph = [[[0]*m for _ in range(n)] for _ in range(h)]
#     # print(tomato_graph)

#     que = deque()
#     inc_xyz = [[1,0,0], [0,1,0], [-1,0,0], [0,-1,0], [0,0,1], [0,0,-1]]
#     # print(inc_xyz)

#     # 처음 0일차
#     day = 0
#     for z in range(h):
#         for y in range(n):
#             for x in range(m):
#                 if tomato_graph[z][y][x] == 1:
#                     # print("zyx :", z, y, x)
#                     que.append([z, y, x])
#     for _ in range(len(que)): tomato_bfs(que, check_graph, tomato_graph, inc_xyz, h, n, m)

#     # 1일차부터 닿을 수 있는 모든 토마토가 다 익을 때까지
#     while que:
#         # len_que = len(que)
#         # print(len_que)
#         for i in range(len(que)): tomato_bfs(que, check_graph, tomato_graph, inc_xyz, h, n, m)
#         day += 1

#     # 안 익은 토마토가 있으면 -1
#     for z in range(h):
#         for y in range(n):
#             for x in range(m):
#                 if tomato_graph[z][y][x] == 0:
#                     return -1
#     return day

# print(solve())


# 2210 숫자판 점프
# import sys
# input = sys.stdin.readline

# def dfs(graph, x, y, inc_xy, count, sum, ans_list):
#     sum += graph[y][x] * 10**(5-count)
#     count += 1

#     if count == 6:
#         if sum not in ans_list: ans_list.append(sum)
#     else:
#         for i in range(4):
#             new_x, new_y = x + inc_xy[i][0], y + inc_xy[i][1]
#             if 0 <= new_x < 5 and 0 <= new_y < 5:
#                 dfs(graph, new_x, new_y, inc_xy, count, sum, ans_list)

# def solve():
#     graph = [list(map(int, input().split())) for _ in range(5)]
#     # print(graph)
#     inc_xy = [[1,0], [0,1], [-1,0], [0,-1]]
#     ans_list = []

#     for y in range(5):
#         for x in range(5):
#             dfs(graph, x, y, inc_xy, 0, 0, ans_list)

#     print(len(ans_list))

# solve()


# 2504 괄호의 값
# import sys

# def solve():
#     bracket_list = list(sys.stdin.readline().rstrip())
#     # print(bracket_list)

#     mul_num = 1
#     sum = 0
#     stack_list = []

#     for i in range(len(bracket_list)):
#         if bracket_list[i] == '(' :
#             mul_num *= 2
#             stack_list.append('(')
#         elif bracket_list[i] == '[' :
#             mul_num *= 3
#             stack_list.append('[')
#         elif bracket_list[i] == ')' :
#             if not stack_list or stack_list.pop() != '(':
#                 sum = 0
#                 break
#             else:
#                 mul_num //= 2
#                 if bracket_list[i-1] == '(': sum += mul_num * 2
#         elif bracket_list[i] == ']' :
#             if not stack_list or stack_list.pop() != '[':
#                 sum = 0
#                 break
#             else:
#                 mul_num //= 3
#                 if bracket_list[i-1] == '[': sum += mul_num * 3
#         # print(i, mul_num, stack_list, sum)
#     if stack_list: print(0)
#     else: print(sum)

# solve()


# 2178 미로 탐색
# graph[x][y] -> graph[y][x], input().split() -> input().rstrip(),
# que.pop() -> que.popleft(), 함수로 바꿀 때 que 포함 시켜야 함
# bfs(graph, que, inc_xy, n, m) : 기본형

# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs(graph, que, inc_xy, n, m):
#     nx, ny, step = que.popleft()
#     for i in range(4):
#         new_x, new_y = nx + inc_xy[i][0], ny + inc_xy[i][1]
#         # print(new_x, new_y)
#         if 0 <= new_x < m and 0 <= new_y < n and graph[new_y][new_x] == 1:
#                 que.append([new_x, new_y, step+1])
#                 graph[new_y][new_x] = step+1

# def solve():
#     n, m = map(int, input().split())
#     graph = [list(map(int, input().rstrip())) for _ in range(n)]
#     check_graph = [[0] * m for _ in range(n)]
#     graph[0][0] = 0
#     # print(graph)
#     que = deque()

#     que.append([0, 0, 1])
#     inc_xy = [[1,0], [0,1], [-1,0], [0,-1]]
#     while que: bfs(graph, que, inc_xy, n, m)

#     # for i in range(n):
#     #     print(graph[i])
#     print(graph[n-1][m-1])

# solve()


# 2667 단지번호붙이기
# import sys
# from collections import deque
# input = sys.stdin.readline

# def map_bfs(graph, check_graph, que, inc_xy, n):
#     nx, ny = que.popleft()
#     for i in range(4):
#         new_x, new_y = nx + inc_xy[i][0], ny + inc_xy[i][1]
#         if 0 <= new_x < n and 0 <= new_y < n:
#             if graph[new_y][new_x] == 1 and check_graph[new_y][new_x] == 0:
#                 check_graph[new_y][new_x] = 1
#                 que.append([new_x, new_y])

# def solve():
#     n = int(input())
#     graph = [list(map(int, input().rstrip())) for _ in range(n)]
#     check_graph = [[0] * n for _ in range(n)]
#     que = deque()
#     area_list = []
#     inc_xy = [[1,0], [0,1], [-1,0], [0,-1]]

#     for y in range(n):
#         for x in range(n):
#             if graph[y][x] == 1 and check_graph[y][x] == 0:
#                 que.append([x, y])
#                 check_graph[y][x] = 1

#                 area = 0
#                 while que :
#                     map_bfs(graph, check_graph, que, inc_xy, n)
#                     area += 1
#                 # print(area)
#                 area_list.append(area)

#     print(len(area_list), *sorted(area_list), sep='\n')

# solve()


# 2644 촌수계산
# import sys
# from collections import deque
# input = sys.stdin.readline

# def par_bfs(par_graph, kid_graph, que, visited, end_num):
#     while que:
#         point, dist = que.popleft()
#         # 부모 출발 (각 사람의 부모는 최대 한 명만 주어진다)
#         for i in range(len(kid_graph[point])):
#             if kid_graph[point][i] not in visited:
#                 if kid_graph[point][i] == end_num:
#                     return dist+1
#                 else:
#                     que.append([kid_graph[point][i], dist+1])
#                     visited.append(kid_graph[point][i])

#         # 자식 출발
#         if par_graph[point] and par_graph[point][0] not in visited:
#             if par_graph[point][0] == end_num:
#                 return dist+1
#             else:
#                 que.append([par_graph[point][0], dist+1])
#                 visited.append(par_graph[point][0])
#     return -1

# def solve():
#     n = int(input())
#     start_num, end_num = map(int, input().split())

#     par_graph = [[] for _ in range(n+1)]
#     kid_graph = [[] for _ in range(n+1)]
#     for _ in range(int(input())):
#         x, y = map(int, input().split())
#         par_graph[y].append(x)
#         kid_graph[x].append(y)
#     # print(par_graph, kid_graph)

#     que = deque([[start_num, 0]])
#     visited = [start_num]
#     print(par_bfs(par_graph, kid_graph, que, visited, end_num))

# solve()


# 4796 캠핑
# import sys
# input = sys.stdin.readline

# case_num = 1
# while True:
#     val_l, val_p, val_v = map(int, input().split())
#     if val_l == 0: break
#     else:
#         print("Case {0}: {1}".format(case_num, (val_v//val_p)*val_l + min(val_v%val_p, val_l)))
#     case_num += 1


# 2468 안전 영역
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def dfs(graph, check_graph, nx, ny, inc_xy, n):
#     if check_graph[ny][nx] == 0:
#         check_graph[ny][nx] = 2
#         for i in range(4):
#             new_x, new_y = nx + inc_xy[i][0], ny + inc_xy[i][1]
#             if 0 <= new_x < n and 0 <= new_y < n:
#                 dfs(graph, check_graph, new_x, new_y, inc_xy, n)
#         return True
#     # else: return False

# def solve():
#     n = int(input())
#     graph = [list(map(int, input().split())) for _ in range(n)]
#     check_graph = [[0] * n for _ in range(n)]
#     inc_xy = [[1,0], [0,1], [-1,0], [0,-1]]

#     # 높이는 1이상 100 이하의 정수
#     min_h, max_h = 100, 1
#     for y in range(n):
#         for x in range(n):
#             if min_h > graph[y][x]: min_h = graph[y][x]
#             if max_h < graph[y][x]: max_h = graph[y][x]
#     # print(min_h, max_h)

#     max_area = 1
#     for h in range(min_h, max_h): # max_h는 계산 안 해도 됨
#         # h 이하의 높이를 가지는 곳은 다 잠김
#         for y in range(n):
#             for x in range(n):
#                 if graph[y][x] <= h: check_graph[y][x] = 1
#                 else: check_graph[y][x] = 0

#         count = 0
#         # dfs 계산해서 count
#         for y in range(n):
#             for x in range(n):
#                 if dfs(graph, check_graph, x, y, inc_xy, n) == True:
#                     count += 1
#         if max_area < count : max_area = count
#     print(max_area)

# solve()


# 1300 K번째 수
# 22퍼 틀렸습니다
# 결국 해결함 ㅋㅋ 이해하는데 좀 걸렸다 맨이야
# n == 5, 20 <= k <= 25 조건으로 해보니까 반례도 잘 보인다 맨이야

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def binary_search(top, bot, n, k):
#     if top < bot : return bot

#     # top >= bot
#     mid = (bot + top)//2
#     below_count = 0
#     for i in range(1, n+1):
#         below_count += min((n, mid//i))
#         # print(i, below_count)
#     # print(top, bot, below_count, mid)
#     if below_count < k: return binary_search(top, mid+1, n, k)
#     else: return binary_search(mid-1, bot, n, k)

# def solve():
#     n = int(input())
#     k = int(input())

#     print(binary_search(n**2, 1, n, k))

# solve()


# import sys
# input = sys.stdin.readline

# def solve():
#     n = int(input())
#     k = int(input())

#     top, bot, ans = n**2, 1, 0
#     while top >= bot:
#         below_count = 0
#         mid = (bot + top) // 2
#         for i in range(1, n+1):
#             below_count += min((n, mid//i))
#         if below_count < k: bot = mid+1
#         else:
#             ans = mid
#             top = mid-1
#     print(ans)

# solve()


# 1697 숨바꼭질
# import sys
# from collections import deque

# def solve():
#     n, k = map(int, sys.stdin.readline().split())
#     # print(n, k)
#     que = deque([[n, 0]])
#     check_graph = [0]*150001

#     if n == k: print(0)
#     else:
#         while que:
#             x, cnt = que.popleft()
#             for nx in [x-1, x+1, x*2]:
#                 # print(nx)
#                 if nx == k :
#                     print(cnt+1)
#                     return
#                 elif nx < 0 or nx > 150000: continue
#                 else:
#                     # print(nx)
#                     if check_graph[nx] == 0:
#                         check_graph[nx] = 1
#                         que.append([nx, cnt+1])
#                     else: continue

# solve()


# 6416 트리인가?
# import sys
# input = sys.stdin.readline

# while True:
#     graph = [[] for _ in range(14)]

#     while True:
#         # 입력 데이터 처리
#         temp_list = list(map(int, input().split()))
#         # print(temp_list)
#         for i in range(len(temp_list)//2):


# 1816 암호 키
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     num = int(input())
#     check = False
#     if num % 2 == 0 : check = True
#     else:
#         div_num = 3
#         while div_num <= 1000000:
#             if num % div_num == 0:
#                 check = True
#                 break
#             div_num += 2
#     if check == True: print("NO")
#     else: print("YES")


# 아무래도이문제는A번난이도인것같다
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     input()
#     print("yes")


# 4153 직각삼각형
# import sys
# input = sys.stdin.readline

# while True:
#     a, b, c = sorted(list(map(int, input().split())))
#     if a == 0 : break

#     if a**2 + b**2 == c**2 : print("right")
#     else: print("wrong")


# 11724 연결 요소의 개수
# 44퍼 틀렸습니다 ? 보완 완료 ~
# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs(graph, check_graph, que):
#     idx = que.popleft()
#     for x in range(len(graph[idx])):
#         if check_graph[graph[idx][x]] == 1: continue
#         else:
#             check_graph[graph[idx][x]] = 1
#             que.append(graph[idx][x])
#     # print(que)

# def solve():
#     n, m = map(int, input().split())
#     graph = [[] for _ in range(n+1)]
#     check_graph = [0]*(n+1)
#     que = deque()

#     for _ in range(m):
#         u, v = map(int, input().split())
#         graph[u].append(v)
#         graph[v].append(u)
#     # print(graph)

#     count = 0
#     for i in range(1, n+1):
#         for x in range(len(graph[i])):
#             if check_graph[graph[i][x]] == 1: continue
#             else:
#                 check_graph[graph[i][x]] = 1
#                 que.append(graph[i][x])
#                 count += 1
#             while que:
#                 bfs(graph, check_graph, que)
#         # 점 하나로만 되어있는 경우도 연결 요소 개수에 포함
#         if not graph[i]:
#             check_graph[i] = 1
#             count += 1
#         # print(check_graph)
#     print(count)

# solve()


# 7576 토마토
# import sys
# from collections import deque
# input = sys.stdin.readline

# def dfs(graph, que, inc_xy, m, n):
#     nx, ny, day = que.popleft()
#     for i in range(4):
#         new_x, new_y = nx + inc_xy[i][0], ny + inc_xy[i][1]
#         if 0 <= new_x < m and 0 <= new_y < n:
#             if graph[new_y][new_x] == 0:
#                 graph[new_y][new_x] = day+1
#                 que.append([new_x, new_y, day+1])

# def solve():
#     m, n = map(int, input().split())
#     graph = [list(map(int, input().split())) for _ in range(n)]
#     que = deque()
#     inc_xy = [[1,0], [0,1], [-1,0], [0,-1]]

#     for y in range(n):
#         for x in range(m):
#             if graph[y][x] == 1:
#                 que.append([x, y, 1])

#     while que:
#         dfs(graph, que, inc_xy, m, n)

#     max = 0
#     for y in range(n):
#         for x in range(m):
#             if graph[y][x] == 0:
#                 print(-1)
#                 return
#             elif max < graph[y][x] : max = graph[y][x]
#     print(max-1)

# solve()


# 11050 이항 계수 1

# def cal_factorial(num):
#     if num <= 1: return 1
#     else:
#         ans = 1
#         for i in range(num, 1, -1):
#             ans *= i
#         return ans

# def solve():
#     n, k = map(int, input().split())
#     ans = cal_factorial(n)//(cal_factorial(k)*cal_factorial(n-k))
#     print(ans)

# solve()


# 1654 랜선 자르기
# import sys
# input = sys.stdin.readline

# def solve():
#     k, n = map(int, input().split())
#     line_list = [int(input()) for _ in range(k)]
#     bot, top = 1, max(line_list)
#     ans = 0

#     while bot <= top:
#         mid = (bot + top)// 2
#         cnt = 0
#         for i in range(k):
#             cnt += line_list[i] // mid
#         # print(cnt)

#         if cnt < n :
#             top = mid-1
#         else:
#             ans = mid
#             bot = mid+1
#         # print(top, bot, mid)
#     print(ans)

# solve()


# 2292 벌집
#  1 6 12 18 24
# import sys

# def solve():
#     num = int(sys.stdin.readline())
#     cnt, ans = 0, 1

#     # while True:
#     #     if num <= ans:
#     #         print(cnt+1)
#     #         break
#     #     else:
#     #         cnt += 1
#     #         ans += cnt*6

#     while num > ans:
#         cnt += 1
#         ans += cnt*6

#     print(cnt+1)

# solve()


# 2805 나무 자르기 (지금의 나는 다르다 !)
# import sys
# input = sys.stdin.readline

# def solve():
#     n, m = map(int, input().split())
#     tree_list = list(map(int, input().split()))
#     bot, top = 1, max(tree_list)
#     ans = 0

#     while bot <= top :
#         mid, sum = (bot+top)//2, 0

#         for tree_height in tree_list:
#             if tree_height > mid:
#                 sum += tree_height - mid

#         if sum >= m :
#             ans = mid
#             bot = mid + 1
#         else: top = mid - 1

#     print(ans)

# solve()


# 2338 긴자리 계산
# import sys
# input = sys.stdin.readline

# a = int(input())
# b = int(input())
# print(a+b, a-b, a*b, sep='\n')


# 10867 중복 빼고 정렬하기
# https://xlog.tistory.com/20
# 방법 1
# import sys
# input = sys.stdin.readline

# n = int(input())
# num_list = list(map(int, input().split()))
# # print(num_list)

# new_num_list = []
# for num in num_list:
#     if num not in new_num_list:
#         new_num_list.append(num)

# print(*sorted(new_num_list))


# 방법2
# import sys
# input = sys.stdin.readline

# n = int(input())
# num_list = list(map(int, input().split()))
# # print(num_list)

# # -1000 ~ +1000
# check_list = [0]*2001
# for num in num_list:
#     if check_list[num+1000] == 0: check_list[num+1000] = 1

# for i in range(2001):
#     if check_list[i] == 1: print(i-1000, end=' ')


# 15829 Hashing
# import sys
# input = sys.stdin.readline

# def solve():
#     num = int(input())
#     val_list = list(map(ord, input().rstrip()))
#     # print(val_list)

#     # num 값으로 r**i (mod M) list를 생성
#     mul_list = [1] * num
#     for i in range(1, num):
#         mul_list[i] = mul_list[i-1] * 31
#         if mul_list[i] >= 1234567891 : mul_list[i] %= 1234567891
#     # print(mul_list)

#     # 정답 ans 계산
#     ans = 0
#     for i in range(num):
#         ans += (val_list[i]-96) * mul_list[i]
#         if ans >= 1234567891 : ans %= 1234567891
#     print(ans)

# solve()


# 1085 직사각형에서 탈출
# x, y, w, h = map(int, input().split())
# print(min([x, y, w-x, h-y]))


# 2573 빙산
# 37퍼 시간초과 ?
# 가능하면 copy.deepcopy()는 안 쓰는 게 메모리 관리나 속도 면에서 유리한 듯

# import sys
# from collections import deque
# input = sys.stdin.readline

# def graph_copy(graph_a, graph_b, n, m):
#     for y in range(1, n-1):
#         for x in range(1, m-1):
#             graph_a[y][x] = graph_b[y][x]

# def solve():
#     n, m = map(int, input().split())
#     pre_graph = [list(map(int, input().split())) for _ in range(n)]
#     new_graph = [[0] * m for _ in range(n)]
#     # print(pre_graph)

#     years = 0
#     all_melt = False
#     while not all_melt:
#         years += 1
#         graph_copy(new_graph, pre_graph, n, m)
#         inc_xy = [[1,0], [0,1], [-1,0], [0,-1]]

#         # 1년이 지났을 때
#         all_melt = True
#         for ny in range(n):
#             for nx in range(m):
#                 if pre_graph[ny][nx] != 0:
#                     for x, y in inc_xy:
#                         if new_graph[ny][nx] > 0 and pre_graph[ny + y][nx + x] == 0:
#                             new_graph[ny][nx] -= 1
#                             all_melt = False
#         # print("years: ", years)
#         # print("new :", new_graph)

#         # n 덩이 계산
#         count = 0
#         que = deque()
#         check_graph = [[0]*m for _ in range(n)]
#         for ny in range(n):
#             for nx in range(m):
#                 if new_graph[ny][nx] != 0 and check_graph[ny][nx] == 0:
#                     count += 1
#                     if count > 1 : return years

#                     check_graph[ny][nx] = 1
#                     que.append([nx, ny])
#                     while que:
#                         # now_x, now_y = que.popleft()
#                         now_x, now_y = que.pop()
#                         for x, y in inc_xy:
#                             if check_graph[now_y + y][now_x + x] == 0 and new_graph[now_y + y][now_x + x] != 0:
#                                 check_graph[now_y + y][now_x + x] = 1
#                                 que.append([now_x + x, now_y + y])
#         # print(count)
#         graph_copy(pre_graph, new_graph, n, m)
#     return 0

# print(solve())


# 37퍼 시간 초과.. 그냥 PyPy3로 해결
# import sys
# from collections import deque
# input = sys.stdin.readline

# def solve():
#     n, m = map(int, input().split())
#     graph = [list(map(int, input().split())) for _ in range(n)]
#     check_graph = [[0]*m for _ in range(n)]
#     # print(graph)

#     years = 0
#     all_melt = False
#     while not all_melt:
#         years += 1
#         inc_xy = [[1,0], [0,1], [-1,0], [0,-1]]

#         # 1년이 지났을 때
#         all_melt = True
#         for ny in range(n):
#             for nx in range(m):
#                 if graph[ny][nx] != 0:
#                     for x, y in inc_xy:
#                         if graph[ny][nx] > 0 and graph[ny + y][nx + x] == 0:
#                             graph[ny][nx] -= 1
#                             # 1개의 그래프로 bfs 방식에서 계산을 정확하게 하기 위해 0이 아닌 값으로 처리
#                             if graph[ny][nx] == 0: graph[ny][nx] = -1
#                             all_melt = False

#         # 완전히 녹은 것들을 0으로 알맞게 초기화, check_graph 초기화
#         for ny in range(n):
#             for nx in range(m):
#                 if graph[ny][nx] == -1: graph[ny][nx] = 0
#                 check_graph[ny][nx] = 0

#         # n 덩이 계산
#         count = 0
#         que = deque()
#         for ny in range(n):
#             for nx in range(m):
#                 if graph[ny][nx] != 0 and check_graph[ny][nx] == 0:
#                     count += 1
#                     if count > 1 : return years

#                     check_graph[ny][nx] = 1
#                     que.append([nx, ny])
#                     while que:
#                         # now_x, now_y = que.popleft()
#                         now_x, now_y = que.pop()
#                         for x, y in inc_xy:
#                             if graph[now_y + y][now_x + x] != 0 and check_graph[now_y + y][now_x + x] == 0 :
#                                 check_graph[now_y + y][now_x + x] = 1
#                                 que.append([now_x + x, now_y + y])
#         # print(count)
#     return 0

# print(solve())


# 11723 집합
# import sys
# input = sys.stdin.readline

# def solve():
#     set_s = set()
#     for _ in range(int(input())):
#         cmd_list = list(map(str, input().split()))
#         # print(cmd_list)

#         if cmd_list[0] == 'add':
#             val = int(cmd_list[1])
#             if val not in set_s:
#                 set_s.add(val)
#         elif cmd_list[0] == 'remove':
#             val = int(cmd_list[1])
#             if val in set_s:
#                 set_s.remove(int(cmd_list[1]))

#         elif cmd_list[0] == 'check':
#             if int(cmd_list[1]) in set_s: print(1)
#             else: print(0)
#         elif cmd_list[0] == 'toggle':
#             val = int(cmd_list[1])
#             if val in set_s: set_s.remove(val)
#             else: set_s.add(val)

#         elif cmd_list[0] == 'all':
#             set_s = {i for i in range(1, 21)}
#         else: # cmd_list[0] == 'empty'
#             set_s.clear()
#         # print(set_s)

# solve()


# 9375 패션왕 신해빈
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     clothes_dict = dict()
#     for i in range(int(input())):
#         clothes_list = list(map(str, input().split()))
#         # print(clothes_list)

#         if clothes_list[1] not in clothes_dict: clothes_dict[clothes_list[1]] = 1
#         else: clothes_dict[clothes_list[1]] += 1
#     # print(clothes_dict)

#     ans = 1
#     for i in clothes_dict:
#         ans *= (clothes_dict[i]+1)

#     print(ans-1)


# 2420 사파리 월드
# n, m = map(int, input().split())
# print(abs(n-m))

# 10871 X보다 작은 수
# n, x = map(int, input().split())
# n_list = list(map(int, input().split()))
# for i in n_list:
#     if i < x:
#         print(i, end=' ')


# 10807 개수 세기
# import sys
# input = sys.stdin.readline

# n = int(input())
# n_list = list(map(int, input().split()))
# target = int(input())
# count = 0

# for i in n_list:
#     if i == target: count += 1

# print(count)


# 5597 과제 안 내신 분..?
# import sys
# input = sys.stdin.readline

# # 0 ~ 30
# attend_list = [0] * 31

# for _ in range(28):
#     attend_list[int(input())] += 1

# for i in range(1, 31):
#     if attend_list[i] == 0: print(i)


# 2738 행렬 덧셈
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# # 행렬 A
# num_list = [list(map(int, input().split())) for _ in range(n)]

# # 행렬 B 합산
# for y in range(n):
#     tmp_list = list(map(int, input().split()))
#     for x in range(m):
#         num_list[y][x] += tmp_list[x]

# # 출력
# for i in range(n):
#     print(*num_list[i])


# 2743 단어 길이 재기
# print(len(input()))

# 2744 대소문자 바꾸기
# str_list = list(input())
# for i in range(len(str_list)):
#     if 65 <= ord(str_list[i]) < 91: print(chr(ord(str_list[i])+32), end='')
#     else: print(chr(ord(str_list[i])-32), end='')


# 14490 백대열

# def gcd(n, m):
#     while m > 0:
#         n, m = m, n%m
#     return n

# n, m = map(int, input().split(':'))
# gcd_num = gcd(n, m)
# print(n//gcd_num, ":", m//gcd_num, sep='')


# 11098 첼시를 도와줘!
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     max_price, max_player_name = 0, ''
#     for _ in range(int(input())):
#         val, name = map(str, input().split())
#         val = int(val)
#         if max_price < val :
#             max_price = val
#             max_player_name = name
#     print(max_player_name)


# 5635 생일
# import sys
# input = sys.stdin.readline

# earlist_birth_name, latest_birth_name= '', ''
# earlist_birth, latest_birth = [31, 12, 2010], [1, 1, 1990]
# for _ in range(int(input())):
#     name, dd, mm, yy = map(str, input().split())
#     dd, mm, yy = map(int, [dd, mm, yy])

#     # if earlist_birth[2] >= yy and earlist_birth[1] >= mm and earlist_birth[0] > dd :
#     #     earlist_birth = [dd, mm, yy]
#     #     earlist_birth_name = name
#     # elif latest_birth[2] <= yy and latest_birth[1] <= mm and latest_birth[0] < dd :
#     #     latest_birth = [dd, mm, yy]
#     #     latest_birth_name = name

#     if earlist_birth[2] > yy or\
#         (earlist_birth[2] == yy and earlist_birth[1] > mm) or\
#         (earlist_birth[2] == yy and earlist_birth[1] == mm and earlist_birth[0] > dd) :
#         earlist_birth = [dd, mm, yy]
#         earlist_birth_name = name

#     if latest_birth[2] < yy or\
#         (latest_birth[2] == yy and latest_birth[1] < mm) or\
#         (latest_birth[2] == yy and latest_birth[1] == mm and latest_birth[0] < dd) :
#         latest_birth = [dd, mm, yy]
#         latest_birth_name = name

# print(latest_birth_name, earlist_birth_name, sep='\n')


# 1408 24
# import sys
# input = sys.stdin.readline

# hh_1, mm_1, ss_1 = map(int, input().split(":"))
# hh_2, mm_2, ss_2 = map(int, input().split(":"))

# time_1 = hh_1 * 3600 + mm_1 * 60 + ss_1
# time_2 = hh_2 * 3600 + mm_2 * 60 + ss_2

# gab = time_2 - time_1
# if gab < 0: gab += 86400

# # print("{0:02d}:{1:02d}:{2:02d}".format(gab//3600, (gab%3600)//60, gab%60, sep=':'))
# print("{0:02d}:{1:02d}:{2:02d}".format(gab//3600, (gab%3600)//60, gab%60))


# 2742 기찍 N
# for i in range(int(input()), 0, -1):
#     print(i)


# 2440 별 찍기 - 3
# for i in range(int(input()), 0, -1):
#     for _ in range(i):
#         print('*', end='')
#     print()


# 2441 별 찍기 - 4
# num = int(input())
# for i in range(num, 0, -1):
#     for _ in range(num-i):
#         print(' ',end='')
#     for _ in range(i):
#         print('*', end='')
#     print()


# 8393 합
# num = int(input())
# print((1+num)*num//2)


# 5565 영수증
# import sys
# input = sys.stdin.readline

# target_price = int(input())
# for _ in range(9):
#     target_price -= int(input())
# print(target_price)

# 10950 A + B - 3
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     print(sum(map(int, input().split())))

# 10952 A + B - 5
# import sys
# input = sys.stdin.readline

# while True:
#     a, b = map(int, input().split())
#     if a == 0 : break
#     else: print(a+b)


# 10984 내 학점을 구해줘
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     credit_hours = 0
#     sum = 0
#     for i in range(int(input())):
#         c, g = map(float, input().split())
#         c = int(c)
#         credit_hours += c
#         sum += c * g

#     print(credit_hours, round(sum/credit_hours, 1))


# 10833 사과
# import sys
# input = sys.stdin.readline

# sum = 0
# for _ in range(int(input())):
#     students_num, apples_num = map(int, input().split())
#     while apples_num >= 0:
#         apples_num -= students_num
#     # print(apples_num + students_num)
#     sum += apples_num + students_num
# print(sum)


# 2443 별 찍기 - 6
# num = int(input())
# for i in range(num):
#     # left
#     for _ in range(i):
#         print(' ', end='')
#     for _ in range(num-i-1):
#         print('*', end='')

#     # mid
#     print('*', end='')

#     # right
#     for _ in range(num-i-1):
#         print('*', end='')

#     # '\n'
#     print()


# 2444 별 찍기 - 7
# num = int(input())
# for i in range(num):
#     print(' ' * (num-i-1), end='')
#     print('*' * (2*i + 1), end='')
#     print()

# for i in range(num-2, -1, -1):
#     print(' ' * (num-i-1), end='')
#     print('*' * (2*i + 1), end='')
#     print()


# 2522 별 찍기 - 12
# num = int(input())
# for i in range(num):
#     print(' ' * (num-i-1), end='')
#     print('*' * (i+1))

# for i in range(num-2, -1, -1):
#     print(' ' * (num-i-1), end='')
#     print('*' * (i+1))


# 2523 별 찍기 - 13
# num = int(input())
# for i in range(num):
#     print('*' * (i+1))
# for i in range(num-2, -1, -1):
#     print('*' * (i+1))


# 9325 얼마?
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     s = int(input())
#     for _ in range(int(input())):
#         q, p = map(int, input().split())
#         s += q*p
#     print(s)


# 2445 별 찍기 - 8
# num = int(input())
# for i in range(num):
#     print('*' * (i+1), end='')
#     print(' ' * 2*(num-i-1), end='')
#     print('*' * (i+1))

# for i in range(num-2, -1, -1):
#     print('*' * (i+1), end='')
#     print(' ' * 2*(num-i-1), end='')
#     print('*' * (i+1))


# 2446 별 찍기 - 9
# num = int(input())
# for i in range(num):
#     print(' ' * i, end='')
#     print('*' * (2*(num-i-1)+1))

# for i in range(num-2, -1, -1):
#     print(' ' * i, end='')
#     print('*' * (2*(num-i-1)+1))


# 2010 플러그
# import sys
# input = sys.stdin.readline

# num = int(input())
# sum = -(num-1)
# for _ in range(num):
#     sum += int(input())
# print(sum)


# 10178 할로윈의 사탕
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     c, v = map(int, input().split())
#     print("You get {0} piece(s) and your dad gets {1} piece(s).".format(c//v, c%v))


# 9295 주사위
# import sys
# input = sys.stdin.readline

# for i in range(1, int(input())+1):
#     print("Case {0}: {1}".format(i, sum(map(int, input().split()))))


# 10569 다면체
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     v, e = map(int, input().split())
#     print(-v+e+2)


# 2921 도미노
# 밑부분 + 윗부분
# sigma from k=1 to n, (k * (k+1)) + (k * (k+1))/2
# n = int(input())
# print(n*(n+1)*(n+2)//2)


# 10995 별 찍기 - 20
# n = int(input())
# for i in range(n):
#     if i % 2 == 1: print(' ', end='')
#     print('*', end='')
#     print(' *' * (n-1))


# 10991 별 찍기 - 16
# n = int(input())
# for i in range(n):
#     print(' ' * (n-i-1), end='')
#     print('*', end='')
#     print(' *' * i)


# 2581 소수
# import sys
# input = sys.stdin.readline

# def prime_check(num):
#     if num == 1 : return False
#     elif num == 2 : return True
#     elif num % 2 == 0 : return False
#     else:
#         for i in range(3, num//3 +1, 2):
#             if num % i == 0 : return False
#         return True

# def solve():
#     m = int(input())
#     n = int(input())
#     sum, min_prime_num = 0, -1

#     for i in range(m, n+1):
#         if prime_check(i) == True:
#             sum += i
#             if min_prime_num == -1:
#                 min_prime_num = i

#     if min_prime_num == -1: print(-1)
#     else: print(sum, min_prime_num, sep='\n')

# solve()


# 2501 약수 구하기
# n, k = map(int, input().split())
# # from 1 to n//2
# for i in range(1, n//2+1):
#     if n % i == 0:
#         k -= 1
#         if k == 0:
#             print(i)
#             quit()
# # n % n == 0
# k -= 1
# if k == 0: print(n)
# else: print(0)


# 2475 검증수
# def str_to_squared_num(num):
#     return int(num) ** 2

# print(sum(map(str_to_squared_num, input().split())) % 10)


# 2576 홀수
# import sys
# input = sys.stdin.readline

# sum_odd_num, min_odd_num = 0, 100
# for _ in range(7):
#     num = int(input())
#     if num % 2 == 1:
#         sum_odd_num += num
#         if min_odd_num > num : min_odd_num = num

# if min_odd_num == 100: print(-1)
# else: print(sum_odd_num, min_odd_num, sep = '\n')


# 9085 더하기
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     input()
#     print(sum(map(int, input().split())))


# 2490 윷놀이
# import sys
# input = sys.stdin.readline

# for _ in range(3):
#     yut_val = sum(map(int, input().split()))
#     if yut_val == 4: print('E')
#     elif yut_val == 3: print('A')
#     elif yut_val == 2: print('B')
#     elif yut_val == 1: print('C')
#     else: print('D')


# 10797 10부제
# import sys
# input = sys.stdin.readline

# def solve():
#     n = int(input())
#     n_list = list(map(int, input().split()))
#     sum = 0

#     for i in n_list:
#         if i == n:
#             sum += 1
#     print(sum)

# solve()


# 2506 점수계산
# import sys
# input = sys.stdin.readline

# n = int(input())
# n_list = list(map(int, input().split()))
# add_num, sum = 0, 0

# for i in n_list:
#     if i == 1:
#         add_num += 1
#         sum += add_num
#     else: add_num = 0

# print(sum)

# Python 배우기 51~100 마지막 문제
# 2455 지능형 기차
# import sys
# input = sys.stdin.readline

# max, number_of_humans = 0, 0
# for _ in range(4):
#     sub_num, add_num = map(int, input().split())
#     number_of_humans -= sub_num - add_num
#     if max < number_of_humans :
#         max = number_of_humans

# print(max)


# 2908 상수
# a, b = map(list, input().split())
# a.reverse(), b.reverse()
# a = 100 * int(a[0]) + 10 * int(a[1]) + int(a[2])
# b = 100 * int(b[0]) + 10 * int(b[1]) + int(b[2])

# if a > b : print(a)
# else: print(b)


# 지능형 기차 2
# import sys
# input = sys.stdin.readline

# max, number_of_humans = 0, 0
# for _ in range(10):
#     sub_num, add_num = map(int, input().split())
#     number_of_humans -= sub_num - add_num
#     if max < number_of_humans :
#         max = number_of_humans

# print(max)


# 2592 대표값
# import sys
# input = sys.stdin.readline

# num_dict = dict()
# sum = 0
# for _ in range(10):
#     num = int(input())
#     sum += num

#     if num in num_dict : num_dict[num] += 1
#     else: num_dict[num] = 1

# num_dict = sorted(num_dict.items(), key=lambda x:-x[1])
# print(sum//10, num_dict[0][0], sep='\n')


# 2711 오타맨 고창영
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n, input_str = map(str, input().split())
#     n, input_str = int(n), list(input_str)

#     input_str.pop(n-1)
#     print(*input_str, sep='')


# 3052 나머지
# import sys
# input = sys.stdin.readline

# remainder_list, ans = [0] * 42, 0
# for _ in range(10):
#     remainder_list[int(input())%42] += 1
# for i in remainder_list:
#     if i != 0 : ans += 1

# print(ans)


# 1292 쉽게 푸는 문제
# n_list, n = [], 1
# while len(n_list) < 1000:
#     for i in range(n):
#         n_list.append(n)
#     n += 1
# # print(n_list)

# a, b = map(int, input().split())
# print(sum(n_list[a-1:b]))


# 3460 이진수
# for _ in range(int(input())):
#     n_list, n = [], int(input())
#     while n > 0:
#         n_list.append(n%2)
#         n //= 2

#     for i in range(len(n_list)):
#         if n_list[i] == 1: print(i, end=' ')


# 5054 주차의 신
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     input()
#     x_list = sorted(list(map(int, input().split())))
#     print(2*(x_list[-1]-x_list[0]))


# 2822 점수 계산
# import sys
# input = sys.stdin.readline

# n_list = []
# for i in range(1, 9):
#     n_list.append([int(input()), i])

# # sort
# n_list = sorted(n_list, key=lambda x:-x[0])[:5]
# n_list = sorted(n_list, key=lambda x:x[1])
# # print(*n_list)

# # sum
# sum = 0
# for i in n_list:
#     sum += i[0]

# # print
# print(sum)
# for i in n_list:
#     print(i[1], end=' ')


# 2750 수 정렬하기
# import sys
# input = sys.stdin.readline

# n_list = []
# for _ in range(int(input())):
#     n_list.append(int(input()))

# print(*sorted(n_list), sep='\n')


# 2752 세수정렬
# n_list = list(map(int, input().split()))
# print(*sorted(n_list))


# 5543 상근날드
# import sys
# input = sys.stdin.readline

# min_burger_price, min_beverage_price = 2000, 2000
# for _ in range(3):
#     burger_price = int(input())
#     if min_burger_price > burger_price:
#         min_burger_price = burger_price
# for _ in range(2):
#     beverage_price = int(input())
#     if min_beverage_price > beverage_price:
#         min_beverage_price = beverage_price

# print(min_burger_price + min_beverage_price - 50)


# 2587 대표값2
# import sys
# input = sys.stdin.readline

# n_list = []
# for _ in range(5):
#     n_list.append(int(input()))

# print(sum(n_list)//5, sorted(n_list)[2], sep='\n')


# 1427 소트인사이드
# list_n = sorted(list(input()), reverse = True)
# for i in range(len(list_n)):
#     print(list_n[i], end='')


# 2309 일곱 난쟁이
# import sys
# input = sys.stdin.readline

# height_list = []
# not_dwarf_height_list = []
# for _ in range(9):
#     height_list.append(int(input()))

# height_sum = sum(height_list)
# # print(height_sum)

# for ones_height in height_list:
#     tmp_height_sum = height_sum - ones_height

#     for the_others_height in height_list:
#         if ones_height == the_others_height: continue
#         elif tmp_height_sum - the_others_height == 100:
#             not_dwarf_height_list.extend([ones_height, the_others_height])
#             break

#     if len(not_dwarf_height_list) != 0: break
# # print(not_dwarf_height_list)

# for height in not_dwarf_height_list:
#     height_list.remove(height)

# print(*sorted(height_list), sep='\n')


# 9076 점수 집계
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     score_list = sorted(list(map(int, input().split())))
#     if score_list[3] - score_list[1] >= 4: print("KIN")
#     else: print(sum(score_list[1:4]))


# 2693 N번째 큰 수
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     print(sorted(list(map(int, input().split())))[-3])


# 5176 대회 자리
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     p, m = map(int, input().split())
#     # 0 ~ m
#     seat_list = [0]*(m+1)
#     for _ in range(p):
#         seat_list[int(input())] += 1

#     sum = 0
#     for num in seat_list:
#         if num > 1:
#             sum += num-1
#     print(sum)


# 3040 백설 공주와 일곱 난쟁이
# import sys
# input = sys.stdin.readline

# height_list, not_dwarf_height_list = [], []
# for _ in range(9):
#     height_list.append(int(input()))

# height_sum = sum(height_list)
# # print(height_sum)

# for ones_height in height_list:
#     tmp_height_sum = height_sum - ones_height

#     for the_others_height in height_list:
#         if ones_height == the_others_height: continue
#         elif tmp_height_sum - the_others_height == 100:
#             not_dwarf_height_list.extend([ones_height, the_others_height])
#             break

#     if len(not_dwarf_height_list) != 0: break
# # print(not_dwarf_height_list)

# for height in not_dwarf_height_list:
#     height_list.remove(height)

# print(*height_list, sep='\n')

# ↑ 이거 제출하면서 시작 ~


# 10809 알파벳 찾기
# str_list = list(input())
# alphabet_list = [-1] * 26
# for i in range(len(str_list)):
#     if alphabet_list[ord(str_list[i])-97] == -1:
#         alphabet_list[ord(str_list[i])-97] = i

# print(*alphabet_list)


# 3058 짝수를 찾아라
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     min_even_num, sum_even_num = 100, 0
#     num_list = list(map(int, input().split()))

#     for i in num_list:
#         if i % 2 == 0:
#             sum_even_num += i
#             if min_even_num > i:
#                 min_even_num = i

#     print(sum_even_num, min_even_num)


# 5800 성적 통계
# import sys
# input = sys.stdin.readline

# for i in range(1, int(input())+1):
#     largest_gab = 0
#     num_list = sorted(list(map(int, input().split()))[1:])
#     for j in range(len(num_list)-1):
#         gab = num_list[j+1] - num_list[j]
#         if largest_gab < gab: largest_gab = gab

#     print("Class", i)
#     print("Max {0}, Min {1}, Largest gap {2}".format(num_list[-1], num_list[0], largest_gab))


# 5576 콘테스트
# import sys
# input = sys.stdin.readline

# num_list_1 = [int(input()) for _ in range(10)]
# num_list_2 = [int(input()) for _ in range(10)]

# print(sum(sorted(num_list_1, reverse = True)[:3]), sum(sorted(num_list_2, reverse = True)[:3]))


# 11047 동전0
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# coin_list = [int(input()) for _ in range(n)]
# total_coin = 0

# for coin in coin_list[::-1]:
#     if k >= coin :
#         total_coin += k // coin
#         k %= coin

# print(total_coin)


# 10953 A + B - 6
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     print(sum(map(int, input().split(","))))


# 2902 KMP는 왜 KMP일까?
# str_list = list(input().split('-'))
# for each_str in str_list:
#     print(each_str[0], end='')


# 1357 뒤집힌 덧셈
# def Rev(num):
#     return_num, mul_num = 0, 1
#     num = list(str(num))

#     for i in range(len(num)):
#         return_num += int(num[i]) * mul_num
#         mul_num *= 10

#     return return_num

# x, y = map(int, input().split())
# print(Rev(Rev(x)+Rev(y)))


# 10987 모음의 개수
# str_list = list(input())
# sum = 0
# for alphabet in str_list:
#     if alphabet in ['a','e','i','o','u']:
#         sum += 1

# print(sum)


# 4458 첫 글자를 대문자로
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     str_list = list(input())
#     if 97 <= ord(str_list[0]) < 123:
#         str_list[0] = chr(ord(str_list[0])-32)

#     print(*str_list, sep='', end='')


# 11721 열 개씩 끊어 출력하기
# str_list = list(input())
# check_10 = 0
# for alphabet in str_list:
#     print(alphabet, end='')
#     check_10 += 1

#     if check_10 == 10:
#         check_10 = 0
#         print()


# 10821 정수의 개수
# n_list = list(map(int, input().split(',')))
# print(len(n_list))
# print(len(list(map(int, input().split(',')))))

# 10808 알파벳 개수
# str_list = list(input())
# alphabet_list = [0] * 26

# for alphabet in str_list:
#     alphabet_list[ord(alphabet)-97] += 1

# print(*alphabet_list)


# 5218 알파벳 거리
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     standard_list, target_list = map(list, input().split())
#     # print(standard_list, target_list)

#     print("Distances:", end=' ')
#     for i in range(len(standard_list)):
#         ans = ord(target_list[i]) - ord(standard_list[i])
#         if ans < 0 : ans += 26
#         print(ans, end=' ')
#     print()


# 9086 문자열
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     str_list = list(input().rstrip())
#     print(str_list[0], str_list[-1], sep='')


# 11365 !밀비 급일
# import sys
# input = sys.stdin.readline

# while True:
#     str_list = input().rstrip()
#     if str_list == 'END': break
#     else: str_list = list(str_list)

#     print(*str_list[::-1], sep='')


# 11170 0의 개수
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     count_zero = 0
#     for num in range(n, m+1):
#         num = list(str(num))
#         for i in num:
#             if i == '0':
#                 count_zero += 1

#     print(count_zero)


# 11655 ROT13
# str_list = list(input())
# for char in str_list:
#     alphabet_num = ord(char)

#     # upper_case
#     if 65 <= ord(char) < 91:
#         alphabet_num += 13
#         if 91 <= alphabet_num:
#             alphabet_num -= 26

#     # lower_case
#     elif 97 <= ord(char) < 123:
#         alphabet_num += 13
#         if 123 <= alphabet_num:
#             alphabet_num -= 26

#     print(chr(alphabet_num), end='')


# 1676 팩토리얼 0의 개수
# num = int(input())
# count_2, count_5 = 0, 0

# for i in range(2, num+1):
#     tmp_num = i
#     while tmp_num % 2 == 0:
#         tmp_num //= 2
#         count_2 += 1

#     while tmp_num % 5 == 0:
#         tmp_num //= 5
#         count_5 += 1

#     # print(i, count_2, count_5)
# print(min(count_2, count_5))

# num = int(input())
# count_5 = 0

# for i in range(5, num+1):
#     tmp_num = i

#     while tmp_num % 5 == 0:
#         tmp_num //= 5
#         count_5 += 1

# print(count_5)


# 2579 계단 오르기
# import sys
# input = sys.stdin.readline

# n = int(input())
# score_list = [int(input()) for _ in range(n)]
# score_list.insert(0, 0)
# # print(score_list)
# dp_list = [[0]*(n+1) for _ in range(3)]
# # print(dp_list)

# # from 1 to n
# for i in range(1, n+1):
#     dp_list[0][i] = dp_list[2][i-1] + score_list[i]
#     dp_list[1][i] = dp_list[0][i-1] + score_list[i]
#     dp_list[2][i] = max(dp_list[0][i-1], dp_list[1][i-1])

# # for y in range(3):
# #     print(dp_list[y])

# print(max(dp_list[0][n], dp_list[1][n]))


# 5585 거스름돈
# n = 1000 - int(input())
# coin_list = [500, 100, 50, 10, 5, 1]
# coin_count = 0
# for coin in coin_list:
#     if n >= coin:
#         coin_count += n // coin
#         n %= coin

# print(coin_count)


# 18185 라면 사기 (Small)
# import sys
# input = sys.stdin.readline

# n = int(input())
# fac_list = list(map(int, input().split()))
# start_index, end_index = 0, 0
# sum = 0

# while start_index < n :
#     # index initialization
#     if fac_list[start_index] == 0:
#         start_index += 1
#         continue
#     end_index = start_index
#     # print(start_index, end_index)

#     # increasing end_index (max : start_index + 2)
#     end_plus_check = 0
#     while end_index+1 < n and fac_list[end_index+1] > 0 and end_plus_check < 2:
#         end_index += 1
#         end_plus_check += 1
#     min_val = min(fac_list[start_index : end_index+1])
#     # print(min_val, end_index, start_index)

#     # index gab - 2 step, 1 step, 0 step(same)
#     if end_index - start_index == 2:
#         sum += min_val * 7
#     elif end_index - start_index == 1:
#         sum += min_val * 5
#     elif end_index == start_index:
#         sum += min_val * 3

#     # sub calculated sum
#     for index in range(start_index, end_index+1):
#         fac_list[index] -= min_val

# print(sum)

# N = int(input())
# list_n = list(map(int, input().split()))
# list_block = [0]*3

# for idx_from in range(N):
#     gab = min(2, N-1-idx_from)
#     # print(gab)
#     tmp_gab = gab
#     tmp_list_n = list_n[idx_from:idx_from+gab+1].copy()
#     tmp_list_block = [0]*(tmp_gab+1)
#     # print(tmp_list_n, tmp_list_block)

#     while tmp_gab >= 0:
#         min_val = min(tmp_list_n[:tmp_gab+1])
#         # print(min_val)
#         for tmp_idx in range(tmp_gab+1):
#             tmp_list_n[tmp_idx] -= min_val
#         # print(tmp_list_n)

#         tmp_list_block[tmp_gab] += min_val
#         tmp_gab -= 1
#     # print(tmp_list_block)

#     if gab == 2:
#         if list_n[idx_from+1] > list_n[idx_from+2]:
#             # val = min(list_n[idx_from+1]-list_n[idx_from+2], tmp_list_block[2])
#             val = min(tmp_list_n[1]-tmp_list_n[2], tmp_list_block[2])
#             tmp_list_block[2] -= val
#             tmp_list_block[1] += val
#             tmp_list_n[2] += val
#     # print(tmp_list_block)

#     for tmp_idx in range(gab+1):
#         list_block[tmp_idx] += tmp_list_block[tmp_idx]
#         list_n[idx_from+tmp_idx] = tmp_list_n[tmp_idx]
#     # print(list_block)
# # print(list_block)
# print(list_block[0]*3 + list_block[1]*5 + list_block[2]*7)
"""
3
2 2 1
[정답] 12 (7+5)
[출력] 13 (5+5+1)
"""


# 1237 정ㅋ벅ㅋ
# clear

# 5525 IOIOI - class 3
# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# str_list = list(input().rstrip())
# ioi_count_list = [0] * m

# ioi_count, o_count = 0, 1000
# for idx in range(m):
#     if str_list[idx] == 'I':
#         # if (0 < idx and str_list[idx-1] == 'I'):
#         # not IOI pattern
#         if  o_count != 1:
#             ioi_count = 0
#         # IOI (IO'I') pattern
#         else:
#             ioi_count += 1
#             ioi_count_list[idx] = ioi_count
#         o_count = 0
#     else: # 'O'
#         o_count += 1
# #     print(idx, ioi_count, o_count)
# # print(ioi_count_list)

# sum = 0
# for val in ioi_count_list:
#     if val >= n:
#         sum += 1

# print(sum)


# 17219 비밀번호 찾기
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# pwd_dict = dict()
# for _ in range(n):
#     domain, pwd = map(str, input().rstrip().split())
#     # print(domain, pwd)
#     pwd_dict[domain] = pwd

# for _ in range(m):
#     print(pwd_dict[input().rstrip()])


# 2630 색종이 만들기
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def count_color_paper(n, ny, nx, graph):
#     global w_count, b_count
#     first_color_val = graph[ny][nx]
#     diff_color_check = False

#     # diff_color_check == False <- all_same_color !
#     for y in range(ny, ny+n):
#         for x in range(nx, nx+n):
#             if graph[y][x] != first_color_val:
#                 diff_color_check = True
#                 break
#         if diff_color_check == True: break

#     if diff_color_check : # True
#         n //= 2
#         count_color_paper(n, ny, nx, graph)
#         count_color_paper(n, ny, nx+n, graph)
#         count_color_paper(n, ny+n, nx, graph)
#         count_color_paper(n, ny+n, nx+n, graph)
#     else: # False
#         if first_color_val == 0: w_count += 1
#         else: b_count += 1

#     # print(n, ny, nx, w_count, b_count)
#     # return w_count, b_count

# def solve():
#     n = int(input())
#     graph = [list(map(int, input().split())) for _ in range(n)]
#     global w_count, b_count
#     w_count, b_count = 0, 0
#     # print(graph)

#     count_color_paper(n, 0, 0, graph)
#     print(w_count, b_count, sep='\n')

# solve()


# 7662 이중 우선순위 큐
# how to solve this
# from queue import PriorityQueue
# que = PriorityQueue()

# que.put((3, 'Apple'))
# que.put((1, 'Banana'))
# que.put((2, 'Cherry'))

# print(que.get()[0])  # Banana
# print(que.get()[1])  # Cherry
# print(que.get()[1])  # Apple

# idea !!
# import sys
# from queue import PriorityQueue

# que.put(1)
# que.put(2)
# que.put(3)

# minus_que = que
# # minus_que.pop()
# print(minus_que.queue.pop())
# print(minus_que.queue.pop())
# # print(minus_que.queue.pop())

# print(minus_que.queue)
# print(que.queue)

# clear ?
# 1 que -> 틀렸습니다
# 2 que -> 1% 시간 초과
# 4 que -> 3% 시간 초과

# import sys
# from queue import PriorityQueue
# input = sys.stdin.readline

# def check_del_que(target_que, del_que):
#     while del_que.queue:
#         val_target_que_get = target_que.get()
#         val_del_que_get = del_que.get()

#         if val_target_que_get != val_del_que_get:
#             target_que.put(val_target_que_get)
#             del_que.put(val_del_que_get)
#             break

# def solve():
#     for _ in range(int(input())):
#         min_que, max_que = PriorityQueue(), PriorityQueue()
#         min_del_que, max_del_que = PriorityQueue(), PriorityQueue()
#         for _ in range(int(input())):
#             operand, val = map(str, input().split())
#             val = int(val)

#             if operand == 'I':
#                 min_que.put(val)
#                 max_que.put(-val)
#             else: # 'D'
#                 if val == -1:
#                     if min_que.queue:
#                         max_del_que.put(-min_que.get())
#                         # check_del_que(min_que, min_del_que)

#                 else: # val == 1
#                     if max_que.queue:
#                         min_del_que.put(-max_que.get())
#                         # check_del_que(max_que, max_del_que)

#             check_del_que(min_que, min_del_que)
#             check_del_que(max_que, max_del_que)
#             # print(min_que.queue, max_que.queue)

#         if not min_que.queue: print('EMPTY')
#         else:
#             print(-max_que.get(), min_que.get())

# solve()


# 2156 포도주 시식
# 계단 오르기랑 비슷하지만 연속으로 안 마셔도 된다는 게 point
# dp 계산을 다르게 적용해야 한다 ~
"""
6
1000
1000
1
1
1000
1000
정답 : 4000
출력 : 3001
"""
# # try 1
# import sys
# input = sys.stdin.readline

# n = int(input())
# dp_list = [[0]*(n+1) for _ in range(3)]

# for i in range(1, n+1):
#     amount_of_wine = int(input())

#     if amount_of_wine == 0:
#         dp_list[2][i] = max(dp_list[j][i-1] for j in range(3))
#     else:
#         dp_list[0][i] = dp_list[2][i-1] + amount_of_wine
#         dp_list[1][i] = dp_list[0][i-1] + amount_of_wine
#         dp_list[2][i] = max(dp_list[0][i-1], dp_list[1][i-1])

# # print(max(dp_list[0][n], dp_list[1][n], dp_list[2][n]))
# print(max(dp_list[j][n] for j in range(3)))

# # for y in range(3):
# #     print(dp_list[y])


# try 2 -> success
# import sys
# input = sys.stdin.readline

# n = int(input())
# dp_list = [0] * (n+1)
# wine_list = [int(input()) for _ in range(n)]
# wine_list.insert(0, 0)

# # 1 <= n <= 10000
# dp_list[1] = wine_list[1]
# if n >= 2:
#     dp_list[2] = wine_list[2] + dp_list[1]

# for i in range(3, n+1):
#     dp_list[i] = max(dp_list[i-1], (dp_list[i-2] + wine_list[i]),\
#                      (dp_list[i-3] + wine_list[i-1] + wine_list[i]))

# print(dp_list[n])


# 절댓값 힙
# import sys
# from queue import PriorityQueue
# input = sys.stdin.readline

# minus_que, plus_que = PriorityQueue(), PriorityQueue()

# for _ in range(int(input())):
#     val = int(input())
#     if val < 0:
#         minus_que.put(-val)
#     elif val > 0:
#         plus_que.put(val)
#     else:
#         is_empty_minus_que = not minus_que.queue
#         is_empty_plus_que = not plus_que.queue

#         if is_empty_minus_que and is_empty_plus_que:
#             print(0)
#         elif not is_empty_minus_que and is_empty_plus_que:
#             print(-minus_que.get())
#         elif is_empty_minus_que and not is_empty_plus_que:
#             print(plus_que.get())
#         else:
#             minus_val = minus_que.queue[0]
#             plus_val = plus_que.queue[0]

#             if minus_val <= plus_val :
#                 print(-minus_que.get())
#             else:
#                 print(plus_que.get())


# 개선
# import sys
# input = sys.stdin.readline
# from heapq import heappush, heappop

# def solve():
#     heap = []
#     for _ in range(int(input())):
#         val = int(input())

#         if val == 0:
#             print(heappop(heap)[1]) if heap else print(0)
#         else:
#             heappush(heap, [abs(val), val])

# solve()


# 1107 리모컨
# import sys
# input = sys.stdin.readline

# channel = str(input().rstrip())
# int_channel = int(channel)

# n, n_list = int(input()), []
# if n > 0 :
#     n_list = list(map(int, input().split()))
# # print(n_list)
# low_max_ans, high_min_ans = 999999, 999999

# # low_max_ans
# for i in range(int_channel, -1, -1):
#     pos_check = True
#     tmp_i = i

#     # for j in range(len_channel):
#     for j in range(len(str(i))):
#         # print(tmp_i)
#         if tmp_i % 10 in n_list:
#             pos_check = False
#             break
#         tmp_i //= 10

#     if pos_check :
#         # print("[ans1] i : ", i)
#         low_max_ans = len(str(i)) + int_channel - i
#         break

# # high_min_ans
# for i in range(int_channel, int_channel+500000):
#     pos_check = True
#     tmp_i = i

#     for j in range(len(str(i))):
#         if tmp_i % 10 in n_list:
#             pos_check = False
#             break
#         tmp_i //= 10

#     if pos_check:
#         # print("[ans2] i : ", i)
#         high_min_ans = len(str(i)) + i - int_channel
#         break

# print(min(low_max_ans, high_min_ans, abs(100-int_channel)))


# 1107 리모컨
# 888 667
# import sys
# input = sys.stdin.readline

# def DFS(numS):
#     defNum =abs(int(n) - int(numS))
#     # print(numS, defNum)
#     if defNum < minDef[1] :
#     # if len(str(defNum)) + defNum < minDef[1] + minDef[2]:
#         minDef[0] = numS
#         minDef[1] = defNum
#         minDef[2] = len(str(int(numS))) # 숫자 첫 번째에 0이 붙으면 제거하기 위해
#         # print(minDef)

#     if len(numS) > len(n):
#         return True
#     else:
#         for i in btn:
#             DFS(numS + i)

# for n in range(1555, 1556):
#     start = 100
#     n = str(n)
#     # n = input() # 이동하려는 채널
#     # m = int(input()) # 고장난 버튼 개수
#     m = 3
#     broke = [0, 1, 9]
#     # if m > 0:
#     #     broke = list(map(int, input().split()))

#     btn = [] # 사용 가능 버튼
#     for i in range(0,10):
#         if i not in broke:
#             btn.append(str(i))

#     # 입력 가능한 버튼을 DFS 방식으로 탐색
#     #  index 0: n과의 차이가 가장 적은 값의 수
#     #  index 1: n과의 차가 가장 작은값
#     #  index 2: 수를 만들기 위해 눌러야 하는 횟수
#     minDef = [100, 500000, 0]
#     for i in btn:
#         DFS(i)

#     print(minDef)
#     res = []
#     # n을 만들기 위해 최소한을 눌러야 하는 총 횟수
#     res.append(minDef[1]+minDef[2])

#     # 만약 +, - 만 누르는 것이 숫자를 누르는 횟수보다 빠른지 확인
#     res.append(abs(int(n)-start))

#     # 최솟값 출력
#     # print(min(res))
#     val_ans_1 = min(res)


#     # channel = str(input().rstrip())
#     # int_channel = int(channel)
#     int_channel = int(n)

#     # val_n, val_n_list = int(input()), []
#     val_n, val_n_list = m, broke
#     # if val_n > 0 :
#     #     val_n_list = list(map(int, input().split()))
#     # print(n_list)
#     low_max_ans, high_min_ans = 999999, 999999

#     # low_max_ans
#     for i in range(int_channel, -1, -1):
#         pos_check = True
#         tmp_i = i

#         # for j in range(len_channel):
#         for j in range(len(str(i))):
#             # print(tmp_i)
#             if tmp_i % 10 in val_n_list:
#                 pos_check = False
#                 break
#             tmp_i //= 10

#         if pos_check :
#             # print("[ans1] i : ", i)
#             low_max_ans = len(str(i)) + int_channel - i
#             # print("haha", i)
#             break

#     # high_min_ans
#     for i in range(int_channel, int_channel+500000):
#         pos_check = True
#         tmp_i = i

#         for j in range(len(str(i))):
#             if tmp_i % 10 in val_n_list:
#                 pos_check = False
#                 break
#             tmp_i //= 10

#         if pos_check:
#             # print("[ans2] i : ", i)
#             high_min_ans = len(str(i)) + i - int_channel
#             break

#     print(low_max_ans, high_min_ans, abs(100-int_channel))
#     # print(min(low_max_ans, high_min_ans, abs(100-int_channel)))
#     val_ans_2 = min(low_max_ans, high_min_ans, abs(100-int_channel))
#     print(n)
#     if val_ans_1 != val_ans_2 :
#         print("haha i found it!", i, val_ans_1, val_ans_2)


# def DFS(target_n:int, now_n:str, btn:list, min_def:list):
#     gap = abs(target_n - int(now_n))
#     if len(now_n) + gap < min_def[1] + min_def[2]:
#         # min_def[0] = now_n
#         min_def[1] = gap
#         min_def[2] = len(now_n)

#     # 길이가 target_n보다 더 길다면 return
#     if len(now_n) > len(str(target_n)):
#         return
#     # 아직 숫자를 더 추가할 필요가 있다면 DFS 수행
#     else:
#         for i in btn:
#             # print(now_n, i, gap, min_def)
#             DFS(target_n, now_n + i, btn, min_def)

# def solve():
#     start = 100             # 시작 채널
#     target_n = int(input()) # 이동하려는 target 채널
#     m = int(input())        # 고장난 버튼의 개수
#     broke_btn = set(map(int, input().split())) if m != 0 else []
#     btn = [str(i) for i in range(10) if i not in broke_btn]

#     # 만들 수 있는 숫자를 DFS 방식으로 탐색하며 최소값 계산
#     # index 0: 현재 n과의 차이가 가장 적은 값 (시작채널로 초기화)
#     # index 1: target_n과의 gap (갱신을 위해 input 가능한 가장 큰 값으로 초기화)
#     # index 2: index 0의 값을 만들기 위해 리모컨을 누르는 횟수
#     min_def = [100, int(5e5), 0]
#     for i in btn:
#         DFS(target_n, i, btn, min_def)

#     # min((n을 만들기 위해 최소한을 눌러야 하는 총 횟수), (+, - 만 누르는 횟수))
#     print(min(sum(min_def[1:]), abs(target_n)-start))

# solve()


# 10951 A + B - 4
# import sys
# lines = sys.stdin.readlines()
# for line in lines:
#     print(sum(list(map(int, line.rsplit()))))


# 14500 테트로미노
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# g = [list(map(int, input().split())) for _ in range(n)]
# # print(g)

# # 1, I - block, col
# max_sum = 0
# for ny in range(0, n-3):
#     for nx in range(m):
#         # print(ny, nx)
#         tmp_sum = 0
#         for y in range(ny, ny+4):
#             tmp_sum += g[y][nx]
#         # print(tmp_sum)
#         if max_sum < tmp_sum : max_sum = tmp_sum

# # 1, I - block, row
# for ny in range(n):
#     for nx in range(0, n-3):
#         # print(ny, nx)
#         tmp_sum = sum(g[ny][nx:nx+4])
#         # print(tmp_sum)
#         if max_sum < tmp_sum : max_sum = tmp_sum

# # O - block
# for ny in range(n-1):
#     for nx in range(n-1):
#         # print(ny, nx)
#         tmp_sum = 0
#         for y in range(ny, ny+2):
#             tmp_sum += sum(g[y][nx:nx+2])
#             # print(g[y])
#         # print(tmp_sum)
#         if max_sum < tmp_sum : max_sum = tmp_sum

# L - block - 8가지 경우
# S - block - 4가지 경우
# T - block - 4가지 경우

# 2x3, 3x2 로 묶을 수 있을 듯?


# div_num = 2
# for div_num in range(2, 698):
#     if 697 % div_num == 0:
#         print(div_num)
#         break


# 1016 제곱 ㄴㄴ 수
# import math

# min, max = map(int, input().split())
# check_list = [1] * (max - min + 1)
# for num in range(2, int(math.sqrt(max))+1):
#     div_num = num ** 2
#     first_val = -1
#     for val in range(min, max+1):
#         if val % div_num == 0:
#             first_val = val
#             # print("[1]", first_val, val)
#             # check_list[first_val] = 0
#             break

#     if first_val != -1:
#         for val in range(first_val, max+1, div_num):
#             if val-min >= max: break
#             # print(div_num, val, min)
#             check_list[val-min] = 0

# # print(check_list)
# print(sum(check_list))


# 1271 엄청난 부자2
# n, m = map(int, input().split())
# print(n//m, n%m, sep='\n')

# 3003 킹, 퀸, 룩, 비숍, 나이트, 폰
# king, queen, rook, bishop, knight, pawn = map(int, input().split())
# print(1-king, 1-queen, 2-rook, 2-bishop, 2-knight, 8-pawn)


# H - Highly Composite Permutations 844/8
# 좀 더 효율적으로 작성할 필요가 있음
# import itertools

# def composite_check(num):
#     if num == 1:
#         return False
#     elif num == 2:
#         return False
#     elif num % 2 == 0:
#         return True
#     else:
#         for i in range(3, (num//3)+1, 2):
#             if num % i == 0:
#                 return True
#         return False

# def solve():
#     n = int(input())
#     num_list = [i for i in range(1, n+1)]

#     # print(list(map(' '.join, itertools.permutations(num_list)))) # 3개의 원소로 수열 만들기
#     # print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기

#     for tmp_num_list in itertools.permutations(num_list):
#         print(tmp_num_list)

#         composite_permutations_check = True
#         tmp_sum = 0
#         # 0 ~ n-1
#         for j in range(n):
#             tmp_sum += tmp_num_list[j]
#             if composite_check(tmp_sum) == False:
#                 composite_permutations_check = False
#                 break

#         if composite_permutations_check == True:
#             print(*tmp_num_list)
#             return

#     print(-1)

# solve()


# 11727 2xn 타일링2
# n = int(input())
# dp_list = [0]*(n+1)
# dp_list[0], dp_list[1] = 1, 1

# for i in range(2, n+1):
#     dp_list[i] = (dp_list[i-1] + 2*dp_list[i-2]) % 10007

# print(dp_list[n])

# 14928 큰 수 (BIG)
# print(int(input()) % 20000303)

# 3733 Shares
# import sys

# lines = sys.stdin.readlines()
# for line in lines:
#     n, s = map(int, line.rstrip().split())
#     print(s//(n+1))

# 9461 파도반 수열
# import sys
# input = sys.stdin.readline

# dp_list = [0]*101
# dp_list[1:6] = [1,1,1,2,2]
# for i in range(6, 101):
#     dp_list[i] = dp_list[i-1] + dp_list[i-5]
# # print(dp_list)

# for _ in range(int(input())):
#     print(dp_list[int(input())])


# 11659 구간 합 구하기 4
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# num_list = list(map(int, input().split()))
# dp_sum_list = [0] * (n+1)

# sum = 0
# for i in range(1, n+1):
#     sum += num_list[i-1]
#     dp_sum_list[i] = sum
# # print(dp_sum_list)

# for _ in range(m):
#     i, j = map(int, input().split())
#     print(dp_sum_list[j] - dp_sum_list[i-1])


# 10171 고양이
# print(\
# "\    /\\",
# " )  ( ')",
# "(  /  )",
# " \(__)|", sep='\n')


# 1253 좋다
# import sys
# input = sys.stdin.readline

# n = int(input())
# n_list = sorted(list(map(int, input().split())))
# idx_left, idx_right = 0, n-1
# # print(n_list[idx_left], n_list[idx_right])

# while idx_left <= idx_right:


# 1747 소수&팰린드롬
# def palindrome_check(num):
#     num_list = list(map(int, str(num)))
#     idx_left, idx_right = 0, len(num_list)-1

#     while idx_left <= idx_right:
#         if num_list[idx_left] != num_list[idx_right]:
#             return False
#         idx_left += 1
#         idx_right -= 1
#     return True

# def prime_check(num):
#     if num == 1: return False
#     elif num == 2: return True
#     elif num % 2 == 0: return False
#     else:
#         for div in range(3, (num//3)+1, 2):
#             if num % div == 0:
#                 return False
#         return True

# def solve():
#     num = int(input())
#     while True:
#         if palindrome_check(num):
#             if prime_check(num):
#                 print(num)
#                 return
#         num += 1

# solve()


# 1759 암호 만들기
# import itertools

# val_l, val_c = map(int, input().split())
# chr_list = sorted(list(input().split()))
# vowles_list = ['a', 'e', 'i', 'o', 'u']
# # print(chr_list)

# # for ans_str in itertools.permutations(chr_list, val_l):
# for ans_str in itertools.combinations(chr_list, val_l):
#     # print(*ans_str)
#     vowles_num, consonants_num = 0, 0

#     for one_chr in ans_str:
#         if one_chr in vowles_list: vowles_num += 1
#         else: consonants_num += 1

#     if vowles_num >= 1 and consonants_num >= 2:
#         # print(ans_str, vowles_num, consonant_num)
#         print(*ans_str, sep='')


# 8370 Plane
# n1, k1, n2, k2 = map(int, input().split())
# print(n1*k1 + n2*k2)


# 17626 For Squares
# import math

# num = int(input())
# dp_list = [0] * (num+1)

# for i in range(1, int(math.sqrt(num))+1):
#     dp_list[i**2] = 1

# for i in range(1, num+1):
#     if dp_list[i] == 1:
#         # print(i, dp_list[i])
#         continue

#     idx_left, idx_right = 1, (i-1)
#     dp_val = 100000
#     while idx_left <= idx_right:
#         tmp_val = dp_list[idx_left] + dp_list[idx_right]
#         if dp_val > tmp_val : dp_val = tmp_val

#         idx_left += 1
#         idx_right -= 1
#     dp_list[i] = dp_val

# # print(dp_list)
# print(dp_list[num])


# N-Queen 9663
# num = int(input())
# chess_board = [[0]*num for _ in range(num)]

# for y in range(num):


# 10819 차이를 최대로
# import itertools

# num = int(input())
# num_list = list(map(int, input().split()))

# ans = 0
# for tmp_num_list in itertools.permutations(num_list, num):
#     # print(tmp_num_list)
#     gab = 0
#     for idx in range(1, num):
#         gab += abs(tmp_num_list[idx] - tmp_num_list[idx-1])
#     if ans < gab : ans = gab

# print(ans)


# 1780 종이의 개수
# import sys
# input = sys.stdin.readline

# def paper_check(graph, n, nx, ny):
#     global cnt_minus_1, cnt_0, cnt_1
#     equality_check = True
#     start_num = graph[ny][nx]

#     for y in range(ny, ny+n):
#         for x in range(nx, nx+n):
#             if graph[y][x] != start_num:
#                 equality_check = False
#                 break
#         if equality_check == False: break

#     if equality_check == False:
#         n //= 3
#         for new_y in range(ny, ny+(2*n)+1, n):
#             for new_x in range(nx, nx+(2*n)+1, n):
#                 paper_check(graph, n, new_x, new_y)
#     else:
#         if start_num == 1: cnt_1 += 1
#         elif start_num == 0: cnt_0 += 1
#         else: cnt_minus_1 += 1

# def solve():
#     num = int(input())
#     graph = [list(map(int, input().split())) for _ in range(num)]
#     # print(graph)
#     global cnt_minus_1, cnt_0, cnt_1
#     cnt_minus_1, cnt_0, cnt_1 = 0, 0, 0

#     paper_check(graph, num, 0, 0)
#     print(cnt_minus_1, cnt_0, cnt_1, sep='\n')

# solve()


# 15650 N과 M (2)
# import itertools

# n, m = map(int, input().split())
# for i in itertools.combinations(range(1,n+1), m):
#     print(*i)

# 15652 N과 M (4)
# import itertools

# n, m = map(int, input().split())
# for i in itertools.combinations_with_replacement(range(1,n+1), m):
#     print(*i)


# 5347 LCM
# import sys
# input = sys.stdin.readline

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# def lcm(a, b):
#     return a * b // gcd(a, b)

# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     print(lcm(a, b))


# 15654 N과 M (5)
# import itertools

# n, m = map(int, input().split())
# num_list = sorted(list(map(int, input().split())))
# for i in itertools.permutations(num_list, m):
#     print(*i)


# 15657 N과 M (8)
# import itertools

# n, m = map(int, input().split())
# num_list = sorted(list(map(int, input().split())))
# for i in itertools.combinations_with_replacement(num_list, m):
#     print(*i)


# 1520 내리막길
# 시간 초과?
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def down_bfs(graph, m, n, nx, ny, inc_xy, num):
#     global cnt
#     for plus_x, plus_y in inc_xy:
#         new_x, new_y = nx + plus_x, ny + plus_y
#         if 0 <= new_x < n and 0 <= new_y < m :
#             if graph[new_y][new_x] < num:
#                 if new_y == m-1 and new_x == n-1:
#                     cnt += 1
#                     continue
#                 down_bfs(graph, m, n, new_x, new_y, inc_xy, graph[new_y][new_x])

# def solve():
#     m, n = map(int, input().split())
#     graph = [list(map(int, input().split())) for _ in range(m)]
#     # print(graph)
#     inc_xy = [[1,0], [0,1], [-1,0], [0,-1]]
#     global cnt
#     cnt = 0

#     down_bfs(graph, m, n, 0, 0, inc_xy, graph[0][0])
#     print(cnt)

# solve()


# 1520 내리막 길
# pm 03:35 ~ 03 ~ 44

# 참고 : https://studyandwrite.tistory.com/387
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(int(1e6))

# def dfs(N, M, board, dp, x, y, inc_xy):
#     # print(x, y)
#     if x == N-1 and y == M-1:
#         return 1

#     if dp[x][y] != -1:
#         return dp[x][y]

#     cnt = 0
#     for px, py in inc_xy:
#         nx, ny = x + px, y + py
#         if 0 <= nx < N and 0 <= ny < M and board[x][y] > board[nx][ny]:
#             cnt += dfs(N, M, board, dp, nx, ny, inc_xy)

#     dp[x][y] = cnt
#     return cnt

# def solve():
#     N, M = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     inc_xy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

#     dp = [[-1]*M for _ in range(N)]
#     print(dfs(N, M, board, dp, 0, 0, inc_xy))

# solve()


# 1269 대칭 차집합
# import sys
# input = sys.stdin.readline

# a, b = map(int, input().split())
# a_set = set(map(int, input().split()))
# b_set = set(map(int, input().split()))
# print(len(a_set) + len(b_set) - 2*len(a_set.intersection(b_set)))


# 5337 웰컴
# print(\
# ".  .   .\n"\
# "|  | _ | _. _ ._ _  _\n"\
# "|/\|(/.|(_.(_)[ | )(/.\n")


# 1149 RGB거리
# dp_list 초기화를 1000으로 하면 안 된다 !
# import sys
# input = sys.stdin.readline

# n = int(input())
# num_list = [list(map(int, input().split())) for _ in range(n)]
# dp_list = [[1000000] * 3 for _ in range(n)]
# dp_list[0] = num_list[0]
# # print(dp_list)

# for y in range(1, n):
#     for x in range(0, 3):
#         for pre_x in range(0, 3):
#             if x != pre_x:
#                 if dp_list[y][x] > dp_list[y-1][pre_x]:
#                     dp_list[y][x] = dp_list[y-1][pre_x]
#         dp_list[y][x] += num_list[y][x]

# print(min(dp_list[n-1]))


# 4375 1
# import sys
# lines = sys.stdin.readlines()

# for line in lines:
#     num = int(line.rstrip())
#     len_only_one_num = 1
#     mul_num = 1
#     target_num = 0

#     while True:
#         target_num += mul_num * 1

#         if target_num % num == 0:
#             # print(target_num, num, len_only_one_num)
#             print(len_only_one_num)
#             break

#         len_only_one_num += 1
#         mul_num *= 10


# 2217 로프
# import sys
# input = sys.stdin.readline

# num = int(input())
# rope_list = sorted([int(input()) for _ in range(num)])
# # print(rope_list)

# # sum_of_weights = sum(rope_list)
# num_of_ropes = len(rope_list)
# max_wk = 0

# for rope in rope_list:
#     tmp_wk = rope * num_of_ropes
#     if max_wk < tmp_wk:
#         max_wk = tmp_wk
#     num_of_ropes -= 1
#     # print(max_wk, tmp_wk)

# print(max_wk)


# 1316 그룹 단어 체커
# import sys
# input = sys.stdin.readline

# total_group_word = 0

# for _ in range(int(input())):
#     text_list = list(input().rstrip())
#     # print(text_list)
#     pre_alphabet = text_list[0]
#     check_list = [0] * 26
#     check_list[ord(pre_alphabet)-97] = 1

#     group_word_check = True
#     for i in range(1, len(text_list)):
#         if pre_alphabet != text_list[i]:
#             # print(ord(text_list[i]))
#             if check_list[ord(text_list[i])-97] == 0:
#                 check_list[ord(text_list[i])-97] = 1
#             else:
#                 group_word_check = False
#                 # print(i, text_list[i])
#                 break
#         pre_alphabet = text_list[i]
#         # print(pre_alphabet)

#     if group_word_check:
#         total_group_word += 1

# print(total_group_word)


# 5338 마이크로소프트 로고
# print("\
#        _.-;;-._\n\
# '-..-'|   ||   |\n\
# '-..-'|_.-;;-._|\n\
# '-..-'|   ||   |\n\
# '-..-'|_.-''-._|\n")


# 1264 모음의 개수
# import sys
# input = sys.stdin.readline

# vowel_list = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
# while True:
#     str_input = input().rstrip()
#     if str_input == '#': break
#     else:
#         vowel_count = 0
#         str_list = list(str_input)
#         # print(str_list)

#         for i in range(len(str_list)):
#             if str_list[i] in vowel_list:
#                 vowel_count += 1

#         print(vowel_count)


# 2810 컵홀더
# import sys
# input = sys.stdin.readline

# def solve():
#     len_sit_list = int(input())
#     sit_list = list(input().rstrip())
#     # print(sit_list)

#     idx, total_cup_holder = 0, 0
#     LL_check = False

#     while idx < len_sit_list:
#         if sit_list[idx] == 'S':
#             total_cup_holder += 1
#             idx += 1
#         else: # LL
#             if not LL_check:
#                 LL_check = True
#                 total_cup_holder += 2
#             else:
#                 total_cup_holder += 1
#             idx += 2

#     print(total_cup_holder)

# solve()


# 1991 트리 순회
# import sys
# input = sys.stdin.readline

# def preorder(tree, root):
#     print(root, end='')
#     left, right = tree[root]
#     # print(left, right)
#     if left != '.': preorder(tree, left)
#     if right != '.': preorder(tree, right)

# def inorder(tree, root):
#     left, right = tree[root]

#     if left != '.': inorder(tree, left)
#     print(root, end='')
#     if right != '.': inorder(tree, right)

# def postorder(tree, root):
#     left, right = tree[root]

#     if left != '.': postorder(tree, left)
#     if right != '.': postorder(tree, right)
#     print(root, end='')

# def solve():
#     node_num = int(input())
#     # tree = [[] for _ in range(node_num)]
#     tree = dict()

#     for i in range(node_num):
#         root, left, right = map(str, input().split())
#         # print(root, left, right)

#         # tree[i] = [root, left, right]
#         tree[root] = [left, right]

#     # print(tree)
#     preorder(tree, 'A')
#     print()
#     inorder(tree, 'A')
#     print()
#     postorder(tree, 'A')

# solve()


# 2083 럭비 클럽
# import sys
# input = sys.stdin.readline

# while True:
#     name, age, weights = map(str, input().split())
#     if name == '#': break
#     else:
#         age, weights = int(age), int(weights)
#         if age > 17 or weights >= 80:
#             ones_class = 'Senior'
#         else:
#             ones_class = 'Junior'

#         print(name, ones_class)


# 1312 소수
# A, B, N = map(int, input().split())
# num = A % B
# decimal_list = [0]*1000000

# for i in range(N):
#     num *= 10
#     decimal_list[i] = num // B
#     num %= B

# # print(A/B)
# # print(decimal_list)
# print(decimal_list[N-1])


# 1475 방 번호
# num_list = list(map(int, input()))
# # print(num_list)
# check_list = [0] * 9 # 0 ~ 8

# for i in range(len(num_list)):
#     if num_list[i] == 9:
#         check_list[6] += 1
#     else:
#         check_list[num_list[i]] += 1

# if check_list[6] % 2 == 1: check_list[6] += 1
# check_list[6] //= 2

# print(max(check_list))


# 1769 3의 배수
# num_list = list(map(int, input()))
# count = 0

# while len(num_list) > 1:
#     num_list = list(map(int, str(sum(num_list))))
#     # print(num_list)
#     count += 1

# print(count, 'YES' if num_list[0] % 3 == 0 else 'NO', sep = '\n')

# try 2 ㅡ better code? ㅡ 비슷하네
# 참고 : https://www.acmicpc.net/board/view/62323
# 시간초과가 났던 이유 ㅡ 숫자가 백만 이하라는 게 아니라 백만 자리 이하의 수를 준다
# sum_value = int(input())
# sum_value = list(map(int, input()))
# # print(sum_value)
# count = 0

# if len(sum_value) >= 2:
#     count += 1
# sum_value = sum(sum_value)

# while sum_value >= 10:
#     count += 1
#     tmp_value = 0

#     while sum_value // 10 != 0:
#         tmp_value += sum_value % 10
#         sum_value //= 10
#         # print(sum_value)
#     sum_value += tmp_value
#     # print(sum_value)

# print(count, 'YES' if sum_value % 3 == 0 else 'NO', sep = '\n')


# 9205 맥주 마시면서 걸어가기
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     convenience_store_num = int(input())
#     convenience_store_list = [] * convenience_store_num

#     home_x, home_y = map(int, input().split())
#     home_xy =
#     for _ in range(convenience_store_num):

#         convenience_store_list.append(map(int, input().split()))


# 1235 학생 번호
# import sys
# input = sys.stdin.readline

# num = int(input())
# num_list = [int(input()) for _ in range(num)]
# # print(num_list)

# len = 1
# while True:
#     check_dict = dict()
#     exclusive_check = True
#     for i in range(num):
#         if num_list[i] % (10**len) in check_dict:
#             exclusive_check = False
#             break
#         else:
#             check_dict[num_list[i] % (10**len)] = 1
#     # print(check_dict)

#     if exclusive_check == True:
#         print(len)
#         break
#     else:
#         len += 1


# 15663 N과 M (9)
# import sys
# import itertools

# input = sys.stdin.readline

# n, m = map(int, input().split())
# num_list = sorted(list(map(int, input().split())))
# ans_list = dict()

# for i in itertools.permutations(num_list, m):
#     if i not in ans_list:
#         print(*i)
#         ans_list[i] = 1


# 15666 N과 M(12)
# import sys
# import itertools

# input = sys.stdin.readline

# n, m = map(int, input().split())
# num_list = sorted(list(map(int, input().split())))
# ans_list = dict()

# for i in itertools.combinations_with_replacement(num_list, m):
#     if i not in ans_list:
#         print(*i)
#         ans_list[i] = 1


# 1660 캡틴 이다솜
# try 1 - input 최대값인 300000 처리하는데 한참 걸린다
# num = int(input())

# cannon_balls_list = [0]*200
# for i in range(1, 200):
#     cannon_balls_list[i] = i*(i+1)*(i+2)//6
# print(cannon_balls_list)
# cannon_balls_idx = 1

# dp_list = [0] * (num+1)
# for i in range(num+1):
#     dp_list[i] = i
# # print(dp_list)

# for i in range(1, num+1):
#     while cannon_balls_idx < 199:
#         if cannon_balls_list[cannon_balls_idx+1] <= dp_list[i]:
#             # print("i", i)
#             cannon_balls_idx += 1
#             # print(cannon_balls_idx)
#         else: break
#     # print(cannon_balls_idx, cannon_balls_list[cannon_balls_idx])

#     dp_list[i] = (i // cannon_balls_list[cannon_balls_idx]) + dp_list[i % cannon_balls_list[cannon_balls_idx]]
#     # print(i, dp_list[i])

#     for j in range(0, i//2):
#         new_dp_val = dp_list[j] + dp_list[i-j]
#         if dp_list[i] > new_dp_val:
#             dp_list[i] = new_dp_val

# print(dp_list[i])


# try2
# 85% 틀렸습니다 ㅡ idx 범위를 수정해도 똑같음
# N = int(input())

# cannon_balls_list = [0]*121
# for i in range(1, 121):
#     cannon_balls_list[i] = i*(i+1)*(i+2)//6
# cannon_balls_list[0], cannon_balls_idx = 1, 1
# print(cannon_balls_list)

# dp_list = [i for i in range(N+1)]
# # print(dp_list)

# for i in range(1, N+1):
#     # find proper index
#     while cannon_balls_idx < 120:
#         if cannon_balls_list[cannon_balls_idx+1] <= dp_list[i]:
#             cannon_balls_idx += 1
#         else: break
#     # print(cannon_balls_idx, cannon_balls_list[cannon_balls_idx])

#     # for idx in range(cannon_balls_idx, cannon_balls_idx//2 -1, -1):
#     for idx in range(cannon_balls_idx, -1, -1):
#         new_dp_val = (i // cannon_balls_list[idx]) + dp_list[i % cannon_balls_list[idx]]
#         # print(i, cannon_balls_list[idx])
#         if dp_list[i] > new_dp_val:
#             dp_list[i] = new_dp_val

# # print(dp_list)
# print(dp_list[i])

# 300000 개 인덱스를 다 받아도 될 듯 ?
# 3:06 ~
# N = int(input())

# cannon_balls_list = [0]*121
# for i in range(1, 121):
#     cannon_balls_list[i] = i*(i+1)*(i+2)//6
#     # if cannon_balls_list[i] > 300000: print(i)
# # print(cannon_balls_list)

# dp_list = [i for i in range(N+1)]
# # print(dp_list)

# # cannon_balls_idx = 1
# for idx in range(1, N+1):
#     # if cannon_balls_idx < 120 and cannon_balls_list[cannon_balls_idx] < idx:
#     # if cannon_balls_idx < 120 and cannon_balls_list[cannon_balls_idx+1] <= idx:
#     #     cannon_balls_idx += 1
#     # print(idx, cannon_balls_idx)
#     # for sub_idx in cannon_balls_list[:cannon_balls_idx+1]:
#     # for sub_idx in cannon_balls_list:
#     #     if sub_idx == idx:
#     #         dp_list[idx] = 1
#     #         break
#     #     elif sub_idx > idx:
#     #         break
#     #     dp_list[idx] = min(dp_list[idx], dp_list[idx - sub_idx]+1)

#     for sub_idx in cannon_balls_list:
#         if sub_idx <= idx:
#             dp_list[idx] = min(dp_list[idx], dp_list[idx - sub_idx]+1)
#         else: break

# # print(dp_list)
# print(dp_list[N])


# 1531 투명
# import sys
# input = sys.stdin.readline

# def solve():
#     graph = [[0] * 100 for _ in range(100)]

#     n, m = map(int, input().split())
#     for _ in range(n):
#         x1, y1, x2, y2 = map(int, input().split())
#         for y in range(y1-1, y2):
#             for x in range(x1-1, x2):
#                 graph[y][x] += 1

#     ans = 0
#     for y in range(100):
#         for x in range(100):
#             if graph[y][x] > m:
#                 ans += 1
#     print(ans)

# solve()


# 11660 구간 합 구하기 5
# try1 - 시간 초과
# import sys
# input = sys.stdin.readline

# def solve():
#     n, m = map(int, input().split())
#     num_list = [list(map(int, input().split())) for _ in range(n)]
#     dp_list = [[0] * (n+1) for _ in range(n+1)]
#     for x in range(1, n+1):
#         sum_of_num = 0
#         for y in range(1, n+1):
#             sum_of_num += num_list[x-1][y-1]
#             dp_list[x][y] = sum_of_num
#     # for y in range(n+1):
#     #     print(dp_list[y])

#     for _ in range(m):
#         x1, y1, x2, y2 = map(int, input().split())
#         ans = 0
#         for x in range(x1, x2+1):
#             ans += dp_list[x][y2] - dp_list[x][y1-1]
#         print(ans)

# solve()


# try 2 - 맞았습니다 !
# import sys
# input = sys.stdin.readline

# def solve():
#     n, m = map(int, input().split())
#     num_list = [list(map(int, input().split())) for _ in range(n)]
#     dp_list = [[0] * (n+1) for _ in range(n+1)]

#     for x in range(1, n+1):
#         sum_of_num = 0
#         for y in range(1, n+1):
#             sum_of_num += num_list[x-1][y-1]
#             dp_list[x][y] = sum_of_num + dp_list[x-1][y]
#     # for y in range(n+1):
#     #     print(dp_list[y])

#     for _ in range(m):
#         x1, y1, x2, y2 = map(int, input().split())
#         ans = dp_list[x2][y2] - dp_list[x2][y1-1] - dp_list[x1-1][y2] + dp_list[x1-1][y1-1]
#         print(ans)

# solve()


# 1343 폴리오미노
# try 1 - code1 을 좀 더 간소화해서 try 1 - code2
# board_list = list(input())
# # print(board_list)

# start_idx, polyomino_len = 0, 0
# polyomino_check, possible_check = False, True

# for idx in range(len(board_list)):
#     # print(idx)
#     if board_list[idx] == 'X':
#         # if polyomino_check == False:
#         #     start_idx = idx
#         #     polyomino_check = True

#         if polyomino_len == 0:
#             start_idx = idx

#         # if polyomino_check == True:
#         polyomino_len += 1

#         if polyomino_len == 4:
#             board_list[start_idx : idx+1] = 'AAAA'
#             polyomino_len = 0
#             # print("new!", board_list)
#     else: # case of '.'
#         polyomino_check = False
#         if polyomino_len == 2:
#             board_list[start_idx : idx] = 'BB'
#             polyomino_len = 0
#         elif polyomino_len % 2 == 1:
#             possible_check = False
#             break
#     # print(idx, board_list)

# # print(polyomino_len)
# if polyomino_len == 2:
#     board_list[-2:] = 'BB'
# elif polyomino_len % 2 == 1:
#     possible_check = False

# if possible_check == True: print(*board_list, sep='')
# else: print(-1)

#  try 1 - code2
# board_list = list(input())
# # print(board_list)

# start_idx, polyomino_len = 0, 0
# possible_check = True

# for idx in range(len(board_list)):
#     # print(idx)
#     if board_list[idx] == 'X':
#         if polyomino_len == 0: start_idx = idx
#         polyomino_len += 1

#         if polyomino_len == 4:
#             board_list[start_idx : idx+1] = 'AAAA'
#             polyomino_len = 0

#     else: # case of '.'
#         if polyomino_len == 2:
#             board_list[start_idx : idx] = 'BB'
#             polyomino_len = 0
#         elif polyomino_len % 2 == 1:
#             possible_check = False
#             break
#     # print(idx, board_list)

# # case of list-end
# # print(polyomino_len)
# if polyomino_len == 2:
#     board_list[start_idx:] = 'BB'
# elif polyomino_len % 2 == 1:
#     possible_check = False

# if possible_check == True: print(*board_list, sep='')
# else: print(-1)


# 2161 카드1
# from collections import deque

# que = deque([i for i in range(1, int(input())+1)])
# while que:
#     print(que.popleft(), end=' ')
#     if que:
#         que.append(que.popleft())


# 1065 한수
# num = int(input())
# cnt = 0

# for i in range(1, num+1):
#     hansu_check = True

#     if i >= 100:
#         i_div_10 = i // 10
#         if (i % 10 - i_div_10 % 10) != (i_div_10 % 10) - (i_div_10 // 10):
#             hansu_check = False

#     if hansu_check:
#         cnt += 1

# print(cnt)


# 1094 막대기
# num = int(input())
# cnt = 0

# while num >= 1:
#     cnt += num % 2
#     num //= 2
# print(cnt)


# 1388 바닥 장식
# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs(que, graph, check_graph, inc_x, inc_y, shape, n, m):
#     x, y = que.popleft()
#     if shape == '-':
#         for plus_x, plus_y in inc_x:
#             new_x, new_y = x + plus_x, y + plus_y
#             if 0 <= new_y < n and 0 <= new_x < m:
#                 if graph[new_y][new_x] == shape and check_graph[new_y][new_x] == False:
#                     que.append([new_x, new_y])
#                     check_graph[new_y][new_x] = True
#     else: # '|'
#         for plus_x, plus_y in inc_y:
#             new_x, new_y = x + plus_x, y + plus_y
#             if 0 <= new_y < n and 0 <= new_x < m:
#                 if graph[new_y][new_x] == shape and check_graph[new_y][new_x] == False:
#                     que.append([new_x, new_y])
#                     check_graph[new_y][new_x] = True

# def solve():
#     n, m = map(int, input().split())
#     graph = [list(input().rstrip()) for _ in range(n)]
#     check_graph = [[False]*m for _ in range(n)]
#     inc_x, inc_y = [[1, 0], [-1, 0]], [[0, 1], [0, -1]]
#     # print(graph)

#     cnt = 0
#     que = deque()
#     for y in range(n):
#         for x in range(m):
#             if check_graph[y][x] == False:
#                 que.append([x, y])
#                 shape = graph[y][x]
#                 cnt += 1

#                 while que:
#                     bfs(que, graph, check_graph, inc_x, inc_y, shape, n, m)

#     print(cnt)

# solve()


# SUAPC 2022 Summer B번 - 내비게이션
# import sys
# input = sys.stdin.readline

# num = int(input())
# sx, sy, ex, ey = map(int, input().split())
# idx, min_dist = 0, sys.maxsize

# for i in range(1, num+1):
#     pre_x, pre_y = sx, sy
#     total_dist = 0
#     for _ in range(int(input())):
#         next_x, next_y = map(int, input().split())
#         total_dist += abs(pre_x - next_x) + abs(pre_y - next_y)
#         pre_x, pre_y = next_x, next_y
#         # print("test", total_dist, pre_x, next_x, pre_y, next_y)
#     total_dist += abs(pre_x - ex) + abs(pre_y - ey)
#     # print("haha", total_dist, i)

#     if min_dist > total_dist:
#         min_dist = total_dist
#         idx = i

# print(idx)


# F번 - 차의 개수
# num = int(input())

# max_list, min_list = [1], [i for i in range(1, num+1)]
# max_set, min_set = set(), set()
# tmp_num, plus_num = 1, 30

# for _ in range(num-1):
#     tmp_num += plus_num
#     max_list.append(tmp_num)
#     plus_num += 31
#     # plus_num += 11
#     # plus_num *= 7
# # print(max_list)
# # print(min_list)

# for num_one in range(0, num-1):
#     for num_two in range(num_one+1, num):
#         if abs(max_list[num_two] - max_list[num_one]) not in max_set:
#             max_set.add(abs(max_list[num_two] - max_list[num_one]))
#         if abs(min_list[num_two] - min_list[num_one]) not in min_set:
#             min_set.add(abs(min_list[num_two] - min_list[num_one]))
# # print(len(max_set), max_set)
# # print(len(min_set), min_set)

# print(len(max_set))
# print(*max_list, sep=' ')
# print(len(min_set))
# print(*min_list, sep=' ')


# I번 - 딸기와 토마토
# import sys
# input = sys.stdin.readline

# n, m, k = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# # print(graph)
# pos_point_list, ans_list = [], []

# # col
# for y in range(n-k+1):
#     for x in range(m):
#         pos_check = True
#         for plus_y in range(k):
#             if graph[y+plus_y][x] != 1:
#                 pos_check = False
#                 break
#         # print(y, x, pos_check)
#         if pos_check:
#             pos_point_list.append([y, x, 0])

# # row
# for y in range(n):
#     for x in range(m-k+1):
#         pos_check = True
#         for plus_x in range(k):
#             if graph[y][x+plus_x] != 1:
#                 pos_check = False
#                 break
#         if pos_check:
#             pos_point_list.append([y, x, 1])
# # print(pos_point_list)

# if len(pos_point_list) == 1:
#     start_y, start_x, direction = pos_point_list[0][0], pos_point_list[0][1], pos_point_list[0][2]
#     # print(start_y, start_x, direction)

#     if direction == 0:
#         for plus_val in range(k):
#             ans_list.append([start_y+plus_val, start_x])
#     else:
#         for plus_val in range(k):
#             ans_list.append([start_y, start_x+plus_val])
#     # print(ans_list)
# else:
#     for i in range(2):
#         start_y, start_x, direction = pos_point_list[i][0], pos_point_list[i][1], pos_point_list[i][2]

#         if direction == 0:
#             for plus_val in range(k):
#                 graph[start_y+plus_val][start_x] += 1
#         else:
#             for plus_val in range(k):
#                 graph[start_y][start_x+plus_val] += 1
#     # print(graph)

#     for y in range(n):
#         for x in range(m):
#             if graph[y][x] == 3:
#                 ans_list.append([y, x])

# # print(ans_list)
# ans_list = sorted(ans_list, key=lambda x:(x[0],x[1]))
# if len(ans_list) == 0: print(0)
# else:
#     print(len(ans_list))
#     for x, y in ans_list:
#         print(x+1, y+1)


# 5014 스타트링크
# from collections import deque

# F, S, G, U, D = map(int, input().split())
# # print(F)
# cnt_list = [-1] * F
# cnt_list[S-1] = 0
# que = deque([[S,0]])

# while que:
#     num, cnt = que.popleft()
#     # print("num:", num, cnt)

#     if num == G:
#         print(cnt)
#         quit()

#     next_step_floor = num+U
#     if next_step_floor <= F and cnt_list[next_step_floor-1] == -1:
#         cnt_list[next_step_floor-1] = cnt
#         que.append([next_step_floor, cnt+1])

#     next_step_floor = num-D
#     if next_step_floor >= 1 and cnt_list[next_step_floor-1] == -1:
#         cnt_list[next_step_floor-1] = cnt
#         que.append([next_step_floor, cnt+1])

# print("use the stairs")


# 2628 종이자르기
# 리팩토링 가능 ~

# import sys
# input = sys.stdin.readline

# col_num, row_num = map(int, input().split())
# row_cut_list, col_cut_list = [], []
# for _ in range(int(input())):
#     check_row_or_col, line_num = map(int, input().split())
#     if check_row_or_col == 0:
#         row_cut_list.append(line_num)
#     else:
#         col_cut_list.append(line_num)

# row_cut_list.append(row_num)
# col_cut_list.append(col_num)

# row_cut_list.sort()
# col_cut_list.sort()

# # print(row_cut_list, col_cut_list)

# pre_val = 0 # 1 아님 ~
# max_row, max_col = 0, 0

# for row_val in row_cut_list:
#     if max_row < row_val - pre_val:
#         max_row = row_val - pre_val
#     pre_val = row_val
#     # print(row_val, pre_val, max_row)
# pre_val = 0
# for col_val in col_cut_list:
#     if max_col < col_val - pre_val:
#         max_col = col_val - pre_val
#     pre_val = col_val
#     # print(col_val, pre_val, max_col)

# print(max_row * max_col)

# 11382 꼬마 정민
# a,b,c = map(int, input().split())
# print(a+b+c)


# 1969 DNA
# 1차 시도 - 문제를 잘못 이해했네
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# DNA_list = [list(input().rstrip()) for _ in range(n)]
# # print(DNA_list)
# Hamming_Distance_list = [0] * n

# for i in range(n):
#     Hamming_Distance = 0
#     for j in range(n):
#         if i != j:
#             for k in range(m):
#                 if DNA_list[i][k] != DNA_list[j][k]:
#                     Hamming_Distance += 1
#     Hamming_Distance_list[i] = Hamming_Distance
# print(Hamming_Distance_list)


# try - 2
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# DNA_list = [list(input().rstrip()) for _ in range(n)]
# new_DNA_list = ['A'] * m
# min_Hamming_Distance = 0

# for i in range(m):
#     DNA_check_list = [0] * 26
#     for j in range(n):
#         # print(j, i)
#         DNA_check_list[ord(DNA_list[j][i])-65] += 1

#     max_val, max_val_idx = 0, 0
#     for alphabet_idx in range(26):
#         if max_val < DNA_check_list[alphabet_idx]:
#             max_val = DNA_check_list[alphabet_idx]
#             max_val_idx = alphabet_idx

#     new_DNA_list[i] = chr(max_val_idx + 65)
#     min_Hamming_Distance += sum(DNA_check_list) - DNA_check_list[max_val_idx]

# print(*new_DNA_list, sep='')
# print(min_Hamming_Distance)


# 1384 메시지
# PN_idx를 range(num)에서 num으로 지정해야 되는 이유를 못 찾고 있었음 ㅋㅋ
# import sys
# input = sys.stdin.readline

# group_num = 1
# while True:
#     num = int(input())
#     if num == 0 : break

#     name_PN_list = [list(map(str, input().split())) for _ in range(num)]
#     # print(name_PN_list)
#     PN_check = False

#     print("Group {0}".format(group_num))
#     for name_idx in range(num):
#         for PN_idx in range(1, num):
##        for PN_idx in range(num): 이거보다 위가 더 좋은 코드 why? Name은 check할 필요가 없으니~
#             if name_PN_list[name_idx][PN_idx] == 'N':
#                 PN_check = True
#                 target_name_idx = name_idx - PN_idx
#                 if target_name_idx < 0: target_name_idx += num
#                 # print(target_name_idx)
#                 print("{0} was nasty about {1}".format(name_PN_list[target_name_idx][0], name_PN_list[name_idx][0]))

#     if not PN_check:
#         print("Nobody was nasty")

#     group_num += 1
#     print()


# 1059 좋은 구간
# import sys
# input = sys.stdin.readline

# len_s = int(input())
# s_list = sorted(list(map(int, input().split())))
# target_num = int(input())
# # print(s_list)

# if len_s == 1 or target_num < s_list[0]:
#     start_num, end_num = 0, s_list[0]
# else:
#     for idx in range(len_s-1):
#         if s_list[idx] <= target_num < s_list[idx+1]:
#             break
#     # print(idx)
#     start_num, end_num = s_list[idx], s_list[idx+1]

# # ans - 1
# # ans = 0
# # for i in range(start_num+1, end_num-1):
# #     for j in range(i+1, end_num):
# #         if i <= target_num <= j:
# #             ans += 1
# #             # print(i, target_num, j)
# # print(ans)

# # ans - 2
# if target_num in s_list: print(0)
# else:
#     print((target_num - start_num) * (end_num - target_num) -1)


# 2875 대회 or 인턴
# N, M, K = map(int, input().split())
# print(min(N//2, M, (N+M-K)//3))


# 1491 나선
# N, M = map(int, input().split())
# sub_cnt = min((N-1)//2, (M-1)//2)
# # print("sub_cnt:", sub_cnt)

# # 동서남북 껍데기 몇 번 제거할 수 있는지 (subbed_N/M은 최대 2를 가짐)
# subbed_N, subbed_M = N-sub_cnt*2, M-sub_cnt*2
# if subbed_N == 1 or subbed_M == 1:
#     print(N-1-sub_cnt, M-1-sub_cnt)
# else: # subbed_N == 2 or subbed_M == 2:
#     print(sub_cnt, sub_cnt+1)

# 이 코드를 위 코드로 간소화
# if subbed_M == 2:
#     # print("1: ",sub_cnt, M-sub_cnt-1)
#     print("1: ",sub_cnt, sub_cnt+1)
# elif subbed_M == 1:
#     print("2: ", N-sub_cnt-1, M-sub_cnt-1)
# elif subbed_N == 2:
#     print("3: ", sub_cnt, sub_cnt+1)
# elif subbed_N == 1:
#     print("4 :", N-sub_cnt-1, M-sub_cnt-1)


# 1835 카드
# import sys
# from collections import deque
# input = sys.stdin.readline

# N = int(input())
# que = deque([i for i in range(N)])
# num_list = [0] * N

# num = 1
# while que:
#     for _ in range(num):
#         que.append(que.popleft())
#     # print(que, num)
#     num_list[que.popleft()] = num
#     # print(num_list)
#     num += 1

# print(*num_list)


# 17404 RGB거리 2
"""
월요일에 제출 ~ 09/12 ~
틀렸습니다 why?
반례
3
26 83 40
49 60 57
13 89 99
위 반례에 대해서 110 이 나올 수가 없음
"""
# import sys
# input = sys.stdin.readline

# N = int(input())
# val_list = [list(map(int, input().split())) for _ in range(N)]
# dp_list = [[1000000]*3 for _ in range(N)]
# idx_list = [[0]*3 for _ in range(N)]
# dp_list[0] = val_list[0]
# idx_list[0] = [0, 1, 2]
# print("dp_list, idx_list :", dp_list, idx_list)

# for y in range(1, N):
#     for x in range(3):
#         for comp_x in range(3):
#             if x != comp_x:
#                 if dp_list[y][x] > dp_list[y-1][comp_x]:
#                     dp_list[y][x] = dp_list[y-1][comp_x]
#                     idx_list[y][x] = idx_list[y-1][comp_x]
#         dp_list[y][x] += val_list[y][x]

# print(dp_list)
# # print(idx_list)

# # 1번 집의 색과 N번 집의 색이 같은 경우를 위한 코드
# for x in range(3):
#     if x == idx_list[N-1][x]:
#         dp_list[N-1][x] -= dp_list[0][x]
#         val_min = 1000
#         for comp_x in range(3):
#             if x != comp_x:
#                 if val_min > dp_list[0][comp_x]:
#                     val_min = dp_list[0][comp_x]
#         dp_list[N-1][x] += val_min

# print(min(dp_list[N-1]))


# import sys
# input = sys.stdin.readline

# N = int(input())
# val_list = [list(map(int, input().split())) for _ in range(N)]
# # print(dp_list)
# val_min = 1000000

# for z in range(3):
#     dp_list = [[1000000]*3 for _ in range(N)]
#     dp_list[0] = val_list[0]
#     for x in range(3):
#         if z != x:
#             dp_list[1][x] = dp_list[0][z] + val_list[1][x]
#     # print(dp_list)

#     for y in range(2, N-1):
#         for x in range(3):
#             for comp_x in range(3):
#                 if x != comp_x:
#                     if dp_list[y][x] > dp_list[y-1][comp_x]:
#                         dp_list[y][x] = dp_list[y-1][comp_x]
#             dp_list[y][x] += val_list[y][x]

#     for x in range(3):
#         if z != x:
#             for comp_x in range(3):
#                 if x != comp_x:
#                     if dp_list[N-1][x] > dp_list[N-2][comp_x]:
#                         dp_list[N-1][x] = dp_list[N-2][comp_x]
#             dp_list[N-1][x] += val_list[N-1][x]
#     # print(dp_list)

#     val_min = min(val_min, min(dp_list[N-1]))
#     # print(val_min)

# print(val_min)


# 1359 복권
# def factorial(num):
#     if num <= 1:
#         return 1
#     else:
#         val = 1
#         for i in range(num, 1, -1):
#             val *= i
#         return val
# # print(factorial(5))

# def combinations(num1, num2):
#     return factorial(num1) // (factorial(num2) * factorial(num1 - num2))

# # if 2*M-K >= N:
# #     print(1.0)
# # else:
# # print(1 - combinations(N, M)*combinations(N-M, M)/(combinations(N, M)**2))
# # print(combinations(N,M), combinations(N-M, M))

# def solve():
#     N, M, K = map(int, input().split())

#     sub_val = 0
#     for k in range(K):
#         sub_val += combinations(N, M) * combinations(M, k) * combinations(N-M, M-k)
#     print(1 - sub_val/combinations(N, M)**2)

# solve()


# 13023 ABCDE
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def dfs(graph, visited_list, n, num):
#     # print(visited_list, n, num)
#     if num == 5:
#         return True
#     for new_n in graph[n]:
#         if new_n not in visited_list:
#             visited_list.append(new_n)
#             return dfs(graph, visited_list, new_n, num+1)
#     return False

# def solve():
#     N, M = map(int, input().split())
#     graph = [[] for _ in range(N)]

#     for _ in range(M):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     # print(graph)

#     ans_check = False
#     for n in range(N):
#         visited_list = [n]
#         for new_n in graph[n]:
#             if new_n not in visited_list:
#                 visited_list.append(new_n)
#                 if dfs(graph, visited_list, new_n, 2) == True:
#                     ans_check = True
#                     break
#             # print(visited_list)
#             # print("new_n : ", new_n)
#             visited_list.remove(new_n)
#             # print(visited_list)

#     if ans_check: print(1)
#     else: print(0)

# solve()

# Backtracking
# import sys
# input = sys.stdin.readline

# def dfs(graph, visited_list, n, num):
#     visited_list[n] = True
#     # print(visited_list)
#     if num == 4:
#         print(1)
#         exit()

#     for new_n in graph[n]:
#         if visited_list[new_n] == False:
#             dfs(graph, visited_list, new_n, num+1)

#     visited_list[n] = False

# def solve():
#     N, M = map(int, input().split())
#     graph = [[] for _ in range(N)]
#     visited_list = [False] * N
#     for _ in range(M):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     # print(graph)

#     for n in range(N):
#         # print(n)
#         dfs(graph, visited_list, n, 0)
#     print(0)

# solve()


# 2407 조합
# def factorial(num):
#     if num <= 1:
#         return 1
#     else:
#         val = 1
#         for i in range(num, 1, -1):
#             val *= i
#         return val

# def solve():
#     n, m = map(int, input().split())
#     print(factorial(n)//(factorial(m)*factorial(n-m)))

# solve()


# 9465 스티커
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     num_list = [list(map(int,input().split())) for _ in range(2)]
#     # print(num_list)
#     dp_list = [[0] * n for _ in range(2)]
#     dp_list[0][0], dp_list[1][0] = num_list[0][0], num_list[1][0]

#     if n >= 2:
#         dp_list[0][1] = dp_list[1][0] + num_list[0][1]
#         dp_list[1][1] = dp_list[0][0] + num_list[1][1]

#     for idx in range(2, n):
#         for x in range(2):
#             dp_list[x][idx] = max(dp_list[(x+1)%2][idx-1], dp_list[(x+1)%2][idx-2]) + num_list[x][idx]

#     # for x in range(2):
#     #     print(dp_list[x])
#     print(max(dp_list[0][n-1], dp_list[1][n-1]))


# 13277 큰 수 곱셈
# a, b = map(int, input().split())
# print(a*b)

# 16430 제리와 톰
# A, B = map(int, input().split())
# print(B-A, B)

# 15740 A+B-9
# A, B = map(int, input().split())
# print(A+B)

# # 1913 달팽이
# N = int(input())
# sqaured_N = N**2
# target_num = int(input())
# target_x, target_y = (N//2)+1, (N//2)+1

# num_table = [[0]*N for _ in range(N)]
# nx, ny = N//2, N//2
# num_table[nx][ny] = 1
# num = 2
# direction, moving_distance = 0, 0

# while num <= sqaured_N:
#     if direction == 0 or direction == 2:
#         moving_distance += 1

#     for _ in range(moving_distance):
#         if direction == 0:
#             nx -= 1
#         elif direction == 1:
#             ny += 1
#         elif direction == 2:
#             nx += 1
#         else:
#             ny -= 1

#         if num == target_num:
#             target_x, target_y = nx+1, ny+1

#         num_table[nx][ny] = num
#         # print(nx, ny, direction)
#         num += 1

#         if nx == 0 and ny == 0:
#             break
#     direction = (direction + 1) % 4

# for x in range(N):
#     print(*num_table[x])
# print(target_x, target_y)


# 9653 스타워즈 로고
# print("\
#     8888888888  888    88888\n\
#    88     88   88 88   88  88\n\
#     8888  88  88   88  88888\n\
#        88 88 888888888 88   88\n\
# 88888888  88 88     88 88    888888\n\
# \n\
# 88  88  88   888    88888    888888\n\
# 88  88  88  88 88   88  88  88\n\
# 88 8888 88 88   88  88888    8888\n\
#  888  888 888888888 88  88      88\n\
#   88  88  88     88 88   88888888")


# 1817 짐 챙기는 숌
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# box, remain_amount = 0, 0

# if N != 0:
#     box_list = list(map(int, input().split()))
#     # print(box_list)

#     for i in range(N):
#         if remain_amount < box_list[i]:
#             box += 1
#             remain_amount = M - box_list[i]
#         else:
#             remain_amount -= box_list[i]
#         # print(box, box_list[i], remain_amount)
# print(box)


# 1476 날짜 계산
# E, S, M = map(int, input().split())
# tmp_E, tmp_S, tmp_M = 1, 1, 1
# year = 1

# # 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19
# while True:
#     if tmp_E == E and tmp_S == S and tmp_M == M:
#         # print(tmp_E, E, tmp_S, S, tmp_M, M)
#         break
#     else:
#         year += 1

#         # tmp_E = (tmp_E + 1) % 16
#         # tmp_S = (tmp_S + 1) % 29
#         # tmp_M = (tmp_M + 1) % 20

#         # if tmp_E == 0: tmp_E = 1
#         # if tmp_S == 0: tmp_S = 1
#         # if tmp_M == 0: tmp_M = 1

#     개선 (better code)
#         tmp_E = (tmp_E % 15) + 1
#         tmp_S = (tmp_S % 28) + 1
#         tmp_M = (tmp_M % 19) + 1
#     # print(tmp_E, tmp_S, tmp_M)
#     # print(year)

# print(year)


# 11723 집합 Q&A ㅡ https://www.acmicpc.net/board/view/100546
# import sys
# input = sys.stdin.readline

# if __name__ == '__main__':
#     m = int(input().rstrip())
#     s = set()
#     all_set = set([i for i in range(1, 21)])
#     for _ in range(m):
#         line = list(input().rstrip().split())
#         o = line[0]
#         n = 0
#         print(o, len(o),line, len(line))
#         if len(o) == 2:
#             n = int(o[1])
#         if o == "add":
#             s.add(n)
#         elif o == "check":
#             print(1 if n in s else 0)
#         elif o == "remove":
#             print(n)
#             print("Is it workded?")
#             s.discard(n)
#         elif o == "toggle":
#             try:
#                 s.remove(n)
#             except:
#                 s.add(n)
#         elif o == "all":
#             s = all_set.copy()
#         elif o == "empty":
#             s = set()
#         print("n : ", n)
#         print(s)


# 1544 사이클 단어
# try1 - 문제를 잘못 이해했다 ㅋㅋㅋ
# import sys
# input = sys.stdin.readline

# word_dict = dict()
# for _ in range(int(input())):
#     alpha_check_list = [0] * 26
#     alpha_list = list(input().rstrip())
#     # print(alpha_list)

#     for alphabet in alpha_list:
#         alpha_check_list[ord(alphabet)-97] += 1

#     alpha_check_list = tuple(alpha_check_list)
#     if alpha_check_list in word_dict:
#         word_dict[alpha_check_list] += 1
#     else:
#         word_dict[alpha_check_list] = 1

# print(len(word_dict))

# try2
# import sys
# input = sys.stdin.readline

# word_dict = dict()
# for i in range(int(input())):
#     word_list = list(input().rstrip())
#     overlapped_word_check = False

#     for start_idx in range(len(word_list)):
#         # this code is not work - new_list : None
#         # new_list = word_list[start_idx:].append(word_list[:start_idx])

#         # be write like below code
#         new_list = word_list[start_idx:]
#         new_list.extend(word_list[:start_idx])
#         # print(new_list)

#         tupled_new_list = tuple(new_list)
#         # print(tupled_new_list)
#         if tupled_new_list in word_dict:
#             word_dict[tupled_new_list] += 1
#             overlapped_word_check = True
#             # print(new_list, "haha !")

#     if overlapped_word_check == False:
#         word_dict[tuple(word_list)] = 1

# print(len(word_dict))


# 15727
# t = int(input())
# if t % 5 == 0 : print(t//5)
# else: print((t//5)+1)


# 1015 수열 정렬
# import sys
# input = sys.stdin.readline

# N = int(input())
# p_list = [0] * N
# num_list = list(map(int, input().split()))
# num_idx_dict = dict()

# for idx in range(N):
#     num_idx_dict[idx] = num_list[idx]
# # print(num_idx_dict)

# new_num_dict = dict(sorted(num_idx_dict.items(), key=lambda x:(x[1], x[0])))
# # print(new_num_dict)

# val = 0
# for idx in new_num_dict.keys():
#     p_list[idx] = val
#     val += 1

# print(*p_list)


# 2355 시그마
# 참고 https://www.acmicpc.net/board/view/82119
# A, B = map(int, input().split())
# if A <= B: print((A+B)*(B-A+1)//2)
# else: print((A+B)*(A-B+1)//2)


# 1629 곱셈
# 2147483647
# A, B, C = map(int, input().split())
# # num_list = [A] * 31
# num_list = [1] * 31
# binary_B_list = list(map(int, bin(B)[2:]))
# binary_B_list.reverse()
# # print(binary_B_list)

# # mul_val = ((A%C)**2)
# # mul_val = ((A%C)**2)%C
# mul_val = (A**2)
# # print("mul_val : ", mul_val)

# num_list[1] = mul_val % C
# for i in range(2, len(num_list)):
#     # num_list[i] = num_list[i-1] * mul_val % C
#     num_list[i] = num_list[i-1] * mul_val
# print(num_list)

# ans = 1
# for idx in range(len(binary_B_list)):
#     if binary_B_list[idx] == 1:
#         # ans = (ans * num_list[idx]) % C
#         ans = (ans * num_list[idx])
#     # print(ans)
# print(ans%C)


# try 2 - 성공
# A, B, C = map(int, input().split())
# num_list = [A] * 31
# binary_B_list = list(map(int, bin(B)[2:]))
# binary_B_list.reverse()
# # print(binary_B_list)

# for i in range(1, len(num_list)):
#     num_list[i] = (num_list[i-1] ** 2) % C
# # print(num_list)

# ans = 1
# for idx in range(len(binary_B_list)):
#     if binary_B_list[idx] == 1:
#         ans = (ans * num_list[idx]) % C
#     # print(ans)
# print(ans)


# 1418 K-세준수
# N = int(input())
# K = int(input())

# se_joon_num_check_list = [0] * (N+1)
# se_joon_num_check_list[1] = 1

# for i in range(2, N+1):
#     if se_joon_num_check_list[i] == 0:
#         prime_num_list = []
#         target_num = i
#         for div_num in range(2, min(target_num+1, K+1)):
#             if target_num % div_num == 0:
#                 prime_num_list.append(div_num)
#                 target_num //= div_num
#             else:
#                 div_num += 1
#         # print(i)
#         # print(prime_num_list)
#         if prime_num_list[-1] <= K:
#             for j in range(2, K):
#                 idx = i
#                 while idx <= N:
#                     se_joon_num_check_list[idx] = 1
#                     idx *= j

# print(se_joon_num_check_list)
# print(sum(se_joon_num_check_list))


# 코드 개선... 했는데 오래 걸림
# 더 빠르게 동작할 수 있어야 함
# N = int(input())
# K = int(input())

# se_joon_num_check_list = [1] * (N+1)

# def prime_num_check(num):
#     if num == 1: return False
#     elif num == 2: return True
#     elif num % 2 == 0: return False
#     else:
#         # for div_num in range(3, num//3):
#         for div_num in range(3, num//3+1, 2):
#             if num % div_num == 0: return False
#         return True

# for i in range(K+1, N+1):
#     if se_joon_num_check_list[i] == 1 and prime_num_check(i) == True:
#         idx = i
#         while idx <= N:
#             se_joon_num_check_list[idx] = 0
#             idx += i

# # for i in range(K+1, N+1):
# #     if se_joon_num_check_list[i] == 1 and prime_num_check(i) == True:
# #         for idx in range(i, N+1, i):
# #             se_joon_num_check_list[idx] = 0

# # print(se_joon_num_check_list)
# print(sum(se_joon_num_check_list)-1)

# import sys
# input = sys.stdin.readline
# n = int(input())
# m = int(input())

# num_list = [0 for _ in range(n+1)]
# for div_num in range(2, n+1):
#     if num_list[div_num] == 0:
#         # for mul_num in range(1, n//div_num+1):
#         #     idx = div_num * mul_num
#         #     num_list[idx] = max(div_num, num_list[idx])
#         for mul_idx in range(div_num, n+1, div_num):
#             if mul_idx % div_num == 0:
#                 num_list[mul_idx] = div_num

# ans = 0
# for num in num_list:
#     if num <= m:
#         ans += 1
# print(ans-1)


# 1380 귀걸이
# import sys
# input = sys.stdin.readline

# scenario_num = 1
# while True:
#     K = int(input())
#     if K == 0: break
#     else:
#         name_list = [input().rstrip() for _ in range(K)]
#         # print(name_list)

#         check_list = [True] * K
#         for _ in range(2*K-1):
#             num, check = map(str, input().split())
#             num = int(num)
#             if check_list[num-1] == True: check_list[num-1] = False
#             else: check_list[num-1] = True
#         # print(check_list)

#         for idx in range(K):
#             if check_list[idx] == False:
#                 print(scenario_num, name_list[idx])
#                 break

#     scenario_num += 1


# #15962 새로운 시작
# print('파이팅!!')

# 2097 조약돌
# import math
# N = int(input())

# if N <= 4: print(4)
# else:
#     sqrt_N = math.sqrt(N)
#     int_sqrt_N = int(sqrt_N)

#     if sqrt_N % 1 == 0 : print(4*(int_sqrt_N-1))
#     elif N <= int_sqrt_N * (int_sqrt_N+1):
#         # 4*(int_sqrt_N-1)+2
#         print(4*int_sqrt_N-2)
#     else:
#         # 4*(int_sqrt_N+1-1)
#         print(4*int_sqrt_N)


# 1331 나이트 투어
# try1 - 실패 - 나이트의 이동경로를 정확히 맞춰가는지 체크해야 함 (앞으로 2칸 옆으로 1칸)
# try2 - 성공

# import sys
# input = sys.stdin.readline

# chess_board_check = [[0] * 6 for _ in range(6)]
# pre_xy_coordinate = list(input().rstrip())
# pre_x, pre_y = ord(pre_xy_coordinate[0])-65, int(pre_xy_coordinate[1])-1
# chess_board_check[pre_x][pre_y] = 1
# start_x, start_y = pre_x, pre_y
# success_check = True
# # xy_coordinate = [list(input().rstrip()) for _ in range(35)]

# for _ in range(35):
#     xy_coordinate = list(input().rstrip())
#     new_x, new_y = ord(xy_coordinate[0])-65, int(xy_coordinate[1])-1
#     # print(xy_coordinate)

#     if ((abs(pre_x - new_x) == 1 and abs(pre_y - new_y) == 2) or\
#         (abs(pre_x - new_x) == 2 and abs(pre_y - new_y) == 1)) and\
#         chess_board_check[new_x][new_y] == 0:
#             chess_board_check[new_x][new_y] = 1
#     else:
#         success_check = False
#         break

#     pre_x, pre_y = new_x, new_y

# if abs(start_x - pre_x) + abs(start_y - pre_y) != 3:
#     success_check = False
# # print(chess_board_check)

# if success_check: print("Valid")
# else: print("Invalid")


# 12865 평범한 배낭
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# dp_list = [[0] * (K+1) for _ in range(N+1)]

# stuff_list = [list(map(int, input().split())) for _ in range(N)]
# stuff_list.insert(0, [0, 0])
# # print(stuff_list)

# for i in range(1, N+1):
#     for j in range(1, K+1):
#         w, v = stuff_list[i][0], stuff_list[i][1]

#         if j < w: dp_list[i][j] = dp_list[i-1][j]
#         else: dp_list[i][j] = max(dp_list[i-1][j], dp_list[i-1][j-w] + v)

# # for i in range(N+1):
# #     print(dp_list[i])
# print(dp_list[N][K])


# 2535 아시아 정보올림피아드
# import sys
# input = sys.stdin.readline

# N = int(input())
# students_list = [list(map(int, input().split())) for _ in range(N)]
# students_list = sorted(students_list, key=lambda x:(-x[2]))
# # for x in range(N):
# #     print(students_list[x])

# if students_list[0][0] == students_list[1][0]:
#     overlapped_country = students_list[0][0]
#     for idx in range(2, N):
#         if students_list[idx][0] != overlapped_country:
#             break
# else:
#     idx = 2

# for country, students_num, score in [students_list[0], students_list[1], students_list[idx]]:
#     print(country, students_num)


# 2740 행렬 곱셈
# 1try - 실패 (IndexError) -> p_C를 잘못 정의했음
# import sys
# input = sys.stdin.readline

# A_N, A_M = map(int, input().split())
# # p_A -> procession_A
# p_A = [list(map(int, input().split())) for _ in range(A_N)]
# # print(p_A)

# B_N, B_M = map(int, input().split())
# p_B = [list(map(int, input().split())) for _ in range(B_N)]
# # print(p_B)

# # p_C = [[0] * A_N for _ in range(B_M)]
# p_C = [[0] * B_M for _ in range(A_N)]
# for x in range(A_N):
#     for y in range(B_M):
#         for k in range(A_M):
#             p_C[x][y] += p_A[x][k] * p_B[k][y]

# for x in range(A_N):
#     print(*p_C[x])

# 16394 홍익대학교
# print(int(input())-1946)

# 1730 판화
# 걸린 시간 40분 ㅡㅡ, 벽에서 넘어가려면 '무시'해야되는 걸 제대로 안 봤음
# import sys
# input = sys.stdin.readline

# N = int(input().rstrip())
# move_list = list(input().rstrip())
# # print(move_list)
# board = [[[False, False] for _ in range(N)] for _ in range(N)]
# # print(board)
# x, y = 0, 0

# for direction in move_list:
#     if (direction == 'L' and y <= 0) or (direction == 'R' and y >= N-1) or\
#         (direction == 'U' and x <= 0) or (direction == 'D' and x >= N-1): continue

#     x_check, y_check = False, False
#     if direction == 'L' or direction == 'R': x_check = True
#     else: y_check = True

#     if x_check: board[x][y][0] = True
#     elif y_check: board[x][y][1] = True

#     if direction == 'L':    y -= 1
#     elif direction == 'R':  y += 1
#     elif direction == 'U':  x -= 1
#     elif direction == 'D':  x += 1
#     # print(direction, x, y)

#     if x_check: board[x][y][0] = True
#     elif y_check: board[x][y][1] = True

# # for x in range(N):
# #     print(board[x])

# for nx in range(N):
#     special_characters_list = [chr(46), chr(124), chr(45), chr(43)]
#     for ny in range(N):
#         if board[nx][ny] == [False, False]:
#             board[nx][ny] = special_characters_list[0]
#         elif board[nx][ny] == [False, True]:
#             board[nx][ny] = special_characters_list[1]
#         elif board[nx][ny] == [True, False]:
#             board[nx][ny] = special_characters_list[2]
#         else: board[nx][ny] = special_characters_list[3]

# for x in range(N):
#     print(*board[x], sep='')

# 1996 지뢰 찾기
# import sys
# input = sys.stdin.readline

# N = int(input())
# mines_list = [list(input().rstrip()) for _ in range(N)]
# map_list = [[0] * N for _ in range(N)]
# # print(mines_list)

# for x in range(N):
#     for y in range(N):
#         if mines_list[x][y] != '.':
#             map_list[x][y] = '*'
#             continue

#         if x == 0: x_list = [0, 1]
#         elif x == N-1: x_list = [-1, 0]
#         else: x_list = [-1, 0, 1]

#         if y == 0: y_list = [0, 1]
#         elif y == N-1: y_list = [-1, 0]
#         else: y_list = [-1, 0, 1]

#         num_of_mines = 0
#         for plus_x in x_list:
#             nx = x + plus_x
#             for plus_y in y_list:
#                 ny = y + plus_y
#                 if mines_list[nx][ny] != '.':
#                     num_of_mines += int(mines_list[nx][ny])

#         if num_of_mines >= 10: map_list[x][y] = 'M'
#         else: map_list[x][y] = num_of_mines

# for x in range(N):
#     print(*map_list[x], sep='')


# 1263 시간 관리
# import sys
# input = sys.stdin.readline

# N = int(input())
# time_list = [list(map(int, input().split())) for _ in range(N)]
# time_list = sorted(time_list, key=lambda x:x[1])
# # print(time_list)

# ans = time_list[0][1] - time_list[0][0]
# # print(ans)
# ans_check = True

# total_time = ans
# for Ti, Si in time_list:
#     total_time += Ti
#     if total_time > Si:
#         ans -= total_time - Si
#         if ans < 0:
#             ans_check = False
#             break
#     print(Ti, Si, total_time, ans)

# if ans_check: print(ans)
# else: print(-1)

"""
반례:
4
1 6
1 6
1 6
1 6
"""

# try - 2, 3
# 35퍼 쯤? 틀렸습니다
# 뭐가 문제지(try2) ㅡ input의 1행부터 Ti가 Si보다 크다면?(try3)
""" 찾았다 반례
2
7 5
1 8
[정답] -1
[출력] -2
"""
# import sys
# input = sys.stdin.readline

# N = int(input())
# time_list = [list(map(int, input().split())) for _ in range(N)]
# time_list = sorted(time_list, key=lambda x:(x[1], x[0]))
# # print(time_list)

# ans = time_list[0][1] - time_list[0][0]
# # print(ans)
# ans_check = True

# total_time = ans
# if ans < 0: print(-1)
# else:
#     for Ti, Si in time_list:
#         total_time += Ti

#         if total_time > Si:
#             time_gab = total_time - Si
#             ans -= time_gab
#             total_time -= time_gab

#             if ans < 0:
#                 ans_check = False
#                 break
#         # print(Ti, total_time, Si, ans)

#     if ans_check: print(ans)
#     else: print(-1)


# 4470 줄번호
# import sys
# input = sys.stdin.readline

# for i in range(1, int(input())+1):
#     print("{0}.".format(i), input(), end='')


# 882/4
# 1000000000000000000
# N, A, L, R = map(int, input().split())
# histogram_check = False
# for_base_L = L

# if L == 0:
#     if A == 0:
#         histogram_check = True
#         print("YES", "0", sep='\n')
#         exit()
#     else:
#         for_base_L += 1
#         # print(for_base_L)

# if not histogram_check:
#     for div_num in range(for_base_L, R+1):
#         if A % div_num == 0:
#             quotient = A // div_num
#             if quotient <= N:
#                 if L >= div_num:
#                     continue
#                 histogram_check = True
#                 break

# if histogram_check:
#     print("YES")
#     for _ in range(quotient):
#         print(div_num, end=' ')
#     print(L)
# else:
#     print("NO")

# 소인수 분해
# import itertools

# N, A, L, R = map(int, input().split())
# histogram_check = False
# for_base_L = L
# div_set = set()

# if L == 0:
#     if A == 0:
#         histogram_check = True
#         print("YES", "0", sep='\n')
#         exit()
#     else:
#         for_base_L += 1
#         # print(for_base_L)

# if not histogram_check:
#     A_list = []
#     div_num = 2
#     tmp_A = A
#     while div_num <= tmp_A//2:
#         while tmp_A % div_num == 0:
#             A_list.append(div_num)
#             tmp_A //= div_num
#         div_num += 1
#     print(A_list)

#     for i in range((len(A_list))+1):
#         for div_num in itertools.combinations(A_list, i):
#             print(div_num)
#             div_val = 1
#             for val in div_num:
#                 div_val *= val
#             print(div_val)
#             if div_val not in div_set:
#                 div_set.add(div_val)

#                 if (L <= div_val <= R) and (A % div_val == 0):
#                     # print("ahha")
#                     quotient = A // div_val
#                     if quotient <= N:
#                         if L >= div_val:
#                             continue
#                         histogram_check = True
#                         break

#         if histogram_check : break

# if histogram_check:
#     print("YES")
#     for _ in range(quotient):
#         print(div_val, end=' ')
#     print(L)
# else:
#     print("NO")


# 2890 카약
# import sys
# input = sys.stdin.readline

# R, C = map(int, input().split())
# kayak_list = [list(input().rstrip()) for _ in range(R)]
# # print(kayak_list)
# rank_list = [[0, 0] for _ in range(R)]

# rank_num = 0
# for y in range(C-2, 0, -1):
#     rank_check = False
#     for x in range(R):
#         # print(x, y)
#         # print(rank_list)
#         if kayak_list[x][y] != '.':
#             if rank_list[x][1] == 0:
#                 rank_list[x][0] = int(kayak_list[x][y])
#                 if rank_check == False:
#                     rank_check = True
#                     rank_num += 1

#                 rank_list[x][1] = rank_num

# rank_list = sorted(rank_list, key=lambda x:(x[0]))
# # print(rank_list)
# for num, rank in rank_list:
#     if num != 0: print(rank)


# 15680 연세대학교
# N = int(input())
# if N == 0: print("YONSEI")
# else: print("Leading the Way to the Future")

# 2891 카약과 강풍
"""
5 3 3
2 3 4
3 4 5
"""
# import sys
# input = sys.stdin.readline

# N, S, R = map(int, input().split())
# broken_team = set(map(int, input().split()))
# extra_team = set(map(int, input().split()))

# broken_team_list = list(broken_team - extra_team)
# extra_team_list = list(extra_team - broken_team)
# # print(broken_team_list)
# # print(extra_team_list)

# broken_kayak_list = [0] * (N+1)
# for idx in broken_team_list:
#     broken_kayak_list[idx] = 1

# for idx in extra_team_list:
#     if broken_kayak_list[idx-1] == 1:
#         broken_kayak_list[idx-1] = 0
#     elif idx < N and broken_kayak_list[idx+1] == 1:
#         broken_kayak_list[idx+1] = 0

# # print(broken_kayak_list)
# print(sum(broken_kayak_list))


# 14645 와이버스 부릉부릉
# 어이가 없네 문제 ㅋㅋㅋ
# print("비와이")


# 3699 주차 빌딩
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     val_h, val_l = map(int, input().split())
#     car_list = [list(map(int, input().split())) for _ in range(val_h)]

#     max_val = 0
#     for x in range(val_h):
#         for y in range(val_l):
#             if max_val < car_list[x][y]: max_val = car_list[x][y]

#     car_idx_list = [[0, 0] for _ in range(max_val)]
#     for h in range(val_h):
#         for i in range(val_l):
#             if car_list[h][i] != -1:
#                 car_idx_list[car_list[h][i]-1] = [h, i]
#     # print(car_idx_list)

#     ans = 0
#     conveyor_belt_index = [0] * val_h
#     for x, y in car_idx_list:
#         gap = abs(conveyor_belt_index[x]-y)
#         ans += (x * 20) + min(gap, val_l - gap) * 5
#         conveyor_belt_index[x] = y
#         # print(ans)
#     print(ans)


# 3711 학번
# try 1
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     g = int(input())
#     g_list = [int(input()) for _ in range(g)]

#     div_num = 1
#     while True:
#         mod_val_list = [0]*10000
#         min_ans_check = True

#         for idx in range(g):
#             if mod_val_list[g_list[idx] % div_num] == 0:
#                 mod_val_list[g_list[idx] % div_num] = 1
#             else:
#                 min_ans_check = False
#             # print(idx, div_num, mod_val_list[:10])

#         if min_ans_check: break
#         else: div_num +=1
#     print(div_num)

# try 2
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     g = int(input())
#     g_list = [int(input()) for _ in range(g)]

#     div_num = 1
#     while True:
#         mod_set = set()
#         min_ans_check = True

#         for idx in range(g):
#             if (g_list[idx] % div_num) not in mod_set:
#                 mod_set.add(g_list[idx] % div_num)
#             else:
#                 min_ans_check = False
#             # print(idx, div_num, mod_val_list[:10])

#         if min_ans_check: break
#         else: div_num +=1
#     print(div_num)


# 16236 아기 상어 ~~~~
# 01:20 ~ 03 : 30
# 해쉬맵 항목 제거로 먹은 물고기 처리 ? no ~
# import sys
# input = sys.stdin.readline
# from queue import deque

# N = int(input())
# g = [list(map(int, input().split())) for _ in range(N)]
# fish_list = [0] * 7
# # num_of_fish = 0
# nx, ny = 0, 0
# for x in range(N):
#     for y in range(N):
#         if g[x][y] not in [0, 9]:
#             fish_list[g[x][y]] += 1
#         elif g[x][y] == 9:
#             g[x][y] = 0
#             nx, ny = x, y
# # print(nx, ny)
# # print(num_of_fish)
# # print(fish_list)

# # up, left, right, down
# inc_x = [-1, 0, 0, 1]
# inc_y = [0, -1, 1, 0]

# day = 0
# body_size = 2
# sum_for_size_up = 0

# while sum(fish_list[:body_size]) != 0:
#     print("fish_list ??!", sum(fish_list[:body_size]))
#     print("haha")
#     # xy_que, fish_que = deque(), deque()
#     xy_que = deque()

#     check_g = [[0]*N for _ in range(N)]
#     check_g[nx][ny] = 1
#     print("now", nx, ny)
#     xy_que.append([nx, ny])
#     print("[_1]", xy_que)

#     fish_found_check = False
#     # while (not fish_found_check) or (sum(fish_list[:body_size]) != 0): # 무한 루프 + check_g 때문에 error
#     while (not fish_found_check):
#         print("fish_list !!?", sum(fish_list[:body_size]))
#         # print()
#         # print("problem?")
#         day += 1
#         for _ in range(len(xy_que)):
#             print("day", day)
#             print("[_2]", xy_que)
#             tmp_x, tmp_y = xy_que.popleft()

#             for idx in range(4):
#                 new_x = tmp_x + inc_x[idx]
#                 new_y = tmp_y + inc_y[idx]
#                 # print(new_x, new_y)
#                 if 0 <= new_x < N and 0 <= new_y < N and check_g[new_x][new_y] == 0 and\
#                     body_size >= g[new_x][new_y]:
#                     # print(new_x, new_y)

#                     check_g[new_x][new_y] = 1
#                     xy_que.append([new_x, new_y])

#                     if 0 < g[new_x][new_y] < body_size:
#                         fish_found_check = True
#                         # g[new_x][new_y] = 0
#                         # fish_list[g[new_x][new_y]] -= 1
#                         fish_list[g[new_x][new_y]] -= 1
#                         g[new_x][new_y] = 0
#                         print(fish_list)
#                         # if g[new_x][new_y] == body_size:
#                         sum_for_size_up += 1
#                         if sum_for_size_up == body_size:
#                             body_size += 1
#                             sum_for_size_up = 0
#                         nx, ny = new_x, new_y
#                         print("size!!", sum_for_size_up, body_size)
#                         break

#                 if fish_found_check: break

#             if fish_found_check: break
#         for x in range(N):
#             print(g[x])
#         print()

# print(day)


# import sys
# input = sys.stdin.readline
# from queue import deque

# N = int(input())
# g = [list(map(int, input().split())) for _ in range(N)]
# fish_list = [0] * 7

# nx, ny = 0, 0
# for x in range(N):
#     for y in range(N):
#         if g[x][y] not in [0, 9]:
#             fish_list[g[x][y]] += 1
#         elif g[x][y] == 9:
#             g[x][y] = 0
#             nx, ny = x, y
# # print(nx, ny)
# # print(fish_list)

# # up, left, right, down
# inc_x = [-1, 0, 0, 1]
# inc_y = [0, -1, 1, 0]

# day = 0
# body_size = 2
# sum_for_size_up = 0
# blocked_check = False

# while sum(fish_list[:body_size]) != 0:
#     xy_que, fish_xy_list = deque(), list()
#     check_g = [[0]*N for _ in range(N)]
#     check_g[nx][ny] = 1
#     xy_que.append([nx, ny])

#     fish_found_check = False
#     blocked_day = 0
#     while (not fish_found_check):
#         # print(xy_que)
#         if not xy_que:
#             day -= blocked_day
#             blocked_check = True
#             break

#         day += 1
#         blocked_day += 1
#         # print("day", day)
#         for _ in range(len(xy_que)):
#             tmp_x, tmp_y = xy_que.popleft()

#             for idx in range(4):
#                 new_x = tmp_x + inc_x[idx]
#                 new_y = tmp_y + inc_y[idx]
#                 if 0 <= new_x < N and 0 <= new_y < N and check_g[new_x][new_y] == 0 and\
#                     body_size >= g[new_x][new_y]:
#                     # print(new_x, new_y)

#                     check_g[new_x][new_y] = 1
#                     xy_que.append([new_x, new_y])

#                     if 0 < g[new_x][new_y] < body_size:
#                         fish_xy_list.append([new_x, new_y])

#         if len(fish_xy_list) != 0:
#             new_x, new_y = sorted(fish_xy_list, key=lambda x:(x[0], x[1]))[0]
#             fish_found_check = True
#             fish_list[g[new_x][new_y]] -= 1
#             g[new_x][new_y] = 0

#             sum_for_size_up += 1
#             if sum_for_size_up == body_size:
#                 body_size += 1
#                 sum_for_size_up = 0

#             nx, ny = new_x, new_y
#             # print("size!!", sum_for_size_up, body_size)

#         # for x in range(N):
#         #     print(g[x])
#         # print()
#     if blocked_check: break

# print(day)

# 14501 퇴사
# 이런 접근인가?
# N = int(input())
# consulting_list = [list(map(int, input().split())) for _ in range(N)]
# consulting_list.insert(0, 0)
# # print(con)
# dp_list = [0] * (N+1)
# print(consulting_list)

# for idx in range(1, N+1):
#     if idx + consulting_list[idx][0] -1 <= N:
#         dp_list[idx + consulting_list[idx][0]-1] = consulting_list[idx][1]
#     print(idx, dp_list)
#     # dp_list[idx] = max(dp_list[idx], dp_list[idx])

# print(dp_list)

# try2
# import sys
# input = sys.stdin.readline

# N = int(input())
# consulting_list = [list(map(int, input().split())) for _ in range(N)]
# consulting_list.insert(0, 0)
# # print(con)
# dp_list = [0] * (N+1)
# # print(consulting_list)

# # max_dp_val = 0
# # # idx_1, idx_2 == standard, sub(-)
# # for idx_1 in range(1, N+1):
# #     # dp_list[idx_1] = max(dp_list[:idx_1])
# #     dp_list[idx_1] = max_dp_val
# #     for idx_2 in range(idx_1):
# #         if idx_2 == consulting_list[idx_1 - idx_2][0] - 1:
# #             dp_list[idx_1] = max(dp_list[idx_1 - idx_2 -1] + consulting_list[idx_1 - idx_2][1], dp_list[idx_1])
# #     max_dp_val = max(max_dp_val, dp_list[idx_1])

# max_dp_val 빼고도 가능
# # idx_1, idx_2 == standard, sub(-)
# for idx_1 in range(1, N+1):
#     # dp_list[idx_1] = max(dp_list[:idx_1])
#     for idx_2 in range(idx_1):
#         if idx_2 == consulting_list[idx_1 - idx_2][0] - 1:
#             dp_list[idx_1] = max(dp_list[idx_1 - idx_2 -1] + consulting_list[idx_1 - idx_2][1], dp_list[idx_1])
#     dp_list[idx_1] = max(dp_list[idx_1-1], dp_list[idx_1])

#     # print(idx_1, dp_list)
# # print(dp_list)
# print(dp_list[N])


# 2828 사과 담기 게임
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# ans = 0
# l, r = 1, M
# for _ in range(int(input())):
#     x = int(input())
#     if x < l:
#         gab = l-x
#         ans += gab
#         l, r = l-gab, r-gab
#     elif x >= r:
#         gab = x-r
#         ans += gab
#         l, r = l+gab, r+gab

# print(ans)


# 1106 호텔
# import sys
# input = sys.stdin.readline

# C, N = map(int, input().split())
# dp_list = [[0]*(C+1) for _ in range(N+1)]
# dp_list[0] = [100000]*(C+1)
# # print(dp_list)

# for x in range(1, N+1):
#     cost, num_of_client = map(int, input().split())
#     for y in range(1, C+1):
#         mul_val = 1
#         while mul_val * num_of_client < y:
#             mul_val += 1

#         dp_list[x][y] = min(dp_list[x-1][y], mul_val * cost)
#         if num_of_client <= y:
#             dp_list[x][y] = min(dp_list[x][y], dp_list[x][y-num_of_client] + cost)

# # for x in range(N+1):
# #     print(dp_list)
# print(dp_list[N][C])


# 9322 철벽 보안 알고리즘
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     dict_1, dict_2 = dict(), dict()
#     # list_1/2 - public_key_1/2
#     list_1 = list(map(str, input().split()))
#     list_2 = list(map(str, input().split()))

#     for idx in range(n):
#         dict_1[list_1[idx]] = idx
#         dict_2[list_2[idx]] = idx

#     idx_list = [[0, 0] for _ in range(n)]
#     for idx in range(n):
#         idx_list[idx] = [dict_1[list_2[idx]], dict_2[list_2[idx]]]
#     # print(idx_list)

#     cryptogram_list = list(map(str, input().split()))
#     # plain_text_list = []*n
#     plain_text_list = [_]*n

#     for idx in range(n):
#         plain_text_list[idx_list[idx][0]] = cryptogram_list[idx_list[idx][1]]
#     print(*plain_text_list)


# 15964 이상한 기호
# A, B = map(int, input().split())
# print((A+B)*(A-B))


# 1072 게임
# 10:45 ~ 11:01
# https://solved.ac/contribute/1072/list
# 1차 부등식으로도 풀 수가 있다고.. (그러네?)

# X, Y = map(int, input().split())
# bot, top = 0, X
# Z = int(Y*100/X)
# # Z = int(Y/X)
# # print(Z)
# ans = 0

# if Z >= 99: print(-1)
# else:
#     while bot <= top:
#         mid = (bot+top)//2
#         # print("mid", mid)
#         if int((Y+mid)*100/(X+mid)) != Z:
#             # print(mid, Y+mid, X+mid, int((Y+mid)*100/(X+mid)))
#             ans = mid
#             top = mid -1
#         else:
#             bot = mid +1

#     print(ans)


# 1963 소수 경로 test
# num_list = [1033 1733 3733 3739 3779 8779 8179]
# def prime_check(num):
#     for div_num in range(3, int(num**(1/2))+1,2):
#         if num % div_num == 0: return False
#     return True

# num_list = list(map(int, input().split()))
# print(num_list)

# for num in num_list:
#     print(prime_check(num))


# 1963 소수경로
# 10:34 ~ 11:23
# 소수 판정, 에라토스테네스의 체, 너비 우선 탐색(BFS)

# import sys
# from queue import deque
# input = sys.stdin.readline

# def prime_check(num):
#     if num == 1: return False
#     elif num == 2: return True
#     elif num % 2 == 0: return False
#     else:
#         # for div_num in range(3, int(num^(1/2))+1, 2):
#         for div_num in range(3, int(num**(1/2))+1, 2):
#             if num % div_num == 0:
#                 return False
#         return True

# # 10:46
# def bfs(que, prime_check_list, num_check_list, target_num):
#     tmp_num, cnt = que.popleft()
#     if tmp_num == target_num:
#         print(cnt)
#         # while que:
#         #     que.popleft()
#         return True
#     # print(list(map(int, str(tmp_num))))
#     num_list = list(map(int, str(tmp_num)))

#     # for num in range(thousands_list):
#     for idx in range(4):
#         tmp_num_list = num_list.copy()
#         place_value = tmp_num // (10**(3-idx))
#         if idx == 0:
#             next_num_list = [i for i in range(1, 10) if i != place_value]
#         else:
#             next_num_list = [i for i in range(10) if i != place_value]

#         for val in next_num_list:
#             tmp_num_list[idx] = val
#             # print(tmp_num_list)

#             next_num = 0
#             for i in range(4):
#                 next_num += tmp_num_list[i] * (10**(3-i))

#             if prime_check_list[next_num] and not num_check_list[next_num]:
#                 num_check_list[next_num] = True
#                 que.append([next_num, cnt+1])

# def solve():
#     # 소수 판정, 에라토스테네스의 체
#     prime_check_list = [True] * 10000
#     for x in range(2, 10000):
#         if prime_check(x):
#             for mul_x in range(x*2, 10000, x):
#                 if prime_check_list[mul_x] == True:
#                     prime_check_list[mul_x] = False
#         # print(x, prime_check_list[x])

#     for _ in range(int(input())):
#         start_num, target_num = map(int, input().split())
#         num_check_list, found_check = [False] * 10000, False
#         que = deque()
#         # print(que)

#         # 너비 우선 탐색(BFS)
#         que.append([start_num, 0])
#         while que:
#             if bfs(que, prime_check_list, num_check_list, target_num):
#                 found_check = True
#             # print(que)
#             # input()
#         if not found_check:
#             print("Impossible")

# solve()


# 15486 퇴사2
# pm 5:10 ~ 5:21
# import sys
# input = sys.stdin.readline

# N = int(input())
# val_list = [list(map(int, input().split())) for _ in range(N)]
# val_list.insert(0, 0)
# dp_list = [0] * (N+1)

# for idx in range(1, N+1):
#     t, p = val_list[idx]
#     if idx + t-1 <= N:
#         dp_list[idx + t-1] = max(dp_list[idx + t-1], dp_list[idx-1] + p)
#     dp_list[idx] = max(dp_list[idx-1], dp_list[idx])
#     # print(idx, dp_list)

# print(dp_list[N])


# 6068 시간 관리하기
# PM 02:46 ~ 02:52
# import sys
# input = sys.stdin.readline

# N = int(input())
# total_T, ans = 0, 1000000
# work_list = [list(map(int, input().split())) for _ in range(N)]
# work_list = sorted(work_list, key=lambda x:x[1])
# work_done_check = True

# for idx in range(N):
#     T_i, S_i = work_list[idx]
#     total_T += T_i
#     # print(T_i, total_T, S_i)
#     if total_T > S_i:
#         work_done_check = False
#         break
#     else:
#         ans = min(S_i - total_T, ans)

# if work_done_check: print(ans)
# else: print(-1)


# 9663 N-Queen
# 6퍼 시간 초과아ㅏ...
# def same_line_check(y_list, x, y):
#     for nx in range(x):
#         ny = y_list[nx]
#         # print(y_list, nx, x, ny, y)
#         if abs(nx-x) == abs(ny-y) :
#             return True
#     return False

# def N_queens(N, y_list, x, n_list):
#     global ans
#     for y in range(N):
#         if y_list[x] == -1 and n_list[y] == 0:
#             if not same_line_check(y_list, x, y):
#                 y_list[x] = y
#                 n_list[y] = 1
#                 # print(y_list, n_list)
#                 if x == (N-1):
#                     ans += 1
#                     y_list[x] = -1
#                     n_list[y] = 0
#                 else:
#                     x += 1
#                     N_queens(N, y_list, x, n_list)
#                     x -= 1
#                     y_list[x] = -1
#                     n_list[y] = 0

# def solve():
#     global ans
#     ans = 0
#     N = int(input())
#     y_list, x = [-1] * N, 0
#     n_list = [0]*(N)
#     N_queens(N, y_list, x, n_list)
#     print(ans)

# solve()

# def N_queens(board, N, y_list, x):
#     global ans
#     for y in range(N):
#         if board[x][y] == 0:
#             y_list[x] = y
#             if x == (N-1):
#                 ans += 1
#             else:
#                 for n in range(N):
#                     board[x][n] += 1
#                     board[n][y] += 1
#                 for nx in range(x):
#                     if y-nx >= 0:
#                         board[x-nx][y-nx] += 1
#                     if y+nx < N:
#                         board[x-nx][y+nx] += 1
#                 for nx in range(N-x):
#                     if y-nx >= 0:
#                         board[x+nx][y-nx] += 1
#                     if y+nx < N:
#                         board[x+nx][y+nx] += 1

#                 x += 1
#                 N_queens(board, N, y_list, x)
#                 x -= 1
#                 y_list[x] = -1

#                 for n in range(N):
#                     board[x][n] -= 1
#                     board[n][y] -= 1
#                 for nx in range(x):
#                     if y-nx >= 0:
#                         board[x-nx][y-nx] -= 1
#                     if y+nx < N:
#                         board[x-nx][y+nx] -= 1
#                 for nx in range(N-x):
#                     if y-nx >= 0:
#                         board[x+nx][y-nx] -= 1
#                     if y+nx < N:
#                         board[x+nx][y+nx] -= 1

# def solve():
#     global ans
#     ans = 0
#     N = int(input())
#     board = [[0]* N for _ in range(N)]
#     y_list, x = [-1] * N, 0
#     N_queens(board, N, y_list, x)
#     print(ans)

# solve()


# 17295 엔드게임 스포일러
# print("Avengers: Endgame")

# 878/1 초콜릿 피라미드
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     R, C = map(int, input().split())
#     sum_white_chocolate, sum_black_chocolate = 0, 0
#     if R > C:
#         R, C = C, R
#     # print("haha", R, C)
#     while R > 1 and C > 1:
#         sum_white_chocolate += (R*C) + (R-1)*(C-1)
#         sum_black_chocolate += (2*R*C) -R -C
#         R -=1
#         C -=1
#     # print(sum_white_chocolate, sum_black_chocolate)

#     if R == 1:
#         if C == 1:
#             sum_white_chocolate += 1
#         while C >= 2:
#             sum_white_chocolate += C
#             sum_black_chocolate += C-1
#             C -= 1

#     print(sum_white_chocolate, sum_black_chocolate)

# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     R, C = map(int, input().split())
#     sum_white_chocolate, sum_black_chocolate = 0, 0
#     if R > C:
#         R, C = C, R
#     # print("haha", R, C)
#     gab = C-R
#     if R >= 2:
#         sum_white_chocolate = 2*(R*(R+1)*((2*R)+(3*gab)+1)//6) -R*C -gab-1
#         sum_black_chocolate = 2*(R*(R+1)*(R-1))//3 + gab*R*R - gab
# print(sum_white_chocolate, sum_black_chocolate)

#     # R 값이 1인 층,
#     if gab == 0:
#         sum_white_chocolate += 1
#     else:
#         sum_white_chocolate += gab+1
#         sum_black_chocolate += gab

#     print(sum_white_chocolate, sum_black_chocolate)


# 878/2 ㅡ 25794 초콜릿과 나이트 게임
# X, Y = map(int, input().split())
# if X == 0 or Y == 0:
#     print(7)
#     k = max(X, Y)
#     print(k, 0)
#     print(k, k)
#     print(k, 2*k)
#     print(0, 2*k)
#     print(-k, 2*k)
#     print(-k, k)
#     print(-0, k)
# elif X == Y:
#     print(7)
#     print(X, Y)
#     print(2*X, 0)
#     print(3*X, -Y)
#     print(2*X, -2*Y)
#     print(X, -3*Y)
#     print(0, -2*Y)
#     print(X, -Y)
# else:
#     print(15)
#     ## X 2  / Y 1
#     x, y = 0, 0
#     x -= Y; y += X
#     print(x, y)
#     x += X; y -= Y
#     print(x, y)

#     x += Y; y += X
#     print(x, y)
#     x += Y; y -= X
#     print(x, y)

#     x += X; y += Y
#     print(x, y)
#     x -= Y; y -= X
#     print(x, y)

#     x += X; y -= Y
#     print(x, y)
#     x -= X; y -= Y
#     print(x, y)

#     x += Y; y -= X
#     print(x, y)
#     x -= X; y += Y
#     print(x, y)

#     x -= Y; y -= X
#     print(x, y)
#     x -= Y; y += X
#     print(x, y)

#     x -= X; y -= Y
#     print(x, y)
#     x += Y; y += X
#     print(x, y)
#     x += X; y += Y
#     print(x, y)


# 878/2
# from queue import deque

# def next_step(que, X, Y):
#     tmp_dict, cnt = que.popleft()
#     # print(pre_list,cnt)
#     # print(tmp_dict[0])
#     nx, ny = tmp_dict[cnt]
#     # print(nx, ny)

#     road_found_check = False
#     tmp_dict_values = tmp_dict.values()
#     # print(tmp_dict_values)

#     for x, y in [[X, Y], [X,-Y], [-X, Y], [-X, -Y], [Y, X], [Y, -X], [-Y, X], [-Y, -X]]:
#         if [nx + x, ny + y] not in tmp_dict_values:
#             road_found_check = True
#             next_dict = tmp_dict.copy()
#             next_dict[cnt+1] = [nx+x, ny+y]
#             que.append([next_dict, cnt+1])

#     if not road_found_check:
#         print(cnt)
#         for x in range(1, cnt+1):
#             print(*tmp_dict[x])
#         que.clear()

# def solve():
#     X, Y = map(int, input().split())
#     tmp_dict = dict({0: [0,0]})
#     # tmp_dict[0] = [0, 0]
#     que = deque([[tmp_dict, 0]])

#     while que:
#         next_step(que, X, Y)

# solve()


# from queue import deque

# def next_step(que, X, Y):
#     pre_list, cnt = que.popleft()
#     nx, ny = pre_list[cnt]
#     # print(nx, ny)

#     road_found_check = False
#     for x, y in [[X, Y], [X,-Y], [-X, Y], [-X, -Y], [Y, X], [Y, -X], [-Y, X], [-Y, -X]]:
#         if [nx + x, ny + y] not in pre_list:
#             road_found_check = True
#             tmp_list = [[0, 0] for _ in range(9)]
#             for k in range(cnt+1):
#                 tmp_list[k] = pre_list[k]
#             tmp_list[cnt+1] = [nx+x, ny+y]
#             # print(tmp_list, pre_list)
#             que.append([tmp_list, cnt+1])
#     # input()

#     if not road_found_check:
#         print(cnt)
#         for x in range(1, cnt+1):
#             print(*pre_list[x])
#         que.clear()

# def solve():
#     X, Y = map(int, input().split())
#     que = deque([[[[0, 0] for _ in range(9)], 0]])

#     while que:
#         next_step(que, X, Y)

# solve()


# 3344 N-Queen
# 새로 짠 N-Queen 코드, 전보다 깔끔하네
# def check_n_queen(N, y_list, y_check_list, x):
#     global ans
#     for y in range(N):
#         if y_check_list[y] == False:
#             y_list[x] = y
#             y_check_list[y] = True

#             safe_place = True
#             # 서로 공격범위에 있는 칸인지 체크
#             for nx in range(x):
#                 ny = y_list[nx]
#                 if abs(y - ny) == abs(x - nx):
#                     safe_place = False
#                     break

#             if safe_place:
#                 if x == (N-1):
#                     ans += 1
#                 else:
#                     check_n_queen(N, y_list, y_check_list, x+1)
#             # BackTracking
#             y_list[x] = -1
#             y_check_list[y] = False

# def solve():
#     global ans
#     ans = 0
#     N = int(input())
#     y_list = [-1]*N
#     y_check_list = [False]*N

#     check_n_queen(N, y_list, y_check_list, 0)
#     print(ans)

# solve()

# 시간 초과, 20부터 시간이 많이 소요됨
# def check_n_queen(N, y_list, x):
#     for y in range(N):
#         y_list[x] = y

#         safe_place = True
#         # 서로 공격범위에 있는 칸인지 체크
#         for nx in range(x):
#             ny = y_list[nx]
#             if y == ny or abs(y - ny) == abs(x - nx):
#                 safe_place = False

#         if safe_place:
#             if x == (N-1):
#                 for idx in range(N):
#                     print(y_list[idx]+1)
#                 exit()
#             else:
#                 check_n_queen(N, y_list, x+1)
#         # BackTracking
#         y_list[x] = -1

# def solve():
#     N = int(input())
#     y_list = [-1]*N

#     check_n_queen(N, y_list, 0)
#     # print(ans)

# solve()


# 1052 물병
# N, K = map(int, input().split())
# if N <= K:
#     print(0)
# else:
#     n_list = [0] * 25
#     idx = 0
#     # binary num (reversed)
#     while N > 0:
#         n_list[idx] = N % 2
#         N //= 2
#         idx += 1
#     # print(n_list)

#     min_idx, ans = 0, 0
#     while True:
#         if sum(n_list) <= K:
#             print(ans)
#             break

#         for idx in range(min_idx, 25):
#             if n_list[idx] == 1:
#                 break
#         n_list[idx] += 1
#         ans += 2**idx
#         while n_list[idx] == 2:
#             n_list[idx] = 0
#             n_list[idx+1] += 1
#             idx += 1
#         min_idx = idx
#         # print(n_list)


# 1374 강의실
# pm 03:00 ~ 03:16
# import sys
# from queue import PriorityQueue
# input = sys.stdin.readline

# N = int(input())
# course_list = [list(map(int, input().split())) for _ in range(N)]
# course_list = sorted(course_list, key=lambda x:(x[1], x[2]))
# # for x in range(N):
# #     print(course_list[x])

# pque = PriorityQueue()
# pque.put(0)

# ans = 1
# for idx in range(N):
#     val_pque_get = pque.get()
#     # print(val_pque_get)
#     if course_list[idx][1] < val_pque_get:
#         ans += 1
#         pque.put(val_pque_get)
#     pque.put(course_list[idx][2])
#     # print(pque.queue)
# print(ans)


# 1379 강의실2
# pm 3:30 ~ 4:32
# import sys
# from queue import PriorityQueue
# input = sys.stdin.readline

# N = int(input())
# course_list = [list(map(int, input().split())) for _ in range(N)]
# course_list = sorted(course_list, key=lambda x:(x[1], x[2]))
# course_room_dict = dict()

# pque = PriorityQueue()
# pque.put((0, 1))
# ans = 1
# for idx in range(N):
#     min_val, room_num  = list(pque.get())
#     if course_list[idx][1] < min_val:
#         ans += 1
#         pque.put((min_val, room_num))
#         room_num = ans

#     course_room_dict[course_list[idx][0]] = room_num
#     pque.put((course_list[idx][2], room_num))

# print(ans)
# for x in range(1, N+1):
#     print(course_room_dict[x])


# 18186 라면 사기 (Large)
# import sys
# input = sys.stdin.readline

# N, B, C = map(int, input().split())
# n_list = list(map(int, input().split()))
# n_list.extend([0])
# # print(n_list)
# cnt_list = [[0]*(N+1) for _ in range(3)]
# cnt_list[0][0] = n_list[0]

# for idx in range(N):
#     min_val = min(cnt_list[0][idx], n_list[idx+1])
#     cnt_list[0][idx] -= min_val
#     cnt_list[1][idx+1] += min_val
#     n_list[idx+1] -= min_val

#     min_val = min(cnt_list[1][idx], n_list[idx+1])
#     cnt_list[1][idx] -= min_val
#     cnt_list[2][idx+1] += min_val
#     n_list[idx+1] -= min_val

#     cnt_list[0][idx+1] = n_list[idx+1]
#     n_list[idx+1] = 0

# for x in range(3):
#     print(cnt_list[x])


# import sys
# input = sys.stdin.readline

# N, B, C = map(int, input().split())
# n_list = list(map(int, input().split()))
# n_list.extend([0])
# # print(n_list)

# if B <= C:
#     print(sum(n_list)*B)
# else:
#     cnt_list = [[0]*(N+1) for _ in range(3)]
#     cnt_list[0][0] = n_list[0]
#     for idx in range(N):
#         for x in range(2):
#             min_val = min(cnt_list[x][idx], n_list[idx+1])
#             cnt_list[x][idx] -= min_val
#             cnt_list[x+1][idx+1] += min_val
#             n_list[idx+1] -= min_val

#         cnt_list[0][idx+1] = n_list[idx+1]
#         n_list[idx+1] = 0

#     # for x in range(3):
#     #     print(cnt_list[x])
#     print(sum(cnt_list[0])*B + sum(cnt_list[1])*(B+C) + sum(cnt_list[2])*(B+2*C))


# 15733 나는 누구인가
# print("I'm Sexy")

# 1051 숫자 정사각형
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# board = [list(map(int, input().rstrip())) for _ in range(N)]
# # print(board)

# ans = 1
# for x in range(N):
#     for y in range(M):
#         dist = 1
#         while True:
#             if x+dist < N and y+dist < M:
#                 if board[x][y] == board[x][y+dist] and\
#                     board[x][y] == board[x+dist][y] and\
#                     board[x][y] == board[x+dist][y+dist]:
#                     ans = max(ans, (dist+1)**2)
#             else:
#                 break
#             dist += 1
# print(ans)

# 20492 세금
# N = int(input())
# print(int(N*0.78), int(N*0.956))

# 18301 Rats
# n1, n2, n12 = map(int, input().split())
# print(int((n1 + 1)*(n2 + 1)/(n12 + 1) - 1))


# 1748 수 이어 쓰기 1
# n = int(input())
# ans = 0
# cmp_num, base_num, num_len = 9, 1, 1
# while True:
#     if n <= cmp_num:
#         ans += (n-base_num+1)*num_len
#         break
#     else:
#         ans += (cmp_num-base_num+1)*num_len
#     cmp_num = cmp_num*10 + 9
#     base_num *= 10
#     num_len += 1
# print(ans)


# 2025 Site Score
# UR, TR, UO, TO = map(int, input().split())
# print(56*UR + 24*TR + 14*UO + 6*TO)

# 1309 동물원
# N = int(input())
# dp = [[1, 0, 0] for _ in range(2)]
# # dp[0] = [1, 1, 1]

# for _ in range(N):
#     dp[1][0] = sum(dp[0])
#     dp[1][1] = dp[1][0] - dp[0][1]
#     dp[1][2] = dp[1][0] - dp[0][2]

#     for idx in range(3):
#         dp[1][idx] = dp[1][idx] % 9901
#         dp[0][idx] = dp[1][idx]

# # print(sum(dp[1]) % 9901)
# print(sum(dp[1]))

# N = int(input())
# dp = [0, 3, 7] + [0]*(N-2)
# for n in range(3, N+1):
#     dp[n] = (2*dp[n-1] + dp[n-2]) % 9901
# print(dp[N])


# 1229 육각수 - 캡틴 이다솜이랑 흡사한 듯
# N = int(input())
# hexagonal_num = [0, 1] + [0] * 711

# val_sub = 1
# for idx in range(2, 711):
#     hexagonal_num[idx] = (idx-1)*6 + hexagonal_num[idx-1] - val_sub
#     val_sub += 2
# # print(hexagonal_num)

# limit_idx = 0
# dp = [6] * (N+1)
# dp[0] = 0
# for idx in range(1, N+1):
#     if idx >= hexagonal_num[limit_idx+1]:
#         limit_idx += 1
#     try:
#         for sub_idx in hexagonal_num[:limit_idx+1]:
#             # print(idx, sub_idx)
#             dp[idx] = min(dp[idx], dp[idx-sub_idx]+1)
#     except IndexError:
#         print("?", idx, limit_idx)
#         input()

# print(dp[N-100:N])


# 22193 Multiply
# input()
# print(int(input())*int(input()))


# 24262 알고리즘 수업 - 알고리즘의 수행 시간 1
# print(1, 0, sep='\n')


# 2410 2의 멱수의 합
# N = int(input())
# dp_list = [0] * (N+1)


# 1351 무한 수열
# def func_add(num_dict, i, p, q):
#     if i not in num_dict:
#         num_dict[i] = func_add(num_dict, i//p, p, q) + func_add(num_dict, i//q, p, q)

#     return num_dict[i]

# N, P, Q = map(int, input().split())
# num_dict = dict({0: 1})

# print(func_add(num_dict, N, P, Q))


# 25314 코딩은 체육과목 입니다
# print("long "*(int(input())//4) + "int")

# 25311 UCPC에서 가장 쉬운 문제 번호는?
# print("A")

# 2670 연속부분최대곱
# import sys
# input = sys.stdin.readline

# N = int(input())
# n_list = [float(input()) for _ in range(N)]
# n_list.insert(0, 0)
# dp_list = [0] * (N+1)

# for idx in range(1, N+1):
#     dp_list[idx] = max(dp_list[idx-1]*n_list[idx], n_list[idx])
# # print(dp_list)
# print(f'{max(dp_list):.3f}')


# pm 01:35 시작
# 894/1 A번 - 안녕 클레오파트라 세상에서 제일가는 포테이토칩
# N, X = map(int, input().split())
# T_list = list(map(int, input().split()))
# idx = 0

# while True:
#     if T_list[idx] < X:
#         print(idx+1)
#         break
#     X += 1
#     idx = (idx+1) % N


# 894/2 B번 - 장인은 도구를 탓하지 않는다
# import sys
# input = sys.stdin.readline

# def factorial(num):
#     return_val = 1
#     for mul_num in range(2, num+1):
#         return_val *= mul_num
#     return return_val

# p_list = sorted([float(input()) for _ in range(10)], reverse=True)
# # print(p_list)

# ans = 1
# for p in p_list[:-1]:
#     ans *= p

# print((ans/factorial(9))*(10**9))


# 894/4
# import sys
# input = sys.stdin.readline

# N = int(input())
# bot, top = 1, N
# ans = 0
# while bot <= top:
#     mid = (bot+top)//2
#     print("?", mid)
#     sys.stdout.flush()

#     returned_val = int(input())
#     if mid == 2*returned_val:
#         ans = mid
#         break
#     elif mid < 2*returned_val:
#         bot = mid+1
#     else: # mid > 2*returned_val
#         top = mid-1

# print("!", ans)


# 894/5 E번 - 수열의 합
# 추후 답 확인
# from collections import defaultdict

# S, T = map(int, input().split())
# total_ans = 0
# total_ans_list = [0] * (T+1)
# for num in range(S, T+1):
#     tmp_num = num
#     div_dict = defaultdict(int)
#     while num % 2 == 0:
#         num //= 2
#         div_dict[2] += 1

#     div_num = 3
#     while num != 1:
#         while num % div_num == 0:
#             num //= div_num
#             div_dict[div_num] += 1
#         div_num += 2
#     # print(div_dict)

#     even_num = 0
#     odd_num = 1
#     for key, val_num in div_dict.items():
#         if key != 2:
#             odd_num *= val_num+1
#         else:
#             even_num += val_num

#     # print(even_num, odd_num)
#     # total_ans += even_num * odd_num - odd_num
#     total_ans += (even_num -1) * odd_num
#     total_ans_list[tmp_num] = (even_num -1) * odd_num

# # print(total_ans)
# print(total_ans_list)


# 1182 부분수열의 합
# import itertools
# N, S = map(int, input().split())
# n_list = list(map(int, input().split()))

# ans = 0
# for n in range(1, N+1):
#     for i in itertools.combinations(n_list, n):
#         if sum(i) == S:
#             ans += 1

# print(ans)


# def backtracking(idx, n_list, bit_list, N, S):
#     global val, ans

#     val += n_list[idx]
#     bit_list[idx] = 1


#     if idx != N-1:
#         backtracking(idx+1, n_list, bit_list, N, S)

#     if val == S and sum(bit_list) != 0:
#         ans += 1
#         print("[1]", idx, bit_list)

#     val -= n_list[idx]
#     bit_list[idx] = 0
#     # if val == S and sum(bit_list) != 0:
#     #     ans += 1
#     #     print("[2]", idx, bit_list)

#     if idx+1 <= N-1:
#         backtracking(idx+1, n_list, bit_list, N, S)

# def solve():
#     N, S = map(int, input().split())
#     n_list = list(map(int, input().split()))
#     global val, ans, bit_list
#     val, ans, bit_list = 0, 0, [0] * N

#     backtracking(0, n_list, bit_list, N, S)
#     print(ans)

# solve()


# def backtracking(idx, n_list, bit, N, S):
#     global val, ans

#     val += n_list[idx]
#     bit += 1

#     if val == S and bit != 0:
#         ans += 1

#     if idx != N-1:
#         backtracking(idx+1, n_list, bit, N, S)

#     val -= n_list[idx]
#     bit -= 1

#     if idx+1 <= N-1:
#         backtracking(idx+1, n_list, bit, N, S)

# def solve():
#     N, S = map(int, input().split())
#     n_list = list(map(int, input().split()))
#     global val, ans
#     val, ans, bit = 0, 0, 0

#     backtracking(0, n_list, bit, N, S)
#     print(ans)

# solve()


# 14499 주사위 굴리기
# N, M, x, y, K = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# cmd = list(map(int, input().split()))
# direction = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
# top, bot, left, right, up, down = [0]*6

# for i in range(K):
#     nx, ny = x + direction[cmd[i]][0], y + direction[cmd[i]][1]
#     # print("cmd(i)", i, cmd[i])
#     # print(nx, ny)
#     if 0 <= nx < N and 0 <= ny < M:
#         tmp_bot = bot
#         if cmd[i] == 1:
#             bot = right
#             right = top
#             top = left
#             left = tmp_bot
#         elif cmd[i] == 2:
#             bot = left
#             left = top
#             top = right
#             right = tmp_bot
#         elif cmd[i] == 3:
#             bot = up
#             up = top
#             top = down
#             down = tmp_bot
#         else:
#             bot = down
#             down = top
#             top = up
#             up = tmp_bot

#         if board[nx][ny] == 0:
#             board[nx][ny] = bot
#         else:
#             bot = board[nx][ny]
#             board[nx][ny] = 0
#         print(top)
#         x, y = nx, ny


# 14888 연산자 끼워넣기
# def backtracking(idx, N, n_list, oprs, oprs_order):
#     global max_val, min_val

#     for i in range(4):
#         # print(idx, i)
#         if oprs[i] != 0:
#             oprs_order[idx] = i
#             oprs[i] -= 1

#             # N-1 까지 가도록
#             if idx != N-2:
#                 backtracking(idx+1, N, n_list, oprs, oprs_order)
#             else: # idx == N-1
#                 # print(oprs_order)
#                 res = n_list[0]
#                 for oprs_idx in range(N-1):
#                     if oprs_order[oprs_idx] == 0:
#                         res += n_list[oprs_idx+1]
#                     elif oprs_order[oprs_idx] == 1:
#                         res -= n_list[oprs_idx+1]
#                     elif oprs_order[oprs_idx] == 2:
#                         res *= n_list[oprs_idx+1]
#                     else: # 3
#                         if res < 0:
#                             res = (-res) // n_list[oprs_idx+1]
#                             res = (-res)
#                         else:
#                             res //= n_list[oprs_idx+1]
#                         # res //= n_list[oprs_idx+1]
#                     # if oprs_order == [1, 3, 0, 0, 2]:
#                     #     print(oprs_idx+1, res)
#                 # print(oprs_order, res)

#                 if max_val < res:
#                     max_val = res
#                 if min_val > res:
#                     min_val = res

#             oprs[i] += 1

# def solve():
#     N = int(input())
#     n_list = list(map(int, input().split()))
#     oprs = list(map(int, input().split())) # operators
#     oprs_order = [-1] * (N-1)

#     global max_val, min_val
#     max_val, min_val = -1e9, 1e9 # -10억, 10억

#     backtracking(0, N, n_list, oprs, oprs_order)
#     print(max_val, min_val, sep='\n')

# solve()


# 17256 달달함이 넘쳐흘러
# a = list(map(int, input().split()))
# c = list(map(int, input().split()))
# print(c[0] - a[2], c[1]//a[1], c[2] - a[0])


# 1068 트리
# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# def dfs(tree, num, target):
#     global ans
#     if num in tree and num != target:
#         for n in tree[num]:
#             if n != target:
#                 # print("n", n)
#                 dfs(tree, n, target)
#     else:
#         ans += 1

# def solve():
#     N = int(input())
#     n_list = list(map(int, input().split()))
#     target = int(input())
#     tree = defaultdict(list)

#     for idx in range(N):
#         if n_list[idx] != -1:
#             tree[n_list[idx]].append(idx)

#     # print(tree)
#     # if target in tree:
#     #     tree.pop(target)
#     # print(tree)

#     global ans
#     ans = 0

#     if target == 0:
#         print(0)
#     else:
#         dfs(tree, 0, target)
#         print(ans)

# solve()


# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# def dfs(tree, num, target):
#     global ans
#     if num in tree and num != target:
#         for n in tree[num]:
#             if n != target:
#                 dfs(tree, n, target)
#             else:
#                 if len(tree[num]) == 1:
#                     ans += 1
#     else:
#         if num != target:
#             ans += 1

# def solve():
#     N = int(input())
#     n_list = list(map(int, input().split()))
#     target = int(input())
#     tree = defaultdict(list)
#     root_node_num = -1

#     for idx in range(N):
#         if n_list[idx] != -1:
#             tree[n_list[idx]].append(idx)
#         else:
#             root_node_num = idx

#     # print(tree)
#     # if target in tree:
#     #     tree.pop(target)
#     # print(tree)

#     global ans
#     ans = 0

#     dfs(tree, root_node_num, target)
#     print(ans)

# solve()


# 24568 Cupcake Party
# print(max(0, 8*int(input())+3*int(input())-28))

# 1855 암호
# K = int(input())
# k_list = list(input())
# # print(k_list)

# if K == 1:
#     print(''.join(k_list))
# else:
#     R = len(k_list) // K
#     # print(r)

#     table = [['_'] * K for _ in range(R)]
#     x, y = -1, 0
#     inc_y = 1
#     k_idx = 0
#     y_count = (K-1)

#     while k_idx < K*R:
#         if x < R and y_count == (K-1):
#             x += 1
#             table[x][y] = k_list[k_idx]
#             k_idx += 1
#             # print("[1]", x, y, k_idx, y_count)
#             y_count = 0

#             if y == 0:
#                 inc_y = 1
#             elif y == (K-1):
#                 inc_y = -1

#         y += inc_y
#         table[x][y] = k_list[k_idx]
#         k_idx += 1
#         y_count += 1
#         # print("[2]", x, y, k_idx, y_count)
#     # print(table)

#     for k in range(K):
#         for r in range(R):
#             print(table[r][k], end='')


# 25372 성택이의 은밀한 비밀
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     if 6 <= len(list(map(str, input().rstrip()))) <= 9:
#         print("yes")
#     else:
#         print("no")

# 25238 가희와 방어율 무시
# a, b = map(int, input().split())
# print(0 if a*(100-b)/100 >= 100 else 1)

# 21598 SciComLove
# print("SciComLove\n"*int(input()))

# 2302 극장 좌석
"""
2
1
1
2 -> 1
"""

# 1st code
# N = int(input())
# M = int(input())
# m_set = set({int(input()) for _ in range(M)})
# dp = [[0]*2 for _ in range(N+1)]
# dp[0] = [1, 0]
# dp[1] = [1, 0]
# # print(m_set)

# ans = 1
# for x in range(1, N+1):
#     if x in m_set:
#         ans *= sum(dp[x-1])
#         dp[x-1] = [0, 0]
#         dp[x] = [1, 0]
#         # dp[x+1]이 있을 경우, [1, 0] 값이 됨
#     else:
#         # [x][0] 은 이 자리를 x가 그대로 차지하는 경우
#         # [x][1] 은 [x-1] 자리의 값과 cross 하는 경우
#         dp[x][0] = sum(dp[x-1])
#         if x >= 2:
#             dp[x][1] = sum(dp[x-2])

# ans *= sum(dp[N])
# print(ans)

# # for x in range(N+1):
# #     print(x, dp[x])

# 2nd code
# N = int(input())
# M = int(input())
# m_set = set({int(input()) for _ in range(M)})

# ans = 1
# dp = [0]*(N+1)
# dp[0:2] = [0 if 1 in m_set else 1, 1]

# ans = 1
# for x in range(2, N+1):
#     if x in m_set:
#         ans *= dp[x-1]
#         dp[x-1] = 0
#         dp[x] = 1
#     else:
#         dp[x] = dp[x-1] + dp[x-2]
# ans *= dp[N]

# print(ans)

# 21300 Bottle Return
# print(sum(list(map(int, input().split())))*5)

# 11942 고려대는 사랑입니다
# print("고려대학교")

# 24736 Football Scoring
# for _ in range(2):
#     T, F, S, P, C = map(int, input().split())
#     print(6*T + 3*F + 2*S + 1*P + 2*C)


# APC
# 902/1
# N = int(input())
# n_list = list(map(str, input().split()))
# n_dict = dict({'B':1, 'S':2, 'G':3, 'P':4, 'D':5})
# pre_problem = n_list[0]
# # print(n_list)

# idx_1, idx_2 = 0, 0
# idx_sum = 0
# for i in range(1, N):
#     if (n_dict[n_list[i-1][0]] > n_dict[n_list[i][0]]) or\
#         (n_dict[n_list[i-1][0]] == n_dict[n_list[i][0]] and int(n_list[i-1][1:]) < int(n_list[i][1:])):
#             if idx_sum == 0:
#                 idx_1 = i-1
#                 idx_2 = i
#                 idx_sum += 1
#             else:
#                 idx_2 = i

# print(idx_1, idx_2)


# 6810
# ans = 91
# mul_num = 1
# for _ in range(3):
#     ans += int(input()) * mul_num

#     if mul_num == 1:
#         mul_num = 3
#     else:
#         mul_num = 1
# print("The 1-3-sum is", ans)


# 16170 오늘의 날짜는?
# print(2022, 11, 14, sep='\n')


# 14581 팬들에게 둘러싸인 홍준
# print(f':fan::fan::fan:\n\
# :fan::{input()}::fan:\n\
# :fan::fan::fan:')


# 5339 콜센터
# print("\
#      /~\\\n\
#     ( oo|\n\
#     _\=/_\n\
#    /  _  \\\n\
#   //|/.\|\\\\\n\
#  ||  \ /  ||\n\
# ============\n\
# |          |\n\
# |          |\n\
# |          |")


# 25083 새싹
# print("\
#          ,r'\"7\n\
#  r`-_   ,'  ,/\n\
#   \\. \". L_r\'\n\
#    `~\\/\n\
#       |\n\
#       |")

# print("\
#          ,r'\"7\n\
# r`-_   ,'  ,/\n\
#  \. \". L_r'\n\
#    `~\/\n\
#       |\n\
#       |")

# 14889 스타트와 링크
# import sys
# input = sys.stdin.readline

# def backtracking(S, idx, cnt, N, team_check):
#     global min_gap

#     # 4명의 사람이 있으면 idx 2까지, 6명이면 3까지
#     # i번째에 대해서 team_check 1
#     # cnt를 재고, i +1 < N으로 backtracking 이 더 가능할 경우 진행 (재귀)
#     for i in range(idx, N):
#         cnt += 1
#         team_check[i] = 1
#         if cnt != (N//2):
#             if i + 1 < N:
#                 backtracking(S, i+1, cnt, N, team_check)

#         else: # cnt == N//2: 즉, N//2 명의 팀이 충족된 경우
#             # print(*team_check)
#             start_team = [k for k in range(N) if team_check[k] == 1]
#             link_team = [k for k in range(N) if team_check[k] == 0]
#             # print(start_team, link_team)

#             start_team_sum, link_team_sum = 0, 0
#             for a in range(N//2):
#                 for b in range(a, N//2):
#                     start_team_sum += S[start_team[a]][start_team[b]] + S[start_team[b]][start_team[a]]
#                     link_team_sum += S[link_team[a]][link_team[b]] + S[link_team[b]][link_team[a]]
#             # print(start_team_sum, link_team_sum)

#             if min_gap > abs(start_team_sum - link_team_sum):
#                 min_gap = abs(start_team_sum - link_team_sum)

#         cnt -= 1
#         team_check[i] = 0

# def solve():
#     N = int(input())
#     S = [list(map(int, input().split())) for _ in range(N)]
#     global min_gap
#     min_gap = 2000

#     team_check = [0] * N
#     backtracking(S, 0, 0, N, team_check)
#     print(min_gap)

# solve()


# 13458 시험 감독
# import sys
# input = sys.stdin.readline

# N = int(input())
# A = list(map(int, input().split()))
# B, C = map(int, input().split())

# ans = 0
# for a in A:
#     # 총감독관 1명
#     a -= B
#     ans += 1

#     # 부감독관이 필요한 경우
#     if a > 0:
#         ans += a//C
#         if a % C != 0:
#             ans += 1
# print(ans)


# 16099 Larger Sport Facility
# N = int(input())
# for _ in range(N):
#     lt, wt, le, we = map(int, input().split())
#     val = lt*wt - le*we
#     if val > 0:
#         print("TelecomParisTech")
#     elif val < 0:
#         print("Eurecom")
#     else:
#         print("Tie")

# 24078 余り (Remainder)
# print(int(input()) % 21)

# 24082 立方体 (Cube)
# print(int(input())**3)

# 24086 身長 (Height)
# h = [int(input()) for _ in range(2)]
# print(abs(h[0]-h[1]))

# 2845 파티가 끝나고 난 뒤
# L, P = map(int, input().split())
# written_num = list(map(int, input().split()))
# for wn in written_num:
#     print(wn - L*P, end=' ')


# 14489 치킨 두 마리(...)
# A, B = map(int, input().split())
# C = int(input())

# if (A+B) >= 2*C:
#     print((A+B) - 2*C)
# else:
#     print(A+B)

# 3765 Celebrity jeopardy
# import sys
# lines = sys.stdin.readlines()

# for line in lines:
#     print(line, end = '')


# 5524 입실 관리
# for _ in range(int(input())):
#     string = list(input())
#     for s in string:
#         print(s.lower(), end='')
#     print()

# 2555
# print("3/19")


# 5893 17배
# mul = 1
# ans = 0
# for n in list(map(int, input()))[::-1]:
#     ans += n * mul
#     mul *= 2
# # print(ans)
# ans *= 17

# idx = 0
# ans_num = []
# while ans > 0:
#     ans_num.append(ans % 2)
#     ans //= 2
# print(*ans_num[::-1], sep='')

# print("{0:b}".format(int(f'0b{int(input())}', 2)*17))


# 10101 삼각형 외우기
# t = sorted([int(input()) for _ in range(3)])

# if sum(t) == 180:
#     if t[0] == t[1] or t[1] == t[2]:
#         if t[1] == 60:
#             print("Equilateral")
#         else:
#             print("Isosceles")
#     else:
#         print("Scalene")

# else:
#     print("Error")


# 5554 심부름 가는 길
# t = sum(int(input()) for _ in range(4))
# print(t // 60, t % 60, sep='\n')


# 5596 시험 점수
# s = [list(map(int, input().split())) for _ in range(2)]
# print(max(sum(s[0]), sum(s[1])))

# 4299 AFC 윔블던
# a, b = map(int, input().split())
# if a < b or (a+b) % 2 != 0:
#     print(-1)
# else:
#     x = (a+b)//2
#     y = (a-b)//2
#     print(x, y)

# 6749 Next in line
# c = list(int(input()) for _ in range(2))
# print(2*c[1]-c[0])


# 5928 Contest Timing
# D, H, M = map(int, input().split())
# ans = (D-11)*1440 + (H-11)*60 + (M-11)
# print(ans if ans >= 0 else -1)


# 10768 특별한 날
# n = list(int(input()) for _ in range(2))

# if n[0] < 2:
#     print("Before")
# elif n[0] > 2:
#     print("After")
# else:
#     if n[1] < 18:
#         print("Before")
#     elif n[1] > 18:
#         print("After")
#     else:
#         print("Special")


# 6887 Squares
# N = int(input())
# print(f'The largest square has side length {int(N**(1/2))}.')


# 5575 타임카드
# for _ in range(3):
#     sh, sm, ss, fh, fm, fs = map(int, input().split())
#     ans = (fh-sh)*3600 + (fm-sm)*60 + (fs-ss)
#     print(ans//3600, (ans%3600)//60, (ans%3600)%60)


# 11945 뜨거운 붕어빵
# N, M = map(int, input().split())
# for _ in range(N):
#     print(*list(input())[::-1], sep='')


# 13118 뉴턴과 사과
# p = list(map(int, input().split()))
# x, y, r = map(int, input().split())

# ans = 0
# for idx in range(len(p)):
#     if p[idx] == x:
#         ans = idx+1
#         break

# print(ans)


# 14924 폰 노이만과 파리
# S, T, D = map(int, input().split())
# print(T*(D//(2*S)))


# 14470 전자레인지
# n = list(int(input()) for _ in range(5))
# print((-n[0])*n[2] + n[3] + n[1]*n[4] if n[0] < 0 else (n[1]-n[0])*n[4])


# 15873 공백 없는 A+B
# s = int(input())
# if s % 10 == 0:
#     print(s//100 + 10)
# else:
#     print(s//10 + s%10)

# print(list(map(int, input())))


# 15700 타일 채우기 4
# N, M = map(int, input().split())
# print(N*M//2)


# 16204 카드 뽑기
# N, M, K = map(int, input().split())
# print(min(M, K) + min(N-M, N-K))


# 1로 만들기 코드 수정
# n = int(input())
# dp = [0, 0, 1, 1] + [int(1e6)+1]*(n-3)

# for idx in range(4, n+1):
#     if idx % 3 == 0: dp[idx] = min(dp[idx//3]+1, dp[idx])
#     if idx % 2 == 0: dp[idx] = min(dp[idx//2]+1, dp[idx])
#     dp[idx] = min(dp[idx], dp[idx-1]+1)

# print(dp[n])


# 26566 Pizza
# import sys
# input = sys.stdin.readline
# import math

# for _ in range(int(input())):
#     A1, P1 = map(int, input().split())
#     R1, P2 = map(int, input().split())
#     pi = math.pi

#     if A1 // P1 < R1*(pi**2)//P2:
#         print("Whole pizza")
#     else:
#         print("Slice of pizza")


# 1325 효율적인 해킹
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**4)
# from collections import defaultdict

# def dfs(g, u, visited, sum_cnt):
#     visited[u] = True
#     sum_cnt += 1
#     for v in g[u]:
#         if not visited[v]:
#             sum_cnt = dfs(g, v, visited, sum_cnt)

#     return sum_cnt

# def solve():
#     N, M = map(int, input().split())
#     g = defaultdict(list)
#     for _ in range(M):
#         A, B = map(int, input().split())
#         g[B].append(A)
#     # print(g)

#     ans = defaultdict(int)
#     for i in range(1, N+1):
#         visited = [False] * (N+1)
#         # print(dfs(g, i, visited, 0))
#         ans[i] = dfs(g, i, visited, 0)
#         # print(i, visited)

#     ans = sorted(ans.items(), key=lambda x:(-x[1], x[0]))
#     print(ans)

#     for key, val in ans:
#         if val == ans[0][1]:
#             print(key, end=' ')
#         else:
#             break

# solve()

"""
7 8
2 1
3 2
1 3
4 2
5 4
6 4
1 7
3 7
"""


# dfs
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**5)

# def dfs(g, u, visited, sum_cnt):
#     visited[u] = True
#     sum_cnt += 1
#     for v in g[u]:
#         if not visited[v]:
#             sum_cnt = dfs(g, v, visited, sum_cnt)

#     return sum_cnt

# def solve():
#     N, M = map(int, input().split())
#     g = [list() for _ in range(N+1)]
#     for _ in range(M):
#         A, B = map(int, input().split())
#         g[B].append(A)
#     # print(g)

#     ans = [0] * (N+1)
#     for i in range(1, N+1):
#         visited = [False] * (N+1)
#         ans[i] = dfs(g, i, visited, 0)
#     # print(ans)

#     max_val = max(ans)
#     for i in range(1, N+1):
#         if ans[i] == max_val:
#             print(i, end=' ')

# solve()


# bfs
# import sys
# input = sys.stdin.readline
# from collections import deque

# def bfs(g, u, visited):
#     visited[u] = True
#     q = deque([u])

#     cnt = 1
#     while q:
#         v = q.popleft()
#         for u in g[v]:
#             if not visited[u]:
#                 visited[u] = True
#                 cnt += 1
#                 q.append(u)

#     return cnt

# def solve():
#     N, M = map(int, input().split())
#     g = [list() for _ in range(N+1)]
#     for _ in range(M):
#         A, B = map(int, input().split())
#         g[B].append(A)
#     # print(g)

#     ans = [0] * (N+1)
#     for i in range(1, N+1):
#         ans[i] = bfs(g, i, [False] * (N+1))
#     # print(ans)

#     max_val = max(ans)
#     for i in range(1, N+1):
#         if ans[i] == max_val:
#             print(i, end=' ')

# solve()


# 싸이클 처리가 안 됨
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**5)
# from collections import defaultdict

# def dfs(g, v, child, visited, group):
#     # 처음 가는 경우 or child가 없는 경우
#     if not visited[v]:
#         for u in g[v]:
#             # print("u", u)
#             visited[u] = True
#             dfs(g, u, child, visited)
#             child[v] += child[u]

# def solve():
#     N, M = map(int, input().split())
#     g = defaultdict(list)
#     for _ in range(M):
#         A, B = map(int, input().split())
#         g[B].append(A)
#     # print("g", g)

#     visited = [False]*(N+1)
#     child = [1]*(N+1)

#     for v in range(1, N+1):
#         # print(v)
#         dfs(g, v, child, visited, set())

#     max_val = max(child)
#     # print("ans", end=' ')
#     for v in range(1, N+1):
#         if child[v] == max_val:
#             print(v, end=' ')

# solve()


# 12852 1로 만들기2
# from collections import defaultdict
# from collections import deque

# def recursion(dp2, n):
#     if dp2[n] != 0:
#         if dp2[n] == 1:
#             recursion(dp2, n+1)
#         else:
#             recursion(dp2, n*dp2[n])

#     print(n, end = ' ')

# def solve():
#     N = int(input())
#     # cnt dp, 역 계산 dp
#     dp1 = defaultdict(int)
#     dp2 = defaultdict(int)
#     init_val = int(1e6)
#     dp1[1] = init_val

#     que = deque()
#     que.append([N, 0, 0])

#     while que:
#         if dp1[1] != init_val:
#             break

#         for _ in range(len(que)):
#             n, cnt, k = que.popleft()
#             if dp1[n] == 0 or dp1[n] > cnt:
#                 dp1[n] = cnt
#                 dp2[n] = k

#             if dp1[1] != init_val:
#                 break

#             if n % 3 == 0:
#                 que.append([n//3, cnt+1, 3])

#             if n % 2 == 0:
#                 que.append([n//2, cnt+1, 2])

#             que.append([n-1, cnt+1, 1])

#     print(dp1[1])
#     # print(dp2)

#     recursion(dp2, 1)

# solve()


# 16199 나이 계산하기
# bidth, standard
# by, bm, bd = map(int, input().split())
# sy, sm, sd = map(int, input().split())

# # 만 나이
# age = (sy-by-1)
# if sm > bm or (sm == bm and sd >= bd):
#     age += 1
# print(age)

# # 세는 나이, 연 나이
# print(sy-by+1)
# print(sy-by)


# 25494 단순한 문제 (Small)
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     a, b, c = map(int, input().split())

#     ans = 0
#     for x in range(1, a+1):
#         for y in range(1, b+1):
#             for z in range(1, c+1):
#                 if (x%y) == (y%z) == (z%x):
#                     ans += 1
#     print(ans)


# 1474 밑 줄
# 14:15 ~ 14:34
# import sys
# input = sys.stdin.readline
# from collections import deque
# import string

# N, M = map(int, input().split())
# # rstrip()
# words = [list(input().rstrip()) for _ in range(N)]
# underbars = M
# lower_case = deque()
# upper_case = deque()

# for idx in range(len(words)):
#     w = words[idx]
#     underbars -= len(w)
#     if idx != 0:
#         if w[0] in string.ascii_lowercase:
#             lower_case.append(idx)
#         else:
#             upper_case.append(idx)
# # print(underbars)

# spaces = [underbars//(N-1)]*(N-1)
# # print(spaces)
# underbars %= (N-1)
# # print(underbars)

# while lower_case and (underbars > 0):
#     spaces[lower_case.popleft()-1] += 1
#     underbars -= 1

# while upper_case and (underbars > 0):
#     spaces[upper_case.pop()-1] += 1
#     underbars -= 1

# for idx in range(N):
#     print(*words[idx], sep='', end='')
#     if idx != N-1:
#         print(spaces[idx]*'_', end='')


# 17362 수학은 체육과목 입니다 2
# pm 02:09 ~ 02:12
# n = int(input())
# n = (n-1) % 8
# ans = [1, 2, 3, 4, 5, 4, 3, 2]
# print(ans[n])


# 이중 우선순위 큐
"""
1
3
I 10
I 10
D 1
"""
# import sys
# input = sys.stdin.readline
# from heapq import heappop, heappush

# for _ in range(int(input())):
#     k = 0
#     min_heap = []
#     max_heap = []
#     popped_heap = []

#     for _ in range(int(input())):
#         cmd, n = map(str, input().rstrip().split())
#         n = int(n)

#         if cmd[0] == 'I':
#             k += 1
#             heappush(min_heap, n)
#             heappush(max_heap, (-n, n))

#         else: #'D'
#             if k > 0:
#                 k -= 1

#                 if n == -1:
#                     heappop(min_heap)
#                 else:
#                     heappush(popped_heap, heappop(max_heap)[1])
#                 # print(popped_heap)

#                 while min_heap and popped_heap and min_heap[0] == popped_heap[0]:
#                     heappop(min_heap)
#                     heappop(popped_heap)

#     if k == 0:
#         print("EMPTY")
#     else:
#         min_val = min_heap[0]
#         max_val = min_heap[0]
#         # print("min_heap", min_heap)
#         while min_heap:
#             val = heappop(min_heap)
#             # print("val", val, popped_heap[0])
#             if popped_heap and val == popped_heap[0]:
#                 heappop(popped_heap)
#             else:
#                 max_val = val

#         print(max_val, min_val)


# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     ans = []
#     for _ in range(int(input())):
#         cmd, n = map(str, input().rstrip().split())
#         n = int(n)

#         if cmd == 'I':
#             ans.append(n)
#         else: #'D'
#             if ans:
#                 ans = sorted(ans, reverse=(True if n == -1 else False))
#                 ans.pop()

#     if not ans:
#         print("EMPTY")
#     else:
#         ans = sorted(ans)
#         print(ans[-1], ans[0])


# 1 n_largest, heapify → timeover
# 2 remove → timeover
# 3 안 쓰고

# 1, 2
# import sys
# input = sys.stdin.readline
# from heapq import heappush, heappop, nlargest, heapify

# for _ in range(int(input())):
#     heap = []
#     for _ in range(int(input())):
#         cmd, n = map(str, input().rstrip().split())
#         n = int(n)

#         if cmd == 'I':
#             heappush(heap, n)
#         else:
#             if heap:
#                 if n == -1:
#                     heappop(heap)
#                 else:
#                     # 1
#                     # heap = nlargest(len(heap), heap)[1:]
#                     # heapify(heap)
#                     # 2
#                     heap.remove(nlargest(1, heap)[0])

#     # print(heap)
#     print(f'{max(heap)} {heap[0]}' if heap else "EMPTY")

# 2
# import sys
# input = sys.stdin.readline
# from heapq import heappop, heappush

# for _ in range(int(input())):
#     min_heap = []
#     max_heap = []

#     k = int(input())
#     executed_kk = [False] * (k)

#     for _ in range(k):
#         cmd, n = map(str, input().rstrip().split())
#         n = int(n)

#         if cmd == 'I':
#             heappush(min_heap, n)
#             heappush(max_heap, -n)
#         else:
#             if min_heap: # if min_heap and max_heap
#             # print(executed_kk)
#                 if n == 1:
#                     min_heap.remove(-heappop(max_heap))
#                 else:
#                     max_heap.remove(-heappop(min_heap))

#     print(f'{-max_heap[0]} {min_heap[0]}' if min_heap else "EMPTY")

# 3 - PriorityQueue
# import sys
# input = sys.stdin.readline
# from queue import PriorityQueue

# for _ in range(int(input())):
#     min_pq = PriorityQueue()
#     max_pq = PriorityQueue()

#     k = int(input())
#     executed_kk = [False] * (k)

#     for kk in range(k):
#         cmd, n = map(str, input().rstrip().split())
#         n = int(n)

#         if cmd == 'I':
#             min_pq.put((n, kk))
#             max_pq.put((-n, kk))
#         else:
#             # print(executed_kk)
#             if n == -1:
#                 while min_pq.queue and executed_kk[min_pq.queue[0][1]]:
#                     min_pq.get()
#                 if min_pq.queue:
#                     executed_kk[min_pq.get()[1]] = True
#             else:
#                 while max_pq.queue and executed_kk[max_pq.queue[0][1]]:
#                     max_pq.get()
#                 if max_pq.queue:
#                     executed_kk[max_pq.get()[1]] = True

#     while min_pq.queue and executed_kk[min_pq.queue[0][1]]: min_pq.get()
#     while max_pq.queue and executed_kk[max_pq.queue[0][1]]: max_pq.get()
#     print(f'{-max_pq.queue[0][0]} {min_pq.queue[0][0]}' if min_pq.queue and max_pq.queue else "EMPTY")


# 3 - heapq
# import sys
# input = sys.stdin.readline
# from heapq import heappop, heappush

# for _ in range(int(input())):
#     min_pq = []
#     max_pq = []

#     k = int(input())
#     executed_kk = [False] * (k)

#     for kk in range(k):
#         cmd, n = map(str, input().rstrip().split())
#         n = int(n)

#         if cmd == 'I':
#             heappush(min_pq, (n, kk))
#             heappush(max_pq, (-n, kk))
#         else:
#             # print(executed_kk)
#             if n == -1:
#                 while min_pq and executed_kk[min_pq[0][1]]:
#                     heappop(min_pq)
#                 if min_pq:
#                     executed_kk[heappop(min_pq)[1]] = True
#             else:
#                 while max_pq and executed_kk[max_pq[0][1]]:
#                     heappop(max_pq)
#                 if max_pq:
#                     executed_kk[heappop(max_pq)[1]] = True

#     while min_pq and executed_kk[min_pq[0][1]]: heappop(min_pq)
#     while max_pq and executed_kk[max_pq[0][1]]: heappop(max_pq)
#     print(f'{-max_pq[0][0]} {min_pq[0][0]}' if min_pq and max_pq else "EMPTY")


# 1039 교환
# pm 03:51 ~ 04:16
# 런타임 에러 (IndexError)
"""
5 1
[ans] -1
[출력] IndexError → not que 일 때도 ans = -1 되게 조정
"""
# import itertools
# from collections import deque

# def return_num(num_list:list):
#     mul_val = 1
#     return_val = 0
#     while num_list:
#         return_val += num_list.pop() * mul_val
#         mul_val *= 10
#     return return_val

# def solve():
#     N, K = map(int, input().split())
#     N = list(map(int, str(N)))
#     # print(N)
#     len_N = len(N)

#     que = deque()
#     que.append(N)

#     k = 0
#     while que and k < K:
#         # print("~~~~~", k)
#         num_set = set()
#         for _ in range(len(que)):
#             n = que.popleft()
#             # print(n)

#             for idxs in itertools.combinations([i for i in range(0, len_N)], 2):
#                 next_n = n[:]
#                 # print(idxs)
#                 next_n[idxs[0]], next_n[idxs[1]] = next_n[idxs[1]], next_n[idxs[0]]
#                 if next_n[0] != 0:
#                     # print("next_n", next_n)
#                     tuple_next_n = tuple(next_n)
#                     if tuple_next_n not in num_set:
#                         num_set.add(tuple_next_n)
#                         que.append(next_n)
#         # print(num_set, que)
#         k += 1

#     # print(k, que)
#     if k != K or not que:
#         ans = -1
#     else: # k == K and que
#         que = list(que)
#         for idx in range(len(que)):
#             que[idx] = return_num(que[idx])
#         ans = sorted(que)[-1]
#     print(ans)

# solve()

"""
7951235 3
[ans]   9755321
[출력]  9753125
"""
# pm 04:20 ~ 05:58
#
# from collections import deque

# # 0, len_N, 1, 2, [], []
# def return_idxs(idx, len_N, k, K, total_idxs:list, now_idxs:list):

#     now_idxs.append(idx)
#     # print(now_idxs)

#     # 숫자를 더 넣을 수 있으면
#     if idx+1 < len_N and k < K:
#         return_idxs(idx+1, len_N, k+1, K, total_idxs, now_idxs)
#     elif k == K:
#         # total_idxs.append(now_idxs)
#         total_idxs.append(now_idxs[:])
#         # print(total_idxs)

#     now_idxs.pop()
#     k -= 1

#     if idx+1 < len_N: # and k < K # and (K-k) >= (len_N-1 - (idx+1))
#         # print(total_idxs, now_idxs, idx+1)
#         return_idxs(idx+1, len_N, k+1, K, total_idxs, now_idxs)

#     # print("final_total_idxs", total_idxs)
#     return total_idxs

# def return_num(num_list:list):
#     mul_val = 1
#     return_val = 0
#     while num_list:
#         return_val += num_list.pop() * mul_val
#         mul_val *= 10
#     return return_val

# def solve():
#     N, K = map(int, input().split())
#     N = list(map(int, str(N)))
#     # print(N)
#     len_N = len(N)

#     que = deque()
#     que.append(N)

#     k = 0
#     while que and k < K:
#         # print("~~~~~", k)
#         num_set = set()
#         for _ in range(len(que)):
#             n = que.popleft()
#             # print(n)

#             for idxs in return_idxs(0, len_N, 1, 2, [], []):
#                 # print(idxs)
#                 next_n = n[:]
#                 next_n[idxs[0]], next_n[idxs[1]] = next_n[idxs[1]], next_n[idxs[0]]
#                 if next_n[0] != 0:
#                     # print("next_n", next_n)
#                     tuple_next_n = tuple(next_n)
#                     if tuple_next_n not in num_set:
#                         num_set.add(tuple_next_n)
#                         que.append(next_n)
#         # print(num_set, que)
#         k += 1

#     # print(k, que)
#     if k != K or not que:
#         ans = -1
#     else: # k == K and que
#         que = list(que)
#         for idx in range(len(que)):
#             que[idx] = return_num(que[idx])
#         ans = sorted(que)[-1]
#     print(ans)

# solve()


# 24883 자동 완성
# print("Naver D2" if input() in ["N", "n"] else "Naver Whale")

# 1197 최소 스패닝 트리
# import sys
# input = sys.stdin.readline
# from heapq import heappush, heappop
# from collections import defaultdict
# from collections import deque

# V, E = map(int, input().split())
# g = defaultdict(list)
# for _ in range(E):
#     A, B, C = map(int, input().split())
#     g[A].append([C, B])
#     g[B].append([C, A])
# # print(g)

# V_set = set()
# V_set.add(1)
# heap = []
# que = deque()
# que.append(1)

# ans = 0
# for _ in range(V-1):
#     u = que.popleft()
#     for v in g[u]:
#         heappush(heap, v)

#     # 가장 가중치가 낮은 간선 중에 이미 방문한 점들을 연결하는 간선은 pop
#     while heap[0][1] in V_set:
#         heappop(heap)

#     # 가장 가중치가 낮은 간선의 가중치와 정점 번호에 대해서
#     val, v = heappop(heap)
#     ans += val
#     que.append(v)
#     V_set.add(v)

# print(ans)


# 23795 사장님 도박은 재미로 하셔야 합니다
# N = int(input())
# ans = 0
# while N != -1:
#     ans += N
#     N = int(input())

# print(ans)


# 25704 출석 이벤트
# N = int(input())
# P = int(input())

# discount = 0
# if N >= 5:
#     discount = max(discount, 500)
# if N >= 10:
#     discount = max(discount, P*0.1)
# if N >= 15:
#     discount = max(discount, 2000)
# if N >= 20:
#     discount = max(discount, P*0.25)

# print(max(int(P-discount), 0))


# 14264 정육각형과 삼각형
# import math

# L = int(input())
# print(L*math.sin(math.pi/6)*L*math.cos(math.pi/6))


# 20040 사이클 게임
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     # else:
#     #     return x
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# def solve():
#     parent = defaultdict(int)
#     n, m = map(int, input().split())

#     for i in range(n):
#         parent[i] = i
#     # print(parent)

#     cycle = False
#     for i in range(m):
#         a, b = map(int, input().split())
#         if find_parent(parent, a) == find_parent(parent, b):
#             cycle = True
#             break
#         else:
#             union_parent(parent, a, b)
#         # print(i, parent)

#     print(i+1 if cycle else 0)

# solve()


# 5532 방학 숙제
# import math

# L = int(input())
# A, B, C, D = [int(input()) for _ in range(4)]
# # print(A, B, C, D)
# print(L - max(math.ceil(A/C), math.ceil(B/D)))


# 1005 ACM Craft
# import sys
# input = sys.stdin.readline
# from collections import deque
# from collections import defaultdict

# for _  in range(int(input())):
#     N, K = map(int, input().split())
#     D = [0] + list(map(int, input().split()))

#     indegree = [0] * (N+1)
#     g = defaultdict(list)
#     for _ in range(K):
#         a, b = map(int, input().split())
#         g[a].append(b)
#         indegree[b] += 1

#     W = int(input())
#     dp = [0] * (N+1)

#     # topology_sort
#     q = deque()
#     for i in range(1, N+1):
#         if indegree[i] == 0:
#             q.append(i)
#             dp[i] = D[i]

#     while q:
#         v = q.popleft()
#         # print(v)
#         for i in g[v]:
#             indegree[i] -= 1
#             dp[i] = max(dp[i], dp[v] + D[i])

#             if indegree[i] == 0:
#                 q.append(i)

#     print(dp[W])


# 11943 파일 옮기기
# A, B = map(int, input().split())
# C, D = map(int, input().split())
# print(min(A+D, B+C))


# 11404 플로이드
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# INF = int(1e9)
# n = int(input())
# m = int(input())
# g = [[INF]*(n+1) for _ in range(n+1)]

# for x in range(1, n+1):
#     g[x][x] = 0
# # print(g)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     # g[a][b] = c
#     g[a][b] = min(g[a][b], c)

# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             g[a][b] = min(g[a][b], g[a][k] + g[k][b])

# for x in range(1, n+1):
#     # print(g[x][1:])
#     for y in range(1, n+1):
#         if g[x][y] == INF:
#             print(0, end=' ')
#         else:
#             print(g[x][y], end=' ')
#     print()


# 14938 서강그라운드
# import sys
# input = sys.stdin.readline

# n, m, r = map(int, input().split())
# t = list(map(int, input().split()))

# INF = int(1e9)
# g = [[INF] * (n+1) for _ in range(n+1)]

# for _ in range(r):
#     x, y, c = map(int, input().split())
#     g[x][y] = min(g[x][y], c)
#     g[y][x] = min(g[y][x], c)

# for x in range(1, n+1):
#     g[x][x] = 0

# for k in range(1, n+1):
#     for x in range(1, n+1):
#         for y in range(1, n+1):
#             g[x][y] = min(g[x][y], g[x][k] + g[k][y])

# max_ans = 0
# for x in range(1, n+1):
#     # print(g[x][1:])
#     ans = 0
#     for y in range(1, n+1):
#         if g[x][y] <= m:
#             ans += t[y-1]
#     max_ans = max(max_ans, ans)

# print(max_ans)


# 1389 케빈 베이컨의 6단계 법칙
# import sys
# input = sys.stdin.readline

# INF = int(1e2)
# N, M = map(int, input().split())
# g = [[INF] * (N+1) for _ in range(N+1)]

# for _ in range(M):
#     a, b = map(int, input().split())
#     g[a][b] = 1
#     g[b][a] = 1

# for a in range(1, N+1):
#     g[a][a] = 0

# for k in range(1, N+1):
#     for x in range(1, N+1):
#         for y in range(1, N+1):
#             g[x][y] = min(g[x][y], g[x][k] + g[k][y])

# min_total_val = int(1e4)
# num = -1
# for x in range(1, N+1):
#     # print(g[x][1:])
#     this_total_val = sum(g[x][1:])
#     if min_total_val > this_total_val:
#         min_total_val = this_total_val
#         num = x

# print(num)


# 10844 쉬운 계단 수
# pm 11:10 ~ 11:25

# N = int(input())
# dp = [[0]*10 for _ in range(N)]

# for y in range(1, 10):
#     dp[0][y] = 1

# for x in range(1, N):
#     for y in range(10):
#         if y >= 1:
#             dp[x][y] += dp[x-1][y-1]
#         if y <= 8:
#             dp[x][y] += dp[x-1][y+1]

# # for x in range(N):
# #     print(dp[x], sum(dp[x]))
# print(sum(dp[N-1]) % int(1e9))


# 1647 도시 분할 계획
# pm 11:30 ~ 12:30

# 프림 알고리즘은 time over
# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque
# from heapq import heappush, heappop

# g = defaultdict(list)
# N, M = map(int, input().split())

# for _ in range(M):
#     A, B, C = map(int, input().split())
#     g[A].append([B, C])
#     g[B].append([A, C])

# init_v = list(g.keys())[0]
# spanning_tree_v = set([init_v])
# # spanning_tree_v.add(init_v)
# ans = 0

# que = deque([init_v])
# # que.append(init_v)

# # print(g)
# heap = []
# max_val = -1

# for _ in range(N-1):
#     u = que.popleft()
#     for v, val in g[u]:
#         if v not in spanning_tree_v:
#             heappush(heap, [val, v])

#     while heap[0][1] in spanning_tree_v:
#         heappop(heap)

#     if heap:
#         spanning_tree_v.add(heap[0][1])
#         que.append(heap[0][1])

#         ans += heap[0][0]
#         # last_val = heap[0][0]
#         max_val = max(max_val, heap[0][0])
#     # print(que, ans)

# print(ans - max_val)


# 크루스칼
# import sys
# input = sys.stdin.readline

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a

# def solve():
#     N, M = map(int, input().split())
#     edges = [list(map(int, input().split())) for _ in range(M)]
#     edges = sorted(edges, key=lambda x:(x[2]))

#     parent = [0] * (N+1)
#     for i in range(1, N+1):
#         parent[i] = i

#     result = 0
#     max_cost = -1

#     for a, b, cost in edges:
#         if find_parent(parent, a) != find_parent(parent, b):
#             union_parent(parent, a, b)
#             result += cost
#             max_cost = max(max_cost, cost)

#     print(result - max_cost)

# solve()


# 17626 Four Squares
# pm 09:58 ~ 10:12

# Python3 시간 초과
# PyPy3 여유롭게 통과

# import math

# n = int(input())

# dp = [0] * (n+1)
# square_nums = [0] + [0]*(int(math.sqrt(n)))

# for i in range(1, n+1):
#     dp[i] = i

# for i in range(1, len(square_nums)):
#     square_nums[i] = i**2
# # print(dp)
# # print(square_nums)

# square_nums_i = 1
# len_square_nums = len(square_nums)

# for i in range(2, n+1):
#     if square_nums_i < len_square_nums - 1 and\
#         square_nums[square_nums_i+1] <= i:
#         square_nums_i += 1

#     for j in range(1, square_nums_i+1):
#         dp[i] = min(dp[i], dp[i-square_nums[j]]+1)

# print(dp[i])


# 1992 쿼드트리
# pm 10: 12 ~ 10 : 27

# def divide_and_conquer(board, std_xy, dist):
#     std_x, std_y = std_xy

#     same = True
#     std_num = board[std_x][std_y]
#     for kx in range(std_x, std_x + dist):
#         for ky in range(std_y, std_y + dist):
#             if board[kx][ky] != std_num:
#                 same = False
#                 break

#         if not same:
#             break

#     if same:
#         print(std_num, end = '')

#     else:
#         print("(", end = '')
#         half_dist = dist//2
#         divide_and_conquer(board, [std_x, std_y], half_dist)
#         divide_and_conquer(board, [std_x, std_y + half_dist], half_dist)
#         divide_and_conquer(board, [std_x + half_dist, std_y], half_dist)
#         divide_and_conquer(board, [std_x + half_dist, std_y + half_dist], half_dist)
#         print(")", end = '')

# def solve():
#     N = int(input())
#     board = [list(map(int, input())) for _ in range(N)]
#     # for x in range(N):
#     #     print(board[x])

#     divide_and_conquer(board, [0, 0], N)

# solve()


# 16928 뱀과 사다리 게임
# pm 10 : 34 ~ 10 : 45
# elif 조건에 next_v = snakes[next_v]라고 해야 되는걸 ladders[next_v]로 했음
# 다시 보니 사다리나 뱀을 그냥 한 번에 처리해도 될 듯

# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque

# def solve():
#     N, M = map(int, input().split())
#     ladders = defaultdict(int)
#     snakes = defaultdict(int)

#     for _ in range(N):
#         x, y = map(int, input().split())
#         ladders[x] = y

#     for _ in range(M):
#         u, v = map(int, input().split())
#         snakes[u] = v

#     que = deque()
#     que.append([1, 0])
#     visited = [False] * (101)
#     visited[1] = True

#     while que:
#         for _ in range(len(que)):
#             v, cnt = que.popleft()

#             for k in range(1, 7):
#                 next_v = v+k
#                 if next_v == 100:
#                     print(cnt+1)
#                     return

#                 if not visited[next_v]:
#                     visited[next_v] = True

#                     if next_v in ladders:
#                         next_v = ladders[next_v]
#                     elif next_v in snakes:
#                         next_v = snakes[next_v]
#                     visited[next_v] = True
#                     que.append([next_v, cnt+1])

#                 else:
#                     continue

# solve()

# 개선 코드
# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque

# def solve():
#     N, M = map(int, input().split())
#     # ladders = defaultdict(int)
#     # snakes = defaultdict(int)
#     moves = defaultdict(int)

#     for _ in range(N+M):
#         x, y = map(int, input().split())
#         moves[x] = y

#     que = deque()
#     que.append([1, 0])
#     visited = [False] * (101)
#     visited[1] = True

#     while que:
#         # for _ in range(len(que)):
#         v, cnt = que.popleft()

#         for k in range(1, 7):
#             next_v = v+k
#             if next_v == 100:
#                 print(cnt+1)
#                 return

#             if not visited[next_v]:
#                 visited[next_v] = True

#                 if next_v in moves:
#                     next_v = moves[next_v]
#                     visited[next_v] = True

#                 que.append([next_v, cnt+1])

# solve()


# 9019 DSLR
# pm 10:54 ~ 12:45

# 시간 초과
# import sys
# input = sys.stdin.readline
# from collections import deque

# def list_n_to_num_n(list_n):
#     return_val = 0
#     mul_val = 1

#     while list_n:
#         return_val += list_n.pop() * mul_val
#         mul_val *= 10

#     return return_val

# def check_visited(que, visited, next_num, tmp_cmd):
#     if not visited[next_num]:
#         # next_num = True
#         visited[next_num] = True
#         que.append([next_num, tmp_cmd])

# def bfs(que, visited):
#     n, cmd = que.popleft()
#     list_n = list(map(int, str(n)))

#     # D
#     tmp_cmd = cmd[:] + ['D']
#     next_num = (n*2)%10000
#     check_visited(que, visited, next_num, tmp_cmd)

#     # S
#     tmp_cmd = cmd[:] + ['S']
#     next_num = (n-1)%10000
#     check_visited(que, visited, next_num, tmp_cmd)

#     # L
#     tmp_list_n = list_n[1:]
#     tmp_list_n.append(list_n[0])
#     tmp_cmd = cmd[:] + ['L']
#     next_num = list_n_to_num_n(tmp_list_n)
#     check_visited(que, visited, next_num, tmp_cmd)

#     # R
#     tmp_list_n = [list_n[-1]]
#     tmp_list_n.extend(list_n[:-1])
#     tmp_cmd = cmd[:] + ['R']
#     next_num = list_n_to_num_n(tmp_list_n)
#     check_visited(que, visited, next_num, tmp_cmd)

# def solve():
#     for _ in range(int(input())):
#         A, B = map(int, input().split())

#         que = deque()
#         que.append([A, []])
#         visited = [False] * int(1e4)

#         while que:
#             if que[0][0] == B:
#                 print(*que[0][1], sep = '')
#                 break

#             bfs(que, visited)

# solve()

# 2nd try
"""
1 100
[정답] LL
[출력] DDDDSLSD

100 1
[정답] RR
[출력] L
"""
# 시간 초과 해결
# defaultdict(list) 대신 dict() 쓰고 que에다가 list대신 string("") append
# visied[A] = True

# import sys
# input = sys.stdin.readline
# from collections import deque

# def check_visited(que, visited, next_num, tmp_cmd, ans_dict):
#     if not visited[next_num]:
#         visited[next_num] = True
#         que.append([next_num, tmp_cmd])
#         ans_dict[next_num] = tmp_cmd

# def bfs(que, visited, ans_dict):
#     n, cmd = que.popleft()

#     # D
#     next_num = (n*2)%10000
#     check_visited(que, visited, next_num, cmd + "D", ans_dict)

#     # S
#     next_num = (n-1)%10000
#     check_visited(que, visited, next_num, cmd + "S", ans_dict)

#     # L
#     next_num = (n * 10) % 10000 + (n * 10) // 10000
#     check_visited(que, visited, next_num, cmd + "L", ans_dict)

#     # R
#     next_num = (n // 10) + (n % 10)*1000
#     check_visited(que, visited, next_num, cmd + "R", ans_dict)

# def solve():
#     for _ in range(int(input())):
#         A, B = map(int, input().split())

#         que = deque()
#         # que.append([A, "[]"])
#         que.append([A, ""])
#         visited = [False] * int(1e4)
#         visited[A] = True
#         ans_dict = dict()

#         while que:
#             if B in ans_dict:
#                 print(ans_dict[B])
#                 break

#             bfs(que, visited, ans_dict)

# solve()


# 6064 카잉 달력
# pm 04: 16 ~ 04: 31

"""
10 12 10 12
[정답] 60
[출력] -1
10 12 6 12
[정답] 36
[출력] -1
"""
# elif문 추가로 해결

# import sys
# input = sys.stdin.readline

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# def lcm(a, b):
#     return a * b // gcd(a, b)

# for _ in range(int(input())):
#     M, N, x, y = map(int, input().split())

#     ans = -1
#     for i in range(x, lcm(M,N)+1, M):
#         if i % N == y:
#             ans = i
#             break
#         elif N == y and (i-N) % N == 0:
#             ans = i
#             break

#     print(ans)


# 10172 개
# print("\
# |\_/|\n\
# |q p|   /}\n\
# ( 0 )\"\"\"\\\n\
# |\"^\"`    |\n\
# ||_/=\\\\__|")

# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|


# 9251 LCS
"""
ABCAAA
AAABC

[[0, 1000], [0, 1000], [0, 1000], [0, 1000], [0, 1000], [0, 1000]]
[[1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0]]
[[2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0]]
[[3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0]]
[[3, 0], [4, 1], [4, 1], [4, 1], [4, 1], [4, 1]]
[[3, 0], [4, 1], [5, 2], [5, 2], [5, 2], [5, 2]]
"""
# from collections import defaultdict

# str1 = list(input())
# str2 = ['_'] + list(input())
# # print(str1, str2)

# INF = int(1e3)
# # [] : 해당 idx까지 체크했을 때 LCS 길이, LCS를 만족하는 마지막 알파벳의 idx
# dp = [[[0, INF] for _ in range(len(str1))] for _ in range(len(str2))]
# alpha_idx = defaultdict(set)

# for idx in range(len(str1)):
#     alpha = str1[idx]
#     alpha_idx[alpha].add(idx)
# # print(alpha_idx)

# for x in range(1, len(str2)):
#     for y in range(len(str1)):
#         # 바로 윗값 그대로 복사
#         dp[x][y] = dp[x-1][y][:]

#         # 해당 알파벳(str2[x])에 대해 일치하는 인덱스(y)가 존재하면 기존 Subsequence에 추가 가능
#         if y in alpha_idx[str2[x]]:
#             dp[x][y][0] += 1
#             dp[x][y][1] = y

#         # 제일 처음 idx가 아니면
#         if y > 0:
#             # 위 계산을 다 했을 때 LCS 길이가 바로 전 idx의 값에 비해 작은 경우
#             if dp[x][y][0] < dp[x][y-1][0]:
#                 dp[x][y] = dp[x][y-1][:]

#             # LCS길이는 같은데 마지막 idx 위치 갱신이 필요한 경우
#             if dp[x][y][0] == dp[x][y-1][0] and dp[x][y][1] > dp[x][y-1][1]:
#                 dp[x][y][1] = dp[x][y-1][1]

# print()
# for x in range(len(str2)):
#     print(dp[x])


# 새로 짠 코드
"""
ABCAAD
AAABCA

ABABA
BABAB

AAAAA
AAAAA

ABCAAD
AABCAK
"""
# from collections import defaultdict, deque

# str1 = list(input())
# str2 = list(input())
# # print(str1, str2)

# idxs = defaultdict(deque)
# idxs_set = defaultdict(set)
# last_idx = defaultdict(int)
# popped_idxs_set = defaultdict(set)

# for idx in range(len(str1)):
#     alpha = str1[idx]
#     idxs[alpha].append(idx)
#     idxs_set[alpha].add(idx)
#     last_idx[alpha] = idx
# # print(idxs)
# # print(last_idx)
# dp = [0] * (len(str1))

# for i in range(len(str2)):
#     alpha = str2[i]
#     # alpha 가 str1에서 한 번이라도 등장하면
#     if alpha in last_idx:
#         max_val = 0
#         # idx : 해당 alphbet이 등장하는 마지막 인덱스까지
#         for idx in range(last_idx[alpha]+1):
#             # 현재 alpha가 동일한(target) alphabet이 아니면 LCS 값으로 max_val 저장
#             if (idx not in idxs_set[alpha]):
#                 max_val = max(max_val, dp[idx])
#             # target alphabet이면
#             else:
#                 dp[idx] = max(dp[idx], max_val+1) # max_val + 1 == LCS + 1

#                 # 동일한 알파벳이 여러 번 나오는 때를 처리,
#                 # str1보다 str2에서 더 많이 등장하지 않은 경우 if문 성립
#                 # if idx in popped_idxs_set[alpha]: # 개선 해서 ↓
#                 if idxs[alpha] and idx in popped_idxs_set[alpha]:
#                     max_val = max(max_val, dp[idx])

#         if idxs[alpha]:
#             popped_idxs_set[alpha].add(idxs[alpha].popleft())
#         # print(popped_idxs_set)
#     print(dp)

# print(max(dp))


# 9251 LCS
# str1 = list(input())
# str2 = list(input())

# x, y = len(str1), len(str2)
# dp = [0] * y

# for kx in range(x):
#     cnt = 0
#     for ky in range(y):
#         if cnt < dp[ky]:
#             cnt = dp[ky]
#         elif str1[kx] == str2[ky]:
#             dp[ky] = cnt+1
#     # print(dp)

# print(max(dp))


# 11725 트리의 부모 찾기
# pm 02:31 ~ 02:38

# BFS
# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque

# N = int(input())
# g = defaultdict(list)

# for _ in range(N-1):
#     a, b = map(int, input().split())
#     g[a].append(b)
#     g[b].append(a)
# # print(g)

# que = deque([1])
# visited = [False] * (N+1)
# visited[1] = True
# parent = [-1] * (N+1)

# while que:
#     u = que.popleft()
#     # print(u)
#     for v in g[u]:
#         if not visited[v]:
#             visited[v] = True
#             que.append(v)
#             parent[v] = u

# print(*parent[2:], sep='\n')


# DFS
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# sys.setrecursionlimit(10**6)

# def dfs(g, visited, parent, u):
#     for v in g[u]:
#         if not visited[v]:
#             visited[v] = True
#             parent[v] = u
#             dfs(g, visited, parent, v)

# def solve():
#     N = int(input())
#     g = defaultdict(list)

#     for _ in range(N-1):
#         a, b = map(int, input().split())
#         g[a].append(b)
#         g[b].append(a)
#     # print(g)

#     visited = [False] * (N+1)
#     visited[1] = True
#     parent = [-1] * (N+1)

#     dfs(g, visited, parent, 1)

#     print(*parent[2:], sep='\n')

# solve()


# 18221 교수님 저는 취업할래요
# pm 05:53 ~ 06:00
# import sys
# input = sys.stdin.readline
# import math

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# prof_xy = list()
# target_xy = list()

# for x in range(N):
#     for y in range(N):
#         if board[x][y] == 2:
#             prof_xy = [x, y]
#         elif board[x][y] == 5:
#             target_xy = [x, y]
# # print(prof_xy, target_xy)

# ans = 0
# if math.sqrt((prof_xy[0]-target_xy[0])**2 + (prof_xy[1]-target_xy[1])**2) >= 5:
#     students = 0
#     for x in range(min(prof_xy[0], target_xy[0]), max(prof_xy[0], target_xy[0])+1):
#         for y in range(min(prof_xy[1], target_xy[1]), max(prof_xy[1], target_xy[1])+1):
#             if board[x][y] == 1:
#                 students += 1

#     if students >= 3:
#         ans = 1

# print(ans)


# 9252 LCS 2
# pm 06:02 ~ 06:19 (틀렸습니다 음)
"""
ABCDEFB
EFABCD
[정답] ABCD
[출력] FBCD
"""
# import sys
# sys.setrecursionlimit(10**4)

# def recursion(dp, n, idx, str2):
#     if n > 1 and idx > -1:
#         recursion(dp, n-1, dp[idx][1], str2)

#     print(str2[idx], end='')

# def solve():
#     str1, str2 = list(input()), list(input())
#     w, h = len(str1), len(str2)

#     dp = [[0, -1] for _ in range(h)]

#     for i in range(w):
#         cnt, pre_idx = 0, -1
#         for j in range(h):
#             if cnt < dp[j][0]:
#                 cnt = dp[j][0]
#                 pre_idx = j
#             # cnt >= dp[j]
#             elif str1[i] == str2[j]:
#                 dp[j][0] = cnt+1
#                 dp[j][1] = pre_idx
#         print(dp)

#     max_val = 0
#     max_val_idx = -1
#     for i in range(h):
#         if max_val < dp[i][0]:
#             max_val = dp[i][0]
#             max_val_idx = i

#     print(max_val)
#     if max_val != 0:
#         recursion(dp, max_val, max_val_idx, str2)

# solve()


# import sys
# sys.setrecursionlimit(10**4)

# def recursion(dp, x, y, str2):
#     if dp[x][y] != 0:
#         if dp[x][y] == dp[x-1][y-1]:
#             recursion(dp, x-1, y-1, str2)
#         elif dp[x][y] == dp[x-1][y]:
#             recursion(dp, x-1, y, str2)
#         elif dp[x][y] == dp[x][y-1]:
#             recursion(dp, x, y-1, str2)
#         else:
#             recursion(dp, x-1, y-1, str2)
#             # +1 보정되어있으므로 y-1
#             print(str2[y-1], end='')

# def solve():
#     str1, str2 = list(input()), list(input())
#     h, w = len(str1), len(str2)
#     dp = [[0] * (w+1) for _ in range(h+1)]

#     for i in range(1, h+1):
#         for j in range(1, w+1):
#             if str1[i-1] == str2[j-1]:
#                 dp[i][j] = dp[i-1][j-1] + 1
#             else:
#                 dp[i][j] = max(dp[i][j-1], dp[i-1][j])
#         # print(dp[i])

#     print(dp[h][w])
#     recursion(dp, h, w, str2)

# solve()


# 2448 별 찍기 - 11
# pm 10:31 ~ 11:00 (출력 형식이 잘못되었습니다)
#          ~ 11:32 (공백 잡아주고 나서 AC)

# def recursion(board, N, x, y, d):
#     if d != 3:
#         half_d = d//2
#         recursion(board, N, x, y, half_d)
#         recursion(board, N, x + half_d, y, half_d)
#         recursion(board, N, x + half_d, y+(2*half_d), half_d)
#     else:
#         board[x][y] = '*'
#         board[x+1][y] = '*'
#         board[x+1][y+1] = ' '
#         board[x+1][y+2] = '*'
#         # board[x+2][y:y+6] = '*'*5
#         for i in range(5):
#             board[x+2][y+i] = '*'

# def solve():
#     N = int(input()) # N은 항상 3×(2**k) 수
#     # board = [[' ']*(6*(N//3)) for _ in range(N)]
#     board = [[' ']*(2*N) for _ in range(N)]

#     recursion(board, N, 0, 0, N)

#     # 출력용
#     for x in range(N):
#         print(' '*(N-1-x), end='')
#         for y in range((2*x)+1):
#             print(board[x][y], end='')
#         print(' '*(N-1-x), end='') # it needs this line's code
#         print()

#     # 확인용
#     # print(*board[N-1], sep='')

# solve()


# 5639 이진 검색 트리

# 시간 초과
# import sys
# sys.setrecursionlimit(10**7)

# from collections import defaultdict

# def make_binary_tree(g, parent, val):
#     if val < parent:
#         if -1 in g[parent]:
#             make_binary_tree(g, g[parent][-1], val)
#         else:
#             g[parent][-1] = val
#             # g[val] = dict() # g = dict() 인 경우

#     else:
#         if 1 in g[parent]:
#             make_binary_tree(g, g[parent][1], val)
#         else:
#             g[parent][1] = val
#             # g[val] = dict() # g = dict() 인 경우

# def post_order(g, val):
#     if -1 in g[val]:
#         post_order(g, g[val][-1])
#     if 1 in g[val]:
#         post_order(g, g[val][1])

#     print(val)

# def solve():
#     vals = sys.stdin.readlines()

#     g = defaultdict(dict)
#     # g = dict()
#     # g[vals[0]] = dict() # g = dict() 인 경우

#     for idx in range(len(vals)):
#         vals[idx] = int(vals[idx])
#     # print(vals)

#     for val in vals[1:]:
#         make_binary_tree(g, vals[0], val)
#     # print(g)

#     post_order(g, vals[0])

# solve()


# dict 대신 배열로
# import sys
# sys.setrecursionlimit(10**7)

# # tree = [[-1, -1, -1] for _ in range(len(vals))]
# def make_binary_tree(tree, parent_idx, idx):
#     if tree[idx][0] < tree[parent_idx][0] :
#         if tree[parent_idx][1] != -1:
#             make_binary_tree(tree, tree[parent_idx][1], idx)
#         else:
#             tree[parent_idx][1] = idx
#     else:
#         if tree[parent_idx][2] != -1:
#             make_binary_tree(tree, tree[parent_idx][2], idx)
#         else:
#             tree[parent_idx][2] = idx

# def post_order(tree, idx):
#     if tree[idx][1] != -1:
#         post_order(tree, tree[idx][1])
#     if tree[idx][2] != -1:
#         post_order(tree, tree[idx][2])

#     print(tree[idx][0])

# def solve():
#     vals = sys.stdin.readlines()

#     tree = [[int(vals[i]), -1, -1] for i in range(len(vals))]
#     for idx in range(1, len(tree)):
#         make_binary_tree(tree, 0, idx)
#     # print(tree)

#     post_order(tree, 0)

# solve()


# 트리 생성 시 각 노드에 대해 삽입만 최악의 경우 O(N) -> N개에 대해 진행하면 O(N**2) -> Time Over
# 메모리 초과
# import sys
# sys.setrecursionlimit(10**7)

# def post_order(vals):
#     if vals:
#         std, next_vals = vals[0], vals[1:]
#         idx, find = 0, False

#         # std 기준으로 제일 처음 만나는 큰 수의 idx
#         for idx in range(len(next_vals)):
#             if next_vals[idx] > std:
#                 find = True
#                 break
#         # 못 찾았으면(없으면) idx+1
#         if not find:
#             idx += 1

#         # 후순위
#         # L
#         post_order(next_vals[:idx])
#         # R
#         post_order(next_vals[idx:])
#         # parent
#         print(std)

# def solve():
#     vals = sys.stdin.readlines()
#     for idx in range(len(vals)):
#         vals[idx] = int(vals[idx])
#     # print(vals)
#     post_order(vals)

# solve()


# Python3 통과, PyPy3 메모리 초과
# import sys
# sys.setrecursionlimit(10**7)

# def post_order(vals, idx_from, idx_to):
#     if idx_from <= idx_to:
#         # print(idx_from, idx_to)
#         std = vals[idx_from]
#         next_std_idx, find = idx_from+1, False

#         # std보다 다 작을 때를 가정해 idx_to 값으로 초기화
#         next_std_idx = idx_to
#         # std 기준으로 제일 처음 만나는 큰 수의 idx
#         for next_std_idx in range(idx_from+1, idx_to+1):
#             if vals[next_std_idx] > std:
#                 find = True
#                 break
#         # std보다 다 작으면 next_std_idx+1
#         if not find:
#             next_std_idx += 1

#         # 후순위
#         # L
#         post_order(vals, idx_from+1, next_std_idx-1)
#         # R
#         post_order(vals, next_std_idx, idx_to)
#         # parent
#         print(std)

# def solve():
#     vals = sys.stdin.readlines()
#     for idx in range(len(vals)):
#         vals[idx] = int(vals[idx])
#     # print(vals)
#     post_order(vals, 0, len(vals)-1)

# solve()


# 13866 팀 나누기
# s = list(map(int, input().split()))
# print(abs(s[0]+s[3]-s[1]-s[2]))


# 1916 최소비용 구하기
# am 01:15 ~ 01:46
# 다익스트라 기억 안 나서 책 봄

# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque
# from heapq import heappush, heappop

# N, M = int(input()), int(input())
# g = defaultdict(list)
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     g[a].append([c, b])
# # print(g)
# start, finish = map(int, input().split())

# heap = []
# INF = int(1e9)
# dist = [INF] * (N+1)

# visited = [False] * (N+1)
# visited[start] = True

# for val, v in g[start]:
#     heappush(heap, [val, v])

# while heap:
#     val, u = heappop(heap)
#     if visited[u]:
#         continue
#     else:
#         visited[u] = True
#         dist[u] = min(dist[u], val)
#         for val, v in g[u]:
#             if not visited[v]:
#                 heappush(heap, [dist[u] + val, v])

# # print(dist)
# print(dist[finish])

# visited 없어도 작동함 → 대신 메모리초과 (Python3 기준 메모리 초과이니 PyPy3는 당연함)
# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque
# from heapq import heappush, heappop

# N, M = int(input()), int(input())
# g = defaultdict(list)
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     g[a].append([c, b])
# # print(g)
# start, finish = map(int, input().split())

# heap = []
# INF = int(1e9)
# dist = [INF] * (N+1)

# for val, v in g[start]:
#     heappush(heap, [val, v])

# while heap:
#     val, u = heappop(heap)
#     if val > dist[u]:
#         continue

#     dist[u] = min(dist[u], val)
#     for val, v in g[u]:
#         heappush(heap, [dist[u] + val, v])

# # print(dist)
# print(dist[finish])


# 15726 이칙연산
# A, B, C = map(int, input().split())
# print(max(int(A*B/C), int(A/B*C)))


# 11948 과목 선택
# A = sum(sorted([int(input()) for _ in range(4)])[1:])
# B = max([int(input()) for _ in range(2)])

# print(A+B)


# 16486
# import math

# d1, d2 = int(input()), int(input())
# print(2*d1 + 2*math.pi*d2)


# 25377 빵
# import sys
# input = sys.stdin.readline

# ans = 1001
# for _ in range(int(input())):
#     A, B = map(int, input().split())
#     if A <= B:
#         ans = min(ans, B)

# print(ans if ans != 1001 else -1)


# 25703 포인터 공부
# N = int(input())
# print("int a;")
# print("int *ptr = &a;")
# for i in range(2, N+1):
#     print('int {0}ptr{1} = &ptr{2};'.format("*"*i, i, (i-1 if i >= 3 else "")))


# 1644 소수의 연속합
# pm 09:50 ~ 10:16
# N = int(input())

# def solve():
#     if N == 1:
#         print(0)
#         return

#     # 에라토스테네스의 체
#     limit = int(N+1)
#     sieves = [True] * limit
#     for i in range(2, limit):
#         if sieves[i] == True:
#             for ii in range(2*i, limit, i):
#                 sieves[ii] = False

#     # 소수 list
#     primes = []
#     for i in range(2, limit):
#         if sieves[i] == True:
#             primes.append(i)
#     # print(primes)

#     # ans 계산
#     l, r = 0, 0
#     now_sum = primes[0]
#     len_primes = len(primes)
#     ans = 0
#     while l <= r:
#         if now_sum < N:
#             if r >= len_primes-1:
#                 break
#             else:
#                 r += 1
#                 now_sum += primes[r]
#         elif now_sum > N:
#             now_sum -= primes[l]
#             l += 1
#         else: # now_sum == N
#             ans += 1
#             now_sum -= primes[l]
#             l, r = l+1, r
#         # print(l, r)
#     print(ans)

# solve()


# 1987 알파벳
# 10:23 ~ 33
# inc_xy 빼줬더니 시간 초과 해결

# import sys
# input = sys.stdin.readline

# def dfs(board, visited, x, y, R, C, inc_xy, cells):
#     global ans

#     a = ord(board[x][y])-65
#     visited[a] = True
#     ans = max(ans, cells)
#     # print(x, y, cells, ans)

#     for p_x, p_y in inc_xy:
#         nx, ny = x + p_x, y + p_y
#         if 0 <= nx < R and 0 <= ny < C and not visited[ord(board[nx][ny])-65]:
#             dfs(board, visited, nx, ny, R, C, inc_xy, cells+1)

#     visited[a] = False
#     # cells -= 1

# def solve():
#     R, C = map(int, input().split())
#     board = [list(input().rstrip()) for _ in range(R)]
#     # for x in range(R):
#     #     print(board[x])
#     visited = [False] * 26
#     inc_xy = [1, 0], [0, 1], [-1, 0], [0, -1]
#     global ans
#     ans = 0

#     dfs(board, visited, 0, 0, R, C, inc_xy, 1)
#     print(ans)

# solve()


# BFS
'''
"""""""""""""""""""""""""""""""""""""""""""""""
'''

# 12865 평범한 배낭
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# items = [list(map(int, input().split())) for _ in range(N)]

# dp = [[0]*(K+1) for _ in range(N+1)]

# # for u, v in items:
# for i in range(1, N+1):
#     u, v = items[i-1]

#     for j in range(1, K+1):
#         dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#         if j >= u:
#             dp[i][j] = max(dp[i][j], dp[i-1][j-u] + v)
# print(dp[N][K])

# # for x in range(N+1):
# #     print(dp[x])


# from heapq import heapify, heappush, heappop
# # from queue import PriorityQueue

# heap = [5, 3, 2, 1]
# heapify(heap)

# # heappush(heap, [1, 2, 3])
# # heappush(heap, [0, 2, 3])
# # heappush(heap, [0, 1, 3])
# # print(heap[0])

# val = heappop(heap)
# print(val)


# 1374 강의실
# import sys
# input = sys.stdin.readline
# from heapq import heappush, heappop

# N = int(input())

# m = [list(map(int, input().split())) for _ in range(N)]
# m = sorted(m, key=lambda x:(x[1], x[2]))
# # for x in range(N):
# #     print(m[x])

# # heap -> 종료시간을 담은 우선순위 큐
# heap = []
# # cnt : 필요한 강의실의 수
# cnt = 0
# for i in range(N):
#     if not heap:
#         cnt += 1
#         heappush(heap, m[i][2])
#     else: # 기존 방이 있음
#         # m : (강의 코드, 시작 시간, 종료시간)
#         if heap[0] <= m[i][1]:
#             heappop(heap)
#         # 강의실이 하나 더 필요해
#         else:
#             cnt += 1

#         heappush(heap, m[i][2])

# print(cnt)

# btr - N과 M
# # import itertools
# N, M = map(int, input().split())

# # for kk in itertools.permutations([i for i in range(1, N+1)], M):
# #     print(*kk, sep=' - ', end='\n\n')

# def btr(nums, N, M, dic, k):
#     for i in range(N):
#         if nums[i] == False:
#             nums[i] = True
#             dic[k-1] = i+1

#             if k+1 <= M:
#                 btr(nums, N, M, dic, k+1)
#             else:
#                 # 변수 같은 거 써서 시간 날림
#                 for ii in range(M):
#                     print(dic[ii], end=' ')
#                 print()

#             nums[i] = False
#             dic[k] = -1

# nums = [False]*N
# dic = dict()
# btr(nums, N, M, dic, 1)


# 19698 헛간 청약
# N, W, H, L = map(int, input().split())
# print(min(N,(W//L)*(H//L)))


# 6764 Sounds fishy!
# def solve():
#     depths = [int(input()) for _ in range(4)]

#     rising, diving, cd = True, True, True
#     for i in range(3):
#         if depths[i] < depths[i+1]:
#             diving, cd = False, False
#         elif depths[i] > depths[i+1]:
#             rising, cd = False, False
#         else:
#             rising, diving = False, False

#     if rising: print("Fish Rising")
#     elif diving: print("Fish Diving")
#     elif cd: print("Fish At Constant Depth")
#     else: print("No Fish")

# solve()


# 1308 D-Day
# def leap_year(n):
#     if n % 400 == 0:
#         return True
#     elif n % 100 == 0:
#         return False
#     elif n % 4 == 0:
#         return True

# def solve():
#     now = list(map(int, input().split()))
#     target = list(map(int, input().split()))

#     # 1 ~ 12 (윤년은 따로 계산)
#     total_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#     # 천 년 이상
#     if (target[0] - now[0]) > 1000:
#         print("gg")
#         return
#     elif (target[0] - now[0]) == 1000:
#         if target[1] > now[1]:
#             print("gg")
#             return
#         elif target[1] == now[1]:
#             if target[2] >= now[2]:
#                 print("gg")
#                 return

#     # 미만
#     ans = 0
#     while now[0] != target[0] or now[1] != target[1]:
#         if (now[1] == 2) and leap_year(now[0]):
#             ans += 1

#         ans += total_days[now[1]]
#         now[1] = (now[1])%12 + 1
#         if now[1] == 1:
#             now[0] += 1
#         # print(ans)

#     ans += (target[2] - now[2])
#     print(f'D-{ans}')

# solve()


# 4963 섬의 개수
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(int(1e5))
# from collections import defaultdict

# def dfs(board, w, h, x, y, inc_xy):
#     if board[x][y] == 1:
#         board[x][y] = 0
#         for p_x, p_y in inc_xy:
#             nx, ny = x + p_x, y + p_y
#             if 0 <= nx < h and 0 <= ny < w:
#                 dfs(board, w, h, nx, ny, inc_xy)

#         return 1

#     else:
#         return 0


# def solve():
#     while True:
#         w, h = map(int, input().split())
#         if w == 0:
#             return 0

#         board = [list(map(int, input().split())) for _ in range(h)]
#         inc_xy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

#         ans = 0
#         for x in range(h):
#             for y in range(w):
#                 ans += dfs(board, w, h, x, y, inc_xy)
#         print(ans)

# solve()


# 브루트포스
# N, M = map(int, input().split())
# cards = sorted(list(map(int, input().split())))

# def solve():
#     max_sum = 0
#     now_sum = 0
#     for i in range(N-2):
#         now_sum += cards[i]
#         for j in range(i+1, N-1):
#             now_sum += cards[j]
#             for k in range(j+1, N):
#                 now_sum += cards[k]
#                 if now_sum == M:
#                     max_sum = M
#                     return max_sum

#                 elif now_sum < M:
#                     if max_sum < now_sum:
#                         max_sum = now_sum
#                 else: # now_sum > M
#                     now_sum -= cards[k]
#                     break

#                 now_sum -= cards[k]
#             now_sum -= cards[j]
#         now_sum -= cards[i]
#     return max_sum

# print(solve())


# 이분 탐색 적용
# N, M = map(int, input().split())
# cards = sorted(list(map(int, input().split())))

# def solve():
#     max_sum = 0

#     for i in range(N-2):
#         if sum(cards[i:i+3]) > M:
#             break

#         for j in range(i+1, N-1):
#             now_sum = cards[i] + cards[j]

#             if now_sum + cards[j+1] > M:
#                 break

#             # binary_search
#             l, r = j+1, N-1
#             while l <= r:
#                 # print(i, j, now_sum, l, r)
#                 mid = (l+r)//2
#                 final_sum = now_sum + cards[mid]

#                 if final_sum == M:
#                     print(M)
#                     return
#                 elif final_sum < M:
#                     max_sum = max(max_sum, final_sum)
#                     l = mid + 1
#                 else:
#                     r = mid - 1

#     print(max_sum)

# solve()


# 두 포인터
# N, M = map(int, input().split())
# cards = sorted(list(map(int, input().split())))

# max_sum = -1
# for mid in range(1, N-1):
#     l, r = mid-1, mid+1
#     now_sum = sum(cards[mid-1:mid+2])

#     while True:
#         if now_sum < M:
#             max_sum = max(max_sum, now_sum)
#             if r < N-1:
#                 now_sum -= cards[r]
#                 r += 1
#                 now_sum += cards[r]
#             else:
#                 break

#         elif now_sum > M:
#             if 0 < l:
#                 now_sum -= cards[l]
#                 l -= 1
#                 now_sum += cards[l]
#             else:
#                 break

#         else: # now_sum == M:
#             max_sum = M
#             break

#     # 더 확인할 필요 없으면 break
#     if max_sum == M:
#         break

# print(max_sum)


# 조합
# N, M = map(int, input().split())
# cards = sorted(list(map(int, input().split())))

# set1, set2 = set({c for c in cards[:2]}), set() # 1장만, 2장 sum
# set2.add(cards[0] + cards[1]) # 3장 찾을 수 있는 입력만 주어지므로 조건문 필요 없음

# def solve():
#     max_ans = -1
#     for i in range(2, N):
#         val = cards[i]

#         # set2 이후 set1 순서
#         for c in set2:
#             if val+c < M:
#                 max_ans = max(max_ans, val+c)
#             elif val+c == M:
#                 max_ans = M
#                 return max_ans

#         for c in set1:
#             if val+c < M:
#                 set2.add(val+c)

#         set1.add(val)

#     return max_ans

# print(solve())


# 2467 용액
# N = int(input())
# # solutions
# s = list(map(int, input().split()))

# def solve():
#     closest_sum = int(2e9)
#     ans = []
#     l, r = 0, N-1

#     while l < r:
#         abs_now_sum = abs(s[l] + s[r])

#         if closest_sum > abs_now_sum:
#             closest_sum = abs_now_sum
#             ans = [s[l], s[r]]
#             if closest_sum == 0:
#                 break

#         if s[l] + s[r] < 0:
#             l += 1

#         else:  #s[l] + s[r] > 0:
#             r -= 1

#     # print(closest_sum)
#     print(*ans)

# solve()

# 19944 뉴비의 기준은 뭘까?
# N, M = map(int, input().split())

# if M <= 2:
#     print("NEWBIE!")
# elif M <= N:
#     print("OLDBIE!")
# else:
#     print("TLE!")

# 20673 Covid-19
# p, q = int(input()), int(input())
# if p <= 50 and q <= 10:
#     print("White")
# elif q > 30:
#     print("Red")
# else:
#     print("Yellow")


# CAPS 15000
# string = list(input())
# # print(string)
# for s in string:
#     print(s.upper(), end='')


# 1965 상자넣기
# N = int(input())
# boxes = list(map(int, input().split()))

# dp = [0] * 1001
# for box in boxes:
#     dp[box] = dp[box-1]+1
#     for idx in range(box, 1001):
#         dp[idx] = max(dp[idx], dp[box])

# print(dp[1000])


# 25625 샤틀버스
# x, y = map(int, input().split())

# if x <= y:
#     print(y-x)
# else:
#     print(y+x)


# 2193 이친수
# N = int(input())
# dp = [[0]*2 for _ in range(N+1)]
# dp[1][1] = 1

# for i in range(2, N+1):
#     dp[i][0] = dp[i-1][0]+dp[i-1][1]
#     dp[i][1] = dp[i-1][0]

# print(sum(dp[N]))


# 2410 2의 멱수의 합
# N = int(input())
# dp = [0] * (N+1)
# dp[0] = 1

# for i in range(1, N+1):
#     k = 1
#     while k <= i:
#         dp[i] += dp[i-k]

#         k *= 2
#     print(dp)

# print(dp)


# 11779 최소비용 구하기 2
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# from heapq import heappush, heappop

# def route_tracking(route, start, now, cnt):
#     if now != start:
#         route_tracking(route, start, route[now], cnt+1)
#     else:
#         print(cnt)

#     print(now, end = ' ')

# def solve():
#     n, m = int(input()), int(input())
#     g = defaultdict(list)
#     for _ in range(m):
#         pre, now, val = map(int, input().split())
#         g[pre].append([val, pre, now])
#     start, finish = map(int, input().split())

#     heap = []
#     for line in g[start]:
#         heappush(heap, line)
#     # print(heap)

#     INF = int(1e9)
#     d = [INF] * (n+1)
#     d[start] = 0
#     visited = [False] * (n+1)
#     visited[start] = True
#     route = [-1] * (n+1)

#     while heap:
#         val, pre, now = heappop(heap)
#         if not visited[now]:
#             visited[now] = True
#             # d[now] = min(d[now], val)
#             d[now] = val
#             route[now] = pre

#             if now == finish:
#                 break

#             for next_val, now, next in g[now]:
#                 if not visited[next]:
#                     heappush(heap, [val + next_val, now, next])

#     print(d[finish])
#     # print(route)
#     route_tracking(route, start, now, 1)

# solve()


# 1535 안녕
# N = int(input())
# hp_loss = list(map(int, input().split()))
# glad_gain = list(map(int, input().split()))
# dp = [0] * 101

# # idx : 체력
# for i in range(N):
#     for idx in range(100, hp_loss[i]-1, -1):
#         dp[idx] = max(dp[idx], dp[idx-hp_loss[i]] + glad_gain[i])

# print(max(dp[:100]))


# 1753 최단경로
# pm 04:08 ~ 04:17

# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# from heapq import heappush, heappop

# def solve():
#     V, E = map(int, input().split())
#     K = int(input())

#     g = defaultdict(list)
#     for _ in range(E):
#         u, v, w = map(int, input().split())
#         g[u].append([w, v])

#     heap = []
#     for line in g[K]:
#         heappush(heap, line)

#     visited = [False] * (V+1)
#     visited[K] = True

#     INF = int(2e5)
#     d = [INF] * (V+1)
#     d[K] = 0

#     while heap:
#         val, v = heappop(heap)
#         if not visited[v]:
#             visited[v] = True
#             d[v] = val

#             for next_val, next_v in g[v]:
#                 if not visited[next_v]:
#                     heappush(heap, [val+next_val, next_v])

#     print(*[i if i != INF else "INF" for i in d[1:]], sep='\n')

# solve()


# 1138 한 줄로 서기
# N = int(input())
# nums = list(map(int, input().split()))

# ans = [0] * N
# idxs = [i for i in range(N)]

# for i in range(N):
#     ans[idxs[nums[i]]] = i+1
#     del idxs[nums[i]]

# print(*ans)


# 9655 돌 게임
# print("SK" if int(input()) % 2 == 1 else "CY")

# 9657 돌 게임 3
# print("SK" if int(input()) % 7 not in [0, 2] else "CY")

# 24723 녹색 거탑
# print(2**(int(input())))


# 2252 줄 세우기
# pm 02:28 ~ 02:47
# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque

# def solve():
#     N, M = map(int, input().split())

#     # cnt, g 초기화
#     cnt = [0]*(N+1)
#     g = defaultdict(list)
#     for _ in range(M):
#         A, B = map(int, input().split())
#         g[A].append(B)
#         cnt[B] += 1

#     # q 초기화
#     q = deque()
#     for v in range(1, N+1):
#         if cnt[v] == 0:
#             q.append(v)

#     # 위상 정렬 수행
#     while q:
#         v = q.popleft()
#         print(v, end=' ')
#         for u in g[v]:
#             cnt[u] -= 1
#             if cnt[u] == 0:
#                 q.append(u)

# solve()


# 1766 문제집
# pm 02:47 ~ 02:50
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# from heapq import heappush, heappop

# def solve():
#     N, M = map(int, input().split())

#     # cnt, g 초기화 (cnt의 개수 : 먼저 해야하는 것들의 개수)
#     cnt = [0]*(N+1)
#     g = defaultdict(list)
#     for _ in range(M):
#         A, B = map(int, input().split())
#         g[A].append(B)
#         cnt[B] += 1

#     # 처음에 cnt가 0인 (먼저 해도 되는) v를 집어넣는다
#     heap = []
#     for v in range(1, N+1):
#         if cnt[v] == 0:
#             heappush(heap, v)

#     # 위상 정렬 수행
#     while heap:
#         v = heappop(heap)
#         print(v, end=' ')

#         # 하나씩 빼면서 0이면 추가
#         for u in g[v]:
#             cnt[u] -= 1
#             if cnt[u] == 0:
#                 heappush(heap, u)

# solve()

"""
100000000
000000000
000000000
000000000
000000000
000000000
000000000
000000000
000000000

"""

# 2239 스도쿠
# def btr(board, std_x, std_y, num_set_3x3, num_set_x, num_set_y):
#     for x in range(std_x, 9):
#         for y in range(0 if std_x != x else std_y, 9):
#             if board[x][y] == 0:
#                 for i in range(1, 10):
#                     # 같은 3x3 구간 검사 및 같은 행, 열 검사
#                     if i not in num_set_3x3[x//3][y//3]:
#                         if (i not in num_set_x[x]) and (i not in num_set_y[y]):
#                             board[x][y] = i
#                             num_set_3x3[x//3][y//3].add(i)
#                             num_set_x[x].add(i)
#                             num_set_y[y].add(i)

#                             # 스도쿠 완성 (끝 부분이 원래 0인 경우)
#                             if x == 8 and y == 8:
#                                 return board

#                             return_val = btr(board, x, y+1, num_set_3x3, num_set_x, num_set_y)
#                             if return_val != None:
#                                 return return_val

#                             # 인터프리터가 이 주석 부분을 지나간다는 건 스도쿠 완성이 안 되는 경우라는 뜻
#                             # 추가했던 값 다시 취소
#                             board[x][y] = 0
#                             num_set_3x3[x//3][y//3].remove(i)
#                             num_set_x[x].remove(i)
#                             num_set_y[y].remove(i)

#                 return # 이 부분 중요, 한 번에 한 좌표만 해야함

#             # 스도쿠 완성 (끝 부분이 원래 0이 아닌 경우)
#             if x == 8 and y == 8:
#                 # for kx in range(9):
#                 #     print(board[kx])
#                 return board

# def solve():
#     board = [list(map(int, str(input()))) for _ in range(9)]
#     # for x in range(9):
#     #     print(board[x])

#     num_set_3x3 = [[set() for _ in range(3)] for _ in range(3)]
#     num_set_x = [set() for _ in range(9)]
#     num_set_y = [set() for _ in range(9)]

#     for x in range(9):
#         for y in range(9):
#             if board[x][y] != 0:
#                 num_set_3x3[x//3][y//3].add(board[x][y])
#                 num_set_x[x].add(board[x][y])
#                 num_set_y[y].add(board[x][y])
#     # print(num_set_3x3)
#     # print(num_set_x)
#     # print(num_set_y)

#     board = btr(board, 0, 0, num_set_3x3, num_set_x, num_set_y)
#     for x in range(9):
#         print(*board[x], sep='')

# solve()


# 16724 피리 부는 사나이

# import sys
# input = sys.stdin.readline
# from collections import deque

# def find_parent(parent, xy:list):
#     x, y = xy
#     if parent[x][y] != xy:
#         parent[x][y] = find_parent(parent, parent[x][y])

#     return parent[x][y]

# def union_parent(parent, xy_1, xy_2):
#     xy_1 = find_parent(parent, xy_1)
#     xy_2 = find_parent(parent, xy_2)

#     if (xy_1[0] < xy_2[0]) or (xy_1[0] == xy_2[0] and xy_1[1] < xy_2[1]):
#         parent[xy_2[0]][xy_2[1]] = parent[xy_1[0]][xy_1[1]]
#     else:
#         parent[xy_1[0]][xy_1[1]] = parent[xy_2[0]][xy_2[1]]

# def solve():
#     N, M = map(int, input().split())
#     board = [list(input().rstrip()) for _ in range(N)]

#     visited = [[False] * M for _ in range(N)]
#     inc_xy = dict({'U':[-1, 0], 'D':[1, 0], 'L' : [0, -1], 'R' : [0, 1]})
#     # print(inc_xy['U'])

#     # parent 초기화
#     parent = [[[-1, -1] for _ in range(M)] for _ in range(N)]
#     for x in range(N):
#         for y in range(M):
#             parent[x][y] = [x, y]

#     # 분리 집합 만들기
#     for x in range(N):
#         for y in range(M):

#             if not visited[x][y]:
#                 visited[x][y] = True
#                 que = deque([[x, y]])

#                 while que:
#                     x, y = que.popleft()
#                     nx, ny = x + inc_xy[board[x][y]][0], y + inc_xy[board[x][y]][1]
#                     union_parent(parent, [x, y], [nx, ny])
#                     if not visited[nx][ny]:
#                         visited[nx][ny] = True
#                         que.append([nx, ny])

#     # for x in range(N):
#     #     print(parent[x])

#     for x in range(N):
#         for y in range(M):
#             find_parent(parent, [x, y])

#     # for x in range(N):
#     #     print(parent[x])

#     ans = set()
#     for x in range(N):
#         for y in range(M):
#             ans.add(tuple(parent[x][y]))
#     # print(ans)
#     print(len(ans))

# solve()

"""
3 4
DLLL
DLDU
RURU
"""
"""
3 4
DLLL
DLRD
RURU
"""
"""
3 4
RLLL
DLRD
RURU
"""

# import sys
# input = sys.stdin.readline

# def dfs(board, visited, inc_xy, x, y, cnt, group):
#     visited[x][y] = True
#     # print(x, y, cnt)

#     nx, ny = x + inc_xy[board[x][y]][0], y + inc_xy[board[x][y]][1]
#     if not visited[nx][ny]:
#         group[x][y] = dfs(board, visited, inc_xy, nx, ny, cnt, group)
#     else:
#         group[x][y] = cnt if group[nx][ny] == 0 else group[nx][ny]

#     return group[x][y]

# def solve():
#     N, M = map(int, input().split())
#     board = [list(input().rstrip()) for _ in range(N)]

#     visited = [[False]*M for _ in range(N)]
#     inc_xy = dict({'U':[-1, 0], 'D':[1, 0], 'L' : [0, -1], 'R' : [0, 1]})
#     group = [[0]*M for _ in range(N)]

#     cnt = 1
#     for x in range(N):
#         for y in range(M):
#             if not visited[x][y]:
#                 # cnt = dfs(board, visited, inc_xy, x, y, cnt, group)+1
#                 cnt = max(cnt, dfs(board, visited, inc_xy, x, y, cnt, group)+1)

#     # for x in range(N):
#     #     print(group[x])
#     print(cnt-1)

# solve()


# 9466 텀 프로젝트
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# # 결국엔 싸이클이 만들어진다 -> route : set()
# def dfs(N, nums, i, visited, route, have_a_team):
#     visited[i] = True

#     if not visited[nums[i]]:
#         route.add(i)
#         return_num, team_check = dfs(N, nums, nums[i], visited, route, have_a_team)
#         have_a_team[i] = team_check
#         # print(i, have_a_team)
#         return [return_num, team_check] if i != return_num else [-1, 0]

#     else:
#         have_a_team[i] = 1 if (i == nums[i] or nums[i] in route) else 0

#         # nums[i] : 싸이클이 처음으로 시작되는 숫자
#         # 자기 자신으로 싸이클이 끝나면(팀이 되면) [nums[i], 0] 반환
#         return [nums[i], have_a_team[i] if i != nums[i] else 0]

# def solve():
#     for _ in range(int(input())):
#         N = int(input())
#         nums = [0] + list(map(int, input().split()))

#         visited = [False] * (N+1)
#         have_a_team = [0] * (N+1)

#         for i in range(N+1):
#             if not visited[i]:
#                 dfs(N, nums, i, visited, set(), have_a_team)

#         # print(visited)
#         # print(heave_a_team)
#         print(N+1 - sum(have_a_team))

# solve()


# 개선? 조건을 하나 줄였음 대신 1000ms 가량 더 걸림
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# # 결국엔 최소 1개의 싸이클이 만들어진다 -> route : set()
# def dfs(N, nums, i, visited, route, have_a_team):
#     visited[i] = True
#     route.add(i)

#     if not visited[nums[i]]:
#         return_num, team_check = dfs(N, nums, nums[i], visited, route, have_a_team)
#         have_a_team[i] = team_check
#         # print(i, have_a_team)
#         return [return_num, team_check] if i != return_num else [-1, 0]

#     else:
#         have_a_team[i] = 1 if nums[i] in route else 0

#         # nums[i] : 싸이클이 처음으로 시작되는 숫자
#         # 자기 자신으로 싸이클이 끝나면(팀이 되면) [nums[i], 0] 반환
#         return [nums[i], have_a_team[i] if i != nums[i] else 0]

# def solve():
#     for _ in range(int(input())):
#         N = int(input())
#         nums = [0] + list(map(int, input().split()))

#         visited = [False] * (N+1)
#         have_a_team = [0] * (N+1)

#         for i in range(N+1):
#             if not visited[i]:
#                 dfs(N, nums, i, visited, set(), have_a_team)

#         # print(visited)
#         # print(heave_a_team)
#         print(N+1 - sum(have_a_team))

# solve()


# 노마드코더 NOMAD_CODER FULL_STACK
# FS = [  '01000010', '01100101', '00100000', '01100110', '01110010', '01100101',\
#         '01100101', '00101110', '00100000', '01000010', '01100101', '00100000',\
#         '01101000', '01100001', '01110000', '01110000', '01111001', '00101110',\
#         '00100000', '01000010', '01100101', '00100000', '01100010', '01110010',\
#         '01100001', '01110110', '01100101', '00100001']
# # print(FS)

# def make_bin_to_dec(num:str):
#     num = list(map(int, num))
#     k = 1
#     return_val = 0

#     for n in num[::-1]:
#         return_val += k*n
#         k *= 2
#     return return_val

# def solve():
#     # cnt = 0
#     for num in FS:
#         print(chr(make_bin_to_dec(num)), end=' ')
#     print()
#         # cnt += 1
#         # if cnt % 6 == 0:
#         #     print()

# solve()


# 2623 음악 프로그램
# pm 08:50 ~ 09:00
# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque

# def solve():
#     N, M = map(int, input().split())

#     g = defaultdict(list)
#     cnt = [0]*(N+1)
#     for _ in range(M):
#         nums = list(map(int, input().split()))
#         for k in range(1, nums[0]):
#             g[nums[k]].append(nums[k+1])
#             cnt[nums[k+1]] +=1
#     # print(g)
#     # print(cnt)

#     q = deque()
#     for idx in range(1, N+1):
#         if cnt[idx] == 0:
#             q.append(idx)

#     ans = []
#     while q:
#         v = q.popleft()
#         ans.append(v)
#         # print(v, ans)

#         for u in g[v]:
#             cnt[u] -= 1
#             if cnt[u] == 0:
#                 q.append(u)

#     print(*ans if len(ans) == N else [0], sep='\n')

# solve()


# 4386 별자리 만들기
# import sys
# input = sys.stdin.readline
# from heapq import heapify, heappop
# import math

# def distance_between_two_points(point1, point2):
#     return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)

#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a

# def solve():
#     N = int(input())

#     xys = [list(map(float, input().split())) for _ in range(N)]
#     parent = [i for i in range(N)]

#     heap = []
#     for i in range(N-1):
#         for j in range(i+1, N):
#             heap.append([distance_between_two_points(xys[i], xys[j]), i, j])
#     heapify(heap)

#     ans = 0
#     while heap:
#         dist, a, b = heappop(heap)
#         if find_parent(parent, a) != find_parent(parent, b):
#             union_parent(parent, a, b)
#             ans += dist

#     print(ans)

# solve()


# 1043 거짓말
# import sys
# input = sys.stdin.readline
# from collections import deque

# def solve():
#     N, M = map(int, input().split())
#     who_knows_truth = list(map(int, input().split()))[1:]

#     # 누구랑 누가 만났었는지를 저장하는 g
#     g = [set() for _ in range(N+1)]
#     parties = [list(map(int, input().split())) for _ in range(M)]
#     for party in parties:
#         for i in range(1, party[0]):
#             for j in range(i+1, party[0]+1):
#                 g[party[i]].add(party[j])
#                 g[party[j]].add(party[i])
#                 # print(i, j)
#     # print(g)

#     # 진실을 아는 사람들과 이어져 있으면 can_tell_truth[i] = False
#     q = deque(who_knows_truth)
#     visited = [False] * (N+1)
#     can_tell_truth = [True] * (N+1)

#     while q:
#         i = q.popleft()
#         visited[i] = True
#         can_tell_truth[i] = False

#         for j in g[i]:
#             if not visited[j]:
#                 visited[j] = True # 효율 개선
#                 q.append(j)
#     # print(can_tell_truth)

#     # 각 파티당 진실을 아는 사람이 1명도 없다면 ans += 1
#     ans = 0
#     for party in parties:
#         pos = True
#         for i in party[1:]:
#             if not can_tell_truth[i]:
#                 pos = False
#                 break

#         if pos:
#             ans +=1

#     print(ans)

# solve()


# 12851 숨바꼭질 2
# 메모리 초과
# from collections import deque

# def solve():
#     N, K = map(int, input().split())
#     q = deque([N])
#     limit = int(1e5+5e4)
#     # print(limit)
#     # 모든 경우를 체크해야 하므로 visited는 없음

#     ans = 0
#     while q:
#         pos = False
#         cnt = 0
#         for _ in range(len(q)):
#             v = q.popleft()
#             if v == K:
#                 pos = True
#                 cnt += 1

#             if v+1 <= limit:
#                 q.append(v+1)
#             if v-1 >= 0:
#                 q.append(v-1)
#             if v*2 <= limit:
#                 q.append(v*2)

#         if pos:
#             print(ans, cnt, sep='\n')
#             break

#         ans += 1

# solve()


# 시간 초과 -> 해결(밑의 배열 방식보다 이게 더 빠르다 ㅎㅎㅎ)
# from collections import defaultdict, deque

# def solve():
#     N, K = map(int, input().split())

#     if N >= K:
#         print(N-K, 1, sep='\n')
#         return

#     q = deque([[N, 1]])
#     limit = int(1e5)
#     # print(limit)
#     # 모든 경우를 체크해야 하므로 visited는 없음
#     visited = [False]*(limit+1)
#     visited[N] = True

#     ans = 1
#     while q:
#         num_dict = defaultdict(int)

#         for _ in range(len(q)):
#             key, val = q.popleft()
#             # num_dict[key] += val

#             if key+1 <= limit and not visited[key+1]:
#                 num_dict[key+1] += val
#             if key-1 >= 0 and not visited[key-1]:
#                 num_dict[key-1] += val
#             if key*2 <= limit and not visited[key*2]:
#                 num_dict[key*2] += val

#         # target 숫자 K가 있으면
#         if K in num_dict:
#             print(ans, num_dict[K], sep='\n')
#             break

#         for key, val in num_dict.items():
#             q.append([key, val])
#             visited[key] = True
#         # print(num_dict)

#         ans += 1

# solve()


# 시간 초과
# def solve():
#     N, K = map(int, input().split())

#     if N >= K:
#         print(N-K, 1, sep='\n')
#         return

#     limit = int(1e5)
#     # print(limit)
#     visited = [False] * (limit+1)
#     visited[N] = True

#     pre_set = set({N})
#     pre_cnt = [0] * (limit+1)
#     pre_cnt[N] = 1

#     ans = 1
#     while pre_set:
#         new_set = set()
#         new_cnt = [0] * (limit+1)

#         for v in pre_set:
#             if v+1 <= limit and not visited[v+1]:
#                 new_cnt[v+1] += pre_cnt[v]
#                 new_set.add(v+1)
#             if v-1 >= 0 and not visited[v-1]:
#                 new_cnt[v-1] += pre_cnt[v]
#                 new_set.add(v-1)
#             if v*2 <= limit and not visited[v*2]:
#                 new_cnt[v*2] += pre_cnt[v]
#                 new_set.add(v*2)

#         # target 숫자 K가 있으면
#         if new_cnt[K] != 0:
#             print(ans, new_cnt[K], sep='\n')
#             break

#         for v in new_set:
#             visited[v] = True

#         pre_set = new_set
#         pre_cnt = new_cnt

#         ans += 1

# solve()


# 1504 특정한 최단 경로
# 다익스트라, 플로이드-와셜
# pm 02:20 ~ 03:10

"""
3 2
1 2 1
2 3 1
1 2
"""
"""
3 2
1 2 1
2 3 1
2 3
"""

# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque

# def dijkstra(N, g, start_v):
#     q = deque([[0, start_v]])
#     for line in g[start_v]:
#         q.append(line)
#     # print(start_v, target_v, heap)

#     dist = [float("INF")]*(N+1)
#     dist[start_v] = 0
#     # print(g)

#     while q:
#         dist_sum_to_v, v = q.popleft()
#         for dist_to_next_v, next_v in g[v]:
#             if dist[next_v] > dist_sum_to_v + dist_to_next_v:
#                 dist[next_v] = dist_sum_to_v + dist_to_next_v
#                 q.append([dist_sum_to_v + dist_to_next_v, next_v])

#     return dist

# def solve():
#     N, E = map(int, input().split())

#     g = defaultdict(list)
#     for _ in range(E):
#         a, b, c = map(int, input().split())
#         g[a].append([c, b])
#         g[b].append([c, a])
#     # print(g)

#     v1, v2 = map(int, input().split())
#     # print(v1, v2)

#     from_1 = dijkstra(N, g, 1)
#     from_v1 = dijkstra(N, g, v1)
#     from_v2 = dijkstra(N, g, v2)
#     # print(from_1, from_v1, from_v2)

#     ans = min(from_1[v1]+from_v1[v2]+from_v2[N], from_1[v2]+from_v2[v1]+from_v1[N])
#     print(ans if ans != float("INF") else -1)

# solve()


# 플로이드-와셜 : O(N^3) -> 시간 초과
# import sys
# input = sys.stdin.readline

# def solve():
#     N, M = map(int, input().split())

#     # dist 초기화
#     dist = [[float("INF") for _ in range(N+1)] for _ in range(N+1)]
#     for _ in range(M):
#         a, b, c = map(int, input().split())
#         dist[a][b] = c # 임의의 두 정점 u와 v사이에는 간선이 최대 1개이므로 min 필요 없음
#         dist[b][a] = c

#     for x in range(N+1):
#         dist[x][x] = 0
#         # print(dist[x])

#     v1, v2 = map(int, input().split())

#     # 플로이드-와셜
#     for k in range(1, N+1):
#         for x in range(1, N+1):
#             for y in range(1, N+1):
#                 dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])

#     ans = min(dist[1][v1]+dist[v1][v2]+dist[v2][N], dist[1][v2]+dist[v2][v1]+dist[v1][N])
#     print(ans if ans != float("INF") else -1)

# solve()


# 13913 숨바꼭질4
# pm 03:58 ~ 04:19

# import sys
# sys.setrecursionlimit(int(1e6))

# def btr(move_type, n):
#     if move_type[n] != -1:
#         if move_type[n] == 0:
#             btr(move_type, n-1)
#         elif move_type[n] == 1:
#             btr(move_type, n+1)
#         else: # 2
#             btr(move_type, n//2)

#     print(n, end=' ')

# def solve():
#     N, K = map(int, input().split())

#     if N == K:
#         print(0, N, sep='\n')
#         return

#     limit = int(1e5)
#     visited = [False] * (limit+1)
#     visited[N] = True
#     move_type = [-1] * (limit+1)

#     now_set = set({N})
#     cnt = 1

#     while now_set:
#         # print(cnt, now_set)
#         next_set = set()

#         for v in now_set:
#             if v+1 <= limit and not visited[v+1]:
#                 next_set.add(v+1)
#                 visited[v+1] = True
#                 move_type[v+1] = 0
#             if v-1 >= 0 and not visited[v-1]:
#                 next_set.add(v-1)
#                 visited[v-1] = True
#                 move_type[v-1] = 1
#             if v*2 <= limit and not visited[v*2]:
#                 next_set.add(v*2)
#                 visited[v*2] = True
#                 move_type[v*2] = 2

#         if K in next_set:
#             print(cnt)
#             break

#         now_set = next_set
#         cnt += 1

#     # print(move_type[:20])
#     btr(move_type, K)

# solve()


# 18290번 - NM과 K (1)
# import sys
# input = sys.stdin.readline

# def btr(board, visited, val, max_ans, cnt, K, x, y, N, M, inc_xy):
#     val += board[x][y]

#     if cnt == K:
#         max_ans[0] = max(max_ans[0], val)
#     else:
#         visited[x][y] = True
#         for nx in range(x, N):
#             for ny in range(0 if nx != x else y, M):
#                 if not visited[nx][ny]:
#                     pos = True
#                     for px, py in inc_xy:
#                         kx, ky = nx + px, ny + py
#                         if 0 <= kx < N and 0 <= ky < M and visited[kx][ky]:
#                             # print(x, y, "//", nx, ny, kx, ky)
#                             pos = False
#                             break

#                     if pos:
#                         btr(board, visited, val, max_ans, cnt+1, K, nx, ny, N, M, inc_xy)

#         visited[x][y] = False

# def solve():
#     N, M, K = map(int, input().split())

#     board = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[False]*M for _ in range(N)]
#     max_ans = [-int(1e6)]
#     inc_xy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

#     for x in range(N):
#         for y in range(M):
#             btr(board, visited, 0, max_ans, 1, K, x, y, N, M, inc_xy)

#     print(max_ans[0])

# solve()


# 25628 햄버거 만들기
# A, B = map(int, input().split())
# print(min(A//2, B))


# 10830 행렬 제곱
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# # 행렬 곱셈
# def mul_mem(N, m1, m2):
#     matrix = [[0]*N for _ in range(N)]

#     for x in range(N):
#         for y in range(N):
#             for k in range(N):
#                 matrix[x][y] += m1[x][k] * m2[k][y]

#             matrix[x][y] %= 1000

#     return matrix

# # 행렬 mem 초기화 (divide and conquer)
# def make_mem(N, A, n, mem):
#     if n not in mem:
#         make_mem(N, A, n//2, mem)
#         mem[n] = mul_mem(N, mem[n//2], mem[n//2])

# def solve():
#     N, B = map(int, input().split())
#     A = [list(map(int, input().split())) for _ in range(N)]
#     mem = defaultdict(list)
#     mem[1] = A
#     # print(A, mem)

#     # B 이하의 가장 큰 2^N 값 찾기
#     max_2_power_N = 1
#     while max_2_power_N <= B:
#         max_2_power_N *= 2
#     max_2_power_N //= 2

#     # mem 만들기 : A^(2^N)을 저장
#     make_mem(N, A, max_2_power_N, mem)
#     # print(mem)

#     # 단위행렬 초기화
#     now_m = [[0]*N for _ in range(N)]
#     for x in range(N):
#         now_m[x][x] = 1

#     # A^B 만들기
#     while max_2_power_N > 0:
#         if (B // max_2_power_N) >= 1:
#             B -= max_2_power_N
#             now_m = mul_mem(N, now_m, mem[max_2_power_N])
#         max_2_power_N //= 2

#     # 출력
#     for x in range(N):
#         print(*now_m[x])

# solve()


# 11444 피보나치 수 6
# n = 1
# a, b = 1, 1
# mod = int(1e9)+7
# # while n <= int(1e18):
# while n <= 100:
#     print(n, n+1, a, b)
#     a, b = (21*a+34*b)%mod, (34*a+55*b)%mod
#     n += 10

# 백준 블로그 참고해서 개선
# 참고 : https://www.acmicpc.net/blog/view/28
# mod = int(1e9)+7

# def matrix_mul(matrix_a, matrix_b):
#     matrix_return = [[0, 0], [0, 0]]
#     for x in range(2):
#         for y in range(2):
#             for k in range(2):
#                 matrix_return[x][y] += matrix_a[x][k] * matrix_b[k][y]

#             matrix_return[x][y] %= mod

#     # for x in range(2):
#     #     print(matrix_return[x])
#     # print()

#     return matrix_return

# def solve():
#     n = int(input())

#     ans = [[1, 0], [0, 1]] # 단위 행렬 E
#     a = [[1, 1], [1, 0]]

#     while n > 0:
#         if n % 2 == 1:
#             ans = matrix_mul(ans, a)

#         a = matrix_mul(a, a)
#         n //= 2

#     print(ans[0][1])

# solve()


# 2096 내려가기
# import sys
# input = sys.stdin.readline

# N = int(input())
# max_dp, min_dp = [0]*3, [0]*3

# for _ in range(N):
#     scores = list(map(int, input().split()))
#     new_max_dp, new_min_dp = [0]*3, [0]*3

#     new_max_dp[0] = scores[0] + max(max_dp[0], max_dp[1])
#     new_min_dp[0] = scores[0] + min(min_dp[0], min_dp[1])

#     new_max_dp[1] = scores[1] + max(max_dp[0], max_dp[1], max_dp[2])
#     new_min_dp[1] = scores[1] + min(min_dp[0], min_dp[1], min_dp[2])

#     new_max_dp[2] = scores[2] + max(max_dp[1], max_dp[2])
#     new_min_dp[2] = scores[2] + min(min_dp[1], min_dp[2])

#     max_dp, min_dp = new_max_dp, new_min_dp

# print(max(max_dp), min(min_dp))


# 17356 욱 제
# A, B = map(int, input().split())
# print(1/(1+10**((B-A)/400)))


# 1238 파티
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# from heapq import heappush, heappop

# def go(heap, X, g, visited, dist, check):
#     while heap:
#         val, v = heappop(heap)
#         if v == X and check:
#             return val

#         if not visited[v]:
#             visited[v] = True
#             dist[v] = val
#             # print(visited, v, check)

#             for val_u, u in g[v]:
#                 if not visited[u]:
#                     heappush(heap, [val+val_u, u])

# def solve():
#     N, M, X = map(int, input().split())
#     g = defaultdict(list)
#     for _ in range(M):
#         a, b, c = map(int, input().split())
#         g[a].append([c, b])

#     dist_go = [0]*(N+1)

#     INF = int(1e7)
#     for i in range(N+1):
#         heap = []
#         heappush(heap, [0, i])
#         dist_go[i] = go(heap, X, g, [False]*(N+1), [INF]*(N+1), True)
#     # print(dist_go)

#     dist_back = [INF]*(N+1)
#     heap = []
#     heappush(heap, [0, X])
#     go(heap, X, g, [False]*(N+1), dist_back, False)
#     # print(dist_back)

#     ans = 0
#     for i in range(1, N+1):
#         ans = max(ans, dist_go[i]+dist_back[i])
#     print(ans)

# solve()


# 개선
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# from heapq import heappush, heappop

# def go(g, N, i, X, check):
#     heap = []
#     heappush(heap, [0, i])
#     dist = [float("inf")]*(N+1)

#     while heap:
#         val, v = heappop(heap)
#         if v == X and check:
#             return val

#         if dist[v] > val:
#             dist[v] = val

#             for val_u, u in g[v]:
#                 cost = val + val_u
#                 if dist[u] > cost:
#                     heappush(heap, [cost, u])

#     return dist

# def solve():
#     N, M, X = map(int, input().split())
#     g = defaultdict(list)
#     for _ in range(M):
#         a, b, c = map(int, input().split())
#         g[a].append([c, b])

#     dist_go = [float("inf")]*(N+1)
#     for i in range(N+1):
#         dist_go[i] = go(g, N, i, X, True)
#     # print(dist_go)

#     dist_back = go(g, N, X, X, False)
#     # print(dist_back)

#     ans = 0
#     for i in range(1, N+1):
#         ans = max(ans, dist_go[i]+dist_back[i])
#     print(ans)

# solve()


# que를 이용한 방법
# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque

# def dijkstra(g, N, start):
#     dist = [float("inf")]*(N+1)
#     dist[start] = 0
#     q = deque([[start, 0]])

#     while q:
#         v, val = q.popleft()
#         for u, val_u in g[v]:
#             if dist[u] > val+val_u:
#                 dist[u] = val+val_u
#                 q.append([u, val+val_u])

#     return dist

# def solve():
#     N, M, X = map(int, input().split())
#     g = defaultdict(list)
#     for _ in range(M):
#         a, b, c = map(int, input().split())
#         g[a].append([b, c])

#     dist_go = [float("inf")]*(N+1)
#     for i in range(1, N+1):
#         dist_go[i] = dijkstra(g, N, i)[X]
#     # print(dist_go)

#     dist_back = dijkstra(g, N, X)
#     # print(dist_back)

#     ans = 0
#     for i in range(1, N+1):
#         ans = max(ans, dist_go[i]+dist_back[i])
#     print(ans)

# solve()


# 2042 구간 합 구하기
# 세그먼트 트리
# import sys
# input = sys.stdin.readline

# def init(start, end, node, nums, tree):
#     if(start == end):
#         tree[node] = nums[start]
#         return tree[node]

#     mid = (start + end) // 2
#     tree[node] = init(start, mid, node*2, nums, tree) + init(mid+1, end, node*2+1, nums, tree)
#     return tree[node]

# def sum_tree(start, end, node, left, right, tree):
#     if (left > end) | (right < start): return 0;
#     elif (left <= start) & (end <= right): return tree[node];

#     mid = (start + end) // 2
#     return sum_tree(start, mid, node*2, left, right, tree) + sum_tree(mid+1, end, node*2+1, left, right, tree)

# def update(start, end, node, index, diff, tree):
#     # if index < start | index > end: return;
#     if (index < start) | (index > end): return;
#     tree[node] += diff
#     if (start == end): return;

#     mid = (start + end) // 2
#     update(start, mid, node*2, index, diff, tree)
#     update(mid+1, end, node*2+1, index, diff, tree)

# def solve():
#     N, M, K = map(int, input().split())
#     nums = [int(input()) for _ in range(N)]
#     # print(nums)
#     tree = [0]*(4*N)
#     init(0, N-1, 1, nums, tree)
#     # print(tree)

#     for _ in range(M+K):
#         a, b, c = map(int, input().split())
#         if a == 1:
#             update(0, N-1, 1, b-1, c-nums[b-1], tree)
#             nums[b-1] = c
#             # print("updated", tree)
#         else:
#             print(sum_tree(0, N-1, 1, b-1, c-1, tree))

# solve()

"""
4 2
1
2
3
4
1 4
3 4
"""
"""
3 2
1
2
3
1 3
2 3
"""
"""
2 2
1
2
"""
# 2357 최댓값과 최솟값

# 세그먼트 트리에서 체크 포인트
# init의 return은 2번 (1. start==end 일 때, 2. 그 외의 경우 함수 마지막에)
# mid 잡고 start~mid / mid+1, end
# init을 재귀로 타고 가면서 node*2

# show()의 범위
# start, end가 재귀를 타고 가면서 바뀌는 범위이므로 이 범위가 left right 안에 속하는 지를 봐야함

# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# def init(start, end, node, nums, tree, check_child):
#     # global cnt
#     # cnt += 1
#     if start == end:
#         tree[node] = [nums[start], nums[start]]
#         # cnt -= 1
#         return tree[node]

#     mid = (start+end)//2
#     if check_child:
#         tree[node][0] = min(init(start, mid, node*2, nums, tree, True)[0], init(mid+1, end, node*2+1, nums, tree, True)[0])
#         tree[node][1] = max(init(start, mid, node*2, nums, tree, False)[1], init(mid+1, end, node*2+1, nums, tree, False)[1])
#     return tree[node] # 놓친 부분

# def show(start, end, node, left, right, tree):
#     # global cnt
#     # cnt += 1
#     if (right < start) or (end < left): return [INF, 1]
#     # elif (start <= left) and (right <= end): # 틀린 부분
#     elif (left <= start) and (end <= right):
#         return tree[node]

#     mid = (start+end)//2
#     left_child, right_child = show(start, mid, node*2, left, right, tree), show(mid+1, end, node*2+1, left, right, tree)
#     return [min(left_child[0], right_child[0]), max(left_child[1], right_child[1])]

# def cal_tree_len(N):
#     tree_len = 1
#     while tree_len < N:
#         tree_len *= 2
#     tree_len *= 2
#     return tree_len

# def solve():
#     N, M = map(int, input().split())
#     nums = [int(input()) for _ in range(N)]

#     tree = [[0, 0] for _ in range(cal_tree_len(N))]
#     # print("tree_len ", cal_tree_len(N))

#     # global cnt
#     # cnt = 0
#     init(0, N-1, 1, nums, tree, True)
#     # print(tree)

#     for _ in range(M):
#         l, r = map(int, input().split())
#         print(*show(0, N-1, 1, l-1, r-1, tree))
#     # print("cnt", cnt)

# solve()

# test code
# def f():
#     global cnt
#     cnt += 1
#     return float("inf")

# def solve():
#     global cnt
#     cnt = 0

#     min(f(), f())
#     print(cnt)

# solve()


# import math
# print(math.log2(int(1e5)))


# 11505 구간 곱 구하기
# pm 02:32 ~ 03:31

"""
5 2 2
1
2
3
4
5
2 1 4
2 1 5
"""

# 복습
# 놓친 부분 : node*2, node*2+1

# import sys
# input = sys.stdin.readline
# mod = int(1e9)+7

# def init(s, e, node, nums, tree):
#     if s == e:
#         tree[node] = nums[s]
#         return tree[node]

#     mid = (s+e)//2
#     tree[node] = (init(s, mid, node*2, nums, tree)*init(mid+1, e, node*2+1, nums, tree))%mod
#     return tree[node] # 놓친 부분

# def show(s, e, node, left, right, tree):
#     if (e < left) or (right < s): return 1;
#     elif (left <= s) and (e <= right): return tree[node]; # else X
#     # print("[show] s, e", s, e)

#     mid = (s+e)//2
#     return (show(s, mid, node*2, left, right, tree)*(show(mid+1, e, node*2+1, left, right, tree)))%mod

# def update(s, e, node, index, diff, tree):
#     # 타겟 index를 벗어나는 범위의 node면 return[node];
#     if not (s <= index <= e):
#         # return; # 놓친 부분
#         return tree[node]; # return 1; 도 아님

#     # 최하단 자식 노드
#     if s == e:
#         # 타겟이면 수정
#         if s == index:
#             tree[node] = diff
#         return tree[node]

#     mid = (s+e)//2
#     tree[node] = (update(s, mid, node*2, index, diff, tree)*update(mid+1, e, node*2+1, index, diff, tree))%mod
#     return tree[node]

# def cal_tree_len(N):
#     tree_len = 1
#     while tree_len < N:
#         tree_len *= 2
#     tree_len *= 2 # 놓친 부분
#     return tree_len

# def solve():
#     N, M, K = map(int, input().split())
#     nums = [int(input()) for _ in range(N)]
#     tree = [1]*(cal_tree_len(N))
#     init(0, N-1, 1, nums, tree)
#     # print(tree)

#     # 구간 곱 출력
#     for _ in range(M+K):
#         a, b, c = map(int, input().split())
#         if a == 1:
#             update(0, N-1, 1, b-1, c, tree)
#             nums[b-1] = c
#             # print("nums", nums)
#         else:
#             print(show(0, N-1, 1, b-1, c-1, tree))
#         # print("tree", tree)

# solve()


# 14428 수열과 쿼리 16
"""
5
5 4 3 2 1
6
2 1 3
2 1 4
1 5 3
2 3 5
1 4 3
2 3 5
"""
# update 범위 벗어나는 부분에서 헤맸다
# 아까랑 같은 실수라서 이제는 확실하게 알겠다 :)

# import sys
# input = sys.stdin.readline

# INF = int(1e9)+1

# def init(s, e, nd, nums, tree):
#     if s == e:
#         tree[nd] = [nums[s], s]
#         return tree[nd]

#     mid = (s+e)//2
#     lnd, rnd = init(s, mid, nd*2, nums, tree), init(mid+1, e, nd*2+1, nums, tree)
#     tree[nd] = lnd if lnd[0] <= rnd[0] else rnd
#     return tree[nd]

# def show(s, e, nd, l, r, tree):
#     if (e < l) or (r < s): return [INF, INF];
#     elif (l <= s) and (e <= r): return tree[nd];

#     mid = (s+e)//2
#     lnd, rnd = show(s, mid, nd*2, l, r, tree), show(mid+1, e, nd*2+1, l, r, tree)
#     # 놓친 부분, show라서 값을 노드에 값을 대입 하는 부분이 있으면 안 됨
#     # tree[nd] = (lnd if lnd[0] <= rnd[0] else rnd)
#     return lnd if lnd[0] <= rnd[0] else rnd

# def update(s, e, nd, idx, val, tree):
#     # if not (s <= idx <= e): return [INF, INF];
#     if not (s <= idx <= e):
#         # print("haha", s, e, idx, tree[nd])
#         return tree[nd];

#     if s == e == idx:
#         # print("im idx?", s, e, idx)
#         tree[nd] = [val, idx];
#         return tree[nd];

#     mid = (s+e)//2
#     lnd, rnd = update(s, mid, nd*2, idx, val, tree), update(mid+1, e, nd*2+1, idx, val, tree)
#     tree[nd] = (lnd if lnd[0] <= rnd[0] else rnd)
#     return tree[nd]

# def cal_tree_len(N):
#     tl = 1
#     while tl < N:
#         tl *= 2
#     tl *= 2
#     return tl

# def solve():
#     N = int(input())
#     nums = list(map(int, input().split()))
#     M = int(input())
#     # value, value's_index
#     tree = [[INF, INF] for _ in range(cal_tree_len(N))]
#     init(0, N-1, 1, nums, tree)
#     # print(tree)

#     for _ in range(M):
#         a, b, c = map(int, input().split())
#         if a == 1:
#             update(0, N-1, 1, b-1, c, tree)
#         else:
#             print(show(0, N-1, 1, b-1, c-1, tree)[1]+1)
#         # print(tree)

# solve()


# 1967 트리의 지름
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# sys.setrecursionlimit(int(1e5))

# def dfs(g, v):
#     # print("v", v)
#     # 가장 큰 값, 두 번째로 큰 값, 현재까지 체크한 트리의 지름
#     first_max, second_max, ans = 0, 0, 0

#     for next_v, cost in g[v]:
#         next_cost, this_ans = dfs(g, next_v)
#         ans = max(ans, this_ans)

#         this_cost = next_cost + cost
#         if first_max <= this_cost:
#             second_max = first_max
#             first_max = this_cost

#         elif second_max < this_cost:
#             second_max = this_cost

#     # print(v, first_max, second_max, ans)
#     return [first_max, max((first_max + second_max), ans)]

# def solve():
#     n = int(input())
#     g = defaultdict(list)
#     for _ in range(n-1):
#         a, b, c = map(int, input().split())
#         g[a].append([b, c])

#     # print("dfs start =====")
#     # 정점은 1부터
#     print(dfs(g, 1)[1])

# solve()


# 14725 개미굴
# import sys
# input = sys.stdin.readline

# def init(g, foods, idx):
#     # print("now : ", foods, idx)
#     if foods[idx] not in g:
#         g[foods[idx]] = dict()

#     foods[0] -= 1
#     if foods[0] > 0:
#         init(g[foods[idx]], foods, idx+1)

# def show(g, depth):
#     g = sorted(g.items(), key=lambda x:(x[0]))
#     for key, next_g in g:
#         print('--'*depth, key, sep='')
#         show(next_g, depth+1)

# def solve():
#     N = int(input())
#     g = dict()

#     # 입력 받고 초기화
#     for _ in range(N):
#         foods = list(input().split())
#         foods[0] = int(foods[0])
#         init(g, foods, 1)
#         # print("total_g", g)

#     # 예제 출력과 같은 format으로 출력
#     show(g, 0)

# solve()


# 1937 욕심쟁이 판다

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(int(1e6))

# def dfs(N, board, dp, inc_xy, x, y):
#     if dp[x][y] != -1:
#         return dp[x][y]

#     next_cnt = 0
#     for px, py in inc_xy:
#         nx, ny = x+px, y+py
#         if 0 <= nx < N and 0 <= ny < N and board[x][y] < board[nx][ny]:
#             next_cnt = max(next_cnt, dfs(N, board, dp, inc_xy, nx, ny))

#     dp[x][y] = next_cnt+1
#     return dp[x][y]

# def solve():
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     dp = [[-1]*N for _ in range(N)]
#     inc_xy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

#     for x in range(N):
#         for y in range(N):
#             dfs(N, board, dp, inc_xy, x, y)

#     # for x in range(N):
#     #     print(dp[x])

#     print(max([max(dp[x]) for x in range(N)]))

# solve()


# 2170 선 긋기
# import sys
# input = sys.stdin.readline

# def solve():
#     N = int(input())
#     lines = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(x[0]))
#     INF = int(1e9)

#     ans, pre_l, pre_r = 0, -INF, -INF
#     for now_l, now_r in lines:
#         # 합치기 불가
#         if pre_r < now_l:
#             ans += pre_r - pre_l
#             pre_l, pre_r = now_l, now_r
#         # 합치기 가능
#         else:
#             pre_r = max(pre_r, now_r)

#     ans += pre_r - pre_l
#     print(ans)

# solve()


# 17070 파이프 옮기기
# import sys
# input = sys.stdin.readline

# def solve():
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]

#     # dp 정의 : 각 좌표는 파이프의 마무리 지점에 대해서 합산
#     # 0은 ㅡ,  1은 우하단 대각선, 2는 ㅣ 방향, 파이프를 합산
#     dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
#     # 0번째 행 1번째 열 0번(ㅡ)
#     dp[0][1][0] = 1

#     # 0번 행 초기화
#     for y in range(2, N):
#         if board[0][y] == 0:
#             dp[0][y][0] = 1
#         else:
#             break

#     # 1번 행부터 dp값 메모이제이션
#     for x in range(1, N):
#         for y in range(N):
#             if board[x][y] == 0:
#                 dp[x][y][2] = dp[x-1][y][1] + dp[x-1][y][2]

#                 # 대각선은 추가로 사이드에 벽이 없는지 확인
#                 if y >= 2 and board[x-1][y] == board[x][y-1] == 0:
#                     dp[x][y][1] = sum(dp[x-1][y-1])

#                 if y >= 3:
#                     dp[x][y][0] = dp[x][y-1][0] + dp[x][y-1][1]

#     # 확인용 코드
#     # print()
#     # for x in range(N):
#     #     for y in range(N):
#     #         print(dp[x][y], end= ' ')
#     #     print()

#     print(sum(dp[N-1][N-1]))

# solve()


# 13549 숨바꼭질 3
# pm 03:48 ~ 04:28
# from collections import deque

# def teleport(INF, visited, q, v, sec, K):
#     next_v = 2*v
#     while next_v <= INF:
#         if not visited[next_v][1]:
#             if next_v == K:
#                 print(sec)
#                 return True
#             visited[next_v][1] = True
#             q.append([next_v, sec])
#             next_v *= 2
#         else:
#             break

# def solve():
#     N, K = map(int, input().split())
#     INF = int(1e5)
#     # (+1 or -1 로 방문) / (순간이동으로 방문)
#     visited = [[False, False] for _ in range(INF+1)]

#     q = deque([[N, 0]])
#     visited[N][0] = True

#     if N >= K:
#         print(N-K)
#         return

#     # 순간이동으로 바로 찾아간 경우
#     if teleport(INF, visited, q, N, 0, K):
#         return

#     while q:
#         v, sec = q.popleft()
#         if v+1 == K:
#             print(sec+1)
#             return
#         elif v-1 == K:
#             print(sec+1)
#             return
#         else:
#             if teleport(INF, visited, q, v, sec, K):
#                 return

#         # IndexError
#         # if not visited[v+1][0] and not visited[v+1][1] and v+1 <= INF:
#         if v+1 <= INF and not visited[v+1][0] and not visited[v+1][1]:
#             visited[v+1][0] = True
#             q.append([v+1, sec+1])
#         if  v-1 >= 0 and not visited[v-1][0] and not visited[v-1][1]:
#             visited[v-1][0] = True
#             q.append([v-1, sec+1])

#         # print(q)

# solve()


# from collections import deque

# def solve():
#     N, K = map(int, input().split())
#     INF = int(1e5)
#     visited = [False] * (INF+1)

#     if N >= K:
#         print(N-K)
#         return

#     q = deque([[N, 0]])
#     while q:
#         v, sec = q.popleft()
#         if v == K:
#             print(sec)
#             return

#         # v*2를 먼저 처리해주어야 한다
#         if v*2 <= INF and not visited[v*2]:
#             q.appendleft([v*2, sec])
#             visited[v*2] = True
#         if v+1 <= INF and not visited[v+1]:
#             q.append([v+1, sec+1])
#             visited[v+1] = True
#         if v-1 >= 0 and not visited[v-1]:
#             q.append([v-1, sec+1])
#             visited[v-1] = True

#         # print(q[0])

# solve()


# 2638 치즈
# import sys
# input = sys.stdin.readline
# from collections import deque

# def board_clear(N, board):
#     for x in range(N):
#         if sum(board[x]) != 0:
#             return False
#     return True

# def solve():
#     N, M = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     inc_xy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

#     hr = 0
#     while not board_clear(N, board):
#         cnt = [[0]*M for _ in range(N)]
#         visited = [[False]*M for _ in range(N)]
#         visited[0][0] = True
#         q = deque([[0, 0]])

#         while q:
#             x, y = q.popleft()
#             for px, py in inc_xy:
#                 nx, ny = x + px, y + py
#                 if 0 <= nx < N and 0 <= ny < M:
#                     if board[nx][ny] != 0:
#                         cnt[nx][ny] += 1

#                     # board[nx][ny] == 0
#                     elif not visited[nx][ny]:
#                         visited[nx][ny] = True
#                         q.append([nx, ny])

#         for x in range(N):
#             for y in range(M):
#                 if cnt[x][y] >= 2:
#                     board[x][y] = 0

#         hr += 1
#         # print(hr)

#     print(hr)

# solve()


# 2631 줄 세우기
# N = int(input())
# nums = [int(input()) for _ in range(N)] # int() 미처리 실수
# dp = [1]*N

# for i in range(1, N):
#     for j in range(0, i):
#         if nums[i] > nums[j] and dp[i] == dp[j]:
#             dp[i] = dp[j]+1

# print(N-max(dp))


# 1918 후위 표기식
"""
(A*B+C)/D
"""
# from string import ascii_uppercase

# exp = list(input())
# # print(exp)

# alpha = set(ascii_uppercase)
# # print(upper)

# ans = ""
# symbols = []
# depth = 0

# for e in exp:
#     if e in alpha:
#         ans += e
#     else:
#         if e == '(':
#             depth += 1
#             continue

#         elif e == ')':
#             while symbols and symbols[-1][0] >= depth:
#                 ans += symbols.pop()[1]
#             depth -= 1
#             continue

#         elif e in ['+', '-']:
#             while symbols and symbols[-1][0] >= depth:
#                 ans += symbols.pop()[1]

#         else:
#             while symbols and symbols[-1][0] >= depth and symbols[-1][1] in ['*', '/']:
#                 ans += symbols.pop()[1]

#         symbols.append([depth, e])

# while symbols:
#     ans += symbols.pop()[1]

# print(ans)


# 11657 타임머신
# import sys
# input = sys.stdin.readline
# INF = float("inf")

# def bellman_ford(N, edges, dist):
#     for i in range(N):
#         for start, end, d in edges:
#             if dist[start] != INF and dist[end] > dist[start]+d:
#                 if i == N-1:
#                     return -1
#                 dist[end] = dist[start]+d

#     return dist[2:]

# def solve():
#     N, M = map(int, input().split())
#     edges = [list(map(int, input().split())) for _ in range(M)]

#     dist = [INF]*(N+1)
#     dist[1] = 0
#     # print(dist)

#     res = bellman_ford(N, edges, dist)
#     if res == -1:
#         print(-1)
#     else:
#         for i in res:
#             print(i) if i != INF else print(-1)

# solve()


# 1865 웜홀
# import sys
# input = sys.stdin.readline
# # INF = float("inf")

# def bellman_ford(N, dist, edges):
#     for i in range(N):
#         for S, E, T in edges:
#             # if dist[S] != INF and dist[E] > dist[S] + T:
#             if dist[E] > dist[S] + T:
#                 if i == N-1:
#                     return "YES"
#                 dist[E] = dist[S] + T

#     return "NO"

# def solve():
#     for _ in range(int(input())):
#         N, M, W = map(int, input().split())

#         # dist = [INF]*(N+1)
#         dist = [0]*(N+1)
#         edges = []
#         for _ in range(M):
#             S, E, T = map(int, input().split())
#             edges.append([S, E, T])
#             edges.append([E, S, T])

#         for _ in range(W):
#             S, E, T = map(int, input().split())
#             edges.append([S, E, -T])

#         # dist[1] = 0
#         print(bellman_ford(N, dist, edges))

# solve()


# 3665 최종 순위
# 문제를 잘못 이해했다
# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque

# def topology_sort(n, nums, news):
#     cnt = [0]*(n+1)
#     g = defaultdict(list)
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if tuple([nums[i], nums[j]]) in news or tuple([nums[j], nums[i]]) in news:
#                 cnt[nums[i]] += 1
#                 g[nums[j]].append(nums[i])
#             else:
#                 cnt[nums[j]] += 1
#                 g[nums[i]].append(nums[j])

#     # 위상정렬
#     ans = []
#     q = deque([v for v in range(1, n+1) if cnt[v] == 0])
#     while q:
#         v = q.popleft()
#         ans.append(v)
#         for next_v in g[v]:
#             cnt[next_v] -= 1
#             if cnt[next_v] == 0:
#                 q.append(next_v)

#     print(*ans) if len(ans) == n else print("IMPOSSIBLE")

# def solve():
#     for _ in range(int(input())):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         m = int(input())
#         news = set(tuple(map(int, input().split())) for _ in range(m))
#         # print(news)

#         topology_sort(n, nums, news)

# solve()


# 2304 창고 다각형
# import sys
# input = sys.stdin.readline

# def solve():
#     N = int(input())
#     ps = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(x[0]))
#     # print(ps)

#     ans = 0
#     max_h = -1
#     # 가장 높은 기둥의 높이값 max_h 찾기
#     for p in ps:
#         max_h = max(max_h, p[1])
#     # print(max_h)

#     visited = False  # max_h 방문했는지 체크
#     p_stack = []    # max_h 이후 p 값들 저장

#     pre_l, pre_h = 0, 0
#     for p in ps:
#         # 최고 높이 만나기 전
#         if not visited:
#             if p[1] == max_h:
#                 visited = True
#                 p_stack.append([p[0]+1, p[1]])

#             if pre_h < p[1]:
#                 ans += pre_h * (p[0] - pre_l)
#                 pre_l, pre_h = p[0], p[1]

#         # 최고 높이 이후
#         else:
#             l, h = p
#             l += 1
#             while p_stack and p_stack[-1][1] <= h:
#                 p_stack.pop()
#             p_stack.append([l, h])

#     # print(p_stack)
#     # print(ans)

#     for l, h in p_stack:
#         ans += h * (l-pre_l)
#         pre_l = l

#     # 마지막 처리
#     print(ans)

# solve()


# 1240 노드 사이의 거리
# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque

# def solve():
#     N, M = map(int, input().split())
#     g = defaultdict(list)
#     for _ in range(N-1):
#         a, b, c = map(int, input().split())
#         g[a].append([b, c])
#         g[b].append([a, c])

#     for _ in range(M):
#         a, b = map(int, input().split())
#         if a == b:
#             print(0)
#             continue

#         q = deque([[a, 0]])
#         visited = [False]*(N+1)
#         visited[a] = True

#         while q:
#             v, d = q.popleft()
#             for next_v, next_d in g[v]:
#                 if next_v == b:
#                     print(d + next_d)
#                     break

#                 if not visited[next_v]:
#                     visited[next_v] = True
#                     q.append([next_v, d + next_d])

# solve()


# 플로이드-와셜 : 시간 초과
# import sys
# input = sys.stdin.readline
# INF = float("inf")

# def solve():
#     N, M = map(int, input().split())
#     g = [[INF]*(N+1) for _ in range(N+1)]
#     for _ in range(N-1):
#         a, b, c = map(int, input().split())
#         g[a][b] = c
#         g[b][a] = c

#     for x in range(1, N+1):
#         g[x][x] = 0
#         # print(g[x])

#     # 플로이드-와셜
#     for k in range(1, N+1):
#         for x in range(1, N+1):
#             for y in range(1, N+1):
#                 if g[x][y] > g[x][k] + g[k][y]:
#                     g[x][y] = g[x][k] + g[k][y]

#     for _ in range(M):
#         a, b = map(int, input().split())
#         print(g[a][b])

# solve()


# 26560 Periods
# for _ in range(int(input())):
#     stc = input()
#     print(stc if stc[-1] == '.' else stc+'.')


# 2512 예산
# def solve():
#     N = int(input())
#     nums = list(map(int, input().split()))
#     limit = int(input())

#     top, bot = max(nums), 0
#     ans = 0
#     while top >= bot:
#         mid = (top+bot)//2

#         now_sum = 0
#         for n in nums:
#             if mid >= n :
#                 now_sum += n
#             else: # mid < n
#                 now_sum += mid

#         if now_sum <= limit:
#             ans = mid
#             bot = mid+1
#         else:
#             top = mid-1

#     print(ans)

# solve()


# 1167 트리의 지름
# pm 11:05 ~ 11:38

# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# def diameter_of_tree(g, v, visited):
#     # Diameter of tree : 트리의 지름
#     first_max, second_max, ans = 0, 0, 0
#     visited[v] = True

#     for next_v, next_dist in g[v]:
#         if not visited[next_v]:
#             sub_first_max, sub_ans = diameter_of_tree(g, next_v, visited)
#             # this_dist : 가장 마지막 자식 노드까지 1자로 쭉 갔을 때 가장 긴 길이
#             this_dist = next_dist + sub_first_max
#             # sub_ans : 각 노드를 기준으로 현재까지 가장 큰 값 (트리의 지름 추정값)
#             ans = max(ans, sub_ans)

#             # 제일 긴 길이, 두 번째로 긴 길이 갱신
#             if first_max <= this_dist:
#                 second_max = first_max
#                 first_max = this_dist

#             elif second_max <= this_dist:
#                 second_max = this_dist

#     # print(v, first_max, second_max, ans)
#     return [first_max, max((first_max + second_max), ans)]

# def solve():
#     V = int(input())
#     g = defaultdict(list)
#     for _ in range(V):
#         ns = list(map(int, input().split()))
#         for i in range(1, len(ns), 2):
#             if ns[i] != -1:
#                 g[ns[0]].append([ns[i], ns[i+1]])
#     # print(g)
#     visited = [False] * (V+1)

#     # 1번 기준으로 재귀
#     print(max(diameter_of_tree(g, 1, visited)))

# solve()


# 2263 트리의 순회
"""
13    
8 4 9 2 10 5 1 6 11 3 12 7 13
8 9 4 10 5 2 11 6 12 13 7 3 1

1 2 4 8 9 5 10 3 6 11 7 12 13 clear
"""
# import sys
# sys.setrecursionlimit(int(1e7))

# def show_preorder(inorder, postorder, inidxs, in_l, in_r, post_l, post_r):
#     root = postorder[post_r]

#     # root 먼저 출력
#     print(root, end=' ')
#     root_idx = inidxs[root]

#     # print("[1]", in_l, root_idx, in_r, post_l, post_r)

#     # L
#     if in_l <= root_idx-1:
#         # print("[2]")
#         # inorder의 l길이-1만큼 post_l에 더해서 post_r 계산 (root_idx-1 - in_l +1 -1)
#         show_preorder(inorder, postorder, inidxs, in_l, root_idx-1, post_l, post_l + (root_idx-1 - in_l))

#     # R
#     if root_idx+1 <= in_r:
#         # print("[3]")
#         # inorder의 R길이-1만큼 port_r-1에서 빼서 post_l 계산
#         show_preorder(inorder, postorder, inidxs, root_idx+1, in_r, post_r-1 - (in_r - root_idx-1), post_r-1)

# def solve():
#     n = int(input())
#     inorder = list(map(int, input().split()))
#     postorder = list(map(int, input().split()))
#     inidxs = dict()
#     for i in range(len(inorder)):
#         inidxs[inorder[i]] = i
#     # print(inidxs)

#     show_preorder(inorder, postorder, inidxs, 0, n-1, 0, n-1)

# solve()


# 2635 수 이어가기
"""
1
[ans]
4
1 1 0 1
[출력]
0
→ for문 범위 (1, N)을 (1, N+1)로 바꿔서 해결
"""
# def solve():
#     N = int(input())

#     max_cnt, ans = 0, []
#     for i in range(1, N+1):
#         cnt, nums = 2, [N, i]
#         while nums[-2]-nums[-1] >= 0:
#             nums.append(nums[-2]-nums[-1])
#             cnt += 1

#         if max_cnt < cnt:
#             max_cnt = cnt
#             ans = nums

#     print(max_cnt)
#     print(*ans)

# solve()


# 2023 신기한 소수
# def make_sieve(n):
#     s = [False, False] + [True]*(n-1)
#     for i in range(1, n+1):
#         if s[i]:
#             for ii in range(2*i, n+1, i):
#                 s[ii] = False

#     return [i for i in range(n+1) if s[i]]

# def check_prime(N, s):
#     for div_num in s:
#         if N <= div_num:
#             break

#         elif N % div_num == 0:
#             return False

#     return True

# def solve():
#     N = int(input())

#     cnt = 1
#     prime_nums = [2, 3, 5, 7]
#     s = make_sieve(min(10**N, 10000))
#     # print(s)

#     while cnt < N:
#         new_prime_nums = []
#         for pn in prime_nums:
#             for k in range(1, 10, 2):
#                 if check_prime(pn*10 + k, s):
#                     new_prime_nums.append(pn*10 + k)

#         prime_nums = new_prime_nums
#         cnt += 1

#     print(*prime_nums, sep='\n')

# solve()


# 1251 단어 나누기
# def solve():
#     s = input()
#     # print(s)

#     ans = []
#     for i in range(0, len(s)-2):
#         for j in range(i+1, len(s)-1):
#             ans.append(s[:i+1][::-1] + s[i+1:j+1][::-1] + s[j+1:][::-1])

#     print(sorted(ans)[0])

# solve()


# 2563 색종이
# def solve():
#     board = [[0]*101 for _ in range(101)]
#     for _ in range(int(input())):
#         x, y = map(int, input().split())
#         for nx in range(x, x+10):
#             for ny in range(y, y+10):
#                 board[nx][ny] += 1

#     ans = 0
#     for x in range(1, 101):
#         for y in range(1, 101):
#             if board[x][y] != 0:
#                 ans += 1

#     print(ans)

# solve()


# 5582 공통 부분 문자열
# 메모리 초과
# def solve():
#     s1, s2 = list(input()), list(input())

#     dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
#     ans = 0
#     for i in range(1, len(s1)+1):
#         for j in range(1, len(s2)+1):
#             if s1[i-1] == s2[j-1]:
#                 # print(i-1, j-1)
#                 dp[i][j] = dp[i-1][j-1]+1
#         ans = max(ans, max(dp[i]))

#     # for x in range(len(s1)+1):
#     #     print(dp[x])

#     print(ans)

# solve()


# 개선 코드 → 통과
# def solve():
#     s1, s2 = list(input()), list(input())

#     len_s2 = len(s2)
#     pre_dp = [0]*(len_s2+1)
#     ans = 0

#     for i in range(1, len(s1)+1):
#         now_dp = [0]*(len_s2+1)
#         for j in range(1, len_s2+1):
#             if s1[i-1] == s2[j-1]:
#                 # print(i-1, j-1)
#                 now_dp[j] = pre_dp[j-1]+1

#         ans = max(ans, max(now_dp))
#         pre_dp = now_dp

#     print(ans)

# solve()


# 9625 BABBA
# def solve():
#     K = int(input())
#     dp = [[0, 0] for _ in range(K+1)]
#     dp[0] = [1, 0]

#     for i in range(1, K+1):
#         dp[i][0] = dp[i-1][1]
#         dp[i][1] = sum(dp[i-1])

#     print(*dp[K])

# solve()

# 1193 분수 찾기
# def solve():
#     X = int(input())

#     n, k = 0, 1
#     while n+k < X:
#         n += k
#         k += 1

#     gab = X-n
#     print(f'{gab}/{k+1-gab}') if k % 2 == 0 else print(f'{k+1-gab}/{gab}')

# solve()


# 1717 집합의 표현
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(int(1e7))

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])

#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# def solve():
#     n, m = map(int, input().split())
#     parent = [i for i in range(n+1)]
#     # print(parent)

#     for _ in range(m):
#         ops, a, b = list(map(int, input().split()))
#         if ops == 0:
#             if a != b:
#                 union_parent(parent, a, b)

#         else:
#             print("YES") if find_parent(parent, a) == find_parent(parent, b) else print("NO")

# solve()


# 1461 도서관
# def solve():
#     N, M = map(int, input().split())
#     nums = list(map(int, input().split()))

#     # 양수 음수 분리 후 정렬
#     pos, neg = [], []
#     for n in nums:
#         if n > 0: pos.append(n)
#         else: neg.append(n)
#     pos, neg = sorted(pos), sorted(neg, reverse=True)
#     # print(pos, neg)

#     # 제일 처음으로 처리해야할 인덱스 각각 계산
#     # pos_idx, neg_idx
#     len_pos, len_neg = len(pos), len(neg)
#     pi, ni = (len_pos-1) % M, (len_neg-1) % M
#     # print(pi, ni)

#     # 한 배열이 마무리 될 때까지 반복
#     ans = 0
#     while pi < len_pos and ni < len_neg:
#         if pos[pi] < (-neg[ni]):
#             ans += pos[pi]*2
#             pi += M
#         else:
#             ans += (-neg[ni])*2
#             ni += M
#     # print("[1]", ans)

#     # pos 좌표들만 남은 경우
#     while pi < len_pos:
#         if pi != len_pos-1:
#             ans += pos[pi]*2
#             pi += M
#         else:
#             ans += pos[pi]
#             break

#     # neg 좌표들만 남은 경우
#     while ni < len_neg:
#         if ni != len_neg-1:
#             ans += (-neg[ni])*2
#             ni += M
#         else:
#             ans += (-neg[ni])
#             break

#     print(ans)

# solve()


# 1253 좋다
"""
4
-1 0 0 1
[ans] 2
5
0 0 0 0 0
[ans] 5
5
2 6 8 10 10
[ans] 3
"""

# 참고 : https://baby-ohgu.tistory.com/30
# def solve():
#     N = int(input())
#     nums = sorted(list(map(int, input().split())))

#     ans = 0
#     for i in range(N):
#         tmp = nums[:i] + nums[i+1:]
#         l, r = 0, N-2

#         while l < r:
#             now = tmp[l] + tmp[r]
#             if now == nums[i]:
#                 ans += 1
#                 break

#             elif now < nums[i]:
#                 l += 1
#             else:
#                 r -= 1

#     print(ans)

# solve()


# 17299 오등큰수
# pm 04:05 ~ 04:20
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# def solve():
#     N = int(input())
#     nums = list(map(int, input().split()))
#     d = defaultdict(int)
#     for n in nums:
#         d[n] += 1

#     ans = [-1]*N
#     stack = []
#     for idx in range(N):
#         while stack and d[nums[stack[-1]]] < d[nums[idx]]:
#             ans[stack.pop()] = nums[idx]
#         stack.append(idx)

#     print(*ans)

# solve()


# 11004 K번째 수
# import sys
# input = sys.stdin.readline

# _, K = map(int, input().split())
# print(sorted(list(map(int, input().split())))[K-1])


# 1189 컴백홈
# pm 09:40 ~ 10:26
# dfs 오랜만인 점 + 전역변수 없이 처리하려니까 좀 걸렸네..
# import sys
# input = sys.stdin.readline

# def dfs(R, C, K, board, x, y, inc_xy, ans, cnt):
#     board[x][y] = '_'
#     # print("[1]", x, y, ans)
#     for px, py in inc_xy:
#         nx, ny = x + px, y + py
#         if (0 <= nx < R) and (0 <= ny < C) and (board[nx][ny] == '.') and (cnt < K):
#             if [nx, ny, cnt+1] == [0, C-1, K]:
#                 board[x][y] = '.'
#                 return ans + 1

#             else:
#                 ans = dfs(R, C, K, board, nx, ny, inc_xy, ans, cnt+1)
#                 # print("[2]", x, y, ans)

#     board[x][y] = '.'
#     return ans

# def solve():
#     R, C, K = map(int, input().split())
#     if (R+C-1 > K):
#         print(0);
#         return

#     board = [list(input().rstrip()) for _ in range(R)]
#     inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

#     print(dfs(R, C, K, board, R-1, 0, inc_xy, 0, 1))

# solve()


# 5427 불
# import sys
# input = sys.stdin.readline
# from collections import deque

# def solve():
#     N = int(input())
#     inc_xy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

#     for _ in range(N):
#         w, h = map(int, input().split())
#         board = [list(input().rstrip()) for _ in range(h)]

#         # 불 위치, 상근이가 서있을 수 있는 위치
#         q_fires, q_sg = deque(), deque()
#         for x in range(h):
#             for y in range(w):
#                 if board[x][y] == '*':
#                     q_fires.append([x, y])
#                 elif board[x][y] == '@':
#                     q_sg.append([x, y])

#         pos = False
#         time = 0
#         while q_sg and (not pos):
#             time += 1

#             if q_fires:
#                 for _ in range(len(q_fires)):
#                     x, y = q_fires.popleft()
#                     for px, py in inc_xy:
#                         nx, ny = x+px, y+py
#                         if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == '.':
#                             board[nx][ny] = '*'
#                             q_fires.append([nx, ny])

#             if q_sg:
#                 for _ in range(len(q_sg)):
#                     x, y = q_sg.popleft()
#                     if (x in [0, h-1]) or (y in [0, w-1]):
#                         pos = True
#                         break

#                     for px, py in inc_xy:
#                         nx, ny = x+px, y+py
#                         if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == '.':
#                             board[nx][ny] = '@'
#                             q_sg.append([nx, ny])

#         print(time) if pos else print("IMPOSSIBLE")

# solve()


# 9205 맥주 마시면서 걸어가기
# pm 08:52 ~ 09:12

# import sys
# input = sys.stdin.readline
# from collections import deque

# def dist(l1, l2):
#     x1, y1 = l1
#     x2, y2 = l2
#     return (abs(x1-x2)+abs(y1-y2))

# def solve():
#     for _ in range(int(input())):
#         n = int(input())
#         q = deque([list(map(int, input().split()))])
#         stores = set(tuple(map(int, input().split())) for _ in range(n))
#         goal = list(map(int, input().split()))

#         pos = False
#         while q:
#             x, y = q.popleft()
#             if dist([x, y], goal) <= 1000:
#                 pos = True
#                 break

#             tmp_xy = set()
#             for sx, sy in stores:
#                 if dist([x, y], [sx, sy]) <= 1000:
#                     q.append([sx, sy])
#                     tmp_xy.add(tuple([sx, sy]))

#             for t in tmp_xy:
#                 stores.remove(t)

#         print("happy") if pos else print("sad")

# solve()


# 17609 회문
# pm 09:15 ~ 09:40
# import sys
# input = sys.stdin.readline

# def is_palidrome(s, l, r):
#     while l <= r:
#         # print(l, r)
#         if s[l] == s[r]:
#             l += 1
#             r -= 1
#         else:
#             break
#     return [l, r]

# def solve():
#     for _ in range(int(input())):
#         s = list(input().rstrip())
#         # print("s", s)
#         sl, sr = is_palidrome(s, 0, len(s)-1)

#         if sl >= sr:
#             print(0)
#             continue

#         pos = False
#         for l, r in [[sl+1, sr], [sl, sr-1]]:
#             tmp_l, tmp_r = is_palidrome(s, l, r)
#             if tmp_l >= tmp_r:
#                 pos = True
#                 print(1)
#                 break

#         if not pos:
#             print(2)

# solve()


# K번째 수 - 개편
# def solve():
#     N = int(input())
#     k = int(input())

#     bot, top = 1, N**2
#     ans = 0
#     while bot <= top:
#         mid = (bot+top)//2
#         cnt = 0
#         for i in range(1, N+1):
#             cnt += min(N, (mid//i))

#         # print(bot, mid top, cnt)
#         if cnt >= k:
#             top = mid-1
#             ans = mid
#         else:
#             bot = mid+1

#     print(ans)

# solve()


# 1132 합
# import sys
# input = sys.stdin.readline

# def solve():
#     vals = [[i, 0] for i in range(26)]
#     # print(vals)

#     # cannot_zero   : 0이 될 수 없는 알파벳을 체크
#     # appeared      : 한 번이라도 등장한 알파벳을 체크
#     cannot_zero = set()
#     appeared = set()
#     for _ in range(int(input())):
#         s = list(input().rstrip())
#         cannot_zero.add(s[0])

#         val = 1
#         for c in s[::-1]:
#             appeared.add(c)
#             vals[ord(c)-65][1] += val
#             val *= 10
#     # print(vals)

#     # 값으로 내림차순
#     vals = sorted(vals, key=lambda x:(-x[1]))[:len(appeared)]
#     # print(vals)
#     # print(appeared)
#     # print(cannot_zero)

#     # 0이 필요한 건 10개의 알파벳이 모두 등장했을 때
#     target = -1
#     if len(appeared) >= 10:
#         for i, _ in vals[::-1]:
#             if chr(i+65) not in cannot_zero:
#                 target = i
#                 break
#     # print(vals)
#     # print(target)

#     ans, num = 0, 9
#     for i, val in vals:
#         if i == target:
#             continue
#         ans += val*num
#         num -= 1
#     print(ans)

# solve()


# 5430 AC - 개선
# 500ms → 124ms
# import sys
# input = sys.stdin.readline

# def solve():
#     for _ in range(int(input())):
#         p = list(input().rstrip())
#         n = int(input())
#         nums = list(input().rstrip()[1:-1].split(','))
#         # print(nums)

#         # l, r = left, right
#         l, r = 0, n-1
#         is_reversed = False
#         pos = True
#         for func in p:
#             if func == 'R':
#                 is_reversed = not is_reversed

#             else: #D
#                 n -= 1
#                 if is_reversed:
#                     r -= 1
#                 else:
#                     l += 1

#             if n < 0: # l > r+1
#                 pos = False
#                 break

#         if pos:
#             print("[", ','.join(nums[l:r+1][::(-1) if is_reversed else 1]), "]", sep='')
#         else:
#             print("error")

# solve()


# 3595 맥주 냉장고
# def solve():
#     n = int(input())

#     ans, min_area = [], int(1e7)
#     for a in range(1, n+1):
#         if n % a == 0:
#             b_times_c = n//a
#             for b in range(1, b_times_c+1):
#                 if b_times_c % b == 0:
#                     c = b_times_c // b
#                     # print(a, b, c)

#                     if min_area > 2*(a*b + b*c + c*a) :
#                         min_area = 2*(a*b + b*c + c*a)
#                         ans = [a, b, c]

#     print(*ans)

# solve()


# 1799 비숍
# def btr(N, board, pos_xy, len_pos_xy, idx, bishop, now_cnt, inc_xy):
#     global ans
#     for now in range(idx, len_pos_xy):
#         bx, by = pos_xy[now]
#         # print(now)

#         # 대각선 검사
#         pos = True
#         for px, py in inc_xy:
#             # print(px, py)
#             tmpx, tmpy = bx+px, by+py
#             # print(bx, by, tmpx, tmpy)
#             while (0 <= tmpx < N) and (0 <= tmpy < N):
#                 if bishop[tmpx][tmpy]:
#                     pos = False

#                 tmpx += px
#                 tmpy += py

#             if not pos: break

#         if pos:
#             bishop[bx][by] = True
#             # print(bx, by, now_cnt)
#             # for kx in range(N):
#             #     print(bishop[kx])
#             # print()
#             # input()

#             ans = max(ans, now_cnt+1)
#             btr(N, board, pos_xy, len_pos_xy, now+1, bishop, now_cnt+1, inc_xy)

#             bishop[bx][by] = False

# def solve():
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     pos_xy = [[x, y] for x in range(N) for y in range(N) if board[x][y] == 1]
#     # print(pos_xy)
#     len_pos_xy = len(pos_xy)

#     bishop = [[False]*N for _ in range(N)]

#     global ans
#     ans = 0

#     inc_xy = [[-1, -1], [-1, 1], [1, 1], [1, -1]]

#     btr(N, board, pos_xy, len_pos_xy, 0, bishop, 0, inc_xy)
#     print(ans)

# solve()


# 개선, 그래도 오래 걸림
# def btr(N, board, pos_xy, len_pos_xy, idx, bishop_xy, now_cnt):
#     global ans
#     for now in range(idx, len_pos_xy):
#         px, py = pos_xy[now]
#         # print(now)

#         pos = True
#         for bx, by in bishop_xy:
#             if abs(px-bx) == abs(py-by):
#                 pos = False
#                 break

#         if pos:
#             bishop_xy.add(tuple([px, py]))

#             ans = max(ans, now_cnt+1)
#             btr(N, board, pos_xy, len_pos_xy, idx+1, bishop_xy, now_cnt+1)

#             bishop_xy.remove(tuple([px, py]))

# def solve():
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     pos_xy = [[x, y] for x in range(N) for y in range(N) if board[x][y] == 1]
#     # print(pos_xy)
#     len_pos_xy = len(pos_xy)

#     # check = [[False]*(N) for _ in range(N)]
#     bishop_xy = set()

#     global ans
#     ans = 0

#     btr(N, board, pos_xy, len_pos_xy, 0, bishop_xy, 0)

#     print(ans)

# solve()

"""
7
1 1 1 1 1 1 1 
1 1 1 1 1 1 1 
1 1 1 1 1 1 1 
1 1 1 1 1 1 1 
1 1 1 1 1 1 1 
1 1 1 1 1 1 1 
1 1 1 1 1 1 1 

8
1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 

9
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1

10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
"""


# 시간 초과
# def btr(N, board, pos_xy, len_pos_xy, idx, now_cnt, now_bishop, cannot_bishop, inc_xy):
#     global ans
#     for now in range(idx, len_pos_xy):
#         bx, by = pos_xy[now]
#         # print("now", now)

#         if cannot_bishop[bx][by]:
#             continue

#         cannot_bishop_xy = []
#         for px, py in inc_xy:
#             tmpx, tmpy = bx+px, by+py
#             # print(bx, by, tmpx, tmpy)
#             while (0 <= tmpx < N) and (0 <= tmpy < N):
#                 if board[tmpx][tmpy] == 1 and not now_bishop[tmpx][tmpy]:
#                     cannot_bishop_xy.append([tmpx, tmpy])
#                 tmpx += px
#                 tmpy += py

#         now_bishop[bx][by] = True
#         for x, y in cannot_bishop_xy:
#             cannot_bishop[x][y] += 1

#         ans = max(ans, now_cnt+1)
#         btr(N, board, pos_xy, len_pos_xy, now+1, now_cnt+1, now_bishop, cannot_bishop, inc_xy)

#         now_bishop[bx][by] = False
#         for x, y in cannot_bishop_xy:
#             cannot_bishop[x][y] -= 1

# def solve():
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     pos_xy = [[x, y] for x in range(N) for y in range(N) if board[x][y] == 1]
#     # print(pos_xy)
#     len_pos_xy = len(pos_xy)

#     now_bishop = [[False]*N for _ in range(N)]
#     # can_bishop = [[True if board[x][y] == 1 else False for y in range(N)] for x in range(N)]
#     cannot_bishop = [[0]*N for _ in range(N)]

#     inc_xy = [[-1, -1], [-1, 1], [1, 1], [1, -1]]

#     global ans
#     ans = 0

#     btr(N, board, pos_xy, len_pos_xy, 0, 0, now_bishop, cannot_bishop, inc_xy)

#     print(ans)

# solve()


# 바꿔도 시간 초과.. 좀 더 고민해봐야겠다
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]

# # / 대각선으로 같은 대각선 원소들 정리
# pos_xy = [[] for _ in range(2*N)]
# # print(pos_xy)
# for x in range(N):
#     for y in range(N):
#         if board[x][y] == 1:
#             pos_xy[x+y].append([x, y])

# for x in range(2*N):
#     print(pos_xy[x])

# # # \ 대각선으로 backtracking
# diag = [True]*(2*N)

# line_idxs = []
# for i in range(2*N):
#     if len(pos_xy[i]) != 0:
#         line_idxs.append(i)
# print(line_idxs)
# # len(line_idxs) # \대각선을 고려하지 않은 가능한 최고 길이
# limit_std_idx = len(line_idxs)
# print(limit_std_idx)
# global ans
# ans = 0

# def btr(N, board, pos_xy, line_idxs, std_idx, limit_std_idx, now_cnt, diag):
#     global ans
#     for i in range(std_idx, limit_std_idx):
#         print("now", i)
#         for bx, by in pos_xy[line_idxs[i]]:
#             # print(i, bx, by)
#             if not (diag[N+by-bx]): continue

#             diag[N+by-bx] = False

#             ans = max(ans, now_cnt+1)
#             if ans == limit_std_idx:
#                 return
#             # btr(N, board, pos_xy, std_idx, limit_std_idx, now_cnt, diag)
#             btr(N, board, pos_xy, line_idxs, i+1, limit_std_idx, now_cnt+1, diag)

#             diag[N+by-bx] = True

# btr(N, board, pos_xy, line_idxs, 0, limit_std_idx, 0, diag)
# print(ans)


# 10811 바구니 뒤집기
# def solve():
#     N, M = map(int, input().split())
#     ns = [i for i in range(N+1)]

#     for _ in range(M):
#         l, r = map(int, input().split())
#         while l < r:
#             ns[l], ns[r] = ns[r], ns[l]
#             l += 1
#             r -= 1

#     print(*ns[1:])

# solve()


# 2941 크로아티아 알파벳
# def solve():
#     s = list(input())
#     ans, i, len_s = 0, 0, len(s)

#     while i < len_s:
#         if (s[i] == 'c') and ((i+1) < len_s) and (s[i+1] in ['=', '-']):
#             i += 2
#         elif s[i] == 'd':
#             if (i+2) < len_s and s[i+1] == 'z' and s[i+2] == '=':
#                 i += 3
#             elif (i+1) < len_s and s[i+1] == '-':
#                 i += 2
#             else:
#                 i += 1
#         elif (s[i] == 'l') and ((i+1) < len_s) and (s[i+1] =='j'):
#             i += 2
#         elif (s[i] == 'n') and ((i+1) < len_s) and (s[i+1] =='j'):
#             i += 2
#         elif (s[i] == 's') and ((i+1) < len_s) and (s[i+1] =='='):
#             i += 2
#         elif (s[i] == 'z') and ((i+1) < len_s) and (s[i+1] =='='):
#             i += 2
#         else:
#             i += 1

#         ans += 1

#     print(ans)

# solve()


# 크로아티아 알파벳 - 코드 개선
# def solve():
#     s = input()
#     ans, i, len_s = 0, 0, len(s)

#     while i < len_s:
#         if (i+1) < len_s:
#             if s[i:i+2] in ["c=", "c-", "d-", "lj", "nj", "s=", "z="]:
#                 i += 1
#             elif ((i+2) < len_s) and (s[i:i+3] == "dz="):
#                 i += 2

#         i += 1
#         ans += 1

#     print(ans)

# solve()


# 7785 회사에 있는 사람
# import sys
# input = sys.stdin.readline

# def solve():
#     names = set()
#     for _ in range(int(input())):
#         name, move = input().rstrip().split()
#         names.add(name) if move == 'enter' else names.remove(name)
#     print(*sorted(names, reverse=True), sep='\n')

# solve()


# 2229 조 짜기
# def solve():
#     N = int(input())
#     grades = [0] + list(map(int, input().split()))
#     dp = [0]*(N+1)

#     for i in range(1, N+1):
#         for j in range(1, i+1):
#             dp[i] = max(dp[i], dp[j-1] + abs(grades[j]-grades[i]))
#     print(dp[N])

# solve()


# 8979 올림픽
# from collections import defaultdict

# def solve():
#     N, K = map(int, input().split())
#     grades = defaultdict(list)

#     for _ in range(N):
#         # num, gold, silver, bronze
#         n, g, s, b = map(int, input().split())
#         grades[n] = [g, s, b]
#     # print(grades)

#     grades = sorted(grades.items(), key=lambda x:(-x[1][0], -x[1][1], -x[1][2]))
#     # print(grades)

#     pre_g, ans, same_cnt = [-1, -1, -1], 0, 0
#     for i in range(N):
#         if pre_g != grades[i][1]:
#             pre_g = grades[i][1]
#             ans += 1 + same_cnt
#             same_cnt = 0
#         else:
#             same_cnt += 1

#         if grades[i][0] == K:
#             print(ans)
#             return

# solve()


# 14916 거스름돈
# def solve():
#     n = int(input())
#     INF = int(1e5)
#     dp = [INF]*(n+1)

#     if n >= 2: dp[2] = 1
#     if n >= 4: dp[4] = 2
#     if n >= 5: dp[5] = 1

#     for i in range(6, n+1):
#         dp[i] = min(dp[i-2], dp[i-5])+1
#     # print(dp)

#     print(dp[n] if dp[n] != INF else -1)

# solve()


# 1707 이분 그래프
# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque

# def bfs(g, q, colors):
#     while q:
#         v, color = q.popleft()
#         # print(v, color)
#         next_color = (color+1)%2

#         for next_v in g[v]:
#             if colors[next_v] == -1:
#                 colors[next_v] = next_color
#                 q.append([next_v, next_color])
#             elif colors[next_v] != next_color:
#                 return False

#     return True

# def solve():
#     for _ in range(int(input())):
#         V, E = map(int, input().split())
#         g = defaultdict(list)
#         for _ in range(E):
#             u, v = map(int, input().split())
#             g[u].append(v)
#             g[v].append(u)
#         # print(g)

#         colors = [-1]*(V+1)
#         pos = True

#         for v in range(1, V+1):
#             if colors[v] == -1:
#                 colors[v] = 0
#                 if not bfs(g, deque([[v, 0]]), colors):
#                     pos = False
#                     break

#         print("YES") if pos else print("NO")

# solve()


# 1417 국회의원 선거
# from heapq import heapify, heappush, heappop

# def solve():
#     n = int(input())
#     target = int(input())

#     heap = [-int(input()) for _ in range(n-1)]
#     heapify(heap)
#     # print(heap)

#     ans = 0
#     while(heap and (target <= -heap[0])):
#         # print(target, -heap[0])
#         heappush(heap, heappop(heap)+1)
#         target += 1
#         ans += 1

#     print(ans)

# solve()


# 1976 여행 가자
"""
5
5
0 1 0 0 0
1 0 0 0 1
0 0 0 1 0
0 0 1 0 1
0 1 0 1 0
3 5 4 2 1

4
4
0 0 0 1
0 0 1 0
0 1 0 1
1 0 1 0
1 2 3 4
"""

# import sys
# input = sys.stdin.readline
# from collections import deque

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)

#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a

# def solve():
#     N, _ = int(input()), int(input())

#     routes = [[0]*N] + [list(map(int, input().split())) for _ in range(N)]
#     # print(routes)

#     g = [[(j+1) for j in range(N) if routes[i][j] == 1] for i in range(N+1)]
#     # print(g)

#     parent = [i for i in range(N+1)]
#     # print(parent)

#     visited = [False] * (N+1)
#     plan = list(map(int, input().split()))
#     for v in plan:
#         if not visited[v]:
#             visited[v] = True
#             q = deque(g[v])
#             # visited 를 확실하기 위해 추가
#             for u in g[v]:
#                 visited[u] = True

#             while q:
#                 u = q.popleft()
#                 union_parent(parent, v, u)
#                 for next_u in g[u]:
#                     if not visited[next_u]:
#                         visited[next_u] = True
#                         q.append(next_u)
#     # print(parent)

#     pos = True
#     for v in plan[1:]:
#         if find_parent(parent, plan[0]) != find_parent(parent, parent[v]):
#             pos = False
#             break

#     print("YES") if pos else print("NO")

# solve()


# 코드 개선
# import sys
# input = sys.stdin.readline

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)

#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a

# def solve():
#     N, _ = int(input()), int(input())

#     routes = [[0]*N] + [list(map(int, input().split())) for _ in range(N)]
#     # print(routes)
#     parent = [i for i in range(N+1)]
#     # print(parent)

#     for i in range(1, N+1):
#         for j in range(N):
#             if routes[i][j] == 1:
#                 union_parent(parent, i, j+1)
#     # print(parent)

#     pos = True
#     plan = list(map(int, input().split()))
#     for v in plan[1:]:
#         if find_parent(parent, plan[0]) != find_parent(parent, parent[v]):
#         # if parent[plan[0]] != parent[v]:
#             pos = False
#             break

#     print("YES") if pos else print("NO")

# solve()


# 20915 숫자 카드 놀이
"""
687687
"""
# import itertools

# def solve():
#     for _ in range(int(input())):
#         t = list(input())
#         len_t = len(t)

#         for i in range(len_t):
#             if t[i] == '6':
#                 t[i] = '9'
#         t = sorted(t, reverse=True)
#         # print(t)

#         ans, default_s = 0, set({k for k in range(len_t)})
#         for c in itertools.combinations(range(len_t), (len_t)//2):
#             s = default_s - set(c)
#             # print(s)
#             n1, n2 = int(''.join([t[k] for k in s])), int(''.join([t[k] for k in c]))
#             ans = max(ans, n1*n2)

#         print(ans)

# solve()


# 개선
# def solve():
#     for _ in range(int(input())):
#         ns = list(map(int, input()))
#         for i in range(len(ns)):
#             if ns[i] == 6:
#                 ns[i] = 9
#         ns.sort(reverse=True)
#         # print(ns)

#         a, b = 0, 0
#         for n in ns:
#             if a <= b:
#                 a = 10*a+n
#             else:
#                 b = 10*b+n
#             print(a,b)
#         print(a*b)

# solve()


# 2447 별 찍기 - 10
# import sys
# input = sys.stdin.readline

# def recursion(N, board, x, y, d):
#     next_d = (d//3)
#     for nx in range(x + next_d, x + next_d*2):
#         for ny in range(y + next_d, y + next_d*2):
#             board[nx][ny] = ' '

#     if d > 1: # d >= 3
#         for nx in range(x, x+d, next_d):
#             for ny in range(y, y+d, next_d):
#                 # 중앙 부분 처리했으니 continue
#                 if (nx == x+next_d) and (ny == y+next_d):
#                     continue
#                 recursion(N, board, nx, ny, next_d)

# def solve():
#     N = int(input())
#     board = [['*']*N for _ in range(N)]

#     recursion(N, board, 0, 0, N)
#     for x in range(N):
#         print(*board[x], sep='')

# solve()


# 7579 앱
"""
mk == 2^k 라면 for문이 1번 돌 때마다 약 2배씩 늘어난다..
"""
# 시간 초과
# import sys
# input = sys.stdin.readline

# def solve():
#     N, M = map(int, input().split())
#     ms, cs = list(map(int, input().split())), list(map(int, input().split()))

#     d = dict()
#     for i in range(N):
#         tmp_d = d.copy()
#         m, c = ms[i], cs[i]
#         if m in d:
#             d[m] = min(d[m], c)
#         else:
#             d[m] = c

#         for tmp_m, tmp_c in tmp_d.items():
#             if m+tmp_m in tmp_d:
#                 d[m+tmp_m] = min(d[m+tmp_m], c+tmp_c)
#             else:
#                 d[m+tmp_m] = c+tmp_c
#     # print(d)

#     # 시간 복잡도 계산해보면 정렬을 안 하고 찾는 게 더 빠를 듯
#     # for k, v in sorted(d.items(), key=lambda x:(-x[0], x[1])):
#     #     print(k, v)

#     ans = int(1e4)
#     for k, v in d.items():
#         if k >= M:
#             ans = min(ans, v)
#     print(ans)

# solve()


# CN 기준 dp 테이블이면 충분할 듯 (최대 100만 인덱스) → 1만으로도 가능
# import sys
# input = sys.stdin.readline

# def solve():
#     N, M = map(int, input().split())
#     ms, cs = list(map(int, input().split())), list(map(int, input().split()))
#     w = sum(cs)

#     dp = [[0]*(w+1) for _ in range(N+1)]
#     for x in range(1, N+1):
#         m, c = ms[x-1], cs[x-1]
#         for y in range(c):
#             dp[x][y] = dp[x-1][y]
#         for y in range(c, w+1):
#             dp[x][y] = max(dp[x-1][y], m+dp[x-1][y-c])

#     # for x in range(1, N+1):
#     #     print(dp[x])

#     ans = -1
#     for y in range(w+1):
#         if dp[N][y] >= M:
#             ans = y
#             break
#     print(ans)

# solve()


# 6051 시간 여행

# 통과는 됐는데.. 최악의 경우 32초/3.2GB를 소모하는 코드라서 개선이 필요하다
# import sys
# input = sys.stdin.readline

# def solve():
#     total_stack, now = [[]], []
#     for _ in range(int(input())):
#         cmd = input().rstrip()
#         if cmd[0] in "at":  # a or t
#             K = int(cmd.split()[1])
#             if cmd[0] == 'a':
#                 now.append(K)
#             else: # t
#                 now = total_stack[K-1][:]

#         elif now: # s
#             now.pop()

#         total_stack.append(now[:])
#         print(now[-1] if now else -1)
#     # print(total_stack)

# solve()


# import sys
# input = sys.stdin.readline
# def solve():
#     N = int(input())
#     # ns 내 원소 : 쿼리를 진행했을 때 [마지막 원소, 쿼리 상 직전 원소가 추가(a)된 쿼리 번호]
#     ns = [[-1, -1] for _ in range(N+1)]

#     for i in range(1, N+1):
#         cmd = input().rstrip()
#         if cmd[0] in "at":
#             K = int(cmd.split()[1])
#             if cmd[0] == 'a':
#                 ns[i] = [K, i-1]
#             else: # 't'
#                 ns[i] = ns[K-1]
#         else: # 's'
#             ns[i] = ns[ns[i-1][1]]

#         print(ns[i][0])
#     print(ns)

# solve()


# 9316 Hello World, Judge 1!
# for i in range(int(input())):
#     print(f'Hello World, Judge {i+1}!')


# 1011 Fly me to the Alpha Centauri
# def solve():
#     for _ in range(int(input())):
#         x, y = map(int, input().split())
#         k = y-x

#         ans, i, check = 0, 1, False
#         while k > 0:
#             k -= i
#             if check:
#                 i += 1
#             ans += 1
#             check = not check

#         print(ans)

# solve()


# 4141 Numbersrebmun
# for _ in range(int(input())):
#     s = list(input())
#     # print(s)

#     for i in range(len(s)):
#         if s[i] in "AaBbCc":
#             s[i] = 2
#         elif s[i] in "DdEeFf":
#             s[i] = 3
#         elif s[i] in "GgHhIi":
#             s[i] = 4
#         elif s[i] in "JjKkLl":
#             s[i] = 5
#         elif s[i] in "MmNnOo":
#             s[i] = 6
#         elif s[i] in "PpQqRrSs":
#             s[i] = 7
#         elif s[i] in "TtUuVv":
#             s[i] = 8
#         else:
#             s[i] = 9
#     # print(s)

#     print("YES") if s == s[::-1] else print("NO")


# 2293 동전 1
# def solve():
#     n, k = map(int, input().split())
#     dp = [0]*(k+1)
#     dp[0] = 1

#     for _ in range(n):
#         num = int(input())
#         for i in range(num, k+1):
#             dp[i] = dp[i-num] + dp[i]

#     print(dp[k])

# solve()


# 11931 수 정렬하기 4
# import sys
# input = sys.stdin.readline

# N = int(input())
# print(*sorted([int(input()) for _ in range(N)], reverse=True), sep='\n')


# 13241 최소공배수
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# A, B = map(int, input().split())
# print(A*B//gcd(A, B))


# 16435 스네이크버드
# N, L = map(int, input().split())
# hs = sorted(list(map(int, input().split())))

# for h in hs:
#     if h <= L:
#         L += 1
#     else:
#         break
# print(L)


# 2294 동전 2
# n, k = map(int, input().split())
# nums = [int(input()) for _ in range(n)]
# dp = [0] + [-1]*k

# for num in nums:
#     for idx in range(num, k+1):
#         if dp[idx-num] != -1:
#             if dp[idx] == -1:
#                 dp[idx] = dp[idx-num]+1
#             else:
#                 dp[idx] = min(dp[idx], dp[idx-num]+1)
# print(dp[k])


# 12015 가장 긴 증가하는 부분 수열 2
# 직접 구현 성공.. wow !
# import sys
# input = sys.stdin.readline

# N = int(input())
# ns = list(map(int, input().split()))

# ans = [0]*N
# values, level = [-1]*N, 0
# values[0] = ns[0]
# # print(values)

# for i in range(1, N):
#     if values[level] < ns[i]:
#         level += 1
#         ans[i] = level
#         values[level] = ns[i]
#         continue

#     target_idx = -1
#     # bot, top → idx 접근
#     bot, top = 0, level
#     while bot <= top:
#         mid = (bot+top)//2

#         if values[mid] < ns[i]:
#             bot = mid+1
#         else: # values[mid] >= ns[i]:
#             top = mid-1
#             target_idx = mid

#     values[target_idx] = ns[i]
#     ans[i] = target_idx
#     print(i, target_idx, ans, values)

# # print(ans)
# # print(values)
# print(max(ans)+1)


# 2629 양팔저울
# def solve():
#     N = int(input())
#     ns = [0] + list(map(int, input().split()))
#     M = int(input())
#     ms = list(map(int, input().split()))
#     # print(ms)
#     w = 30001

#     dp = [[0]*w for _ in range(N+1)]
#     for i in range(1, N+1):
#         # \\\\\\
#         for y in range(w-ns[i]):
#             dp[i][y+ns[i]] += dp[i-1][y]

#         # //////
#         for y in range(ns[i], w):
#             dp[i][y-ns[i]] += dp[i-1][y]

#         # ││││││
#         for y in range(w):
#             dp[i][y] += dp[i-1][y]

#         dp[i][ns[i]+15000] += 1
#         dp[i][-ns[i]+15000] += 1
#     # print(dp[N][15000:15030])

#     for m in ms:
#         print("Y", end=' ') if (m <= 15000) and (dp[N][m+15000] > 0) else print("N", end=' ')

# solve()


# 14003 가장 긴 증가하는 부분 수열 5
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(int(1e7))

# def btr(A, pre_idxs, i):
#     if i != -1:
#         btr(A, pre_idxs, pre_idxs[i])
#         print(A[i], end=' ')

# def solve():
#     N = int(input())
#     A = list(map(int, input().split()))

#     # values : 현idx, value
#     values, level, updated_idx = [[-1, 0] for _ in range(N)], 0, 0
#     values[0] = [0, A[0]]
#     # print(values)
#     pre_idxs = [-1]*N

#     for i in range(1, N):
#         if A[i] > values[level][1]:
#             level += 1
#             updated_idx = i
#             values[level] = [i, A[i]]
#             pre_idxs[i] = values[level-1][0]
#             continue

#         # target_level 찾기
#         bot, top = 0, level
#         target = -1
#         while bot <= top:
#             mid = (bot+top)//2
#             if A[i] > values[mid][1]:
#                 bot = mid+1
#             else: # A[i] <= values[mid][1]:
#                 top = mid-1
#                 target = mid

#         values[target] = [i, A[i]]
#         if target != 0:
#             pre_idxs[i] = values[target-1][0]

#     # print(values, pre_idxs, updated_idx, sep='\n')
#     print(level+1)
#     btr(A, pre_idxs, updated_idx)

# solve()


# 15963 CASIO
# N, M = map(int, input().split())
# print(1 if N == M else 0)


# # 17388 와글와글 숭고한
# S, K, H = map(int, input().split())

# if S+K+H >= 100:
#     print("OK")
# elif S < K and S < H:
#     print("Soongsil")
# elif K < S and K < H:
#     print("Korea")
# else:
#     print("Hanyang")


# 1100 하얀 칸
# import sys
# input = sys.stdin.readline

# def solve():
#     board = [list(input().rstrip()) for _ in range(8)]
#     # print(board)

#     ans = 0
#     for x in range(8):
#         for y in range(8):
#             if (x+y) % 2 == 0 and board[x][y] == 'F':
#                 ans += 1
#     print(ans)

# solve()


# 15439 베라의 패션
# N = int(input())
# print(N*(N-1))


# 5555 반지
# import sys
# input = sys.stdin.readline

# def solve():
#     ring = input().rstrip()
#     ans = 0
#     for _ in range(int(input())):
#         target = str(input().rstrip())
#         target *= 2
#         # print(target)
#         if ring in target:
#             ans += 1
#     print(ans)

# solve()


# 12779 상품 is 뭔들
# import math

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# def solve():
#     a, b = map(int, input().split())
#     # k = int(math.sqrt(b)) - int(math.sqrt(a))
#     k = math.isqrt(b) - math.isqrt(a)
#     gcd_val = gcd(k, b-a)
#     print(f'{k//gcd_val}/{(b-a)//gcd_val}' if k != 0 else 0)

# solve()


# ??
# print(math.sqrt(1152921504606846976))
# print(math.sqrt(1152921504606846975))

# print(math.isqrt(1152921504606846976))
# print(math.isqrt(1152921504606846975))


# 4485 녹색 옷 입은 애가 젤다지?
# import sys
# input = sys.stdin.readline
# from collections import deque

# def solve():
#     N, INF, cnt = -1, int(2e5), 0
#     inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

#     while (N != 0):
#         N = int(input())
#         if N == 0:
#             break
#         cnt += 1

#         board = [list(map(int, input().split())) for _ in range(N)]
#         rupee = [[INF]*N for _ in range(N)]
#         # print(rupee)
#         rupee[0][0] = board[0][0]

#         q = deque([[0, 0]])
#         while q:
#             x, y = q.popleft()
#             for px, py in inc_xy:
#                 nx, ny = x+px, y+py
#                 if 0 <= nx < N and 0 <= ny < N:
#                     if rupee[nx][ny] > rupee[x][y] + board[nx][ny]:
#                         rupee[nx][ny] = rupee[x][y] + board[nx][ny]
#                         q.append([nx, ny])

#         print(f'Problem {cnt}: {rupee[N-1][N-1]}')

# solve()


# 17130 토끼가 정보섬에 올라온 이유
"""
3 4
R..O
####
CCCO
[정답] 0

1 4
ROCO
[정답] 1

1 1
R
[정답] -1

2 2
..
.R
[정답] -1
"""

# import sys
# input = sys.stdin.readline
# from collections import deque

# def solve():
#     N, M = map(int, input().split())
#     board = [list(input().rstrip()) for _ in range(N)]
#     dp = [[0]*M for _ in range(N)]
#     ans = 0
#     inc_x = [-1, 0, 1]

#     for y in range(1, M):
#         for x in range(N):
#             if board[x][y] == '#':
#                 continue

#             for px in inc_x:
#                 if x == 0 and px == -1:
#                     continue
#                 elif x == N-1 and px == 1:
#                     continue
#                 dp[x][y] = max(dp[x][y], dp[x+px][y-1])

#             if board[x][y] == 'C':
#                 dp[x][y] += 1
#             elif board[x][y] == 'O':
#                 ans = max(ans, dp[x][y])

#     # for x in range(N):
#     #     # print(board[x])
#     #     print(dp[x])

#     print(ans if ans != 0 else -1)

# solve()


# 새로 짠 코드
# import sys
# input = sys.stdin.readline
# from collections import deque

# def solve():
#     N, M = map(int, input().split())
#     board = [list(input().rstrip()) for _ in range(N)]
#     dp = [[0]*M for _ in range(N)]
#     ans = -1
#     inc_x = [-1, 0, 1]
#     xy_set = set()

#     q = deque()
#     for x in range(N):
#         for y in range(M):
#             if board[x][y] == 'R':
#                 q.append([x, y])

#     if q[0][1] == M-1:
#         print(-1)
#         return

#     while q:
#         x, y = q.popleft()
#         # print(x, y)
#         if board[x][y] == 'C':
#             dp[x][y] += 1

#         for px in inc_x:
#             nx = x+px
#             if not (0 <= nx < N):
#                 continue
#             elif board[nx][y+1] == '#':
#                 continue
#             elif board[nx][y+1] == 'O':
#                 ans = max(ans, dp[x][y])

#             # 'O' / 'C' / '.'
#             if y < M-2:
#                 dp[nx][y+1] = max(dp[x][y], dp[nx][y+1])
#                 if tuple([nx, y+1]) not in xy_set:
#                     xy_set.add(tuple([nx, y+1]))
#                     q.append([nx, y+1])

#     print(ans)

# solve()


# 1038 감소하는 수
"""
9876543210
[정답] 1022
"""
# def btr(s, e, max_l, v, N, cnt):
#     for i in range(s, e):
#         if s != 0:
#             # return btr(s-1, i, max_l, now_l+1, 10*v+i, N, cnt)
#             ans = btr(s-1, i, max_l, 10*v+i, N, cnt)
#             if ans != None:
#                 return ans
#         else:
#             cnt[0] += 1
#             # print(cnt, 10*v, i)
#             if cnt[0] == N:
#                 return 10*v+i

# def solve():
#     N = int(input())
#     cnt, ans = [-1], -1

#     # max_l : 1 ~ 10 (9876543210)
#     for max_l in range(1, 11):
#         ans = btr(max_l-1, 10, max_l, 0, N, cnt)
#         if ans != None:
#             break

#     print(ans if ans != None else -1)

# solve()


# 2981 검문
# a % M == k 이고 b % M == k 라면 (a-b) % M == 0
# import sys
# input = sys.stdin.readline
# import math

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# def divisors(n):
#     divs = set({n})
#     for i in range(2, math.isqrt(n)+1):
#         if n % i == 0:
#             divs.add(i)
#             divs.add(n//i)
#     # print(divs)
#     return sorted(divs)

# def solve():
#     N = int(input())
#     ns = [int(input()) for _ in range(N)]
#     gaps = [abs(ns[i]-ns[j]) for i in range(N) for j in range(i+1, N)]
#     # print(gaps)

#     gcd_val = gaps[0]
#     for gap in gaps[1:]:
#         gcd_val = gcd(gcd_val, gap)
#     # print(gcd_val)

#     print(*divisors(gcd_val))

# solve()


# 17386 선분 교차 1
# 참고1 : https://degurii.tistory.com/47#prev
# 참고2 : https://imucoding.tistory.com/1059
# def ccw(x1, y1, x2, y2, x3, y3):
#     a = x1*y2 + x2*y3 + x3*y1
#     b = y1*x2 + y2*x3 + y3*x1
#     return a-b

# def solve():
#     x1, y1, x2, y2 = map(int, input().split())
#     x3, y3, x4, y4 = map(int, input().split())

#     if ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4) < 0 and\
#         ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x2, y2) < 0:
#         print(1)
#     else:
#         print(0)

# solve()


# 13171
"""
1000000000000000000
1000000000000000000
"""
# 1e18? 2^10 ≒ 10e3
# A, X = int(input()), int(input())
# mod = int(1e9+7)
# # print(mod)

# bins, tmp_X = [], X
# while tmp_X > 0:
#     bins.append(tmp_X%2)
#     tmp_X //= 2
# # print(bins)

# len_bins = len(bins)
# muls = [0]*len_bins
# muls[0] = (A%mod)
# for i in range(1, len_bins):
#     muls[i] = (muls[i-1]**2)%mod
# # print(muls)

# ans = 1
# for i in range(len_bins):
#     if bins[i] == 1:
#         ans = (ans*muls[i])%mod
# print(ans)


# 11758 CCW
# x1, y1 = list(map(int, input().split()))
# x2, y2 = list(map(int, input().split()))
# x3, y3 = list(map(int, input().split()))

# ccw =  (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)
# if ccw > 0:
#     print(1)
# elif ccw < 0:
#     print(-1)
# else:
#     print(0)


# 2022 사다리
# import math
# x, y, c = map(float, input().split())
# # print(x, y, c)

# bot, top = 0, min(x, y)
# target = 1/c
# ans = -1
# while (bot - top) <= -0.0001:
#     # print(bot, top)
#     mid = (bot+top)/2

#     now_val = (1/math.sqrt(x**2-mid**2)) + (1/math.sqrt(y**2-mid**2))
#     if now_val >= target:
#         ans = mid
#         top = mid
#     else:
#         bot = mid

# print('{0:.3f}'.format(ans))


# 2410 2의 멱수의 합
"""
15
26
"""
# 시간 복잡도 : NlogN → 1e6 기준 약 2천만이므로 1억당 1초라 할 때 0.2초
# N = int(input())
# mod = int(1e9)

# dp = [0]*(N+1)
# dp[0] = 1

# for i in range(1, N+1):
#     if i % 2 == 1:
#         dp[i] = dp[i-1]
#     else: # i is even(짝수)
#         dp[i] = (i//2)+1
#         k = 4
#         while k <= i:
#             dp[i] += dp[i-k]
#             k *= 2
#     dp[i] %= mod

# print(dp)
# # print(dp[N])


# 힌트 참고
# N = int(input())
# dp = [1]+[0]*N
# mod = int(1e9)

# for i in range(1, N+1):
#     if i % 2 == 1:
#         dp[i] = dp[i-1]
#     else:
#         dp[i] = dp[i-1]+dp[i//2]
#         dp[i] %= mod

# print(dp[N])


# 25551 멋쟁이 포닉스
"""
5 1
2 5
5 2
[정답] 3
"""
# MW, MB = map(int, input().split())
# TW, TB = map(int, input().split())
# PW, PB = map(int, input().split())

# DTW, DTB = min(MB, TW, PB), min(MW, TB, PW)
# print(DTW*2 if DTW==DTB else min(DTW,DTB)*2+1)


# 16918 봄버맨
"""
3 3 5
.O.
OOO
.O.

[정답]
OOO
OOO
OOO
"""
# import sys
# input = sys.stdin.readline

# def print_board(board, R):
#     for x in range(R):
#         print(*board[x], sep='')

# def make_board(board, R, C):
#     new_board = [['O']*C for _ in range(R)]
#     bombs = [[x, y] for x in range(R) for y in range(C) if board[x][y] == 'O']
#     # print(bombs)
#     inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

#     for x, y in bombs:
#         new_board[x][y] = '.'
#         for px, py in inc_xy:
#             nx, ny = x+px, y+py
#             if 0 <= nx < R and 0 <= ny < C:
#                 new_board[nx][ny] = '.'
#     return new_board

# def solve():
#     R, C, N = map(int, input().split())
#     board = [list(input().rstrip()) for _ in range(R)]

#     if (N-2)%2 == 0:
#         print_board([['O']*C for _ in range(R)], R)
#         return

#     board_3sec = make_board(board, R, C)
#     if (N-2)%4 == 3:
#         if N == 1:
#             print_board(board, R)
#         else: # N >= 5
#             # 1초 후랑 5초 후가 다른 경우가 있음
#             board_5sec = make_board(board_3sec, R, C)
#             print_board(board_5sec, R)
#     else: #(N-2)%4 == 1:
#         print_board(board_3sec, R)

# solve()


# 13398 연속합 2
# def solve():
#     N = int(input())
#     ns = list(map(int, input().split()))
#     ans = ns[0]

#     dp = [[ns[0], -1], [0, -1]]
#     for i in range(1, N):
#         dp[0][1] = max(ns[i], dp[0][0]+ns[i])
#         dp[1][1] = max(dp[0][0], dp[1][0]+ns[i])
#         ans = max(ans, dp[0][1], dp[1][1])

#         dp[0][0] = dp[0][1]
#         dp[1][0] = dp[1][1]

#     print(ans)

# solve()


# 2473 세 용액
# N = int(input())
# ns = sorted(list(map(int, input().split())))
# # print(ns)
# ans, closest_sum = [], int(3e9)+1

# out_l, out_r = 0, N-1
# while out_l < out_r-1:
#     in_l, in_r = out_l+1, out_r-1

#     while in_l <= in_r:
#         mid = (in_l+in_r)//2
#         now_sum = abs(ns[out_l] + ns[mid] + ns[out_r])
#         if closest_sum > now_sum:
#             ans = [ns[out_l], ns[mid], ns[out_r]]
#             closest_sum = now_sum

#         if now_sum >= 0:
#             in_r = mid-1
#         else:
#             in_l = mid+1

#     if ns[out_l] + ns[out_r] >= 0:
#         out_r -= 1
#     else:
#         out_l += 1

# print(*ans)

"""
5
-5 -1 2 3 4
"""
# 2try - clear
# Python3 - 시간 초과, PyPy3 - 통과 (240ms)

# N = int(input())
# ns = sorted(list(map(int, input().split())))
# # print(ns)
# ans, closest_sum = [], int(3e9)+1

# for mid in range(1, N-1):
#     l, r = mid-1, mid+1
#     while 0 <= l and r <= N-1:
#         now_sum = ns[l]+ns[mid]+ns[r]
#         # print(l, mid, r, closest_sum, now_sum)
#         if closest_sum > abs(now_sum):
#             closest_sum = abs(now_sum)
#             ans = [ns[l], ns[mid], ns[r]]

#         if now_sum >= 0:
#             l -= 1
#         else:
#             r += 1

# print(*ans)


# 10942 팰린드롬?
"""
3
1 1 1
1
1 2
"""
# import sys
# input = sys.stdin.readline

# def palindrome_check(N, ns, dp, l, r):
#     while 0 <= l and r <= N-1:
#         if ns[l] == ns[r]:
#             dp[l][r] = 1
#             l -= 1
#             r += 1
#         else:
#             break

# def solve():
#     N = int(input())
#     ns = list(map(int, input().split()))

#     dp = [[0]*N for _ in range(N)]
#     for i in range(N):
#         palindrome_check(N, ns, dp, i, i)
#         palindrome_check(N, ns, dp, i, i+1)

#     # for x in range(N):
#     #     print(dp[x])

#     for _ in range(int(input())):
#         S, E = map(int, input().split())
#         print(dp[S-1][E-1])

# solve()


# 14912 숫자 빈도수
# n, d = map(int, input().split())
# ans = 0
# for i in range(1, n+1):
#     k = i
#     while k > 0:
#         if k % 10 == d:
#             ans += 1
#         k //= 10

# print(ans)


# 1009 분산 처리
# nums = dict()
# nums[0] = [10]
# nums[1] = [1]
# nums[2] = [2, 4, 8, 6]
# nums[3] = [3, 9, 7, 1]
# nums[4] = [4, 6]
# nums[5] = [5]
# nums[6] = [6]
# nums[7] = [7, 9, 3, 1]
# nums[8] = [8, 4, 2, 6]
# nums[9] = [9, 1]

# for _ in range(int(input())):
#     ans = 1
#     a, b = map(int, input().split())
#     a %= 10
#     print(nums[a][(b-1)%len(nums[a])])


# 1024 수열의 합
# def solve():
#     N, L = map(int, input().split())
#     for i in range(L, 101):
#         # 리스트의 첫 숫자 k를 계산해서 조건에 부합하는지 체크
#         k = (N/i)-(i-1)/2
#         if k >= 0 and k == float(int(k)):
#             # print(i, k)
#             for ans_num in range(int(k), int(k)+i):
#                 print(ans_num, end=' ')
#             return

#     print(-1)

# solve()


# 4659 비밀번호 발음하기
# import sys
# input = sys.stdin.readline

# while True:
#     S = input().rstrip()
#     if S == 'end':
#         break
#     # print(S)

#     pos = True
#     vowel_cnt = 0
#     cond2 = [0, 0]
#     pre_s = ''

#     for s in S:
#         if s in "aeiou":
#             vowel_cnt += 1
#             cond2[0] += 1
#             cond2[1] = 0
#         else:
#             cond2[0] = 0
#             cond2[1] += 1

#         if cond2[0] == 3 or cond2[1] == 3:
#             pos = False
#             break

#         if pre_s == s:
#             if s in 'eo':
#                 continue
#             pos = False
#             break
#         pre_s = s

#     if vowel_cnt == 0:
#         pos = False

#     print(f'<{S}> is ', '' if pos else 'not ', 'acceptable.', sep='')


# 3048 개미
# 위치 변경에 대해서 일괄 적용해야한다
# N1, N2 = map(int, input().split())
# ants1, ants2 = list(input()), list(input())
# ans = [[a, 0] for a in ants1[::-1]] + [[a, 1] for a in ants2]
# # print(ans)

# total_len = N1+N2
# for _ in range(int(input())):
#     pre_a, changing_idxs = -1, []
#     for idx in range(total_len):
#         if pre_a == 0 and ans[idx][1] == 1:
#             changing_idxs.append(idx)
#         pre_a = ans[idx][1]

#     for idx in changing_idxs:
#         ans[idx-1], ans[idx] = ans[idx], ans[idx-1]
#     # print(ans)

# print(''.join(a[0] for a in ans))


# 11688 최소공배수 찾기
# 다시 보니까 좀 더 간단하게 풀 수 있다
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# def lcm(a, b):
#     return a*b//gcd(a, b)

# def sieve(a, b):
#     s = [True]*(max(a, b)+1)
#     len_s = len(s)
#     for i in range(2, len_s):
#         if s[i]:
#             for ii in range(2*i, len_s, i):
#                 s[ii] = False
#     return [i for i in range(2, len_s) if s[i]]

# def solve():
#     a, b, L = list(map(int, input().split()))
#     if L % lcm(a,b) != 0:
#         print(-1)
#         return

#     primes = sieve(a, b)
#     # print(primes)

#     c = 1
#     for prime in primes:
#         if a * b == 1:
#             break

#         cnt = 0
#         while True:
#             can_divide_a, can_divide_b = (a % prime == 0), (b % prime == 0)
#             if not (can_divide_a | can_divide_b):
#                 break

#             cnt += 1
#             if can_divide_a: a //= prime
#             if can_divide_b: b //= prime
#             L //= prime # 최소공배수를 만족하므로 조건문 없이 가능
#             # print(prime, a, b, L)

#         if L % prime == 0:
#             while L % prime != 0:
#                 L //= prime
#                 cnt += 1
#             c *= prime**cnt

#     # print(c, L)
#     print(c*L)

# solve()


# 13172 ∑
# def inverse(n, X):
#     # b^(X-2) ≡ b^(-1) (mod X)
#     target = X-2
#     bins = []
#     while target > 0:
#         bins.append(target%2)
#         target//=2
#     # print("bins", bins)

#     len_bins = len(bins)
#     muls = [0]*len_bins
#     muls[0] = n % X
#     for i in range(1, len_bins):
#         muls[i] = (muls[i-1]**2) % X
#         # muls[i] = ((muls[i-1]%X)**2) % X
#     # print("muls", muls)

#     inverse_val = 1
#     for i in range(len_bins):
#         if bins[i]:
#             inverse_val = (inverse_val * muls[i]) % X
#     # print("inverse_val", inverse_val)
#     return inverse_val

# def solve():
#     X = int(1e9)+7
#     ans = 0
#     for _ in range(int(input())):
#         Ni, Si = map(int, input().split())
#         # E(X + Y) = E(X) + E(Y)
#         ans += Si*inverse(Ni, X)
#     print(ans % X)

# solve()


# 개선 코드
# def power(n, p, X):
#     # print(n, p, X)
#     if p == 1:
#         return n
#     # 홀수
#     elif p % 2:
#         return (n * power(n, p-1, X)) % X
#     # 짝수
#     else:
#         tmp = power(n, p//2, X)
#         return (tmp**2) % X

# def solve():
#     ans, X = 0, int(1e9)+7
#     for _ in range(int(input())):
#         Ni, Si = map(int, input().split())
#         ans += Si*power(Ni, X-2, X)
#     print(ans % X)

# solve()


# 1075 나누기
# N, F = int(input()), int(input())

# N = (N//100)*100
# while N % F != 0:
#     N += 1

# print('{0:0>2}'.format(N%100))


# 4948 베르트랑 공준
# limit = 2*123456
# s = [False, False] + [True]*(limit-1)
# for i in range(2, limit+1):
#     if s[i]:
#         for ii in range(2*i, limit+1, i):
#             s[ii] = False

# cnt = [0]*(limit+1)
# for i in range(2, limit+1):
#     cnt[i] = cnt[i-1]
#     if s[i]:
#         cnt[i] += 1

# n = int(input())
# while n > 0:
#     print(cnt[2*n]-cnt[n])
#     n = int(input())


# 11049 행렬 곱셈 순서
# import sys
# input = sys.stdin.readline

# N = int(input())
# ns = [list(map(int, input().split())) for _ in range(N)]
# ns = [ns[i][0] for i in range(N)] + [ns[-1][1]]
# # print(ns)

# INF = int(2**31)-1
# dp = [[INF]*(N+2) for _ in range(N+2)]

# for x in range(N+2):
#     if x-1 >= 0:
#         dp[x][x-1] = 0
#     dp[x][x] = 0
#     if x+1 < (N+2):
#         dp[x][x+1] = 0

# # 전체 숫자 : N+1개
# # w : width 길이, s : 시작점 위치, i : 기준점 위치
# for w in range(3, N+2):
#     for s in range(0, N+2-w):
#         # print(w, s)
#         for i in range(1, w-1):
#             dp[s][s+w-1] = min(dp[s][s+w-1], dp[s][s+i]+dp[s+i][s+w-1]+(ns[s]*ns[s+i]*ns[s+w-1]))

# print(dp[0][N])


# 2143 두 배열의 합
"""
5
3
3 3 3
3
2 2 2
"""
# def make_new_s(n, ns):
#     new_s = [0]*(n*(n+1)//2)
#     k = 0
#     for i in range(n):
#         for j in range(i, n):
#             if i == j:
#                 new_s[k] = ns[i]
#             else:
#                 new_s[k] = new_s[k-1]+ns[j]
#             k += 1
#     return new_s

# def solve():
#     T = int(input())
#     n, ns = int(input()), list(map(int, input().split()))
#     m, ms = int(input()), list(map(int, input().split()))
#     # print(ns, ms)

#     new_ns, new_ms = make_new_s(n, ns), sorted(make_new_s(m, ms))
#     # print(new_ns, new_ms, sep='\n')

#     ans, len_new_ms = 0, len(new_ms)
#     for nn in new_ns:
#         low_bot, low_top = 0, len_new_ms-1
#         high_bot, high_top = 0, len_new_ms-1
#         low_i, high_i = -1,-1

#         while low_bot <= low_top:
#             mid = (low_bot+low_top)//2
#             if new_ms[mid]+nn >= T:
#                 low_i = mid
#                 low_top = mid-1
#             else:
#                 low_bot = mid+1

#         while high_bot <= high_top:
#             # print("bot, top", high_bot, high_top)
#             mid = (high_bot+high_top)//2
#             if new_ms[mid]+nn <= T:
#                 high_i = mid
#                 high_bot = mid+1
#             else:
#                 high_top = mid-1

#         # print("l, h", low_i, high_i)
#         if low_i != -1 and high_i != -1 and new_ms[low_i] == new_ms[high_i]:
#             ans += (high_i-low_i)+1

#     print(ans)

# solve()


# 2166 다각형의 면적
# import sys
# input = sys.stdin.readline

# def solve():
#     N = int(input())
#     points = [list(map(int, input().split())) for _ in range(N)]
#     # print(points)

#     ans = 0
#     x1, y1 = points[0]
#     for i in range(1, N-1):
#         x2, y2 = points[i]
#         x3, y3 = points[i+1]
#         ans += ((x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1))
#     print('{:.1f}'.format(abs(ans)/2))

# solve()


# 2342 Dance Dance Revolution
# def cal_energy(std, k):
#     if std == 0:
#         return 2
#     elif std == k:
#         return 1
#     # std : 1 ~ 4
#     elif abs(std-k) != 2:
#         return 3
#     else:
#         return 4

# ns = list(map(int, input().split()))
# # print(ns)

# INF = 4*(int(1e5))+1
# pre_dp = [[INF]*5 for _ in range(5)]
# pre_dp[0][0] = 0

# for n in ns[:-1]:
#     # n : 1 ~ 4
#     now_dp = [[INF]*5 for _ in range(5)]
#     for x in range(5):
#         for y in range(5):
#             if pre_dp[x][y] != INF:
#                 now_dp[n][y] = min(now_dp[n][y], pre_dp[x][y]+cal_energy(x, n))
#                 now_dp[x][n] = min(now_dp[x][n], pre_dp[x][y]+cal_energy(y, n))

#     # for x in range(5):
#     #     print(now_dp[x])
#     # print()

#     pre_dp = now_dp

# ans = min(min(pre_dp[x]) for x in range(5))
# print(ans if ans != INF else 0)


# 2665 미로 만들기
# import sys
# input = sys.stdin.readline
# from collections import deque

# def solve():
#     n = int(input())
#     board = [list(map(int, input().rstrip())) for _ in range(n)]
#     board = [[0 if board[x][y] == 1 else 1 for y in range(n)] for x in range(n)]
#     # print(board)
#     inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

#     INF = 2501
#     cnts = [[INF]*n for _ in range(n)]
#     # cnt[0][0] = 0

#     que = deque([[0, 0, 0]])
#     while que:
#         x, y, cnt = que.popleft()
#         if cnts[x][y] > cnt:
#             cnts[x][y] = cnt
#             for px, py in inc_xy:
#                 nx, ny = x+px, y+py
#                 if 0 <= nx < n and 0 <= ny < n:
#                     next_cnt = cnt + board[nx][ny]
#                     if cnts[nx][ny] > next_cnt:
#                         que.append([nx, ny, next_cnt])
#                         # print(que)

#     # for x in range(n):
#     #     print(cnts[x])

#     print(cnts[n-1][n-1])

# solve()


# 16946 벽 부수고 이동하기 4
# import sys
# input = sys.stdin.readline
# from collections import deque

# def solve():
#     N, M = map(int, input().split())
#     board = [list(map(int, input().rstrip())) for _ in range(N)]
#     cnt_board, area_board = [[0]*M for _ in range(N)], [[0]*M for _ in range(N)]
#     visited = [[False]*M for _ in range(N)]
#     # print(board)

#     inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#     zero_que, sec_zero_que = deque(), deque()
#     area_num = 0

#     # 0인 블럭들 처리
#     for x in range(N):
#         for y in range(M):
#             if board[x][y] == 0 and not visited[x][y]:
#                 visited[x][y] = True
#                 zero_que.append([x, y])
#                 area_num += 1

#             # 0인 곳을 기점으로 bfs 해서 몇 개 있는지 cnt
#             cnt = 0
#             while zero_que:
#                 cnt += 1
#                 sec_zero_que.append(zero_que[0])
#                 kx, ky = zero_que.popleft()

#                 for px, py in inc_xy:
#                     nx, ny = kx+px, ky+py
#                     if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and not visited[nx][ny]:
#                         visited[nx][ny] = True
#                         zero_que.append([nx, ny])

#             # 0으로 이어진 좌표마다 해당 영역의 total 개수를 저장
#             cnt %= 10
#             # print("szq", sec_zero_que)
#             while sec_zero_que:
#                 kx, ky = sec_zero_que.popleft()
#                 cnt_board[kx][ky] = cnt
#                 area_board[kx][ky] = area_num

#     # for x in range(N):
#     #     print(area_board[x])

#     # 상하좌우 합 계산
#     for x in range(N):
#         for y in range(M):
#             if board[x][y] == 1:
#                 area_set = set()
#                 cnt = 1
#                 for px, py in inc_xy:
#                     nx, ny = x+px, y+py
#                     if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
#                         if area_board[nx][ny] not in area_set:
#                             cnt += cnt_board[nx][ny]
#                             area_set.add(area_board[nx][ny])
#                 print(cnt%10, end='')
#             else:
#                 print(0, end='')
#         print()

# solve()


# 1501 영어 읽기
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# def cnt_arr(arr):
#     cnt = [0]*52
#     for w in arr:
#         ord_w = ord(w)
#         # 대문자인 경우
#         if ord_w - 97 < 0:
#             cnt[ord_w-65] += 1
#         # 소문자인 경우
#         else:
#             # -97+26 == -71
#             cnt[ord_w-71] += 1

#     return cnt

# def solve():
#     N = int(input())
#     words = dict()
#     for _ in range(N):
#         word = list(input().rstrip())
#         # print(word)

#         # cnt = cnt_arr(word[1:-1])
#         cnt = cnt_arr(word)
#         # print(cnt[:26])
#         # print(cnt[26:])

#         key_word = word[0]+word[-1]
#         if not key_word in words:
#             words[key_word] = defaultdict(int)
#         words[key_word][tuple(cnt)] += 1
#     # print(words)

#     M = int(input())
#     for _ in range(M):
#         targets, ans = list(input().rstrip().split()), 1

#         for t in targets:
#             key_word = t[0]+t[-1]
#             cnt = cnt_arr(t)
#             try:
#                 ans *= words[key_word][tuple(cnt)]
#             except KeyError:
#                 ans = 0
#                 break

#         print(ans)

# solve()


# 2485 가로수
# import sys
# input = sys.stdin.readline

# def gcd(a,b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# N = int(input())
# ns = sorted([int(input()) for _ in range(N)])
# # print(ns)
# gabs = [ns[i+1]-ns[i] for i in range(N-1)]
# # print(gabs)

# total_gcd = gabs[0]
# for g in gabs[1:]:
#     total_gcd = gcd(total_gcd, g)
# # print(total_gcd)

# ans = 0
# for g in gabs:
#     ans += (g - total_gcd) // total_gcd
# print(ans)


"""
ZZKZZ
4
ZZBZZBBZZ

ZZZZAZZZZ
"""
# 15927 회문은 회문아니야!!
# def solve():
#     S = list(input())
#     len_S = len(S)

#     for i in range(0, (len_S//2)+1):
#         if (S[0] != S[len_S-1-i]) | (S[i] != S[len_S-1]):
#             print(len_S-i)
#             return

#     print(-1)

# solve()


# def solve():
#     S = list(input())
#     len_S = len(S)

#     # 전체 검사
#     for i in range(len_S//2):
#         if S[i] != S[len_S-1-i]:
#             print(len_S)
#             return

#     # 부분 검사
#     # 하나만 다른 부분이 있어도 가능
#     pre_A = S[0]
#     pos = False
#     for i in range((len_S//2)+1):
#         if (S[i] != pre_A) or (S[len_S-1-i] != pre_A):
#             pos = True
#             break

#     print(len_S-1 if pos else -1)

# solve()


# 9328 열쇠
"""
3
4 4
****
a**A
****
***C
c

1
5 9
*********
.......a*
***.*****
*$Ab*****
*********
0
"""
# import sys
# input = sys.stdin.readline
# from collections import deque

# def open_doors(i, doors, q):
#     while doors[i]:
#         q.append(doors[i].popleft())

# def check(visited, board, x, y, q, doors, keys):
#     global ans

#     if not visited[x][y] and board[x][y] != '*':
#         # print(x,y)
#         visited[x][y] = True
#         ord_val = ord(board[x][y])

#         # 빈 공간
#         if board[x][y] == '.':
#             q.append([x, y])
#         # 문서
#         elif board[x][y] == '$':
#             ans += 1
#             q.append([x, y])
#         # A~Z : doors
#         elif 65 <= ord_val <= 90:
#             doors[ord_val-65].append([x, y])
#             if keys[ord_val-65]:
#                 open_doors(ord_val-65, doors, q)
#         # a~z : keys
#         else:
#             keys[ord_val-97] = True
#             open_doors(ord_val-97, doors, q)
#             q.append([x, y])

# def solve():
#     for _ in range(int(input())):
#         global ans
#         ans = 0

#         h, w = map(int, input().split())
#         board = [list(input().rstrip()) for _ in range(h)]
#         # for x in range(h):
#         #     print(board[x])
#         visited = [[False]*w for _ in range(h)]
#         inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

#         # 열쇠 check
#         keys = [False]*26
#         given_keys = list(input().rstrip())
#         if given_keys[0] != '0':
#             for key in given_keys:
#                 keys[ord(key)-97] = True
#         # print(keys)
#         doors = [deque() for _ in range(26)]

#         q = deque()
#         for k in range(w):
#             for x, y in [[0, k], [h-1, k]]:
#                 check(visited, board, x, y, q, doors, keys)

#         for k in range(h):
#             for x, y in [[k, 0], [k, w-1]]:
#                 check(visited, board, x, y, q, doors, keys)
#         # print(doors)
#         # print(keys)

#         while q:
#             x, y = q.popleft()
#             for px, py in inc_xy:
#                 nx, ny = x+px, y+py
#                 if 0 <= nx < h and 0 <= ny < w:
#                     check(visited, board, nx, ny, q, doors, keys)

#         print(ans)

# solve()


# 25191 치킨댄스를 추는 곰곰이를 본 임스
# N = int(input())
# A, B = map(int, input().split())

# print(min(N, (A//2)+B))


# 14935 FA
# print("FA")


# 2669 직사각형 네개의 합집합의 면적 구하기
# board = [[0]*102 for _ in range(102)]
# for _ in range(4):
#     x1, y1, x2, y2 = map(int, input().split())
#     for x in range(x1, x2):
#         board[x][y1] += 1
#         board[x][y2] -= 1

# ans = 0
# for x in range(1, 101):
#     k = 0
#     for y in range(1, 101):
#         k += board[x][y]
#         if k > 0:
#             ans += 1

# # for x in range(10, -1, -1):
# #     print(board[x][:10])

# print(ans)


"""
5 12
4 4 2 2 2
[정답] 3
"""
"""
5 0
0 0 0 0 0
[정답] 31
"""

# 1208 부분수열의 합 2
# from collections import defaultdict

# def num_dict(ns:list):
#     ndict = defaultdict(int)
#     # print(nset)

#     for n in ns:
#         new_ndict = ndict.copy()
#         for element_n in ndict:
#             new_ndict[element_n+n] += ndict[element_n]
#         new_ndict[n] += 1
#         ndict = new_ndict

#     return ndict

# def solve():
#     N, S = map(int, input().split())
#     ns = list(map(int, input().split()))

#     ns1, ns2 = ns[:(N//2)], ns[(N//2):]
#     # print(num_dict(ns1))
#     # print(num_dict(ns2))

#     nd_ns1 = num_dict(ns1)
#     nd_ns2 = num_dict(ns2)

#     ans = 0
#     if S in nd_ns1: ans += nd_ns1[S]
#     if S in nd_ns2: ans += nd_ns2[S]

#     ns1 = sorted(nd_ns1.items(), key=lambda x:(x[0]))
#     ns2 = sorted(nd_ns2.items(), key=lambda x:(x[0]))

#     idx1, idx2 = 0, len(ns2)-1
#     len_ns1 = len(ns1)

#     while idx1 <= (len_ns1-1) and idx2 >= 0:
#         if ns1[idx1][0] + ns2[idx2][0] == S:
#             ans += ns1[idx1][1] * ns2[idx2][1]
#             idx1 += 1
#             idx2 -= 1
#         elif ns1[idx1][0] + ns2[idx2][0] < S:
#             idx1 += 1
#         else:
#             idx2 -= 1
#         # print(idx1, idx2)

#     print(ans)

# solve()


# 1202 보석 도둑
# Branch-and-Bound for the 0-1 Knapsack Problem
# 참고 : https://inf.run/LwtC
# from heapq import heappush, heappop

# class SSTNode:
#     def __init__(self, level, profit, weight):
#         self.level = level
#         self.profit = profit
#         self.weight = weight
#         self.bound = 0

#     # def print(self):
#     #     print(self.level, self.profit, self.weight, self.bound)

# def bound(u, p, w, W):
#     n = len(p)-1
#     if (u.weight >= W):
#         return 0

#     result = u.profit
#     j = u.level+1
#     totweight = u.weight
#     while (j <= n and totweight + w[j] <= W):
#         totweight += w[j]
#         result += p[j]
#         j += 1

#     if (j <= n):
#         result += (W - totweight) * p[j] / w[j]

#     return result

# def knapsack4 (p, w, W):
#     heap = []
#     v = SSTNode(0, 0, 0)
#     maxprofit = 0
#     # root_node
#     v.bound = bound(v, p, w, W)
#     heappush(heap, [-v.bound, v])

#     while heap:
#         v = heappop(heap)[1]
#         # print(v)
#         if (v.bound > maxprofit):
#             level = v.level+1

#             u = SSTNode(level, v.profit + p[level], v.weight + w[level])
#             if (u.weight <= W and u.profit > maxprofit):
#                 maxprofit = u.profit
#             u.bound = bound(u, p, w, W)
#             if (u.bound > maxprofit):
#                 heappush(heap, [-u.bound, u])

#             u = SSTNode(level, v.profit, v.weight)
#             u.bound = bound(u, p, w, W)
#             if (u.bound > maxprofit):
#                 heappush(heap, [-u.bound, u])
#         # print(heap, maxprofit)

#     return maxprofit

# def solve():
#     profit = [0, 40, 30, 50, 10]
#     weight = [0, 2, 5, 10, 5]
#     W = 16

#     maxprofit = knapsack4(profit, weight, W)
#     print('maxprofit = ', maxprofit)

# solve()


# 다른 접근
# 지금 보니 가방 1개에 보석 1개씩 넣을 수 있다
# 가격/무게 ?
# 무게 - 가격 정렬 X : 예제 2번이 반례
# 위 정렬에 heap 추가로 clear

# import sys
# input = sys.stdin.readline

# from heapq import heappush, heappop, heappushpop

# def solve():
#     N, K = map(int, input().split())
#     jewels = [list(map(int, input().split())) for _ in range(N)]
#     jewels.sort(key=lambda x:(-x[0], -x[1]))
#     # print(jewels)

#     bags = sorted([int(input()) for _ in range(K)], reverse=True)
#     # print(bags)

#     # jewels_idx, bags_idx
#     heap, bi = [], 0
#     for ji in range(N):
#         # 빈 가방에 보석을 넣을 수 있는 경우
#         if (bi < K) and (jewels[ji][0] <= bags[bi]):
#             # 보석에 대해 무게순 정렬을 했으므로 가격만 넣어서 비교
#             # 이후 heap을 통해 비교해도 이전 보석보다 가벼운 보석이므로 무게 고려 안 해도 됨
#             heappush(heap, jewels[ji][1])
#             bi += 1

#         # 현재 bi 인덱스의 가방에 못 넣는 경우
#         # 더 이상 가방이 없거나 현재 순번의 가방에 보석을 못 넣는 경우
#         else:
#             # 보석을 넣어둔 기존 가방에서 가격 비교
#             if heap and (heap[0] < jewels[ji][1]):
#                 heappop(heap)
#                 heappush(heap, jewels[ji][1])
#                 # heappushpop(heap, jewels[ji][1])
#         # print(heap)

#     print(sum(heap))

# solve()


# 2225 합분해
# N, K = map(int, input().split())
# INF = int(1e9)

# dp = [[0]*(N+1) for _ in range(K+1)]
# for y in range(N+1):
#     dp[1][y] = 1

# for x in range(2, K+1):
#     for y in range(N+1):
#         for k in range(y+1):
#             dp[x][y] = (dp[x][y] + (dp[x-1][k])) % INF

# # for x in range(K+1):
# #     print(dp[x])

# print(dp[K][N])


# Total count
# import sys
# input = sys.stdin.readline

# words_dict, words_list = dict(), []
# while True:
#     word = input().rstrip()
#     if word == '0':
#         sum_val = 0
#         for word in words_list:
#             print(f'{word}: {words_dict[word]}')
#             sum_val += words_dict[word]
#         print(f'Grand Total: {sum_val}')
#         break

#     if word not in words_dict:
#         words_dict[word] = 1
#         words_list.append(word)
#     else:
#         words_dict[word] += 1


# 2493 탑
# N = int(input())
# ns = list(map(int, input().split()))
# ans = [0]*N
# stack = []

# for idx in range(N-1, -1, -1):
#     while stack and ns[stack[-1]] <= ns[idx]:
#         ans[stack.pop()] = idx+1
#     stack.append(idx)

# print(*ans)


# 2470 두 용액
# N = int(input())
# ns = sorted(list(map(int, input().split())))
# # print(ns)

# ans, min_val = [], int(2e9)+1
# l, r = 0, N-1

# while l < r:
#     # print(l, r)
#     this_val = ns[l]+ns[r]

#     if abs(this_val) < min_val:
#         ans = [l, r]
#         min_val = abs(this_val)

#     if this_val >= 0:
#         r -= 1
#     else:
#         l += 1

# print(ns[ans[0]], ns[ans[1]])


# 2565 전깃줄
# greedy 접근 → 실패
# import sys
# input = sys.stdin.readline

# def cal_cnt(N, ns):
#     cross_cnts = [0]*N
#     for x in range(N):
#         if ns[x][1] == -1: continue
#         for y in range(N):
#             if (x == y) or (ns[y][1] == -1):
#                 continue
#             elif x < y:
#                 if ns[x][1] > ns[y][1]:
#                     cross_cnts[x] += 1
#             else: # x > y:
#                 if ns[x][1] < ns[y][1]:
#                     cross_cnts[x] += 1
#     # print(cross_cnts)

#     max_val, idx = 0, -1
#     for x in range(N):
#         if max_val < cross_cnts[x]:
#             max_val = cross_cnts[x]
#             idx = x

#     # print(max_val, idx)
#     return max_val, idx

# def solve():
#     N = int(input())
#     ns = [list(map(int, input().split())) for _ in range(N)]
#     ns.sort(key=lambda x:x[0])
#     # print(ns)

#     ans = 0
#     max_val, target_idx = cal_cnt(N, ns)

#     while max_val != 0:
#         ns[target_idx][1] = -1
#         ans += 1
#         max_val, target_idx = cal_cnt(N, ns)

#     print(ans)

# solve()


# LIS 였다니 !!! 이걸 생각 못 했다니 ~~~
# import sys
# input = sys.stdin.readline

# N = int(input())
# ns = [list(map(int, input().split())) for _ in range(N)]
# ns.sort(key=lambda x:x[0])

# # LIS
# dp = [0]*N
# for x in range(1, N):
#     for y in range(x):
#         if dp[x] == dp[y] and ns[x][1] > ns[y][1]:
#             dp[x] += 1

# print(N-max(dp)-1)


# 23825 SASA 모형을 만들어보자
# N, M = map(int, input().split())
# print(min(N//2, M//2))


# 1935 후위 표기식2
# N = int(input())
# exp = list(input())
# ns = [int(input()) for _ in range(N)]

# stack = []
# for e in exp:
#     if e in "*+/-":
#         n2, n1 = stack.pop(), stack.pop()
#         if e == '*':    stack.append(n1*n2)
#         elif e == '+':  stack.append(n1+n2)
#         elif e == '/':  stack.append(n1/n2)
#         else: stack.append(n1-n2)
#     else:
#         stack.append(ns[ord(e)-65])

# # print(stack)
# print('{:.2f}'.format(stack[0]))


# 1922 네트워크 연결
# import sys
# input = sys.stdin.readline
# from heapq import heapify, heappop

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def combine(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)

#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a

# def solve():
#     N = int(input())
#     M = int(input())

#     lines = [list(map(int, input().split()))[::-1] for _ in range(M)]
#     parent = [i for i in range(N+1)]
#     heapify(lines)
#     # print(lines)

#     ans = 0
#     while lines:
#         cost, a, b = heappop(lines)
#         if find_parent(parent, a) != find_parent(parent, b):
#             combine(parent, a, b)
#             ans += cost

#     print(ans)

# solve()


# 16938 캠프 준비
# import itertools

# def solve():
#     N, L, R, X = map(int, input().split())
#     ns = list(map(int, input().split()))

#     ans = 0
#     for k in range(1, N+1):
#         for idxs in itertools.combinations([i for i in range(N)], k):
#             tns = [ns[i] for i in idxs]
#             # print(this_ns)

#             if (L <= sum(tns) <= R) and (max(tns) - min(tns) >= X):
#                 ans += 1

#     print(ans)

# solve()


# 11549 Identifying tea
# T = int(input())
# print(sum([1 if T == i else 0 for i in list(map(int, input().split()))]))


# 오르막 수
# N = int(input())
# mod = int(1e4)+7

# dp = [[0]*10 for _ in range(N)]
# dp[0] = [1]*10
# # print(dp)

# for x in range(1, N):
#     for y in range(10):
#         for k in range(y+1):
#             dp[x][y] = (dp[x][y] + dp[x-1][k]) % mod
# # print(dp)

# print(sum(dp[N-1]) % mod)


# 2589 보물섬
# import sys
# input = sys.stdin.readline
# from collections import deque

# h, w = map(int, input().split())
# board = [list(input().rstrip()) for _ in range(h)]
# inc_xy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# ans = 0

# for x in range(h):
#     for y in range(w):
#         if board[x][y] == 'L':
#             visited = [[False]*w for _ in range(h)]
#             visited[x][y] = True

#             q = deque([[x, y, 0]])
#             while q:
#                 kx, ky, cnt = q.popleft()
#                 # print(kx, ky)
#                 ans = max(ans, cnt)
#                 for px, py in inc_xy:
#                     nx, ny = kx+px, ky+py
#                     if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 'L' and not visited[nx][ny]:
#                         visited[nx][ny] = True
#                         q.append([nx, ny, cnt+1])

# print(ans)


# 5557 1학년
# N = int(input())
# ns = list(map(int, input().split()))

# dp = [[0]*21 for _ in range(N+1)]
# dp[0][0] = 1
# # print(dp)

# # i+1
# for i in range(N):
#     for k in range(21-ns[i]):
#         dp[i+1][k+ns[i]] += dp[i][k]
#     for k in range(ns[i], 21):
#         dp[i+1][k-ns[i]] += dp[i][k]

# for x in range(N):
#     print(dp[x])


# N = int(input())
# ns = list(map(int, input().split()))

# dp = [[0]*21 for _ in range(N-1)]
# dp[0][ns[0]] = 1
# # print(dp)

# # i+1
# for i in range(1, N-1):
#     for k in range(21-ns[i]):
#         dp[i][k+ns[i]] += dp[i-1][k]
#     for k in range(ns[i], 21):
#         dp[i][k-ns[i]] += dp[i-1][k]

# # for x in range(N-1):
# #     print(dp[x])

# print(dp[N-2][ns[N-1]])


# 2568 전깃줄 - 2
# 반례 https://www.acmicpc.net/board/view/82980
# import sys
# input = sys.stdin.readline

# N = int(input())
# lines = [list(map(int, input().split())) for _ in range(N)]
# lines.sort(key=lambda x:(x[0]))
# # print(lines)

# limit = int(5e5)+1
# # lcs
# lcs = [lines[0]]
# len_lcs = 1
# # print(lcs)

# dp = [0]*limit
# dp[lines[0][0]] = 1

# for i in range(1, N):
#     if lcs[-1][1] < lines[i][1]:
#         lcs.append(lines[i])
#         len_lcs += 1
#         target_idx = len_lcs-1
#     else:
#         l, r = 0, len_lcs-1
#         target_idx = -1
#         while l <= r:
#             mid = (l+r)//2
#             if lcs[mid][1] >= lines[i][1]:
#                 target_idx = mid
#                 r = mid-1
#             else:
#                 l = mid+1

#         lcs[target_idx] = lines[i]

#     dp[lines[i][0]] = target_idx+1
# # print(lcs)
# # print(dp[:11])

# target_val = max(dp)
# targets = set()
# for i in range(limit-1, -1, -1):
#     if dp[i] == target_val:
#         target_val -= 1
#         targets.add(i)

# ans = set(line[0] for line in lines) - targets
# print(len(ans), *ans, sep='\n')


# 10610 30
# N = sorted(list(map(int, input())), reverse=True)
# # print(N)

# if sum(N) % 3 == 0 and N[-1] == 0:
#     print(*N, sep='')
# else:
#     print(-1)


# 27866 문자와 문자열
# S = list(input())
# N = int(input())
# print(S[N-1])


# 14729 칠무해
# import sys
# input = sys.stdin.readline

# N = int(input())
# ns = sorted([float(input()) for _ in range(N)])
# for i in range(7):
#     print('{0:.3f}'.format(ns[i]))


# https://www.acmicpc.net/problem/7562
# 7562 나이트의 이동


# 2011 암호코드
# def solve():
#     pw = list(map(int, input()))
#     # print(pw)

#     if pw[0] == 0:
#         print(0)
#         return

#     dp = [0]*len(pw)
#     dp[0] = 1
#     mod = int(1e6)

#     for i in range(1, len(pw)):
#         if i >= 2:
#             dp[i] += dp[i-2]

#         if dp[i-1] == 0:
#             if dp[i] == 0:
#                 print(-1)
#                 return
#         elif dp[i-1] == 1:
#             if dp[i] != 0: # 1~9
#                 dp[i] += dp[i-1]
#         elif dp[i-1] == 2:
#             if 1 <= dp[i] <= 6:
#                 dp[i] += dp[i-1]
#         else:

#         dp[i] %= mod

# solve()


# 11441 합 구하기
# import sys
# input = sys.stdin.readline

# N = int(input())
# ns = list(map(int, input().split()))

# sums = [0]*(N+1)
# for i in range(1, N+1):
#     sums[i] = sums[i-1]+ns[i-1]
# # print(sums)

# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     print(sums[b]-sums[a-1])


# 28074 모비스
# s = list(input())

# if ("M" in s) and ("O" in s) and ("B" in s) and ("I" in s) and ("S" in s):
#     print("YES")
# else:
#     print("NO")


# 18110 solved.ac
# 반례 : https://www.acmicpc.net/board/view/49706
# round 해결 : https://yangnyang.tistory.com/10
# import sys
# input = sys.stdin.readline

# def roundUp(n):
#     if (n - int(n)) >= 0.5:
#         return int(n)+1
#     else:
#         return int(n)

# def solve():
#     n = int(input())
#     if n == 0:
#         print(0)
#         return

#     ns = sorted([int(input()) for _ in range(n)])
#     # cut_val
#     cv = roundUp(n*0.15)
#     # print(cv)
#     # print(sum(ns[cv:n-cv])/(n-2*cv))
#     print('{0:d}'.format(roundUp(sum(ns[cv:n-cv])/(n-2*cv))))

# solve()


# 14940 쉬운 최단 거리
# import sys
# input = sys.stdin.readline
# from collections import deque

# def solve():
#     n, m = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(n)]
#     visited = [[False]*m for _ in range(n)]
#     ans = [[0]*m for _ in range(n)]
#     inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

#     q = deque()
#     for x in range(n):
#         for y in range(m):
#             if board[x][y] == 2:
#                 q.append([x, y, 1])
#                 visited[x][y] = True

#     while q:
#         x, y, cnt = q.popleft()
#         for px, py in inc_xy:
#             nx, ny = x+px, y+py
#             if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 ans[nx][ny] = cnt
#                 q.append([nx, ny, cnt+1])

#     for x in range(n):
#         # print(*ans[x])
#         for y in range(m):
#             if visited[x][y]:
#                 print(ans[x][y], end=' ')
#             else:
#                 print(0 if board[x][y] == 0 else -1, end=' ')
#         print()

# solve()


# 21736 헌내기는 친구가 필요해
# import sys
# input = sys.stdin.readline
# from collections import deque

# N, M = map(int, input().split())
# board = [list(input().rstrip()) for _ in range(N)]
# visited = [[False]*M for _ in range(N)]
# inc_xy = [[0,1], [1,0], [0,-1], [-1,0]]

# # for x in range(N):
# #     print(board[x])

# q = deque()
# for x in range(N):
#     for y in range(M):
#         if board[x][y] == 'I':
#             q.append([x, y])
#             visited[x][y] = True

# ans = 0
# while q:
#     x, y = q.popleft()
#     for px, py in inc_xy:
#         nx, ny = x+px, y+py
#         if 0 <= nx < N and 0 <= ny < M and (board[nx][ny] != 'X') and not visited[nx][ny]:
#             visited[nx][ny] = True
#             q.append([nx, ny])
#             if board[nx][ny] == 'P':
#                 ans += 1

# print(ans if ans != 0 else 'TT')


# 24228 젓가락
# N, R = map(int, input().split())
# print(N+(2*(R-1)+1))


# 20529 가장 가까운 세 사람의 심리적 거리
# import sys
# input = sys.stdin.readline

# def d(s1, s2):
#     n = 0
#     for k in range(4):
#         if s1[k] != s2[k]:
#             n +=1
#     return n

# def solve():
#     for _ in range(int(input())):
#         N = int(input())
#         # mbtis
#         ms = list(map(str, input().split()))
#         # print(ms)
#         if N >= 33: # 16*2+1
#             print(0)
#         else:
#             ans = 12
#             for i in range(N-2):
#                 for j in range(i+1, N-1):
#                     for k in range(j+1, N):
#                         # print(i, j, k)
#                         ans = min(ans, d(ms[i], ms[j]) + d(ms[j], ms[k])+ d(ms[k], ms[i]))
#             print(ans)

# solve()


# 28097 모범생 포닉스
# N = int(input())
# ns = list(map(int, input().split()))
# ans = sum(ns)+8*(N-1)
# print(ans//24, ans%24)


# 10825 국영수
# import sys
# input = sys.stdin.readline

# N = int(input())
# strs = [list(input().rstrip().split()) for _ in range(N)]
# d = dict()
# for i in range(N):
#     d[strs[i][0]] = [int(strs[i][k]) for k in range(1, 4)]
# # print(d)

# d = list(d.items())
# # print(d)

# d = sorted(d, key=lambda x:(-x[1][0], x[1][1], -x[1][2], x[0]))
# print(*(d[i][0] for i in range(N)), sep='\n')


# 20303 할로윈의 양아치
# 잘 짠 코드 : 노션 정리
"""
5 3 3 
1 1 1 1 1
1 2
3 4
1 3
[0, 1, 1, 1, 3, 5]   print(parent) 4번째 index의 값이 1이어야 함
2
[정답] 1
[출력] 2
4 3 3
1 2 4 8
1 4
2 3
3 4
[정답] 0
"""

# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque

# def solve():
#     N, M, K = map(int, input().split())
#     ns = [0]+list(map(int, input().split()))

#     conns = [list(map(int, input().split())) for _ in range(M)]
#     g = defaultdict(list)
#     d = []
#     for a, b in conns:
#         g[a].append(b)
#         g[b].append(a)

#     visited = [False]*(N+1)
#     for i in range(1, N+1):
#         if visited[i]:
#             continue

#         q = deque([i])
#         visited[i] = True
#         v_list = [i]
#         candy_sum = ns[i]
#         while q:
#             v = q.popleft()
#             for next_v in g[v]:
#                 if not visited[next_v]:
#                     q.append(next_v)
#                     visited[next_v] = True
#                     v_list.append(next_v)
#                     candy_sum += ns[next_v]
#         # print(v_list, candy_sum)
#         d.append([len(v_list), candy_sum])
#     # print(d)

#     h = len(d)
#     dp = [[0]*K for _ in range(h+1)]
#     for x in range(1, h+1):
#         for y in range(1, K):
#             dp[x][y] = dp[x-1][y]

#         cnt = d[x-1][0]
#         if cnt >= K:
#             continue

#         for y in range(cnt, K):
#             dp[x][y] = max(dp[x][y], dp[x-1][y-cnt]+d[x-1][1])

#     print(dp[h][K-1])

# solve()


# 11478 서로 다른 부분 문자열의 개수
# S = input()
# word_set = set()
# len_S = len(S)

# ans = 0
# for i in range(len_S):
#     for j in range(i, len_S):
#         word = S[i:j+1]
#         if word not in word_set:
#             word_set.add(word)
#             ans += 1
# print(ans)


# 14226 이모티콘
# from collections import deque

# def solve():
#     S = int(input())
#     q = deque([[1, 0]])
#     na_set = set()
#     cnt = 0

#     while q:
#         for _ in range(len(q)):
#             n, a = q.popleft()
#             if n == S:
#                 print(cnt)
#                 return

#             if tuple([n, n]) not in na_set:
#                 na_set.add(tuple([n, n]))
#                 q.append([n, n])
#             if tuple([n+a, a]) not in na_set:
#                 na_set.add(tuple([n+a, a]))
#                 q.append([n+a, a])

#             if n >= 2 and tuple([n-1, 0]) not in na_set:
#                 na_set.add(tuple([n-1, 0]))
#                 q.append([n-1, 0])

#         cnt += 1
#         # print(q, cnt)

# solve()


# 11576 Base Conversion
# A, B = map(int, input().split())
# input()
# k, mul_val = 0, 1

# ns = list(map(int, input().split()))
# for n in ns[::-1]:
#     k += n*mul_val
#     mul_val *= A

# ans = []
# while k > 0:
#     ans.append(k % B)
#     k //= B

# print(*ans[::-1])


# 1021 회전하는 큐
# from collections import deque

# N, M = map(int, input().split())
# ns = list(map(int, input().split()))
# ans = 0
# q = deque([i for i in range(1, N+1)])
# for n in ns:
#     idx_front = q.index(n)
#     idx_back = len(q)-1-idx_front

#     if idx_front < (idx_back+1):
#         for _ in range(idx_front):
#             ans += 1
#             q.append(q.popleft())
#     else:
#         for _ in range(idx_back+1):
#             ans += 1
#             q.appendleft(q.pop())
#     q.popleft()

# print(ans)


# 24508 나도리팡
# N, K, T = map(int, input().split())
# ns = sorted(list(map(int, input().split())))

# l, r = 0, N-1
# cnt = 0
# while l <= r and cnt < T:


# 27323 직사각형
# print(int(input())*int(input()))


# 20003 거스름돈이 싫어요
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# def lcm(a, b):
#     return a*b//gcd(a, b)

# def solve():
#     N = int(input())
#     ns = [list(map(int, input().split())) for _ in range(N)]

#     numerators = [ns[i][0] for i in range(N)]
#     denominators = [ns[i][1] for i in range(N)]
#     # print(numerators)
#     # print(denominators)

#     lcm_denominators = denominators[0]
#     for d in denominators[1:]:
#         lcm_denominators = lcm(lcm_denominators, d)
#         # print(lcm_denominators)

#     lcm_numerators = lcm_denominators//denominators[0]*numerators[0]
#     for idx in range(1, N):
#         lcm_numerators = gcd(lcm_numerators, (lcm_denominators//denominators[idx])*numerators[idx])

#     gcd_val = gcd(lcm_numerators, lcm_denominators)
#     print(lcm_numerators//gcd_val, lcm_denominators//gcd_val)

# solve()


# 27433 팩토리얼 2
# N = int(input())
# ans = 1
# for i in range(2, N+1):
#     ans *= i
# print(ans)


# 1002 터렛
# 참고 0 https://mathbang.net/101#gsc.tab=0
# 참고 1 https://www.acmicpc.net/board/view/96827
# 참고 2 https://www.acmicpc.net/board/view/113688

# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     if x1 == x2 and y1 == y2:
#         if r1 == r2 :
#             if r1 == 0:
#                 print(1)
#             else:
#                 print(-1)
#         else:
#             print(0)
#         continue

#     squared_dist = (x2-x1)**2+(y2-y1)**2
#     sqaured_r2_plus_r1 = (r2+r1)**2
#     sqaured_r2_minus_r1 = (r2-r1)**2
#     print(sqaured_r2_minus_r1)

#     if squared_dist > sqaured_r2_plus_r1:
#         print(0)
#     elif squared_dist == sqaured_r2_plus_r1:
#         print(1)
#     elif sqaured_r2_minus_r1 < squared_dist < sqaured_r2_plus_r1:
#         print(2)
#     elif sqaured_r2_minus_r1 == squared_dist:
#         print(1)
#     else:
#         print(0)


# 4344 평균은 넘겠지
# import sys
# input = sys.stdin.readline

# def round(n):
#     a = n*1000
#     if (a - int(a)) >= 0.5:
#         return (int(a)+1)/1000
#     else:
#         return int(a)/1000

# def solve():
#     for _ in range(int(input())):
#         ns = list(map(int, input().split()))
#         avg = sum(ns[1:])/ns[0]
#         print('{:.3f}%'.format(round(100*sum(1 for n in ns[1:] if n > avg)/ns[0])))

# solve()


# 28256 초콜릿 보관함
# import sys
# input = sys.stdin.readline
# from collections import deque

# for _ in range(int(input())):
#     cs = [list(input().rstrip()) for _ in range(3)]
#     ns = list(map(int, input().split()))
#     # print(cs, ns)

#     q = deque([cs[0][i] for i in range(3)] + [cs[1][2]] + [cs[2][i] for i in range(2, -1, -1)] + [cs[1][0]])
#     for _ in range(9):
#         if q[0] == 'X':
#             break
#         else:
#             q.append(q.popleft())
#     # print(q)

#     ans = []
#     cnt = 0
#     for a in q:
#         if a == 'O':
#             cnt += 1
#         else:
#             if cnt != 0:
#                 ans.append(cnt)
#             cnt = 0

#     if cnt != 0:
#         ans.append(cnt)
#     # print(ans)

#     print(1 if sorted(ans) == ns[1:] else 0)


# 16936 나3곱2
# N = int(input())
# ns = list(map(int, input().split()))

# nsets = [set(n for n in ns)]
# # print(nsets)

# i, div_val = 0, 3
# while nsets[i]:
#     nsets.append(set())
#     remove_set = set()
#     for a in nsets[i]:
#         if a % div_val == 0:
#             remove_set.add(a)
#             nsets[i+1].add(a)
#             # print("a", a)

#     for a in remove_set:
#         nsets[i].remove(a)

#     i += 1
#     div_val *= 3
# # print(nsets)

# for s in nsets[::-1][1:]:
#     print(*sorted(s), end=' ')


# 1689 겹치는 선분
# https://www.acmicpc.net/problem/1689
# import sys
# input = sys.stdin.readline
# from heapq import heappush, heappop

# N = int(input())
# lines = [list(map(int, input().split())) for _ in range(N)]
# lines.sort(key=lambda x:(x[0]))
# heap = []

# ans, cnt = 0, 0
# for now_l, now_r in lines:
#     while heap and heap[0] <= now_l:
#         heappop(heap)
#         cnt -= 1
#     heappush(heap, now_r)
#     cnt += 1
#     ans = max(ans, cnt)

# print(ans)


# TLE ( python3, pypy3 )
# import sys
# input = sys.stdin.readline

# N = int(input())
# lines = [[-1, -1] for _ in range(2*N)]
# for i in range(N):
#     l, r = map(int, input().split())
#     lines[2*i] = [l, 1]
#     lines[2*i+1] = [r, -1]
# lines.sort(key=lambda x:(x[0], x[1]))

# ans, cnt = 0, 0
# for _, val in lines:
#     cnt += val
#     ans = max(ans, cnt)

# print(ans)


# 20205 교수님 그림이 깨지는데요?
# N, K = map(int, input().split())
# for _ in range(N):
#     ns = list(map(int, input().split()))
#     for _ in range(K):
#         for n in ns:
#             for _ in range(K):
#                 print(n, end=' ')
#         print()


# 10973 이전 순열
# def solve():
#     N = int(input())
#     ns = [10001] + list(map(int, input().split()))
#     idx = N
#     now_val = ns[idx]

#     for idx in range(N-1, -1, -1):
#         if now_val > ns[idx]:
#             now_val = ns[idx]
#         else:
#             break

#     if idx == 0:
#         print(-1)
#         return

#     new_ns = sorted(ns[idx:])
#     now_val = new_ns[0]
#     for n in new_ns:
#         if ns[idx] > n:
#             now_val = n
#         else:
#             break

#     new_ns.remove(now_val)
#     print(*ns[1:idx], now_val, *new_ns[::-1], sep=' ')

# solve()


# 27907
# print('7 '*int(input()))


# 3135 라디오
# A, B = map(int, input().split())
# N = int(input())
# ns = [int(input()) for _ in range(N)]
# print("ns", ns)

# ans = abs(A-B)
# for n in ns:
#     ans = min(ans, abs(n-B)+1)

# print(ans)


# 24263 알고리즘 수업 - 알고리즘의 수행 시간 2
# print(int(input()), 1, sep='\n')


# 20041 Escaping
# import sys
# input = sys.stdin.readline

# N = int(input())
# # polices, target
# pxys = [list(map(int, input().split())) for _ in range(N)]
# tx, ty = map(int, input().split())

# # → ← ↑ ↓
# pos = [1]*4

# for px, py in pxys:
#     if not sum(pos):
#         break

#     # 도둑 기준으로 유리한 좌표 이동 수 계산
#     gap_x = abs(tx-px)
#     gap_y = abs(ty-py)
#     sign_x = 1 if (tx-px) > 0 else -1
#     sign_y = 1 if (ty-py) > 0 else -1

#     # →
#     sub_x = sign_x*gap_x
#     if (sub_x + gap_y) <= 0:
#         pos[0] = 0

#     # ←
#     sub_x = -sign_x*gap_x
#     if (sub_x + gap_y) <= 0:
#         pos[1] = 0

#     # ↑
#     sub_y = sign_y*gap_y
#     if (gap_x + sub_y) <= 0:
#         pos[2] = 0

#     # ↓
#     sub_y = -sign_y*gap_y
#     if (gap_x + sub_y) <= 0:
#         pos[3] = 0

# print("YES" if sum(pos) else "NO")


# 1456 거의 소수
# import math

# A, B = map(int, input().split())
# limit = math.isqrt(B)
# checks = [False, False] + [True]*(limit-1)

# for i in range(2, limit+1):
#     if checks[i]:
#         for ii in range(2*i, limit+1, i):
#             checks[ii] = False
# primes = [i for i in range(2, limit+1) if checks[i]]
# # print(len(primes))

# ans = 0
# for p in primes:
#     now_val = p**2
#     while now_val <= B:
#         if now_val >= A:
#             ans += 1
#         now_val *= p
#         # print(ans, now_val)

# print(ans)


# 15633 Fan Death
# n = int(input())
# ans = 0

# for i in range(1, int(n**(1/2))+1):
#     if n % i == 0:
#         ans += i + (n//i)
#         if i == (n//i):
#             ans -= i

# print(ans*5-24)


# 5567 결혼식
# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque

# def solve():
#     n = int(input())
#     g = defaultdict(list)

#     for _ in range(int(input())):
#         a, b = map(int, input().split())
#         g[a].append(b)
#         g[b].append(a)

#     ans = 0
#     visited = [False]*(n+1)
#     visited[1] = True
#     q = deque([1])

#     for _ in range(2):
#         for _ in range(len(q)):
#             v = q.popleft()
#             for u in g[v]:
#                 if not visited[u]:
#                     ans += 1
#                     visited[u] = True
#                     q.append(u)

#     print(ans)

# solve()


# 27902 CVE: Life is Way Too Short
# 2**14284 까지 출력
# n = int(input())
# if n <= 14284:
#     print(2**n)

# s = 2 ** int(input())
# if len(str(s)) <= 4300:
#     print(s)


# 28235
# D = dict()
# D["SONGDO"] = "HIGHSCHOOL"
# D["CODE"] = "MASTER"
# D["2023"] = "0611"
# D["ALGORITHM"] = "CONTEST"

# print(D[input()])


# 3047 ABC
# ns = sorted(list(map(int, input().split())))
# d = dict()
# d['A'] = ns[0]
# d['B'] = ns[1]
# d['C'] = ns[2]

# for c in input():
#     print(d[c], end=' ')


# 2566 최댓값

# i, j, max_val = -1, -1, -1
# for k in range(9):
#     ns = list(map(int, input().split()))
#     for idx in range(9):
#         if max_val < ns[idx]:
#             max_val = ns[idx]
#             i = k
#             j = idx

# print(max_val)
# print(i+1, j+1)


# 15894 수학은 체육과목 입니다
# print(4*int(input()))


# 27535 제주 초콜릿 지키기
# def cal_n_base(n, base):
#     if n == 0: return 0

#     k = ""
#     while n > 0:
#         k += str(n % base)
#         n //= base
#     return k[::-1]

# def solve():
#     alphas = "HTCKG"
#     tmp_ns = list(map(int, input().split()))
#     ns = dict()
#     for i in range(5):
#         ns[alphas[i]] = tmp_ns[i]
#     # print("ns", ns)
#     base = sum(tmp_ns)%10
#     if base <= 1:
#         base = 10

#     for _ in range(int(input())):
#         tmp_ns = list(map(int, input().split()))
#         for i in range(5):
#             ns[alphas[i]] -= tmp_ns[i]
#         # print(ns)

#         sum_ns = sum(ns.values())
#         print(f"{cal_n_base(sum_ns, base)}7H")

#         if sum_ns == 0:
#             print("NULL")
#             continue
#         else:
#             vals = sorted(ns.items(), key=lambda x: (-x[1], x[0]))
#             for i in range(5):
#                 if vals[i][1] == 0:
#                     break
#                 print(vals[i][0], end="")
#             print()

#             base = sum_ns % 10
#             if base <= 1:
#                 base = 10

# solve()


# 2857 FBI
# ans = []
# for i in range(5):
#     name = list(input().split("-"))
#     checks = False
#     for n in name:
#         if "FBI" in n:
#             checks = True
#             break

#     if checks:
#         ans.append(i + 1)

# print(*ans) if ans else print("HE GOT AWAY!")


# 1799 비숍
"""
10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
"""

# def btr(board:list, checks:list, N, len_board, std_x):
#     global cnt, max_cnt

#     for i in range(std_x, len_board):
#         for j in range(len(board[i])):
#             x, y = board[i][j]
#             if not checks[N-x+y]:
#                 checks[N-x+y] = True
#                 cnt += 1
#                 max_cnt = max(max_cnt, cnt)

#                 btr(board, checks, N, len_board, i+1)
#                 checks[N-x+y] = False
#                 cnt -= 1

# def solve():
#     N = int(input())
#     input_board = [list(map(int, input().split())) for _ in range(N)]

#     # separated boards : 흑백 따로
#     sep_boards = [[[] for _ in range(N)], [[] for _ in range(N-1)]]
#     # print(sep_boards)

#     checks = [False]*(2*N)

#     for x in range(N):
#         for y in range(N):
#             if input_board[x][y]:
#                 sep_boards[(x+y)%2][(x+y)//2].append([x,y])
#     # for k in range(2):
#     #     print(sep_boards[k])

#     ans = 0
#     global cnt, max_cnt
#     for i in range(2):
#         cnt, max_cnt = 0, 0
#         btr(sep_boards[i], checks, N, len(sep_boards[i]), 0)
#         ans += max_cnt

#     print(ans)

# solve()


# 10775 공항
"""
5
10
5
5
5
5
5
4
[정답] 5
"""
# import sys
# input = sys.stdin.readline

# G = int(input())
# parent = [i for i in range(G+1)]

# def find_parent(x):
#     if x != parent[x]:
#         parent[x] = find_parent(parent[x])
#     return parent[x]

# ans = 0
# for _ in range(int(input())):
#     gi = int(input())

#     # if parent[gi] == 0:
#     if find_parent(gi) == 0:
#         break

#     ans += 1
#     # parent[find_parent(parent[gi])] -= 1
#     parent[parent[gi]] -= 1
#     find_parent(gi)
#     # print(ans, parent)

# print(ans)


# 1956 운동
# import sys
# input = sys.stdin.readline

# V, E = map(int, input().split())
# INF = int(5e6)
# dist = [[INF] * V for _ in range(V)]
# # for i in range(V):
# #     dist[i][i] = 0
# # print("dist", dist)

# for _ in range(E):
#     a, b, c = map(int, input().split())
#     dist[a - 1][b - 1] = c

# for k in range(V):
#     for m in range(V):
#         for n in range(V):
#             dist[k][n] = min(dist[k][n], dist[k][m] + dist[m][n])

# ans = INF
# for i in range(V):
#     for j in range(V):
#         ans = min(ans, dist[i][j] + dist[j][i])

# print(ans if ans != INF else -1)


# 11256 사탕
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     J, N = map(int, input().split())
#     cnt = 0
#     boxes = [list(map(int, input().split())) for _ in range(N)]
#     boxes = sorted([boxes[i][0] * boxes[i][1] for i in range(N)], reverse=True)
#     # print(boxes)

#     for b in boxes:
#         J -= b
#         cnt += 1
#         if J <= 0:
#             break

#     print(cnt)


# 1547 공
# ans = 1
# for _ in range(int(input())):
#     X, Y = map(int, input().split())
#     if X == ans:
#         ans = Y
#     elif Y == ans:
#         ans = X

# print(ans)


# 1509 팰린드롬 분할
# s = list(input())
# # print(s)

# len_s = len(s)
# dp1 = [[0] * len_s for _ in range(len_s)]
# dp2 = [[0] * len_s for _ in range(len_s)]

# for i in range(len_s):
#     for k in range(min(i, len_s - 1 - i) + 1):
#         if s[i - k] == s[i + k]:
#             dp1[i][i - k] = 2 * k + 1
#         else:
#             break

# for i in range(len_s - 1):
#     for k in range(min(i, len_s - 2 - i) + 1):
#         if s[i - k] == s[i + k + 1]:
#             dp2[i][i - k] = 2 * (k + 1)
#         else:
#             break

# # for i in range(len_s):
# #     print(dp1[i])
# #     # print(dp2[i])
# # print()

# dp3 = [2500] * (len_s + 1)
# dp3[0] = 0

# for y in range(len_s):
#     for x in range(len_s):
#         for this_dp in [dp1, dp2]:
#             if this_dp[x][y] == 0:
#                 continue

#             ny = y + this_dp[x][y]
#             dp3[ny] = min(dp3[ny], dp3[y] + 1)

# print(dp3[len_s])


# 12850 본대 산책2
# A^D

# mod = int(1e9) + 7

# def mul_matrix(matrix_a, matrix_b):
#     return_matrix = [[0] * 8 for _ in range(8)]
#     for i in range(8):
#         for j in range(8):
#             for k in range(8):
#                 return_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
#             return_matrix[i][j] %= mod
#     return return_matrix

# def matrix_power_n(matrix: list, n: int):
#     if n % 2 == 1:
#         if n == 1:
#             return matrix
#         return mul_matrix(matrix, matrix_power_n(matrix, n - 1))
#     else:
#         matrix_power_half_n = matrix_power_n(matrix, n // 2)
#         return mul_matrix(matrix_power_half_n, matrix_power_half_n)

# def solve():
#     D = int(input())
#     A = [
#         [0, 1, 1, 0, 0, 0, 0, 0],
#         [1, 0, 1, 1, 0, 0, 0, 0],
#         [1, 1, 0, 1, 1, 0, 0, 0],
#         [0, 1, 1, 0, 1, 1, 0, 0],
#         [0, 0, 1, 1, 0, 1, 1, 0],
#         [0, 0, 0, 1, 1, 0, 0, 1],
#         [0, 0, 0, 0, 1, 0, 0, 1],
#         [0, 0, 0, 0, 0, 1, 1, 0],
#     ]
#     print(matrix_power_n(A, D)[0][0])

# solve()


# 12833 XORXORXOR
# A, B, C = map(int, input().split())
# if C % 2 == 0:
#     print(A)
# else:
#     print(A ^ B)


# 24389 2의 보수
# N = int(input())
# print(32 - len(str(bin(N ^ (~N + 1)))[4:]))


# 1740 거듭제곱
# N = int(input())
# ans, mul_val = 0, 1

# for n in format(N, "b")[::-1]:
#     ans += int(n) * mul_val
#     mul_val *= 3
# print(ans)


# 11811 데스스타
# import sys
# input = sys.stdin.readline

# N = int(input())
# ns = [list(map(int, input().split())) for _ in range(N)]
# ans = [0] * N

# for i in range(N):
#     for j in range(N):
#         ans[i] |= ns[i][j]

# print(*ans)


# 2098

# INF = int(20e6)


# def isIn(i, A):
#     if A & (1 << (i - 2)):
#         return True
#     return False

# def diff(A, j):
#     t = 1 << (j - 2)
#     return A & (~t)

# def count(A, n):
#     count = 0
#     for i in range(n):
#         if (A & (1 << i)) != 0:
#             count += 1
#     return count


# def minimum(W, D, i, A):
#     minValue = INF
#     n = len(W) - 1
#     for j in range(2, n + 1):
#         if isIn(j, A):
#             m = W[i][j] + D[j][diff(A, j)]
#             if minValue > m:
#                 minValue = m
#     return minValue

# def travel(W):
#     n = len(W) - 1
#     size = 2 ** (n - 1)
#     D = [[0] * size for _ in range(n + 1)]
#     for i in range(2, n + 1):
#         D[i][0] = W[i][1]
#     for k in range(1, n - 1):
#         for A in range(1, size):
#             if count(A, n) == k:
#                 for i in range(2, n + 1):
#                     if not isIn(i, A):
#                         D[i][A] = minimum(W, D, i, A)
#     A = size - 1
#     for i in range()
#     D[1][A] = minimum(W, D, 1, A)

#     # print("D")
#     # for i in range(n + 1):
#     #     print(*D[i])

#     return D


# def solve():
#     N = int(input())
#     W = [[-1] * (N + 1), *[[-1] + list(map(int, input().split())) for _ in range(N)]]
#     print(travel(W)[1][-1])


# solve()


# 28239 배고파(Easy)
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     m = int(input())
#     str = bin(m)[2:][::-1]

#     cnt = 0
#     idxs = []
#     for i in range(len(str)):
#         if str[i] == "1":
#             idxs.append(i)
#             cnt += 1
#     # print(cnt, idxs)

#     print(*idxs) if cnt == 2 else print(*([idxs[0] - 1] * 2))


# 15787 기차가 어둠을 헤치고 은하수를
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# trains = [0] * (N+1)
# cut = (1 << 20)-1

# for _ in range(M):
#     cmd = list(map(int, input().split()))
#     if cmd[0] == 1:
#         i, x = cmd[1:]
#         trains[i] |= 1 << (x-1)
#     elif cmd[0] == 2:
#         i, x = cmd[1:]
#         trains[i] &= ~(1 << (x-1))
#     elif cmd[0] == 3:
#         i = cmd[1]
#         trains[i] *= 2
#         trains[i] &= cut
#     else:
#         i = cmd[1]
#         trains[i] //= 2

# train_set = set()
# for t in trains[1:]:
#     if t not in train_set:
#         train_set.add(t)

# print(len(train_set))


# 13411 하늘에서 정의가 빗발친다!
# import math
# import sys
# input = sys.stdin.readline

# N = int(input())
# ns = [list(map(int, input().split())) for _ in range(N)]
# ps = [[math.sqrt(ns[i][0]**2+ns[i][1]**2)/ns[i][2], i+1] for i in range(N)]
# ps.sort(key=lambda x:(x[0], x[1]))
# print(*[ps[i][1] for i in range(N)], sep='\n')


# 28282 운명
# X, K = map(int, input().split())
# ns = list(map(int, input().split()))
# left, right = ns[:X], ns[X:]
# # print(left, right)

# acc_left, acc_right = [0]*(K+1), [0]*(K+1)
# for l in left: acc_left[l] += 1
# for r in right: acc_right[r] += 1
# # print(acc_left, acc_right)
# sum_left, sum_right = sum(acc_left), sum(acc_right)

# ans = 0
# for i in range(1, K+1):
#     ans += acc_left[i] * (sum_right - acc_right[i])
# print(ans)


# 3474 교수가 된 현우
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     T = int(input())
#     ans, div_num = 0, 5

#     while div_num <= T:
#         ans += T // div_num
#         div_num *= 5
#     print(ans)


# 10810 공 넣기
# N, M = map(int, input().split())
# ans = [0]*(N+1)
# for _ in range(M):
#     i, j, k = map(int, input().split())
#     for idx in range(i, j+1):
#         ans[idx] = k
# print(*ans[1:])


# 3049 다각형의 대각선
# def fac(n):
#     val = 1
#     for k in range(2, n+1):
#         val *= k
#     return val

# def solve():
#     N = int(input())
#     print(fac(N)//(fac(N-4)*fac(4)))

# solve()



# 2766 Candy Sharing Game
# def end_check(ns, N):
#     end = True
#     for i in range(1, N):
#         if ns[0] != ns[i]:
#             end = False
#             break
#     return end

# def solve():
#     import sys
#     input = sys.stdin.readline

#     while True:
#         N = int(input())
#         if N == 0:
#             break

#         rounds = 0
#         ns = [int(input()) for _ in range(N)]
        
#         while not end_check(ns, N):
#             tmp_ns = [0]*N
#             for i in range(N):
#                 tmp_ns[i] -= ns[i] //2
#                 tmp_ns[(i+1)%N] += ns[i]//2

#             for i in range(N):
#                 ns[i] += tmp_ns[i]
#                 if ns[i] % 2 != 0:
#                     ns[i] += 1

#             rounds += 1

#         print(rounds, ns[0])

# solve()


# 23663 Deja vu of Go Players
# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     input(), input()
#     print("Yes") if n <= m else print("No")


# 7453 합이 0인 네 정수
# import sys
# input = sys.stdin.readline

# n = int(input())
# ns = [list(map(int, input().split())) for _ in range(n)]

# ws, xs, ys, zs = [[ns[i][k] for i in range(n)] for k in range(4)]
# # print(ws, xs, ys, zs)

# js, ks = sorted([w+x for w in ws for x in xs]), sorted([y+z for y in ys for z in zs])
# # print(js, ks)

# l, len_js, r = 0, len(js), len(ks)-1

# ans = 0
# while l <= len_js-1 and r >= 0:
#     s = js[l]+ks[r]
#     if s < 0:
#         l += 1
#     elif s > 0:
#         r -= 1
#     else:
#         l_cnt, r_cnt = 1, 1
#         while l + l_cnt <= len_js-1 and js[l] == js[l+l_cnt]:
#             l_cnt += 1

#         while r - r_cnt >= 0 and ks[r] == ks[r-r_cnt]:
#             r_cnt += 1

#         l += l_cnt
#         r -= r_cnt
#         ans += (l_cnt * r_cnt)

# print(ans)


# 19638 센티와 마법의 뿅망치
# from heapq import heapify, heappush, heappop

# N, H, T = map(int, input().split())
# heap = [-int(input()) for _ in range(N)]
# heapify(heap)
# # print(heap)

# H = -H
# cnt = 0
# while T > 0:
#     if heap[0] > H: break
#     heappush(heap, min((heappop(heap)+1)//2, -1))
#     T -= 1
#     cnt += 1

# print("YES", cnt, sep='\n') if heap[0] > H else print("NO", -heap[0], sep='\n')


# 17352 여러분의 다리가 되어 드리겠습니다!
'''
6
1 2
3 4
3 5
5 2
'''
'''
4
2 3
1 2
'''

# import sys
# input = sys.stdin.readline

# N = int(input())
# parent = [i for i in range(N+1)]

# def find_parent(x):
#     if x != parent[x]:
#         parent[x] = find_parent(parent[x])
#     return parent[x]

# def union_parent(a, b):
#     a = find_parent(a)
#     b = find_parent(b)

#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a

# def solve():
#     for _ in range(N-2):
#         a, b = map(int, input().split())
#         union_parent(a, b)
#         # print("parent a b", a, b, parent)

#     # why
#     # for i in range(2, N+1):
#     #     find_parent(i)
#     print(parent)

#     for i in range(2, N+1):
#         if parent[i] != 1:
#             print(1, i)
#             break

# solve()


# 24313 알고리즘 수업 - 점근적 표기 1
# a1, a0 = map(int, input().split())
# c = int(input())
# n0 = int(input())

# if c >= a1:
#     print(1) if a0 <= n0*(c-a1) else print(0)
# else:
#     print(0)



# 3053 택시 기하학
# import math

# R = int(input())
# print('{0:.6f}'.format(math.pi*(R**2)))
# print('{0:.6f}'.format(2*(R**2)))


# 28449 누가 이길까
# import sys
# input = sys.stdin.readline

# _, M = map(int, input().split())
# ns = sorted(list(map(int, input().split())))
# ms = sorted(list(map(int, input().split())))

# win, lose, draw = 0, 0, 0
# for n in ns:
#     l, r = 0, M-1
#     target = 0
#     while l <= r:
#         mid = (l+r)//2

#         if ms[mid] <= n:
#             target = mid
#             if ms[mid] == n:
#                 break
#             l = mid+1
#         elif ms[mid] > n:
#             r = mid-1
#     # print("target", target, "mid", mid)

#     if ms[target] < n:
#         win += target+1
#         lose += (M-target-1)
#     elif ms[target] > n:
#         win += target
#         lose += (M-target)
#     else: # ms[target] == n
#         ll, lr = 0, target
#         l_target = target
#         while ll <= lr:
#             mid = (ll+lr) //2
#             if ms[mid] < ms[target]:
#                 ll = mid+1
#             else:
#                 l_target = mid
#                 lr = mid-1

#         rl, rr = target, M-1
#         r_target = target
#         while rl <= rr:
#             mid = (rl+rr) //2
#             if ms[mid] <= ms[target]:
#                 r_target = mid
#                 rl = mid+1
#             else:
#                 rr = mid-1

#         win += l_target
#         draw += r_target-l_target+1
#         lose += M-r_target-1
#     # print(n, "n", win, lose, draw)

# print(win, lose, draw)


# 28449 누가 이길까
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# ns = list(map(int, input().split()))
# ms = list(map(int, input().split()))

# limit = (int(1e5)+1)
# cnt_ms = [0]*limit

# for m in ms:
#     cnt_ms[m] += 1

# for i in range(1, limit):
#     cnt_ms[i] += cnt_ms[i-1]

# win, lose, draw = 0, 0, 0
# for n in ns:
#     win += cnt_ms[n-1]
#     draw += cnt_ms[n]-cnt_ms[n-1]
#     lose += M-cnt_ms[n]

# print(win, lose, draw)


# 2942 퍼거슨과 사과
# import math

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

# def solve():
#     R, G = map(int, input().split())
#     divisor = gcd(R, G)
#     # print(divisor)

#     for i in range(1, math.isqrt(divisor)+1):
#         if divisor % i == 0:
#             print(i, R//i, G//i)
#             if i != divisor//i:
#                 div_val = divisor//i
#                 print(div_val, R//div_val, G//div_val)

# solve()


# 16165 걸그룹 마스터 준석이
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# girlGroupDict1 = dict()
# girlGroupDict2 = dict()

# for _ in range(N):
#     groupName = input().rstrip()
#     cnt = int(input())
#     members = sorted([input().rstrip() for _ in range(cnt)])
#     girlGroupDict1[groupName] = members

#     for m in members:
#         girlGroupDict2[m] = groupName

# for _ in range(M):
#     name = input().rstrip()
#     n = int(input())
#     if n == 0:
#         print(*girlGroupDict1[name], sep='\n')
#     else:
#         print(girlGroupDict2[name])


# 16945 매직 스퀘어로 변경하기
# import itertools

# board = [list(map(int, input().split())) for _ in range(3)]
# board = [board[i][j] for i in range(3) for j in range(3)]

# ans = 100
# for k in itertools.permutations(range(1, 10), 9):
#     # print(k)

#     rs = [[k[3*i + j] for j in range(3)] for i in range(3)]
#     # print(rs)

#     cs = [[k[i + 3*j] for j in range(3)] for i in range(3)]
#     # print(cs)

#     std = (k[0]+k[4]+k[8])
#     if std == (k[2]+k[4]+k[6]):
#         pos = True

#         for i in range(3):
#             if std != sum(rs[i]) or std != sum(cs[i]):
#                 pos = False
#                 break

#         if pos:
#             tmp_sum = 0
#             for i in range(9):
#                 tmp_sum += abs(k[i] - board[i])
#             # print(tmp_sum)
#             ans = min(ans, tmp_sum)

# print(ans)


# 28470 슥~빡! 빡~슥!
# N = int(input())
# As = list(map(int, input().split()))
# Bs = list(map(int, input().split()))
# Ks = list(map(float, input().split()))

# ans = 0
# for i in range(N):
#     if Ks[i] >= 1:
#         ans += int(As[i]*(Ks[i]*10))//10 - Bs[i]
#     else:
#         ans += As[i] - int(Bs[i]*(Ks[i]*10))//10

# print(ans)


# 28471 W키가 빠진 성원이
# import sys
# input = sys.stdin.readline
# from collections import deque

# N = int(input())
# board = [list(input().rstrip()) for _ in range(N)]
# # print(board)
# inc_xy = [[0, 1], [1, 1], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
# visited = [[False]*N for _ in range(N)]

# q = deque([[x, y] for x in range(N) for y in range(N) if board[x][y]=='F'])
# x, y = q[0]
# visited[x][y] = True

# ans = 0
# while q:
#     x, y = q.popleft()
#     for px, py in inc_xy:
#         nx, ny = x+px, y+py
#         if 0 <= nx < N and 0 <= ny < N:
#             if board[nx][ny] == '.' and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 q.append([nx, ny])
#                 ans += 1

# print(ans)


# 20001 고무오리 디버깅

# cnt = 0
# while True:
#     s = input()
#     if s == '문제':
#         cnt += 1
#     elif s == '고무오리':
#         if cnt == 0:
#             cnt += 2
#         else:
#             cnt -= 1
#     elif s == '고무오리 디버깅 끝':
#         break

# print("고무오리야 사랑해" if not cnt else "힝구")


# 12886 돌 그룹
# from collections import deque

# def solve():
#     q = deque([list(map(int, input().split()))])
#     # print(q)
#     ns_set = set(tuple(q[0]))
#     # print(ns_set)

#     while q:
#         ns = q.popleft()
#         if ns[0] == ns[1] == ns[2]:
#             print(1)
#             return

#         for i in range(0, 2):
#             for j in range(i+1, 3):
#                 check = False
#                 next = []

#                 if ns[i] < ns[j]:
#                     for k in range(3):
#                         if k != i and k != j:
#                             check = True
#                             next = sorted([[i, 2*ns[i]], [j, ns[j]-ns[i]], [k, ns[k]]], key=lambda x:(x[0]))
#                 elif ns[i] > ns[j]:
#                     for k in range(3):
#                         if k != i and k != j:
#                             check = True
#                             next = sorted([[i, ns[i]-ns[j]], [j, 2*ns[j]], [k, ns[k]]], key=lambda x:(x[0]))

#                 if check:
#                     next = tuple([next[i][1] for i in range(3)])
#                     if next not in ns_set:
#                         ns_set.add(next)
#                         q.append(next)
#     print(0)

# solve()


# from collections import deque

# def q_append_check(next, ns_set, q):
#     if next:
#         next = tuple(next)
#         if next not in ns_set:
#             ns_set.add(next)
#             q.append(next)

# def solve():
#     q = deque([list(map(int, input().split()))])
#     # print(q)
#     ns_set = set(tuple(q[0]))
#     # print(ns_set)

#     while q:
#         ns = q.popleft()
#         if ns[0] == ns[1] == ns[2]:
#             print(1)
#             return

#         next = []
#         if ns[0] > ns[1]:   next = [ns[0]-ns[1], 2*ns[1], ns[2]]
#         elif ns[0] < ns[1]: next = [2*ns[0], ns[1]-ns[0], ns[2]]
#         q_append_check(next, ns_set, q)

#         next = []
#         if ns[0] > ns[2]:   next = [ns[0]-ns[2], ns[1], 2*ns[2]]
#         elif ns[0] < ns[2]: next = [2*ns[0], ns[1], ns[2]-ns[0]]
#         q_append_check(next, ns_set, q)

#         next = []
#         if ns[1] > ns[2]:   next = [ns[0], ns[1]-ns[2], 2*ns[2]]
#         elif ns[1] < ns[2]: next = [ns[0], 2*ns[1], ns[2]-ns[1]]
#         q_append_check(next, ns_set, q)

#     print(0)

# solve()


# 27918 탁구 경기
# import sys
# input = sys.stdin.readline

# N = int(input())
# D, P = 0, 0

# for _ in range(N):
#     c = input().rstrip()
#     if c == 'D': D += 1
#     else: P += 1

#     if abs(D-P) >= 2:
#         break

# print(f'{D}:{P}')


# 5648 역원소 정렬
# import sys

# strs = sys.stdin.readlines()
# strs = [s.rstrip().split() for s in strs]
# strs[0] = strs[0][1:]
# # print(strs)

# ans = [int(s[::-1]) for ss in strs for s in ss]
# print(*sorted(ans), sep='\n')


# 10472 십자뒤집기
# import sys
# input = sys.stdin.readline
# from collections import deque

# def toggle(board, x, y):
#     if board[x][y] == '*':
#         board[x][y] = '.'
#     else:
#         board[x][y] = '*'

# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# for _ in range(int(input())):
#     target = tuple(tuple(input().rstrip()) for _ in range(3))
#     # print(target)

#     start_board = tuple([tuple(['.']*3) for _ in range(3)])
#     # board_set = set(start_board)
#     board_set = set()
#     board_set.add(start_board)
#     # print(board_set)

#     q = deque([[start_board, 0]])
#     while q:
#         now, cnt = q.popleft()
#         if now == target:
#             print(cnt)
#             break

#         for x in range(3):
#             for y in range(3):
#                 new_board = [list(now[i][:]) for i in range(3)]
#                 toggle(new_board, x, y)

#                 for px, py in inc_xy:
#                     nx, ny = x+px, y+py
#                     if 0 <= nx < 3 and 0 <= ny < 3:
#                         toggle(new_board, nx, ny)

#                 tupled_new_board = tuple(tuple(new_board[i][:]) for i in range(3))
#                 if tupled_new_board not in board_set:
#                     board_set.add(tupled_new_board)
#                     q.append([tupled_new_board, cnt+1])


# 18765 정*수-를+[만들자!]
# from collections import deque

# dp = [1000]*1001
# ans = ['+[]',
#         '+!![]',
#         '!![]+!![]',
#         '!![]+!![]+!![]',
#         '!![]+!![]+!![]+!![]',
#         '!![]+!![]+!![]+!![]+!![]',
#         '[!![]+!![]+!![]]*[!![]+!![]]',
#         '[+!![]]+[+[]]-!![]-!![]-!![]',
#         '[+!![]]+[+[]]-!![]-!![]',
#         '[+!![]]+[+[]]-!![]',
#         '[+!![]]+[+[]]'
#         ] + ['_'*1000]*990
# # print(ans[:13])

# q = deque([[10, len('[+!![]]+[+[]]')]])

# max_len = 0
# for i in range(11, 1001):
#     tmp_ans = '[' + ']+['.join([ans[k] for k in list(map(int, str(i)))]) + ']'
#     ans[i] = tmp_ans
#     # print(tmp_ans)
#     max_len = max(max_len, len(tmp_ans))
#     q.append([i, len(tmp_ans)])
# # print(max_len)

# for i in range(1001):
#     dp[i] = len(ans[i])

# while q:
#     v, l = q.popleft()

#     if v-1 >= 0 and dp[v-1] > (dp[v]+5):
#         dp[v-1] = dp[v]+5
#         q.append([v-1, dp[v]+5])
#         ans[v-1] = f'{ans[v]}-!![]'

#     if v+1 <= 1000 and dp[v+1] > (dp[v]+5):
#         dp[v+1] = dp[v]+5
#         q.append([v+1, dp[v]+5])
#         ans[v+1] = f'{ans[v]}+!![]'

#     for k in range(2, 11):
#         if k*v <= 1000:
#             next_dp_len = dp[v]+5+len(ans[k])
#             if dp[k*v] > next_dp_len:
#                 dp[k*v] = next_dp_len
#                 q.append([k*v, next_dp_len])
#                 ans[k*v] = f'[{ans[v]}]*[{ans[k]}]'
#         else:
#             break

#     if v >= 2:
#         now = v
#         for k in range(2, 11):
#             # now == v**k
#             now *= v
#             if now <= 1000:
#                 next_dp_len = dp[v]+6+len(ans[k])
#                 if dp[now] > next_dp_len:
#                     dp[now] = next_dp_len
#                     q.append([now, next_dp_len])
#                     ans[now] = f'[{ans[v]}]**[{ans[k]}]'
#             else:
#                 break

# # print(dp[:20])
# # print(*ans[:11], sep='\n')
# # print([len(ans[i]) for i in range(11)])

# print(max(len(ans[i]) for i in range(1001)))

# f = open("./result.txt", 'w')
# for i in range(1001):
#     f.write(f'+[{ans[i]}]\n')
# f.close()


# 24049 정원 (Easy)
# N, M = map(int, input().split())

# board = [[0]*(M+1) for _ in range(N+1)]
# ns = list(map(int, input().split()))
# ms = list(map(int, input().split()))

# for i in range(N):
#     board[1+i][0] = ns[i]
# for i in range(M):
#     board[0][1+i] = ms[i]

# for x in range(1, N+1):
#     for y in range(1, M+1):
#         board[x][y] = board[x][y-1] ^ board[x-1][y]

# print(board[N][M])


# 2230 수 고르기
# N, M = map(int, input().split())
# ns = sorted([int(input()) for _ in range(N)])

# l, r = 0, 0
# ans = int(2e9)

# while l <= r and r <= N-1:
#     gap = ns[r]-ns[l]
#     if gap < M:
#         r += 1
#     elif gap > M:
#         ans = min(ans, gap)
#         l += 1
#     else:
#         ans = M
#         break

# print(ans)


# 16922 로마 숫자 만들기
# def btr(now_idx, rest_n, ns, ans, sum_set):
#     for val in range(0, rest_n+1):
#         ns[now_idx] = val
#         if now_idx < 3:
#             btr(now_idx+1, rest_n-val, ns, ans, sum_set)
#         else:
#             ns[3] = rest_n
#             now_sum = ns[0] + 5*ns[1] + 10*ns[2] + 50*ns[3]
#             if now_sum not in sum_set:
#                 sum_set.add(now_sum)
#                 ans[0] += 1

# def solve():
#     N = int(input())
#     ns = [0]*4
#     ans = [0]
#     sum_set = set()

#     btr(0, N, ns, ans, sum_set)
#     print(ans[0])

# solve()


# 5587 카드 캡터 상근이
# n = int(input())

# ns = sorted([int(input()) for _ in range(n)])
# ns_have = [True]*(n)
# ns_set = set(ns)

# ms = sorted([i for i in range(1, 2*n+1) if i not in ns_set])
# ms_have = [True]*(n)
# # print(ms)

# ans_n, ans_m = 0, 0
# now_n, now_m = n, n
# field_card = 0
# sg_turn = True

# while now_n > 0 and now_m > 0:
#     pos = False

#     if sg_turn:
#         for i in range(n):
#             if field_card < ns[i] and ns_have[i]:
#                 field_card = ns[i]
#                 ns_have[i] = False
#                 now_n -= 1
#                 pos = True
#                 break
#     else:
#         for i in range(n):
#             if field_card < ms[i] and ms_have[i]:
#                 field_card = ms[i]
#                 ms_have[i] = False
#                 now_m -= 1
#                 pos = True
#                 break

#     sg_turn = not sg_turn

#     if not pos:
#         field_card = 0

# print(now_m, now_n, sep='\n')


# kKK
# A
# A, B = map(int, input().split())
# K, X = map(int, input().split())
# # ans = min(K+X, B)-max(max(K-X, 0), A)+1
# # print(ans if ans else "IMPOSSIBLE")

# checks = [0]*10001
# for i in range(max(K-X, 0), min(K+X, B)+1):
#     checks[i] = 1

# ans = sum(checks[A:B+1])
# print(ans if ans else "IMPOSSIBLE")


# B
# import sys
# input = sys.stdin.readline

# # 등수
# def cal_round(n):
#     if n > 4500:
#         return "Round 1"
#     elif n > 1000:
#         return "Round 2"
#     elif n > 25:
#         return "Round 3"
#     else:
#         return "World Finals"

# for i in range(1, int(input())+1):
#     print(f'Case #{i}: {cal_round(int(input()))}')


# C
# https://brownbears.tistory.com/483
# yyyy, mm, dd = list(map(int, input().split('-')))
# # tot = 360*yyyy + 30*mm + dd
# # tot += int(input())
# # yyyy, mm, dd = tot//360, ((tot%360)//30), ((tot-1)%30)+1

# dd += int(input())
# mm_prime = (dd-1)//30
# dd = (dd-1)%30+1

# mm += mm_prime
# yyyy_prime = (mm-1)//12
# mm = (mm-1)%12+1

# yyyy += yyyy_prime

# print(f'{yyyy}-{str(mm).zfill(2)}-{str(dd).zfill(2)}')


# D
# szero, N, M = map(int, input().split())
# U = 0

# for _ in range(N+M):
#     cmd = int(input())
#     if cmd:
#         U += 1
#         if szero < U:
#             szero *= 2
#     else:
#         U -= 1

# print(szero)


# E
# N, M, K = map(int, input().split())
# print(max(0, N-M*K), N-(M*(K-1)+1))


# F
# sumWeight = 0
# sumA = 0

# for _ in range(int(input())):
#     T, W, H, L = map(str, input().split())
#     W, H, L = int(W), int(H), int(L)

#     if T == 'A':
#         cnt = (W//12)*(H//12)*(L//12)
#         sumWeight += 1000 + 500*cnt
#         sumA += cnt
#     else:
#         sumWeight += 6000

# print(sumWeight, sumA*4000, sep='\n')


# G
# checks
# N, M = map(int, input().split())
# mod = int(1e9)+7

# A = M
# for i in range(N-1):
#     A = (A*M)%mod

# B = M-1
# for i in range(N-1):
#     B = (B*(M-1))%mod

# print((A-B)%mod)


# H
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# cols = ['']+[sum([board[x][y] for x in range(N)]) for y in range(M)]
# # print(cols)
# A = int(input())

# sums = [0]*(M+1)
# for i in range(1, M+1):
#     sums[i] = sums[i-1] + cols[i]
# # print(sums)

# max_val = -1
# for i in range(A, M+1):
#     max_val = max(max_val, sums[i]-sums[i-A])
#     # print(i, i-A)
# print(max_val)


# Z
# s_set = set({
# 'Never gonna give you up',
# 'Never gonna let you down',
# 'Never gonna run around and desert you',
# 'Never gonna make you cry',
# 'Never gonna say goodbye',
# 'Never gonna tell a lie and hurt you',
# 'Never gonna stop'}
# )
# # print(s_set)

# hacked = False
# for _ in range(int(input())):
#     s = input()
#     if s not in s_set:
#         hacked = True
#         break

# print("Yes" if hacked else "No")


# Y
# board = [list(input()) for _ in range(8)]
# w, b = 0, 0

# for x in range(8):
#     for y in range(8):
#         if board[x][y] == 'P': w += 1
#         elif board[x][y] == 'N': w += 3
#         elif board[x][y] == 'B': w += 3
#         elif board[x][y] == 'R': w += 5
#         elif board[x][y] == 'Q': w += 9

#         elif board[x][y] == 'p': b += 1
#         elif board[x][y] == 'n': b += 3
#         elif board[x][y] == 'b': b += 3
#         elif board[x][y] == 'r': b += 5
#         elif board[x][y] == 'q': b += 9

# print(w-b)


# X
# 지문 이해 때문에 시간 잡아먹음
# N, M = map(int, input().split())
# T, S = map(int, input().split())

# zip_add_time = S*((N-1)//8)
# dzd_cnt = (M-1)//8
# dok_add_time = 2*T*dzd_cnt + S*dzd_cnt

# zip_tot_time = N+zip_add_time
# dok_tot_time = T+M+dok_add_time

# isZipFast = zip_tot_time < dok_tot_time
# print('Zip' if isZipFast else 'Dok')
# print(zip_tot_time if isZipFast else dok_tot_time)


# W
# ascii_code
# https://stepbystep1.tistory.com/10
# J, N = map(int, input().split())

# cnt = 0
# for _ in range(N):
#     s = list(input())
#     # print(s)

#     now = 0
#     for a in s:
#         ord_a = ord(a)
#         if 65 <= ord_a <= 90:
#             now += 4
#         elif (97 <= ord_a <= 122) or (48 <= ord_a <= 57):
#             now += 2
#         else:
#             now += 1
#     # print(now)

#     if now <= J:
#         cnt += 1

# print(cnt)


# V
# input()
# s = list(input())
# # cnts
# c = [0]*27
# for a in s:
#     c[ord(a)-64] += 1
# # print(c)

# print(min(c[2], c[18]//2, c[15], c[14], c[26], c[5]//2, c[19], c[9], c[12], c[22]))


# U
# 다시 한 번 보자 (복습 필요)

'''
07:00 12:00
4 60
'''
# s, e = map(str, input().split())
# N, T = map(int, input().split())

# sh, sm = map(int, s.split(':'))
# eh, em = map(int, e.split(':'))
# # print(ss, se)

# s_time = sh*60+sm
# e_time = eh*60+em
# # print(s_time, e_time)
# gap = e_time - s_time

# cnt_per_day = (gap-1) // T
# print(cnt_per_day)
# # tot_day = (N+1)//cnt_per_day
# tot_day = N//cnt_per_day
# # s_time += ((N+1)-tot_day*cnt_per_day)*T
# s_time += ((N+1)%cnt_per_day)*T # 이것도 될 듯 # 다시 보니 안 된다

# print(tot_day)
# print(f'{str(s_time//60).zfill(2)}:{str(s_time%60).zfill(2)}')


# T
# 두 포인터 가능

'''
2 1 1
.R
'''
# N, M, K = map(int ,input().split())
# s = list(input())

# infected = [0]*N
# for i in range(N):
#     if s[i] == 'R':
#         for k in range(max(0, i-K), min(N, i+K+1)):
#             infected[k] = 1
# # print(infected)

# print("Yes" if sum(infected) <= M else "No")


# S
'''
4 2 2
a 10
b 20
c 30
d 40
'''
# N, M, K = map(int, input().split())

# sub_dict = dict()
# for _ in range(N):
#     si, pi = input().split()
#     pi = int(pi)
#     sub_dict[si] = pi
# # print(sub_dict)

# now_sum = 0
# for _ in range(K):
#     si = input().rstrip()
#     now_sum += sub_dict[si]
#     del sub_dict[si]

# # print(sub_dict)
# # print(now_sum)
# ns = sorted(sub_dict.values())
# print(now_sum+sum(ns[:M-K]), now_sum+(sum(ns[-(M-K):]) if M-K else 0))


# R
# import sys
# input = sys.stdin.readline

# R, C, H = map(int, input().split())
# board = [[list(input().rstrip()) for _ in range(R)] for _ in range(H)]
# # print(board)

# inc_xyz = [[x, y, z] for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2) if not(not x and not y and not z)]
# # print(len(inc_xyz))

# cnt = [[[0]*C for _ in range(R)] for _ in range(H)]
# for z in range(H):
#     for x in range(R):
#         for y in range(C):
#             for px, py, pz in inc_xyz:
#                 nx, ny, nz = x+px, y+py, z+pz
#                 if 0 <= nx < R and 0 <= ny < C and 0 <= nz < H:
#                     if board[nz][nx][ny] == '*':
#                         cnt[z][x][y] += 1
# # print(cnt)

# for z in range(H):
#     for x in range(R):
#         for y in range(C):
#             print('*' if board[z][x][y] =='*' else cnt[z][x][y]%10, end='')
#         print()


# Q
# T = int(input())
# INF = int(1e15)

# for _ in range(T):
#     sc = int(input())
#     tot_exp = sc*(sc+1)//2

#     l, r = 0, INF
#     ans = -1
#     while l <= r:
#         mid = (l+r)//2

#         # 레벨업에 필요한 경험치보다 현재 경험치가 많은 경우
#         # if 2*mid*(mid+1)//2 <= tot_exp:
#         if mid*(mid+1) <= tot_exp:
#             ans = mid
#             l = mid+1
#         else:
#             r = mid-1
#         # print("mid",mid)

#     print(ans+1)


# I
'''
boj.kr/1307
boj.kr/1305
'''
# N = int(input())
# boj, not_boj = [], []

# for _ in range(N):
#     s = input()
#     if s[:7] == 'boj.kr/':
#         boj.append(s)
#     else:
#         not_boj.append(s)
# # print(boj, not_boj)

# not_boj = sorted(not_boj, key=lambda x:(len(x), x))
# boj = [[boj[i], int(boj[i][7:])] for i in range(len(boj))]
# # print(boj)

# boj = sorted(boj, key=lambda x:(x[1]))
# # print(boj)

# if not_boj:
#     print(*not_boj, sep='\n')
# print(*[boj[i][0] for i in range(len(boj))], sep='\n')


# J
# 좌표 계산 실수
# N, K = map(int, input().split())
# board = [[0]*N for _ in range(N)]
# pos = [[0]*N for _ in range(N)]

# inc_xy = [[0, 2], [2, 0], [0, -2], [-2, 0]]
# # print(inc_xy)

# # dbb = [list(map(int, input().split())) for _ in range(K)]
# dbb = []
# for _ in range(K):
#     x, y = map(int, input().split())
#     dbb.append([x-1, y-1])

# for x, y in dbb:
#     board[x][y] = 1
# # print(board)

# for x, y in dbb:
#     for px, py in inc_xy:
#         nx, ny = x+px, y+py
#         if 0 <= nx < N and 0 <= ny < N:
#             if not board[nx][ny]:
#                 pos[nx][ny] = 1

# for x in range(N):
#     print(pos[x])

# print(sum([sum(pos[i]) for i in range(N)]))


# N, K = map(int, input().split())
# # xy = set()
# ans_sets  = [set() for _ in range(N)]
# dbb_sets = [set() for _ in range(N)]

# dbb = ['']*K
# for i in range(K):
#     x, y = map(int, input().split())
#     dbb[i] = [x-1, y-1]
#     dbb_sets[x-1].add(y-1)
# # print(dbb)

# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# for x, y in dbb:
#     for px, py in inc_xy:
#         nx, ny = x+2*px, y+2*py
#         if 0 <= nx < N and 0 <= ny < N:
#             if ny not in dbb_sets[nx]:
#                 ans_sets[nx].add(ny)

# # for i in range(N):
# #     print(i, ans_sets[i])

# print(sum(len(ans_sets[i]) for i in range(N)))


# K
# 조합 !!!!!
# 문제 이해 실수 두 번

# N, M = map(int, input().split())
# X, Y = map(int, input().split())

# certainly_knows = 0
# uncertainly_knows = 0

# def p(n, k):
#     val = 1
#     for a in range(n, n-k, -1):
#         val *= a
#     return val

# for _ in range(M):
#     a, b = map(int, input().split())
#     if a != 0:
#         certainly_knows += 1
#     else:
#         uncertainly_knows += 1

# # rest
# r = N-certainly_knows
# tries = p(r, uncertainly_knows) * p(9-certainly_knows-uncertainly_knows, r-uncertainly_knows)
# # print(tries)

# print((tries*X) + ((tries-1)//3)*Y)


# L
# 범위가.. dict였네 !
# N = int(input())
# ns = list(map(int, input().split()))
# limit = int(2e5)+1
# cnts = dict()
# for n in ns:
#     cnts[n] += 1

# M = int(input())
# for _ in range(M):
#     As = list(map(int, input().split()))[1:]
#     Bs = list(map(int, input().split()))[1:]

#     pos = True
#     tmp_cnts = [0]*limit

#     set_As = set(As)
#     for a in As:
#         tmp_cnts[a] += 1

#     for a in set_As:
#         if cnts[a] < tmp_cnts[a]:
#             pos = False
#             break

#     if pos:
#         for a in set_As:
#             cnts[a] -= tmp_cnts[a]

#         for b in Bs:
#             cnts[b] += 1
#     print("tmp_cnts", tmp_cnts[:10])
#     print("pos", pos)
#     print("cnts", cnts[:10])

# ans = 0
# sum(cnts)
# for i in range(limit):
#     for _ in range(cnts[i]):
#         print(i)

'''
3
1 3 5
3
1 1
0
0
2 1 1
2 3 5
2 4 6
'''
# from collections import defaultdict

# input()
# ns = list(map(int, input().split()))
# cnts = defaultdict(int)
# for n in ns:
#     cnts[n] += 1
# # print(cnts)

# Q = int(input())
# for _ in range(Q):
#     As = list(map(int, input().split()))[1:]
#     Bs = list(map(int, input().split()))[1:]

#     pos = True
#     dict_As = defaultdict(int)

#     for a in As:
#         dict_As[a] += 1

#     for k in dict_As.keys():
#         # print("cns[k]", cnts[k])
#         if cnts[k] < dict_As[k]:
#             pos = False
#             break

#     if pos:
#         for k in dict_As.keys():
#             cnts[k] -= dict_As[k]
#             if not cnts[k]:
#                 del cnts[k]

#         for b in Bs:
#             cnts[b] += 1
#     # print(cnts)

# sums = sum(cnts.values())
# print(sums)
# if sums:
#     for k, v in cnts.items():
#         for _ in range(v):
#             print(k, end=' ')

# MNOP


# 1356 유진수
# def calc(ns):
#     val = 1
#     for n in ns:
#         val *= n
#     return val

# ns = list(map(int, input()))
# pos = False

# for i in range(1, len(ns)):
#     if calc(ns[:i]) == calc(ns[i:]):
#         pos = True
#         break

# print("YES" if pos else "NO")


# 17245 서버실
# import sys
# input = sys.stdin.readline

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# tot_com = sum(sum(board[x]) for x in range(N))
# # print(tot_com)

# bot, top = 0, int(1e7)
# ans = 0
# while bot <= top:
#     mid = (bot+top)//2

#     cool_com = 0
#     for x in range(N):
#         for y in range(N):
#             cool_com += min(board[x][y], mid)

#     if cool_com*2 >= tot_com:
#         ans = mid
#         top = mid-1
#     else:
#         bot = mid+1

# print(ans)


# 25318 solved.ac 2022
'''
3
2020/08/15 15:17:53 24
2020/08/01 22:41:52 24
2020/08/02 09:20:19 26
'''
# def cal_time(info):
#     Y, M, D = map(int, info[0].split('/'))
#     h, m, s = map(int, info[1].split(':'))

#     tot_day = 365*(Y-1) + (D-1)
#     now_M = 1
#     while now_M < M:
#         if now_M in [1, 3, 5, 7, 8, 10, 12]:
#             tot_day += 31
#         elif now_M in [4, 6, 9, 11]:
#             tot_day += 30
#         else:
#             tot_day += 28
#         now_M += 1

#     if (Y >= 2021) or (Y >= 2020 and M >= 3):
#         tot_day += 1

#     tot_time = tot_day*86400 + 3600*h + 60*m + s
#     return [tot_time, int(info[2])]

# def solve():
#     N = int(input())
#     if N == 0:
#         print(0)
#         return

#     infos = [list(input().split()) for _ in range(N)]
#     infos = [cal_time(info) for info in infos]
#     # print(infos)

#     # 31536000 == 365 * 86400
#     ps = [max(0.5**((infos[N-1][0]-infos[i][0])/31536000), 0.9**((N-1)-i)) for i in range(N)]
#     # print(ps)

#     X = sum([ps[i] * infos[i][1] for i in range(N)])/sum(ps)
#     print(int(X*10+5)//10)

# solve()


# 14888 연산자 끼워넣기
# def btr(idx, max_idx, ns, cmds, now_val):
#     global min_ans, max_ans
#     for i in range(4):
#         if cmds[i]:
#             cmds[i] -= 1

#             if i == 0:      next_val = now_val+ns[idx]
#             elif i == 1:    next_val = now_val-ns[idx]
#             elif i == 2:    next_val = now_val*ns[idx]
#             else:           next_val = int(now_val/ns[idx])

#             if idx < max_idx:
#                 btr(idx+1, max_idx, ns, cmds, next_val)
#             else:
#                 max_ans = max(max_ans, next_val)
#                 min_ans = min(min_ans, next_val)

#             cmds[i] += 1

# def solve():
#     N = int(input())
#     ns = list(map(int, input().split()))
#     cmds = list(map(int, input().split()))

#     global max_ans, min_ans
#     max_ans, min_ans = -int(1e9), int(1e9)

#     btr(1, N-1, ns, cmds, ns[0])
#     print(max_ans, min_ans, sep='\n')

# solve()


# 12789 도키도키 간식드리미
# N = int(input())
# ns = list(map(int, input().split()))
# s = []
# target = 1
# idx = 0
# pos = True

# while pos:
#     if s and s[-1] == target:
#         s.pop()
#         target += 1
#     else:
#         if idx >= N:
#             pos = False
#             break

#         if ns[idx] == target:
#             target += 1
#         else:
#             s.append(ns[idx])
#         idx += 1

#     if target > N:
#         break

# print("Nice" if pos else "Sad")


# 4771 아름다운 삼각형
# import sys
# import math

# def dist(x1, y1, x2, y2):
#     return (x2-x1)**2+(y2-y1)**2
#     # math.sqrt() 적용하면
#     # 부동소수점에 의해 계산이 안 맞는 경우가 생길 수 있음

# for line in sys.stdin.readlines()[:-1]:
#     x1, y1, x2, y2, x3, y3 = map(float, line.rstrip().split())
#     # print(x1, y1, x2, y2, x3, y3)

#     dist1, dist2, dist3 = dist(x1, y1, x2, y2), dist(x2, y2, x3, y3), dist(x3, y3, x1, y1)
#     dists = sorted([dist1, dist2, dist3])
#     print(dists)

#     if dists[0] == dists[1] == dists[2]:
#         print("Equilateral", end=' ')
#     elif dists[0] == dists[1] or dists[0] == dists[2] or dists[1] == dists[2]:
#         print("Isosceles", end=' ')
#     else:
#         print("Scalene", end=' ')

#     if dists[2] > dists[1]+dists[0]:
#         print("Obtuse")
#     elif dists[2] == dists[1]+dists[0]:
#         print("Right")
#     else:
#         print("Acute")


# 9063 대지
# min_x, max_x = int(1e4), -int(1e4)
# min_y, max_y = int(1e4), -int(1e4)

# for _ in range(int(input())):
#     x, y = map(int, input().split())
#     min_x = min(min_x, x)
#     max_x = max(max_x, x)
#     min_y = min(min_y, y)
#     max_y = max(max_y, y)

# print((max_x - min_x)*(max_y - min_y))


# 2121 넷이 놀기
# N = int(input())
# A, B = map(int, input().split())
# pts = [list(map(int, input().split())) for _ in range(N)]
# # print(pts)

# pt_dict = dict()
# for x, y in pts:
#     if x not in pt_dict:
#         pt_dict[x] = set({y})
#     else:
#         pt_dict[x].add(y)
# # print(pt_dict)

# ans = 0
# for pt in pts:
#     pos = True
#     for px, py in [[x, y] for x in [0, A] for y in [0, B]]:
#         # print("px, py", px, py)
#         nx, ny = pt[0]+px, pt[1]+py
#         if (nx not in pt_dict) or (ny not in pt_dict[nx]):
#             pos = False
#             break

#     if pos:
#         ans += 1

# print(ans)


# 1004 어린 왕자
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     x1, y1, x2, y2 = map(int, input().split())
#     ans = 0
#     for _ in range(int(input())):
#         cx, cy, r = map(int, input().split())
#         cnt = 0
#         for tx, ty in [[x1, y1], [x2, y2]]:
#             if (tx-cx)**2+(ty-cy)**2 < r**2:
#                 cnt += 1
#         if cnt == 1:
#             ans += 1
#     print(ans)


# 814 - 1
# f = open("./result.txt", 'w')
# f.write('-8140 -8140\n')
# f.write('8139 8140\n')
# for i in range(812):
#     f.write(f'8140 8140\n')
# f.close()

# print('-8140 -8140')
# print('8139 8140')
# for i in range(812):
#     print('8140 8140')

# 사각형
# 삼각형 모양이라면?
# 한 라인이어도 약간씩 지그재그

# def solve():
#     gap = (8140*2)//28
#     cnt = 0

#     for x in range(29):
#         nx = -8140 + x*gap
#         for y in range(29):
#             print(nx, -8140+y*gap)
#             cnt += 1
#             if cnt == 812:
#                 print(f'8140 {8140-gap+1}')
#                 print("8140 8140")
#                 return

# solve()


# 9723 Right Triangle
# import sys
# input = sys.stdin.readline

# for i in range(1, int(input())+1):
#     print(f'Case #{i}: ', end='')
#     a, b, c = sorted(list(map(int, input().split())))
#     if (a**2 + b**2) == (c**2):
#         print("YES")
#     else:
#         print("NO")


# 1198 삼각형으로 자르기
# N = int(input())
# ans = 0

# def cal_s(x1, y1, x2, y2, x3, y3):
#     return abs((x1*y2+x2*y3+x3*y1) - (x1*y3+x2*y1+x3*y2))/2

# pts = [list(map(int, input().split())) for _ in range(N)]
# for a in range(N-2):
#     for b in range(N-1):
#         for c in range(N):
#             x1, y1 = pts[a]
#             x2, y2 = pts[b]
#             x3, y3 = pts[c]
#             ans = max(ans, cal_s(x1, y1, x2, y2, x3, y3))

# print(ans)


# 1709 타일 위의 원
# import math

# N = int(input())
# pre = y = r = N // 2
# r_square = r**2
# ans = 0

# for x in range(1, r+1):
#     x_square = x**2
#     target = math.isqrt(r_square - x_square)
#     while y > target:
#         y -= 1

#     ans += pre-y
#     pre = y+1

#     if r_square == x_square + (y**2):
#         pre -= 1
#         break

# print(ans*4)


# 1297 TV 크기
# import math

# D, H, W = map(int, input().split())
# k = D/math.sqrt(H**2+W**2)
# # print(k)

# print(int(H*k), int(W*k))


# 1485 정사각형
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# for _ in range(int(input())):
#     d = defaultdict(int)
#     xys = [list(map(int, input().split())) for _ in range(4)]
#     for i in range(3):
#         for j in range(i+1, 4):
#             x1, y1 = xys[i]
#             x2, y2 = xys[j]
#             d[(x2-x1)**2+(y2-y1)**2] += 1

#     print(1 if len(d) == 2 else 0)


# 2527 직사각형
# def check2(x1, y1, p1, q1, x2, y2, p2, q2):
#     if (y1 == q2) or (y2 == q1):
#         if (x1 == p2) or (p1 == x2): return True
#         return False
#     return False

# def check3(x1, y1, p1, q1, x2, y2, p2, q2):
#     if (y1 == q2) or (y2 == q1):
#         if ((x1 <= x2 < p1) or (x1 < p2 <= p1) or (x2 <= x1 < p2)):
#             return True
#         return False
#     elif (x1 == p2) or (x2 == p1):
#         if ((y1 <= y2 < q1) or (y1 < q2 <= q1) or (y2 <= y1 < q2)):
#             return True
#         return False
#     return False

# for _ in range(4):
#     x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

#     if (p1 < x2) or (p2 < x1) or (q1 < y2) or (q2 < y1):
#         print('d')
#         continue

#     if check2(x1, y1, p1, q1, x2, y2, p2, q2):
#         print('c')
#         continue

#     if check3(x1, y1, p1, q1, x2, y2, p2, q2):
#         print('b')
#         continue

#     print('a')


# 1940 주몽
# N = int(input())
# M = int(input())
# ns = sorted(list(map(int, input().split())))

# l, r = 0, N-1
# ans = 0

# while l < r :
#     now_sum = ns[l]+ns[r]
#     if now_sum == M:
#         ans += 1
#         l += 1
#         r -= 1
#     elif now_sum < M:
#         l += 1
#     else:
#         r -= 1

# print(ans)


# 3684 어려운 문제
# T = int(input())
# ns = [-1]*(2*T)

# for i in range(T):
#     ns[2*i] = int(input())
# # print(ns)

# for a in range(10001):
#     for b in range(10001):
#         for i in range(1, 2*T):
#             if i % 2:
#                 ns[i] = (a*ns[i-1]+b) % 10001
#                 if i == 2*T-1:
#                     print(*[ns[k] for k in range(1, 2*T, 2)], sep='\n')
#                     exit()
#             else:
#                 if ns[i] != (a*ns[i-1]+b) % 10001:
#                     break


# 15319 동혁이의 생일선물
# import sys
# input = sys.stdin.readline

# # reverse
# def r_bin(K):
#     K = int(K)
#     n = ''
#     while K > 0:
#         n += str(K%2)
#         K //= 2
#     return n

# ans = 0
# for _ in range(int(input())):
#     x, K = map(int, input().split())
#     d = dict()
#     k = list(map(int, r_bin(K)))
#     # print(k)
#     mod = int(1e9)+7

#     powers = [1]*30
#     for i in range(1, 30):
#         powers[i] = (powers[i-1]*x) % mod

#     val = 0
#     for i in range(len(k)):
#         val = (val+k[i]*powers[i]) % mod
#     ans += val

# print(ans % mod)


# 1487 물건 팔기
# N = int(input())
# ns = [list(map(int, input().split())) for _ in range(N)]
# ns.sort(key=lambda x:(x[0]))

# max_sum = 0
# ans = 0
# for i in range(N):
#     tmp_sum = 0
#     for j in range(i, N):
#         tmp_sum += max(0, ns[i][0] - ns[j][1])

#     if max_sum < tmp_sum:
#         max_sum = tmp_sum
#         ans = ns[i][0]

# print(ans)


# 17433 신비로운 수
# import sys
# input = sys.stdin.readline

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a%b
#     return a

# def all_same(ns):
#     c = True
#     for n in ns[1:]:
#         if n != ns[0]:
#             c = False
#             break
#     return c

# def solve():
#     for _ in range(int(input())):
#         N = int(input())
#         ns = list(map(int, input().split()))
#         if all_same(ns):
#             print('INFINITY')
#             continue

#         new_ns = [ns[i]-ns[0] for i in range(1, N)]
#         # print(new_ns)

#         ans = new_ns[0]
#         for n in new_ns[1:]:
#             ans = gcd(ans, n)

#         print(abs(ans))

# solve()


# 1569 정사각형으로 가리기
'''
3
1 0
0 1
1 2
[정답] 2
'''
'''
4
10 10
1 10
10 6
2 0
[정답] 10
'''
# def solve():
#     N = int(input())
#     pts = [list(map(int, input().split())) for _ in range(N)]

#     gaps = set()
#     for i in range(N-1):
#         for j in range(i+1, N):
#             gaps.add(abs(pts[i][0]-pts[j][0]))
#             gaps.add(abs(pts[i][1]-pts[j][1]))
#     # gaps = sorted(gaps)
#     # print(gaps)

#     for i in range(N):
#         for j in range(N):
#             for d in gaps:
#                 x, y = pts[i][0], pts[j][1]
#                 for px, py in [[d, d], [d, -d], [-d, -d], [-d, d]]:
#                     nx, ny = x+px, y+py
#                     # print(x, y, nx, ny, d)
#                     xs, ys = sorted([x, nx]), sorted([y, ny])

#                     can_make_square = True
#                     for ptx, pty in pts:
#                         if (ptx not in xs) and (pty not in ys):
#                             can_make_square = False
#                             break
#                         if (ptx in xs and not (ys[0] <= pty <= ys[1])) or (pty in ys and not (xs[0] <= ptx <= xs[1])):
#                             can_make_square = False
#                             break
#                     if can_make_square:
#                         print(d)
#                         return
#     print(-1)

# solve()


# 29753 최소 성적
'''
2 2.01
'''

# def solve():
#     d = dict({
#         'A+':450,
#         'A0':400,
#         'B+':350,
#         'B0':300,
#         'C+':250,
#         'C0':200,
#         'D+':150,
#         'D0':100,
#         'F': 0,
#     })

#     N, X = input().split()
#     N = int(N)
#     # X = int(100*float(X))
#     X = int(''.join(X.split('.')))
#     # print(N, X)

#     tot_grade, tot_ci = 0, 0
#     for _ in range(N-1):
#         ci, gi = input().split()
#         ci = int(ci)

#         tot_grade += ci*d[gi]
#         tot_ci += ci

#     ci = int(input())
#     tot_ci += ci

#     for k, v in sorted(d.items(), key=lambda x:(x[1])):
#         # print(k, v)
#         if (tot_grade + ci*v)//tot_ci > X:
#             print(k)
#             return

#     print("impossible")

# solve()


# 14411 합집합
# import sys
# input = sys.stdin.readline

# N = int(input())
# pts = [list(map(int, input().split())) for _ in range(N)]
# pts.sort(key=lambda x:(-x[0]))
# # print(pts)

# ans = 0
# pre_x, pre_y = int(1e7), 0
# for x, y in pts:
#     ans += (pre_x-x)*pre_y
#     pre_x = x
#     if pre_y < y:
#         pre_y = y
#     # print(ans, pre_y)

# ans += pts[-1][0]*pre_y
# print(ans)


# 25418 정수 a를 k로 만들기
# A, K = map(int, input().split())
# dp = [int(1e6)]*(K+1)
# dp[A] = 0

# for i in range(A+1, K+1):
#     if i % 2 == 0:
#         dp[i] = min(dp[i-1], dp[i//2])+1
#     else:
#         dp[i] = dp[i-1]+1
# print(dp[K])


# 2098 외판원 순회

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0]*(1 << N) for _ in range(N)]
# all_visited = (1 << N)-1
# inf = int(2e7)

# def tsp(cur, visited):
#     if visited == (all_visited):
#         return board[cur][0] if board[cur][0] else inf

#     if dp[cur][visited]:
#         return dp[cur][visited]

#     min_dist = inf
#     for next_v in range(N):
#         if not(visited & (1 << next_v)) and board[cur][next_v]:
#             min_dist = min(min_dist, board[cur][next_v] + tsp(next_v, visited+(1 << next_v)))

#     dp[cur][visited] = min_dist
#     return min_dist

# print(tsp(0, 1 << 0))


# 28278 스택 2
# import sys
# input = sys.stdin.readline

# s = []
# len_s = 0

# N = int(input())
# for _ in range(N):
#     cmds = list(map(int, input().split()))
#     if cmds[0] == 1:
#         s.append(cmds[1])
#         len_s += 1
#     elif cmds[0] == 2:
#         if s:
#             print(s.pop())
#             len_s -= 1
#         else: print(-1)
#     elif cmds[0] == 3:
#         print(len_s)
#     elif cmds[0] == 4:
#         if s: print(0)
#         else: print(1)
#     else:
#         if s: print(s[-1])
#         else: print(-1)


# 2841 외계인의 기타 연주

# import sys
# input = sys.stdin.readline

# N, _ = map(int, input().split())
# biggest_frets = [[0] for _ in range(N+1)]
# ans = 0
# for _ in range(N):
#     line, pret = map(int, input().split())

#     while biggest_frets[line][-1] > pret:
#         biggest_frets[line].pop()
#         ans += 1

#     if biggest_frets[line][-1] != pret:
#         biggest_frets[line].append(pret)
#         ans += 1

# print(ans)


# 1562 계단 수
# def solve():
#     block = 1 << 10
#     blocks = block*10

#     N = int(input())
#     dp = [[0]*blocks for _ in range(N+1)]
#     mod = int(1e9)

#     for i in range(1, 10):
#         dp[1][(block*i) + (1 << i)] = 1

#     for i in range(1, N):
#         for j in range(blocks):
#             n = j // block

#             for k in range(10):
#                 t = (1 << k)
#                 next_j = j | t

#                 if n == (k-1):
#                     next_j += block
#                     dp[i+1][next_j] = (dp[i+1][next_j] + dp[i][j]) % mod
#                 if n == (k+1):
#                     next_j -= block
#                     dp[i+1][next_j] = (dp[i+1][next_j] + dp[i][j]) % mod

#     print(sum([dp[N][block*i + (block-1)] for i in range(10)]) % mod)

# solve()

# ans = 0
# for i in range(1, 41):
#     ans += solve(i)
#     print(ans)

# 직전 정보를 저장하지 못 한다.
# def solve():
#     block = 1 << 10

#     N = int(input())
#     dp = [[0]*block for _ in range(N+1)]
#     # print(len(dp[0]))
#     mod = int(1e9)

#     for i in range(1, 10):
#         dp[1][1 << i] = 1
#     # dp[1][1 << 0] = 0
#     # print(dp[1][:50])

#     for i in range(1, N):
#         for j in range(block):
#             for k in range(10):
#                 t = 1 << k
#                 # print(t, bin(t))

#                 if (k and (j & (1 << k-1))) or (j & (1 << k+1)):
#                     if not (j & t):
#                         dp[i+1][j+t] = (dp[i+1][j+t] + dp[i][j]) % mod
#                     else:
#                         dp[i+1][j-t] = (dp[i+1][j-t] + dp[i][j]) % mod

#     print(dp[N][block-1])

# solve()


# 14607 피자(Large)
# d = dict()

# def rec(N):
#     half_N = N //2
#     if N == 1:
#         d[1] = 0
#     elif N % 2 == 0:
#         if N not in d:
#             d[N] = half_N**2 + 2*rec(half_N)
#     else:
#         if N not in d:
#             d[N] = half_N*(half_N+1) + rec(half_N) + rec(half_N+1)

#     return d[N]

# print(rec(int(input())))


# 26267 은?행 털!자 1
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# d = defaultdict(int)
# for _ in range(int(input())):
#     Xi, Ti, Ci = map(int, input().split())
#     d[Xi-Ti] += Ci

# print(max(d.values()))


# 2785 체인
# N = int(input())
# ns = sorted(list(map(int, input().split())))

# l, r = 0, N-1
# cnt = 0

# while l < r:
#     cnt += 1
#     if ns[l] > 0:
#         ns[l] -= 1
#         if ns[l] == 0:
#             l += 1
#     r -= 1

# print(cnt)


# 20126 교수님의 기말고사
# import sys
# input = sys.stdin.readline

# def solve():
#     N, M, S = map(int, input().split())
#     xys = [list(map(int, input().split())) for _ in range(N)]
#     xys.sort(key=lambda x:(x[0], x[1]))

#     now = 0
#     for i in range(N):
#         if M <= (xys[i][0]-now):
#             print(now)
#             return
#         now = sum(xys[i])

#     if M <= (S-now):
#         print(now)
#         return

#     print(-1)

# solve()


# 17211 좋은 날 싫은 날
# def r(N):
#     return int((N*10+5)//10)

# N, K = map(int, input().split())
# ns = list(map(float, input().split()))
# # print(ns)

# pre_p = [(1-K)*1000, K*1000]
# now_p = [0, 0]
# for _ in range(N):
#     pp1, pp2 = pre_p
#     np1 = (pp1*ns[0] + pp2*ns[2])
#     np2 = (pp1*ns[1] + pp2*ns[3])
#     now_p = [np1, np2]
#     pre_p = now_p

# print(r(now_p[0]), r(now_p[1]), sep='\n')


# 21318 피아노 체조
# import sys
# input = sys.stdin.readline

# N = int(input())
# ns = list(map(int, input().split()))
# new_ns = [0] + [1 if (ns[i]>ns[i+1]) else 0 for i in range(N-1)] + [0]
# # print(new_ns)

# sums = [0]*(N+1)
# for i in range(1, N+1):
#     sums[i] = sums[i-1]+new_ns[i]
# # print(sums)

# for _ in range(int(input())):
#     x, y = map(int, input().split())
#     print(sums[y-1]-sums[x-1])


# 17265 나의 인생에는 수학과 함께
# N = int(input())
# board = [list(input().split()) for _ in range(N)]
# # print(board)

# for x in range(N):
#     for y in range(N):
#         if (x+y) % 2 == 0:
#             board[x][y] = int(board[x][y])
# # print(board)

# global max_val, min_val
# max_val, min_val = -3125, 3125
# inc_xy = [[1, 0], [0, 1]]

# def dfs(x, y, val, op):
#     global max_val, min_val
#     for px, py in inc_xy:
#         nx, ny = x+px, y+py
#         if 0 <= nx < N and 0 <= ny < N:
#             next_val = val
#             if (nx+ny) % 2:
#                 op = board[nx][ny]
#             else:
#                 if op == '+':   next_val += board[nx][ny] 
#                 elif op == '-': next_val -= board[nx][ny]
#                 elif op == '*': next_val *= board[nx][ny] 

#                 if nx == N-1 and ny == N-1:
#                     max_val = max(max_val, next_val)
#                     min_val = min(min_val, next_val)
#                     return
#             dfs(nx, ny, next_val, op)

# dfs(0, 0, board[0][0], '')

# print(max_val, min_val)


# 2865 나는 위대한 슈퍼스타K
# N, M, K = map(int, input().split())
# vals = [0]*(N+1)

# for _ in range(M):
#     ns = list(input().split())
#     for i in range(0, 2*N, 2):
#         n = int(ns[i])
#         vals[n] = max(vals[n], float(ns[i+1]))

# def r(n):
#     return ((n*100+5)//10)/10

# print(r(sum(sorted(vals, reverse=True)[:K])))


# 25416 빠른 숫자 탐색
# from collections import deque

# def solve():
#     board = [list(map(int, input().split())) for _ in range(5)]
#     x, y = map(int, input().split())
#     if board[x][y] == 1:
#         print(0)
#         return

#     visited = [[False]*5 for _ in range(5)]
#     visited[x][y] = True

#     inc_xy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

#     q = deque([[x, y, 0]])
#     while q:
#         x, y, cnt = q.popleft()
#         for px, py in inc_xy:
#             nx, ny = x+px, y+py
#             if 0 <= nx < 5 and 0 <= ny < 5 and board[nx][ny] != -1 and not visited[nx][ny]:
#                 if board[nx][ny] == 1:
#                     print(cnt+1)
#                     return
#                 visited[nx][ny] = True
#                 q.append([nx, ny, cnt+1])
#     print(-1)

# solve()


# 2938 3으로 나누어 떨어지지 않는 배열
# import sys
# input = sys.stdin.readline

# N = int(input())
# ns = list(map(int, input().split()))

# rs = [[] for _ in range(3)]
# for n in ns:
#     if n % 3 == 0:
#         rs[0].append(n)
#     elif n % 3 == 1:
#         rs[1].append(n)
#     else:
#         rs[2].append(n)
# # print(rs)

# len_rs = [len(rs[i]) for i in range(3)]
# if len_rs[0] == 0:
#     if len_rs[1] == 0:
#         print(*rs[2])
#     elif len_rs[2] == 0:
#         print(*rs[1])
#     else:
#         print(-1)
# elif (sum(len_rs[1:])+1) >= len_rs[0]:
#     # k = min(len_rs[1], len_rs[0]-1)

#     for _ in range(len_rs[1]-len_rs[0]+1):
#         print(rs[1].pop(), end=' ')

#     for _ in range(len_rs[0]-1):
#         print(rs[0].pop(), end=' ')
#         if rs[1]:
#             print(rs[1].pop(), end=' ')
#         else:
#             print(rs[2].pop(), end=' ')

#     print(rs[0].pop(), end=' ')
#     while rs[2]:
#         print(rs[2].pop(), end=' ')
# else:
#     print(-1)


# 9838 XMAS
# N = int(input())

# d = dict()
# for i in range(1, N+1):
#     d[i] = int(input())
# # print(d)

# d = sorted(d.items(), key=lambda x:(x[1]))
# # print(d)

# print(*[n[0] for n in d], sep='\n')


# N = int(input())
# ns = [0]*(N+1)
# for i in range(N):
#     ns[int(input())] = i+1
# print(*ns[1:], sep='\n')


# 11346 Cornell Party
# for _ in range(int(input())):
#     s_set = set()
#     [input() for _ in range(2)]
#     for _ in range(2):
#         for s in list(input().split()):
#             s_set.add(s)
#     print(len(s_set))


# 3005 크로스워드 퍼즐 쳐다보기
# R, C = map(int, input().split())

# board = [input() for _ in range(R)]
# words = []
# for x in range(R):
#     ss = board[x].split('#')
#     [words.append(s) for s in ss if len(s) >= 2]

# for y in range(C):
#     ss = ''.join([board[x][y] for x in range(R)]).split('#')
#     [words.append(s) for s in ss if len(s) >= 2]

# # print(words)
# print(sorted(words)[0])


# 7661 Boundless Boxes
# import sys
# input = sys.stdin.readline
# from collections import deque

# inc_xy = [[x, y] for x in [-1, 0, 1] for y in [-1, 0, 1] if x|y]
# # print(inc_xy)
# m, n, s = map(int, input().split())
# while not (not m and not n and not s):
#     board = [[0]*n for _ in range(m)]
#     visited = [[0]*n for _ in range(m)]

#     q = deque()
#     for _ in range(s):
#         x, y = map(int, input().split())
#         x -= 1; y-= 1
#         q.append([x, y])
#         visited[x][y] = True

#     cnt = 0
#     while q:
#         cnt += 1
#         for _ in range(len(q)):
#             x, y = q.popleft()
#             for px, py in inc_xy:
#                 nx, ny = x+px, y+py
#                 if 0 <= nx < m and 0 <= ny < n:
#                     if not visited[nx][ny]:
#                         visited[nx][ny] = True
#                         q.append([nx, ny])
#     print(cnt)
#     input()
#     m, n, s = map(int, input().split())


# 9196 정수 직사각형
# diags = [[w**2+h**2, h, w] for w in range(1, 151) for h in range(1, 151) if w > h]
# diags.sort(key=lambda x:(x[0], x[1]))
# len_diags = len(diags)
# # print(diags)

# x, y = map(int, input().split())
# while x|y:
#     for i in range(len_diags):
#         d, h, w = diags[i]
#         if h == x and y == w:
#             print(diags[i+1][1], diags[i+1][2])
#     x, y = map(int, input().split())


# 5747 Odd or Even
# import sys
# input = sys.stdin.readline

# N = int(input())
# while N:
#     ox, ex = 0, 0
#     oy, ey = 0, 0

#     xs = list(map(int, input().split()))
#     ys = list(map(int, input().split()))

#     for x in xs:
#         if x % 2:   ox += 1
#         else:       ex += 1
#     for y in ys:
#         if y % 2:   oy += 1
#         else:       ey += 1

#     print(N-min(ox,ey)-min(ex,oy))
#     N = int(input())


# 25333 개구리
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

# for _ in range(int(input())):
#     a, b, x = map(int, input().split())
#     print(x//gcd(a,b))


# 14467 소가 길을 건너간 이유
# import sys
# input = sys.stdin.readline

# N, ans = int(input()), 0
# vals = [-1]*(N+1)
# for _ in range(N):
#     n, val = map(int, input().split())
#     if vals[n] == -1:
#         vals[n] = val
#         continue

#     if vals[n] != val:
#         vals[n] = val
#         ans += 1

# print(ans)


# 1, 2, 3 더하기 4
# import sys
# input = sys.stdin.readline

# N = int(input())
# dp = [[0, 0, 0] for _ in range(10001)]
# dp[1] = [1, 0, 0]
# dp[2] = [1, 1, 0]
# dp[3] = [2, 0, 1]

# for i in range(4, 10001):
#     dp[i][0] = sum(dp[i-1])     # 1이 하나 이상 들어간 경우
#     dp[i][1] = sum(dp[i-2][1:]) # 2나 3만 있는 경우
#     dp[i][2] = dp[i-3][2]       # 3만 있는 경우

# for _ in range(N):
#     print(sum(dp[int(input())]))


# 11140 LOL
# for _ in range(int(input())):
#     ss = input()
#     if 'lol' in ss:
#         print(0)
#     else:
#         check = False
#         len_ss = len(ss)
#         for i in range(len_ss):
#             if ss[i] == 'l' and (i+2) <= len_ss-1 and ss[i+2] == 'l':
#                 print(1)
#                 check = True
#                 break
#         if check:
#             continue

#         if ('lo' in ss) or ('ol' in ss) or ('ll' in ss):
#             print(1)
#         elif ('l' in ss) or ('o' in ss):
#             print(2)
#         else:
#             print(3)


# 1354 무한 수열 2
# dp = dict()
# dp[0] = 1

# def rec(N, P, Q, X, Y):
#     if N <= 0: return 1

#     # lto : less_than_one
#     lto = [False, False]
#     ns = [(N//P)-X, (N//Q)-Y]

#     for i in range(2):
#         if ns[i] <= 0: lto[i] = True
#         elif ns[i] not in dp:
#             dp[ns[i]] = rec(ns[i], P, Q, X, Y)

#     return (1 if lto[0] else dp[(N//P)-X]) + (1 if lto[1] else dp[(N//Q)-Y])

# def solve():
#     N, P, Q, X, Y = map(int, input().split())
#     print(rec(N, P, Q, X, Y))

# solve()


# 3054 피터팬 프레임
# ss = list(input())
# len_row = len(ss)*4+1
# board = [['.']*len_row for _ in range(5)]

# def rhombus(ky, s:str):
#     for x in [0, 4]:
#         board[x][ky+2] = s

#     for x in [1, 3]:
#         for y in [1, 3]:
#             board[x][ky+y] = s

#     for y in [0, 4]:
#         board[2][ky+y] = s

# for ky in range(0, len_row-1, 4):
#     rhombus(ky, '#')

# for ky in range(8, len_row-1, 12):
#     rhombus(ky, '*')

# for ky in range(2, len_row-1, 4):
#     board[2][ky] = ss[ky//4]

# for x in range(5):
#     print(*board[x], sep='')


# 16969 차량 번호판 2
# ss = list(input())
# mod = int(1e9)+9
# pre = ''
# ans = 1

# for s in ss:
#     tmp = 0
#     if s == 'c':    tmp = 26
#     elif 'd':       tmp = 10

#     if pre == s:
#         tmp -= 1

#     ans = (ans * tmp) % mod
#     pre = s

# print(ans)


# 27446 그래서 대회 이름 뭐로 하죠
'''
3
ACA
'''

# N, M = map(int, input().split())
# ss = list(input())[::-1]
# # print(ss)

# consonant = [chr(i) for i in range(65, 91) if chr(i) not in 'AEIOU']
# # print(consonant)

# ans = ''
# c_check, cnt_a = False, 0
# for idx in range(N):
#     s = ss[idx]
#     if not c_check:
#         if (s in consonant):
#             c_check = True
#             ans += s
#         continue

#     if cnt_a < 2:
#         if s == 'A':
#             cnt_a += 1
#             ans += 'A'
#         continue

#     if len(ans)+(N-idx) < M:
#         ans = ''
#         break
#     else:
#         ans += ''.join(ss[idx:idx+M-len(ans)])
#         break

# print('YES', ans[::-1], sep='\n') if len(ans) == M else print('NO')


# 14728 벼락치기
# N, T = map(int, input().split())
# dp = [[0]*(T+1) for _ in range(N+1)]

# for x in range(1, N+1):
#     K, S = map(int, input().split())
#     for y in range(1, T+1):
#         dp[x][y] = dp[x-1][y]
#         dp[x][y] = max(dp[x][y], dp[x][y-1])
#         if y >= K:
#             dp[x][y] = max(dp[x][y], dp[x-1][y-K]+S)

# print(dp[N][T])


# 30160 제곱 가중치
# N = int(input())
# ns = [0] + list(map(int, input().split()))

# sums = [0]*(N+1)
# for i in range(1, N+1):
#     sums[i] = sums[i-1]+ns[i]
# # print(sums)

# ans, acc_tmp = 0, 0
# for i in range(1, N+1):
#     acc_tmp += 2*sums[i-1]+ns[i]
#     ans += acc_tmp
#     print(ans, end=' ')


# 15922 아우으 우아으이야!!
# import sys
# input = sys.stdin.readline

# N = int(input())
# lines = [list(map(int, input().split())) for _ in range(N)]
# lines.sort(key=lambda x:(x[0]))
# # print(lines)

# ans = 0
# # pre, now
# pl, pr = lines[0]
# for nl, nr in lines[1:]:
#     if pr < nl:
#         ans += pr-pl
#         pl = nl

#     if pr < nr:
#         pr = nr

# ans += pr-pl
# print(ans)


# 12931 두배 더하기
# def cnt_one(n):
#     cnts = 0
#     for i in range(10):
#         cnts += 1 if n & (1<<i) else 0
#     return cnts

# def cal_max_exp(ns):
#     for i in range(9, -1, -1):
#         for n in ns:
#             if n & (1 << i):
#                 return i
#     return 0

# def solve():
#     N = int(input())
#     ns = list(map(int, input().split()))
#     print(sum([cnt_one(n) for n in ns]) + cal_max_exp(ns))

# solve()


# 1484 다이어트
# G = int(input())
# l, r = 1, 1

# ans = []
# while l <= r:
#     val = (r**2) - (l**2)
#     if val < G:
#         r += 1
#         if r == 100000:
#             break
#     elif val > G:
#         l += 1
#     else:
#         ans.append(r)
#         l += 1
#         r += 1
#         if r == 100000:
#             break

# print(*ans, sep='\n') if ans else print(-1)


# 3107 IPv6
'''
1:2:3:4:5:6:7::
'''

# ss = list(input())
# len_ss = len(ss)
# ans = []
# token = ''

# def four_digits(t):
#     while len(t) < 4:
#         t = '0' + t
#     return t

# i = 0
# while i < len(ss):
#     s = ss[i]
#     if s != ':':
#         token += s
#     else:
#         ans.append(four_digits(token))
#         token = ''

#         if i < (len_ss-1) and ss[i+1] == ':':
#             ans.append('_')
#             i += 2
#             continue
#     i += 1

# if token != '':
#     ans.append(four_digits(token))
# # print(ans)

# new_ans = []
# for a in ans:
#     if a != '_':
#         new_ans.append(a)
#     else:
#         for _ in range(8-len(ans)+1):
#             new_ans.append('0000')
# # print(new_ans)

# print(':'.join(new_ans))


# 2660 회장뽑기
# import sys
# input = sys.stdin.readline

# INF = int(1e2)
# N = int(input())
# g = [[INF]*(N+1) for _ in range(N+1)]
# a, b = map(int, input().split())

# for x in range(1, N+1):
#     g[x][x] = 0

# while a != -1 and b != -1:
#     g[a][b] = 1
#     g[b][a] = 1
#     a, b = map(int, input().split())
# # print(g)

# for k in range(1, N+1):
#     for a in range(1, N+1):
#         for b in range(1, N+1):
#             g[a][b] = min(g[a][b], g[a][k]+g[k][b])

# min_max_val, ans = 100, []
# for x in range(1, N+1):
#     tmp_max_val = max(g[x][1:])
#     if min_max_val == tmp_max_val:
#         ans.append(x)
#     elif min_max_val > tmp_max_val:
#         min_max_val = tmp_max_val
#         ans = [x]

# print(min_max_val, len(ans))
# print(*ans)


# 20002 사과나무
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# sums = [[0]*N for _ in range(N)]

# # prefix sum
# for x in range(N):
#     for y in range(N):
#         if x == 0:
#             sums[x][y] = board[x][y]
#         else:
#             sums[x][y] = sums[x-1][y]+board[x][y]

# for y in range(1, N):
#     for x in range(N):
#         sums[x][y] = sums[x][y-1]+sums[x][y]

# # nb : new_board
# nb = [[0]*(N+1) for _ in range(N+1)]
# for x in range(N):
#     for y in range(N):
#         nb[x+1][y+1] = sums[x][y]

# ans = -int(9e7)
# for k in range(1, N+1):
#     for x in range(N+1-k):
#         for y in range(N+1-k):
#             ans = max(ans, nb[x+k][y+k]-nb[x+k][y]-nb[x][y+k]+nb[x][y])

# print(ans)


# 10835 카드게임
# N = int(input())
# ls = list(map(int, input().split()))[::-1]
# rs = list(map(int, input().split()))[::-1]
# # print(rs)

# maxs = [0]*N
# maxs[0] = ls[0]
# for i in range(1, N):
#     maxs[i] = max(maxs[i-1], ls[i])

# print(ls)
# print(maxs)
# print(rs)

# ans = 0
# while rs:
#     if ls[-1] < rs[-1]:

#     if maxs[-1] <= rs[-1]:
#         maxs.pop()
#         rs.pop()
#     else:
#         ans += rs.pop()

# print(ans)


# 23747 와드
'''
3 3
abc
def
ghi
3 3
WLLUU
'''
# import sys
# input = sys.stdin.readline
# from collections import deque

# R, C = map(int, input().split())
# board = [list(input().rstrip()) for _ in range(R)]

# x, y = map(int, input().split())
# x -= 1; y -= 1
# cmds = list(input().rstrip())
# ans = [['#']*C for _ in range(R)]

# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# UDLR = dict({'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]})

# for c in cmds:
#     if c == 'W':
#         ans[x][y] = '.' # 여기 빼먹음
#         now = board[x][y]
#         q = deque([[x, y]])
#         while q:
#             tx, ty = q.popleft()
#             for px, py in inc_xy:
#                 nx, ny = tx+px, ty+py
#                 if (0 <= nx < R) and (0 <= ny < C) and (board[nx][ny] == now) and (ans[nx][ny] != '.'):
#                     ans[nx][ny] = '.'
#                     q.append([nx, ny])
#         continue

#     px, py = UDLR[c]
#     nx, ny = x+px, y+py
#     if 0 <= nx < R and 0 <= ny < C:
#         x, y = nx, ny

# ans[x][y] = '.'
# for px, py in inc_xy:
#     nx, ny = x+px, y+py
#     if 0 <= nx < R and 0 <= ny < C:
#         ans[nx][ny] = '.'

# for x in range(R):
#     print(*ans[x], sep='')


# 11578 팀원 모집
# N, M = map(int, input().split())

# ns = [0]*M
# for i in range(M):
#     ms = list(map(int, input().split()))[1:]
#     for m in ms:
#         ns[i] += (1 << (m-1))
# # print(ns)

# def zero_fill(s):
#     return '0'*(M-len(s))+s

# target = (2**N-1)
# ans = 11
# for k in range(1, 2**M):
#     val = 0
#     m = list(map(int, zero_fill(bin(k)[2:])))

#     cnt = 0
#     for i in range(M):
#         if m[i]:
#             val |= ns[i]
#             cnt += 1

#     if val == target:
#         ans = min(ans, cnt)

# print(ans if ans != 11 else -1)


# 21278 호석이 두 마리 치킨
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# INF = int(1e5)
# g = [[INF]*(N+1) for _ in range(N+1)]

# for x in range(N+1):
#     g[x][x] = 0

# for _ in range(M):
#     a, b = map(int, input().split())
#     g[a][b] = 1
#     g[b][a] = 1

# for k in range(1, N+1):
#     for x in range(1, N+1):
#         for y in range(1, N+1):
#             g[x][y] = min(g[x][y], g[x][k]+g[k][y])

# for x in range(N+1):
#     g[x][x] = INF

# # for x in range(N+1):
# #     print(g[x])

# min_val, ans_xys = INF, []
# for a in range(1, N):
#     for b in range(a+1, N+1):
#         vals = [1]*(N+1) #
#         vals[a] = 0; vals[b] = 0

#         tsum = 0
#         for x in range(1, N+1):
#             if vals[x]:
#                 tsum += 2*min(g[x][a], g[x][b])
#         # print(tsum)

#         if min_val > tsum:
#             min_val = tsum
#             ans_xys = [[a, b]]
#         elif min_val == tsum:
#             ans_xys.append([a, b])

# ans_xys.sort(key=lambda x:(x[0], x[1]))
# print(*ans_xys[0], min_val)


# 5904 Moo 게임
# N = int(input())
# N -= 1
# level = 0
# len_s = 3

# while N >= len_s:
#     level += 1
#     len_s = 2*len_s + (3+level)

# def moo(len_s, M, level):
#     if level == 0:
#         return 'm' if M == 0 else 'o'

#     # ll : left limit
#     mid = 3+level
#     ll = (len_s-mid)//2
#     rl = ll + mid

#     if M < ll:
#         return moo(ll, M, level-1)
#     elif ll <= M < rl:
#         return moo(M, M-ll, 0)
#     else:
#         return moo(len_s-rl, M-rl, level-1)

# print(moo(len_s, N, level))


# 12934 턴 게임
# x, y = map(int, input().split())
# k = x+y

# now = 0
# tmp = 1
# # 이분탐색 가능
# while now < k:
#     now += tmp
#     tmp += 1
# tmp -= 1

# ans = 0
# if now == k:
#     while x > 0:
#         if x > tmp:
#             while x > tmp :
#                 x -= tmp
#                 ans += 1
#                 tmp -= 1
#         else:
#             ans += 1
#             break
#     print(ans)
# else:
#     print(-1)


# 25343 최장 최장 증가 부분 수열
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# dp = [[[0]*10001 for _ in range(N)] for _ in range(N)]
# dp[0][0][board[0][0]] = 1

# for x in range(N):
#     for y in range(N):
#         if x != 0:
#             for k in range(10001):
#                 dp[x][y][k] = max(dp[x][y][k], dp[x-1][y][k])
#         if y != 0:
#             for k in range(1, 10001):
#                 dp[x][y][k] = max(dp[x][y][k], dp[x][y-1][k])

#         dp[x][y][board[x][y]] = max(dp[x][y][:board[x][y]])+1

# print(max(dp[N-1][N-1]))

# 2nd try
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# dp = [[1]*N for _ in range(N)]

# for x in range(N):
#     for y in range(N):
#         for i in range(x+1):
#             for j in range(y+1):
#                 if board[i][j] < board[x][y]:
#                     dp[x][y] = max(dp[x][y], dp[i][j]+1)

# print(max(max(dp[x]) for x in range(N)))


# 30408 춘배가 선물하는 특별한 하트
# from collections import deque

# M, N = map(int, input().split())
# nset = set({M})
# q = deque([M])

# while q:
#     n = q.popleft()
#     if n % 2 == 0:
#         nn = n//2
#         if nn not in nset:
#             nset.add(nn)
#             q.append(nn)
#     else:
#         a, b = (n-1)//2, (n+1)//2
#         for nn in [a, b]:
#             if nn not in nset:
#                 nset.add(nn)
#                 q.append(nn)

# print('YES' if N in nset else 'NO')


# 17178 줄서기
# N = int(input())
# words = [list(input().split()) for _ in range(N)]
# wds = [['_'] for _ in range(5*N)]

# for x in range(N):
#     for y in range(5):
#         a, n = words[x][y].split('-')
#         wds[5*x+y] = [words[x][y], ord(a)*1000+int(n), 0]

# wds.sort(key=lambda x:(x[1]))
# for k in range(5*N):
#     wds[k][2] = k+1
# # print(wds)

# wd_dict = dict({})
# for w in wds:
#     wd_dict[w[0]] = w[2]
# # print(wd_dict)

# words = [[wd_dict[words[x][y]] for y in range(5)] for x in range(N)]
# # print(words)

# target = 1
# stack = []
# pos = True

# for x in range(N):
#     for y in range(5):
#         while stack and stack[-1] == target:
#             target = stack.pop()+1
#         stack.append(words[x][y])

# while stack and stack[-1] == target:
#     target = stack.pop()+1

# print('GOOD' if target > 5*N else 'BAD')


# 2591 숫자카드
# def solve():
#     ns = [0] + list(map(int, input()))
#     N = len(ns)
#     dp = [[0, 0] for _ in range(N)] 
#     # print(ns)

#     dp[1][0] = 1
#     for i in range(2, N):
#         if ns[i] == 0:
#             if not (1 <= ns[i-1] <= 3) :
#                 print(0)
#                 return
#         dp[i][1] = dp[i-1][0] if (ns[i-1]*10+ns[i]) <= 34 else 0
#         dp[i][0] = sum(dp[i-1]) if ns[i] != 0 else 0

#     print(sum(dp[N-1]))

# solve()


# 6159 Costume Party
# N, S = map(int, input().split())
# ns = sorted([int(input()) for _ in range(N)])

# l, r = 0, N-1
# ans = 0

# while l < r:
#     if (ns[l]+ns[r]) <= S:
#         ans += r-l
#         l += 1
#     else:
#         r -= 1

# print(ans)


# 15721 번데기
# A = int(input())
# T = int(input())
# t = int(input())

# cnt, i, n = 0, 0, 1
# while True:
#     for c in '0101'+'0'*(n+1)+'1'*(n+1):
#         if int(c) == t:
#             cnt += 1
#             if cnt == T:
#                 print(i % A)
#                 exit()
#         i += 1
#     n += 1


# 21554 마법의 돌 장난감
# N = int(input())
# ns = list(map(int, input().split()))

# ans, i = [], 0
# while i < N-1:
#     if ns[i] != i+1:
#         for j in range(i+1, N):
#             if ns[j] == i+1:
#                 ans.append([i+1, j+1])
#                 for k in range((j-i+1)//2):
#                     ns[i+k], ns[j-k] = ns[j-k], ns[i+k]
#     i += 1

# print(len(ans))
# for i in range(len(ans)):
#     print(*ans[i])


# 20493 세상은 하나의 손수건
# N, T = map(int, input().split())
# inc_xy = [[1, 0], [0, -1], [-1, 0], [0, 1]]

# x, y = 0, 0
# now, d = 0, 0
# for _ in range(N):
#     n, s = input().split()
#     n = int(n)

#     px, py = inc_xy[d]
#     x += px*(n-now)
#     y += py*(n-now)

#     turn = 1 if s == 'right' else -1
#     d = (d+turn)%4
#     now = n

# px, py = inc_xy[d]
# x += px*(T-now)
# y += py*(T-now)

# print(x, y)


'''

5 
-47 49 13 46 97
'''

# 1684 같은 나머지
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# def solve():
#     N = int(input())
#     ans = int(2e6)
#     ns = list(map(int, input().split()))
#     ns = [abs(ns[i+1]-ns[i]) for i in range(N-1)]
#     ns = [n for n in ns if n]
#     if len(ns) == 1:
#         print(ns[0])
#         return

#     for i in range(len(ns)-1):
#         ans = min(ans, gcd(ns[i], ns[i+1]))
#     print(ans)

# solve()


# 1755 숫자놀이
# M, N = map(int, input().split())
# ns = [[i, '_'] for i in range(M, N+1)]

# n_dict = dict({
#     0 : 'zero',
#     1 : 'one',
#     2 : 'two',
#     3 : 'three',
#     4 : 'four',
#     5 : 'five',
#     6 : 'six',
#     7 : 'seven',
#     8 : 'eight',
#     9 : 'nine',
# })
# # print(n_dict)

# def w(n):
#     a = []
#     while n > 0:
#         a.append(n_dict[n%10])
#         n //= 10
#     return ' '.join(a[::-1])

# for i in range(N-M+1):
#     ns[i][1] = w(ns[i][0])

# ns.sort(key=lambda x:(x[1]))
# # print(ns)

# for i in range(N-M+1):
#     print(ns[i][0], end=' ')
#     if i % 10 == 9:
#         print()


# 20548 칠리소스

'''
727272 단계의 매운맛
15831930576
'''

# def base7(ms):
#     now, tmp = 0, 1
#     for m in ms:
#         now += m*tmp
#         tmp *= 7
#     return now

# def solve():
#     N = int(input())

#     ans = 0
#     ms = [0]*30
#     while True:
#         ans += 1
#         ms[0] += 1
#         for i in range(29):
#             if ms[i] <= 2: break
#             ms[i] = 0
#             ms[i+1] += 1

#         if N == base7(ms):
#             print(ans)
#             return

# solve()


# 3989 좋은 단어
# ans = 0
# for _ in range(int(input())):
#     a, b = 0, 0
#     s = []
#     for c in list(input()):
#         if s and s[-1] == c:
#             s.pop()
#             continue
#         s.append(c)
#     if not s: ans += 1

# print(ans)


# 5426 편지
# import math

# for _ in range(int(input())):
#     s = list(input())
#     k = math.isqrt(len(s))

#     for i in range(k-1, -1, -1):
#         for j in range(k):
#             print(s[i+k*j], end='')
#     print()


# 17488 수강 바구니
# N, M = map(int, input().split())
# limits = [0] + list(map(int, input().split()))
# ans = [[] for _ in range(N+1)]

# for _ in range(2):
#     tmps = [[] for _ in range(M+1)]
#     for i in range(N):
#         ns = list(map(int, input().split()))
#         for n in ns[:-1]:
#             tmps[n].append(i+1)

#     for i in range(1, M+1):
#         len_tmps_i = len(tmps[i])
#         if limits[i] >= len_tmps_i:
#             for k in tmps[i]:
#                 ans[k].append(i)
#         limits[i] -= len_tmps_i

# for i in range(1, N+1):
#     print(*sorted(ans[i])) if ans[i] else print('망했어요')


# 28298 더 흔한 타일 색칠 문제
# N, M, K = map(int, input().split())
# board = [list(input()) for _ in range(N)]
# cnts = [[[0]*26 for _ in range(K)] for _ in range(K)]

# for x in range(N):
#     for y in range(M):
#         cnts[x%K][y%K][ord(board[x][y])-65] += 1
# # print(cnts)

# ans = 0
# repeat = N*M//K
# for x in range(K):
#     for y in range(K):
#         max_cnt, alpha = 0, ''
#         for i in range(26):
#             if max_cnt < cnts[x][y][i]:
#                 max_cnt = cnts[x][y][i]
#                 alpha = i
#         new_alpha = chr(alpha+65)
#         if board[x][y] != new_alpha:
#             board[x][y] = new_alpha
#             ans += 1

# for i in range(N//K):
#     for j in range(M//K):
#         for x in range(K):
#             for y in range(K):
#                 if board[x+i*K][y+j*K] != board[x][y]:
#                     board[x+i*K][y+j*K] = board[x][y]
#                     ans += 1

# print(ans)
# for x in range(N):
#     print(*board[x], sep='')


'''
11777777
'''

# 11059 크리 문자열
# def solve():
#     ns = [0]+list(map(int, input()))
#     N = len(ns)
#     sums = [0]*N

#     for i in range(1, N):
#         sums[i] = sums[i-1]+ns[i]
#     # print(sums)

#     ans = 0
#     for i in range(N-1):
#         for k in range((N-1-i)//2, 0, -1):
#             if (sums[i+k]-sums[i]) == (sums[i+2*k]-sums[i+k]):
#                 ans = max(ans, 2*k)
#     print(ans)

# solve()


# 21921 블로그
# N, X = map(int, input().split())
# ns = list(map(int, input().split()))

# l, r = 0, X-1
# now = sum(ns[l:r+1])
# max_sum = now
# cnt = 1

# while True:
#     r += 1
#     if r >= N:
#         break
#     now += ns[r]
#     now -= ns[l]
#     l += 1

#     if max_sum < now:
#         max_sum = now
#         cnt = 1
#     elif max_sum == now:
#         cnt += 1

# print(max_sum, cnt, sep='\n') if max_sum > 0 else print('SAD')


# 5911 선물
# N, B = map(int, input().split())
# ns = [list(map(int, input().split())) for _ in range(N)]
# ns.sort(key=lambda x:(x[0]+x[1], x[0]))
# for i in range(N):
#     ns[i].append(sum(ns[i]))
# # print(ns)

# ans = 0
# for t in range(N):
#     now, cnt = ns[t][0]//2 + ns[t][1], 1
#     if now > B: continue
#     ans = max(ans, 1)

#     for i in range(N):
#         if i != t:
#             now += ns[i][2]
#             cnt += 1

#             if now <= B:
#                 ans = max(ans, cnt)
#             else:
#                 break
# print(ans)


# 1639 행운의 티켓
# ns = [0] + list(map(int, input()))
# N = len(ns)
# sums = [ns[0]]*N
# for i in range(1, N):
#     sums[i] = sums[i-1] + ns[i]
# # print(sums)

# ans = 0
# for i in range(0, N-1):
#     k = 1
#     while i+2*k < N:
#         if (sums[i+k]-sums[i]) == (sums[i+2*k]-sums[i+k]):
#             ans = max(ans, 2*k)
#         k += 1
# print(ans)


# 19637 IF문 좀 대신 써줘
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# ns = [list(input().split()) for _ in range(N)]
# for i in range(N):
#     ns[i][1] = int(ns[i][1])
# # print(ns)

# for _ in range(M):
#     target = int(input())
#     l, r = 0, N-1
#     ans = 0

#     while l <= r:
#         mid = (l+r)//2
#         if target <= ns[mid][1]:
#             ans = mid
#             r = mid-1
#         else:
#             l = mid+1

#     print(ns[ans][0])


# 3518 공백왕 빈-칸
# import sys
# lines = sys.stdin.readlines()
# lines = [line.split() for line in lines]
# # print(lines)

# ans = [0]*90
# for line in lines:
#     i = 0
#     for w in line:
#         ans[i] = max(ans[i], len(w))
#         i += 1

# def fill(s, len_s, n):
#     return s+' '*(n-len_s)

# for line in lines:
#     i = 0
#     for w in line[:-1]:
#         print(fill(w, len(w), ans[i]), end=' ')
#         i += 1
#     print(line[-1])


# 11068 회문인 수
# def base(n, b):
#     s = []
#     while n > 0:
#         s.append(n%b)
#         n //= b
#     return s

# for _ in range(int(input())):
#     n = int(input())
#     pos = False
#     for B in range(2, 65):
#         new_n = base(n, B)
#         if new_n == new_n[::-1]:
#             pos = True
#             break

#     print(1 if pos else 0)


# 22234 가희와 은행
# import sys
# input = sys.stdin.readline
# from collections import deque

# N, T, W = map(int, input().split())
# q = deque([list(map(int, input().split())) for _ in range(N)])
# # print(q)

# d = dict()
# for _ in range(int(input())):
#     p, t, c = map(int, input().split())
#     d[c] = [p, t]
# # print(d)

# time = 0
# tmp_T = T
# tmp_p, tmp_t = q.popleft()

# for _ in range(W):
#     time += 1
#     if time in d:
#         q.append(d[time])

#     if tmp_T and tmp_t:
#         print(tmp_p)
#         tmp_T -= 1
#         tmp_t -= 1

#     if not tmp_T:
#         if tmp_t:
#             q.append([tmp_p, tmp_t])
#         tmp_T = T
#         if q:
#             tmp_p, tmp_t = q.popleft()

#     if not tmp_t:
#         tmp_T = T
#         if q:
#             tmp_p, tmp_t = q.popleft()


# 5078 Shirts
# N = int(input())

# repeat = True
# while repeat:
#     for i in range(2):
#         if i == 0:
#             if N > 0:
#                 d = dict()
#                 for s in "SML":
#                     d[s] = []
#                 # print(d)
#             else:
#                 repeat = False
#                 break

#         for _ in range(N):
#             s, c = list(input())
#             d[s].append(c)
#         # print(d)

#         if i == 1:
#             for s in "SML":
#                 d[s].sort()

#             for s in "SML":
#                 for c in d[s]:
#                     print(f'{s}{c}', end=' ')
#             print()

#         N = int(input())


# 11645 I’ve Been Everywhere, Man
# for _ in range(int(input())):
#     print(len(set([input() for _ in range(int(input()))])))


# 11504 돌려 돌려 돌림판!
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     N, M = map(int, input().split())
#     X = int(''.join(list(input().split())))
#     Y = int(''.join(list(input().split())))
#     ns = list(input().split())

#     ns = ns+ns
#     ans = 0
#     for i in range(N):
#         n = int(''.join(ns[i:i+M]))
#         if X <= n <= Y:
#             ans += 1
#     print(ans)


# 17204 죽음의 게임
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# ds = [int(input()) for _ in range(N)]
# visited = [False]*N

# ans = -1
# cnt, v = 0, 0

# while v != K and not visited[v]:
#     cnt += 1
#     visited[v] = True
#     v = ds[v]
#     if v == K:
#         ans = cnt

# print(ans)


# 2011 암호코드
# def solve():
#     ns = list(map(int, input()))
#     N = len(ns)
#     dp = [[0, 0] for _ in range(N)]
#     mod = int(1e6)

#     pos = True
#     for i in range(N):
#         if ns[i] == 0:
#             if i > 0:
#                 if ns[i-1] == 0:
#                     pos = False
#                 elif ns[i-1] in [1, 2]:
#                     dp[i][1] = dp[i-1][0]
#             else:
#                 pos = False
#         else:
#             if i > 0:
#                 dp[i][0] = sum(dp[i-1]) % mod
#                 if (ns[i-1] == 1) or (ns[i-1] == 2 and ns[i] <= 6):
#                     dp[i][1] = dp[i-1][0]
#             else:
#                 dp[i][0] = 1

#         if not pos:
#             print(0)
#             return

#     # print(dp)
#     print(sum(dp[N-1]) % mod)

# solve()


# 31218 자료 구조의 왕
# import sys
# input = sys.stdin.readline

# n, m, Q = map(int, input().split())
# board = [[0]*m for _ in range(n)]
# rest = n*m

# for _ in range(Q):
#     cmd = list(map(int, input().split()))
#     if cmd[0] == 1:
#         _, dy, dx, y, x = cmd
#         y, x = y-1, x-1
#         while not board[y][x]:
#             board[y][x] = 1
#             rest -= 1
#             ny, nx = y+dy, x+dx
#             if 0 <= ny < n and 0 <= nx < m:
#                 y, x = ny, nx
#             else:
#                 break
#     elif cmd[0] == 2:
#         _, y, x = cmd
#         print(board[y-1][x-1])
#     else: # cmd[0] == 3:
#         print(rest)


# 1337 올바른 배열
'''
2
2
6
'''
'''
6
1
2
3
4
5
6
'''

# sort, two_pointer
# N = int(input())
# ns = sorted([int(input()) for _ in range(N)])

# ans = 4
# r = 0
# for l in range(N):
#     while r < N-1:
#         r += 1
#         if (ns[r] - ns[l]) >= 5:
#             r -= 1
#             break
#     ans = min(ans, 4-r+l)

# print(ans)


# set
# N = int(input())
# ns = [int(input()) for _ in range(N)]
# set_ns = set(ns)

# ans = 4
# for n in ns:
#     for k in range(n-2, n+3):
#         tmp_ans = 5
#         l, r = k, k

#         if k in set_ns:
#             tmp_ans -= 1

#         for _ in range(2):
#             l -= 1
#             if l in set_ns:
#                 tmp_ans -= 1

#         for _ in range(2):
#             r += 1
#             if r in set_ns:
#                 tmp_ans -= 1

#         ans = min(ans, tmp_ans)

# print(ans)


# 20365 블로그2

# sol 1
# N = int(input())
# colors = list(input())

# ans = N
# for t in "RB":
#     tmp_ans = 1
#     pre = ''

#     for c in colors:
#         if (pre != c) and (c == t):
#             tmp_ans += 1
#         pre = c
#     ans = min(ans, tmp_ans)

# print(ans)


# sol 2
# N = int(input())
# colors = list(input())
# dict_c = dict({'B' : 0, 'R' : 0})
# dict_c[colors[0]] += 1

# for i in range(1, N):
#     if colors[i-1] != colors[i]:
#         dict_c[colors[i]] += 1

# print(min(dict_c.values())+1)


# 비교
# def btr(t, len_t, n):
#     if len_t == n:
#         # print(t)

#         # solution? 1
#         N = len_t
#         colors = t

#         # boj_summited code #1
#         # ans = N
#         # for _ in range(2):
#         #     tmp_ans = 0
#         #     for target in "RB":
#         #         now = ''
#         #         for c in colors:
#         #             if now != c and c == target:
#         #                 tmp_ans += 1
#         #             now = c
#         #         ans = min(ans, tmp_ans+1)
#         #     print(t, "ta", tmp_ans)
#         # ans_a = ans

#         # sol 1
#         ans = N
#         for t in "RB":
#             tmp_ans = 1
#             pre = ''

#             for c in colors:
#                 if (pre != c) and (c == t):
#                     tmp_ans += 1
#                 pre = c
#             ans = min(ans, tmp_ans)

#         ans_a = ans


#         # solution 2
#         dict_c = dict({'B' : 0, 'R' : 0})
#         dict_c[colors[0]] += 1

#         for i in range(1, N):
#             if colors[i-1] != colors[i]:
#                 dict_c[colors[i]] += 1

#         ans_b = min(dict_c.values())+1

#         if ans_a != ans_b:
#             print(t, ans_a, ans_b)
#         return

#     for a in "BR":
#         tmp_t = t[:]
#         tmp_t.append(a)
#         btr(tmp_t, len_t+1, n)

# btr([], 0, int(input()))


# 1261 알고스팟
# from collections import deque

# M, N = map(int, input().split())
# board = [list(map(int, input())) for _ in range(N)]
# cnt = [[N*M]*M for _ in range(N)]
# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# q = deque([[0, 0, 0]]) # x, y, 부순 횟수
# while q:
#     x, y, c = q.popleft()
#     if cnt[x][y] > c:
#         cnt[x][y] = c
#         for px, py in inc_xy:
#             nx, ny = x+px, y+py
#             if 0 <= nx < N and 0 <= ny < M:
#                 q.append([nx, ny, c+board[nx][ny]])

# print(cnt[N-1][M-1])


# 2559 수열
# N, K = map(int, input().split())
# ns = list(map(int, input().split()))

# now = sum(ns[:K])
# ans = now

# for i in range(N-K):
#     now = now - ns[i] + ns[i+K]
#     ans = max(ans, now)
# print(ans)


# 21940 가운데에서 만나기
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# INF = int(4e5)+1
# board = [[INF]*(N+1) for _ in range(N+1)]

# for _ in range(M):
#     a, b, t = map(int, input().split())
#     board[a][b] = min(board[a][b], t)

# for x in range(1, N+1):
#     board[x][x] = 0

# # core
# for k in range(1, N+1):
#     for a in range(1, N+1):
#         for b in range(1, N+1):
#             board[a][b] = min(board[a][b], board[a][k]+board[k][b])

# # for x in range(N+1):
# #     print(board[x])

# K = int(input())
# cs = list(map(int, input().split()))

# ans_d = INF
# ans_vs = []
# for v in range(1, N+1):
#     tmp_d = 0
#     for c in cs:
#         tmp_d = max(tmp_d, board[c][v]+board[v][c])

#     if ans_d > tmp_d:
#         ans_d = tmp_d
#         ans_vs = [v]
#     elif ans_d == tmp_d:
#         ans_vs.append(v)

# # print(ans_d)
# print(*ans_vs)


# 2668 숫자 고르기
# N = int(input())
# ns = [0] + [int(input()) for _ in range(N)]
# ans = []

# def dfs(aset, bset, v, visited):
#     if visited[v]:
#         if sorted(aset) == sorted(bset):
#             ans.extend(list(aset))
#         return

#     visited[v] = True
#     aset.add(v)

#     nv = ns[v]
#     bset.add(nv)
#     dfs(aset, bset, nv, visited)

# for v in range(1, N+1):
#     dfs(set(), set(), v, [False]*(N+1))

# ans = set(ans)
# print(len(ans))
# print(*sorted(ans), sep='\n')


# 18115 카드 놓기
# import sys
# input = sys.stdin.readline
# from collections import deque

# N = int(input())
# ns = [0] + list(map(int, input().split()))[::-1]
# q = deque()

# for n in range(1, N+1):
#     if ns[n] == 1:
#         q.appendleft(n)
#     elif ns[n] == 2:
#         for k in [n, q.popleft()]:
#             q.appendleft(k)
#     else:
#         q.append(n)

# print(*q)


# 1652 누울 자리를 찾아라
# N = int(input())
# board = [list(input()) for _ in range(N)]
# ans = []

# # row
# cnt = 0
# for x in range(N):
#     cnt += len([1 for s in ''.join(board[x]).split('X') if len(s) >= 2])
# ans.append(cnt)

# # col
# cnt = 0
# for y in range(N):
#     cnt += len([1 for s in ''.join([board[x][y] for x in range(N)]).split('X') if len(s) >= 2])
# ans.append(cnt)

# print(*ans)


# 9084 동전
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     N = int(input())
#     ns = [0] + list(map(int, input().split()))
#     M = int(input())
#     board = [[1]+[0]*M for _ in range(N+1)]

#     for x in range(1, N+1):
#         for y in range(1, M+1):
#             board[x][y] = board[x-1][y]
#             c = ns[x]
#             if y >= c:
#                 board[x][y] += board[x][y-c]

#     print(board[N][M])


# 9613 GCD 합
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# for _ in range(int(input())):
#     ns = list(map(int, input().split()))
#     N, ns = ns[0], ns[1:]

#     ans = 0
#     for i in range(N-1):
#         for j in range(i+1, N):
#             ans += gcd(ns[i], ns[j])
#     print(ans)


# 10282 해킹
# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque

# for _ in range(int(input())):
#     n, d, c = map(int, input().split())

#     INF = int(1e12)+1
#     time = [INF]*(n+1)

#     q = deque([[c, 0]])
#     g = defaultdict(list)
#     for _ in range(d):
#         a, b, s = map(int, input().split())
#         g[b].append([a, s])

#     while q:
#         v, t = q.popleft()
#         if time[v] > t:
#             time[v] = t
#             for a, s in g[v]:
#                 q.append([a, t+s])

#     infected = [i for i in range(n+1) if time[i] != INF]
#     print(len(infected), max(time[i] for i in infected))


# 15889 호 안에 수류탄이야!!
'''
3
0 10 20
1 100
'''

# import sys
# input = sys.stdin.readline

# N = int(input())
# xs = list(map(int, input().split()))

# pos = True
# if N > 1:
#     rs = list(map(int, input().split()))
#     mx = rs[0]

#     for i in range(N-1):
#         if mx < xs[i]:
#             break
#         nx = xs[i]+rs[i]
#         if mx < nx:
#             mx = nx

#     if mx < xs[N-1]:
#         pos = False

# print('권병장님, 중대장님이 찾으십니다' if pos else '엄마 나 전역 늦어질 것 같아')


# 25591 푸앙이와 종윤이
# x, y = map(int, input().split())
# a, b = (100-x), (100-y), 
# c, d, q, r = (100-a-b), a*b, a*b//100, a*b%100

# print(a, b, c, d, q, r)
# print(c+q, r)


# 28217 두 정삼각형
# rotate
# def rot(A, N):
#     C = [[0]*N for _ in range(N)]
#     for x in range(N):
#         for y in range(x+1):
#             C[N-1-x+y][N-1-x] = A[x][y]
#     return C

# # inversion
# def inv(A, N):
#     C = [[0]*N for _ in range(N)]
#     for x in range(N):
#         l, r = 0, x
#         while l <= r:
#             C[x][l], C[x][r] = A[x][r], A[x][l]
#             l += 1; r -= 1
#     return C

# # count
# def cnt(A, B, N):
#     n = 0
#     for x in range(N):
#         for y in range(x+1):
#             n += 1 if A[x][y] != B[x][y] else 0
#     return n

# def solve():
#     N = int(input())
#     A = [[] for _ in range(N)]
#     B = [[] for _ in range(N)]

#     for x in range(N):
#         A[x] = list(map(int, input().split()))
#     for x in range(N):
#         B[x] = list(map(int, input().split()))

#     ans = N*(N+1)//2
#     for G in [A, inv(A, N)]:
#         RG = rot(G, N)
#         for T in [G, RG, rot(RG, N)]:
#             ans = min(ans, cnt(T, B, N))

#     print(ans)

# solve()


# 28450 컨벤 데드가 하고싶어요
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# board = [[0]] + [[0]+list(map(int, input().split())) for _ in range(N)]
# dp = [[int(1e11)]*(M+1) for _ in range(N+1)]
# dp[0][1] = 0

# for x in range(1, N+1):
#     for y in range(1, M+1):
#         dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + board[x][y]

# H = int(input())
# print("YES", dp[N][M], sep='\n') if H >= dp[N][M] else print("NO")


# 16987 계란으로 계란치기
'''
3
1 4
8 1
3 1
'''
'''
8
7 100
6 100
100 1
100 1
100 1
100 1
100 1
100 1
'''
'''
6
5 100
4 100
100 1
100 1
100 1
100 1
'''

# N = int(input())
# ns = [list(map(int, input().split())) for _ in range(N)]
# global ans
# ans = 0

# def cnt():
#     return sum([1 if ns[i][0] <= 0 else 0 for i in range(N)])

# def btr(i):
#     global ans
#     if i >= N:
#         ans = max(ans, cnt())
#         return

#     if ns[i][0] <= 0:
#         btr(i+1)
#         return

#     cannot_attack = True
#     for j in range(N):
#         if i != j and ns[j][0] > 0:
#             cannot_attack = False
#             ns[i][0] -= ns[j][1]
#             ns[j][0] -= ns[i][1]
#             btr(i+1)
#             ns[i][0] += ns[j][1]
#             ns[j][0] += ns[i][1]

#     if cannot_attack:
#         btr(i+1)

# def solve():
#     btr(0)
#     print(ans)

# solve()


# 1987 알파벳
# retry

# R, C = map(int, input().split())
# board = [input() for _ in range(R)]
# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# visited = [[False]*C for _ in range(R)]
# alphas = [False]*26
# alphas[ord(board[0][0])-65] = True

# global ans
# ans = 1

# def btr(x, y, cnt):
#     global ans
#     ans = max(ans, cnt)
#     if ans >= 26:
#         return

#     for px, py in inc_xy:
#         nx, ny = x+px, y+py
#         if 0 <= nx < R and 0 <= ny < C:
#             oa = ord(board[nx][ny])-65
#             if not visited[nx][ny] and not alphas[oa]:
#                 visited[nx][ny] = True
#                 alphas[oa] = True
#                 btr(nx, ny, cnt+1)

#                 visited[nx][ny] = False
#                 alphas[oa] = False

# def solve():
#     visited[0][0] = True
#     btr(0, 0, 1)
#     print(ans)

# solve()


# 5107 마니또
# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque

# N = int(input())
# case_num = 1

# while N > 0:
#     g = defaultdict(list)
#     names, visited = set(), set()
#     for _ in range(N):
#         a, b = input().split()
#         g[a].append(b)
#         names.add(a)

#     ans = 0
#     for name in names:
#         if name not in visited:
#             ans += 1
#             visited.add(name)
#             q = deque([name])

#             while q:
#                 v = q.popleft()
#                 for u in g[v]:
#                     if u not in visited:
#                         visited.add(u)
#                         q.append(u)

#     print(case_num, ans)
#     N = int(input())
#     case_num += 1


# 10451 순열 사이클
# for _ in range(int(input())):
#     N = int(input())
#     ns = [0] + list(map(int, input().split()))
#     visited = [False]*(N+1)

#     ans = 0
#     for i in range(1, N+1):
#         if not visited[i]:
#             ans += 1
#             visited[i] = True
#             v = ns[i]
#             while v != i:
#                 visited[v] = True
#                 v = ns[v]

#     print(ans)


# 1394 암호
# cs = list(input())
# ts = list(input())
# C, T = len(cs), len(ts)
# mod = 900528

# # powers
# pws = [1]*T
# for i in range(1, T):
#     pws[i] = (pws[i-1]*C) % mod

# # 앞에 몇 개의 알파벳이 있는지
# d = dict()
# for i in range(C):
#     d[cs[i]] = i
# # print(d)

# # 총 길이(T)보다 자리수가 적은 경우
# ans = 1
# for i in range(1, T):
#     ans = (ans + pws[i]) % mod
# # print(ans)

# # 총 길이 맞춘 이후 각 알파벳이 올 때까지 횟수 plus
# for i in range(T):
#     t = ts[i]
#     ans = (ans + d[t]*pws[T-1-i]) % mod

# print(ans)


# 1990 소수인팰린드롬
'''
1 10000
'''
# import math

# a, b = map(int, input().split())
# # isqrt_b = math.isqrt(b)

# # sieves, primes
# ss = [True]*(10000)
# for i in range(2, 10000):
#     if ss[i]:
#         for ii in range(2*i, 10000, i):
#             ss[ii] = False
# ps = [i for i in range(2, 10000) if ss[i]]
# # print(ps)
# # print(len(ps)) max : 1229

# def prime_check(n):
#     isqrt_n = math.isqrt(n)
#     for p in ps:
#         # if isqrt_n < p:
#         #     break
#         if n % p == 0:
#             return False
#     return True

# def solve():
#     for n in range(2, 8):
#         if a <= n <= b and prime_check(n):
#             print(n)
#         elif n > b:
#             return

#     # d : 자릿수
#     for d in range(2, 9):
#         dl = d//2
#         dm = d%2

#         pn = 10**(dl-1)
#         for n in range(pn, 10*pn):
#             if (n // pn) % 2 == 0 : continue
#             sn = str(n)

#             if dm != 0:
#                 for km in range(10):
#                     tn = int(sn+str(km)+sn[::-1])
#                     if tn > b: return
#                     if prime_check(tn): print(tn)
#                 continue

#             # 소수 체크
#             tn = int(sn+sn[::-1])
#             if tn > b: return
#             if prime_check(tn): print(tn)

# solve()
# print(-1)


# 28018 시간이 겹칠까?
# import sys
# input = sys.stdin.readline

# N = int(input())
# lmt = int(1e6)+1
# check = [0]*(lmt+1)
# sums = [0]*lmt

# for _ in range(N):
#     S, E = map(int, input().split())
#     check[S] += 1
#     check[E+1] -= 1

# for i in range(lmt):
#     sums[i] = sums[i-1]+check[i]

# input()
# for n in map(int, input().split()):
#     print(sums[n])


# 1990 소수인 팰린드롬 (리트) - 클리어
# import math

# def prime_check(n):
#     if n == 1: return False
#     elif n == 2: return True
#     elif n % 2 == 0: return False
#     else:
#         for k in range(3, math.isqrt(n)+1, 2):
#             if n % k == 0:
#                 return False
#         return True

# def rn(n, hw):
#     sn = str(n)
#     return int(sn+sn[:hw][::-1])

# def solve():
#     a, b = map(int, input().split())

#     for w in range(1, 8, 2):
#         bn = 10**(w//2)
#         for n in range(bn, 10*bn):
#             target = rn(n, w//2)
#             if a > target:
#                 continue
#             if target <= b:
#                 if prime_check(target):
#                     print(target)
#             else:
#                 return

#         if w == 1 and a <= 11 <= b:
#             print(11)

# solve()
# print(-1)


# 14719 빗물
# H, W = map(int, input().split())
# ns = list(map(int, input().split()))

# # std : standard, mhi : max_height_index
# ans, std = 0, 0
# mhi = ns.index(max(ns))

# def cal_s(s, e, delta):
#     global ans
#     mhi_yet = s
#     for i in range(s+delta, e+delta, delta):
#         if ns[mhi_yet] <= ns[i]:
#             for j in range(mhi_yet, i, delta):
#                 ans += ns[mhi_yet] - ns[j]
#             mhi_yet = i

# cal_s(0, mhi, 1)
# cal_s(W-1, mhi, -1)
# print(ans)


# 5637 가장 긴 단어
# import sys
# input = sys.stdin.readline

# word, ml = '', 0
# end = False

# while not end:
#     for ss in list(input().split()):
#         w = ''
#         for i in range(len(ss)):
#             c = ss[i]
#             if (65 <= ord(c) < 91) or (97 <= ord(c) < 123) or (c == '-'):
#                 w += c
#             else:
#                 len_w = len(w)
#                 if ml < len_w:
#                     ml = len_w
#                     word = w
#                 w = ''

#         if w != '':
#             if w == 'E-N-D':
#                 end = True
#                 break
#             len_w = len(w)
#             if ml < len_w:
#                 ml = len_w
#                 word = w

# print(word.lower())


# 1655 가운데를 말해요
# 반 잘라서 제일 큰 값 pq(중앙값 미만 index), 제일 작은 값 pq (중앙값 포함)
'''
5
1
2
3
4
5
'''
# import sys
# input = sys.stdin.readline
# from heapq import heappush, heappop

# maxq, minq = [], []
# for i in range(int(input())):
#     n = int(input())
#     if i % 2 == 0:
#         heappush(maxq, -n)
#     else:
#         heappush(minq, n)

#     if minq and (-maxq[0]) > minq[0]:
#         tmax = -heappop(maxq)
#         heappush(maxq, -heappop(minq))
#         heappush(minq, tmax)

#     print(-maxq[0])


# 12904 A와 B
# S = input()
# T = input()
# t, now = len(S), len(T)

# l, r = 0, now-1
# rev = False

# while t < now:
#     if not rev:
#         if T[r] == 'B':
#             rev = True
#         r -= 1
#     else:
#         if T[l] == 'B':
#             rev = False
#         l += 1
#     now -= 1

# T = T[l:r+1][::-1 if rev else 1]
# print(1 if S == T else 0)


# 15720 카우버거
# B, C, D = map(int, input().split())

# bs = sorted(list(map(int, input().split())))
# cs = sorted(list(map(int, input().split())))
# ds = sorted(list(map(int, input().split())))

# ans = sum(bs)+sum(cs)+sum(ds)
# print(ans)

# k = min(B, C, D)
# ans -= 0.1*(sum(bs[-k:])+sum(cs[-k:])+sum(ds[-k:]))
# print(int(ans))


# 14921 용액 합성하기
# N = int(input())
# ns = list(map(int, input().split()))

# l, r = 0, N-1
# val = int(2e8)+1

# while l < r:
#     now = ns[l]+ns[r]
#     if abs(val) > abs(now):
#         val = now

#     if now < 0: l += 1
#     else: r -= 1

# print(val)


# 23300 웹 브라우저 2
# import sys
# input = sys.stdin.readline

# N, Q = map(int, input().split())
# s, now, e = -1, -1, -1
# pgs = []

# for _ in range(Q):
#     cmds = list(input().split())
#     # print(cmds)

#     if cmds[0] == "B":
#         if s < now:
#             now -= 1
#     elif cmds[0] == "F":
#         if now < e:
#             now += 1
#     elif cmds[0] == "A":
#         n = int(cmds[1])
#         if now == -1:
#             s, now, e = 0, 0, 0
#             pgs = [n]
#         else:
#             for _ in range(e-now):
#                 pgs.pop()
#             pgs.append(n)
#             now += 1
#             e = now
#     else:
#         if now != -1:
#             tmp_pgs = []
#             prev = -1

#             for p in pgs[:now]:
#                 if prev != p:
#                     tmp_pgs.append(p)
#                 prev = p

#             gap = now-len(tmp_pgs)
#             tmp_pgs.extend(pgs[now:])
#             pgs = tmp_pgs

#             now -= gap
#             e -= gap

# # print(s, now, e)
# # print(pgs)

# print(pgs[now])
# print(*pgs[:now][::-1]) if s < now else print(-1)
# print(*pgs[(now+1):]) if now < e else print(-1)




# 13140 Hello World!
# def check_exp(N, h, w, e, o, l, r, d):
#     now = 10000*(h+w)+1000*e+1001*o+120*l+100*r+d
#     if N == now: return True
#     else: return False

# def print_answer(N, h, w, e, o, l, r, d):
#     print(f'  {h}{e}{l}{l}{o}')
#     print(f'+ {w}{o}{r}{l}{d}')
#     print(f'-------')
#     SN = str(N)
#     print(' '*(7-len(SN)), SN, sep='')

# def solve():
#     N = int(input())
#     check = [False]*10

#     for h in range(1, 10):
#         check[h] = True
#         for w in range(1, 10):
#             if check[w]: continue
#             check[w] = True
#             for e in range(0, 10):
#                 if check[e]: continue
#                 check[e] = True
#                 for o in range(0, 10):
#                     if check[o]: continue
#                     check[o] = True
#                     for l in range(0, 10):
#                         if check[l]: continue
#                         check[l] = True
#                         for r in range(0, 10):
#                             if check[r]: continue
#                             check[r] = True
#                             for d in range(0, 10):
#                                 if check[d]: continue
#                                 check[d] = True
#                                 if check_exp(N, h, w, e, o, l, r, d):
#                                     print_answer(N, h, w, e, o, l, r, d)
#                                     return

#                                 check[d] = False
#                             check[r] = False
#                         check[l] = False
#                     check[o] = False
#                 check[e] = False
#             check[w] = False
#         check[h] = False
#     print('No Answer')

# solve()


# 6593 상범 빌딩
# import sys
# input = sys.stdin.readline
# from collections import deque

# L, R, C = map(int, input().split())
# inc_xyz = [[0, 0, 1], [0, 1, 0], [0, 0, -1], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]
# while not (L == 0 and R == 0 and C == 0):
#     visited = [[[False]*C for _ in range(R)] for _ in range(L)]
#     board = []
#     for _ in range(L):
#         board.append([list(input().rstrip()) for _ in range(R)])
#         input()
#     # print(board)

#     q = deque()
#     for z in range(L):
#         for x in range(R):
#             for y in range(C):
#                 if board[z][x][y] == 'S':
#                     q.append([z, x, y, 0])
#                     visited[z][x][y] = True
#     # print(szxy)

#     can_sb_escape = False
#     while q:
#         z, x, y, cnt = q.popleft()
#         # print(z, x, y, cnt)
#         for pz, px, py in inc_xyz:
#             nz, nx, ny = z+pz, x+px, y+py
#             if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
#                 if board[nz][nx][ny] != '#' and not visited[nz][nx][ny]:
#                     if board[nz][nx][ny] == 'E':
#                         can_sb_escape = True
#                         print(f'Escaped in {cnt+1} minute(s).')
#                         q = []
#                         break
#                     q.append([nz, nx, ny, cnt+1])
#                     visited[nz][nx][ny] = True

#     if not can_sb_escape:
#         print('Trapped!')

#     L, R, C = map(int, input().split())


# 22862 가장 긴 짝수 연속한 부분 수열 (large)
# 하나도 없을 수 있음
# default l, r 설정
# 짝수들 인덱스 저장해두고 사용해도 될 듯,,, 이렇게 했어야 됐네
# 인덱스 저장 안 하고도 두 포인터로 풀 수 있었을 듯
'''
8 1
2 3 3 4 5 5 6 7
[ans] 1
'''
'''
8 1
1 1 1 1 1 1 1 2
[ans] 1
'''
'''
8 5
2 2 1 1 1 1 2 3
[ans] 3
'''
# def solve():
#     N, K = map(int, input().split())
#     ns = list(map(int, input().split()))

#     # even_idxs
#     eis = [i for i in range(N) if ns[i] % 2 == 0]
#     if not eis:
#         print(0)
#         return

#     l, r = 0, 0
#     len_eis = len(eis)
#     ans = 1
#     while l <= r:
#         # ((all cnt) - inner even cnt) <= K
#         while ((eis[r]-1-eis[l])-(max(0, r-l-1))) <= K:
#             r += 1
#             if r >= len_eis:
#                 break
#         r -= 1
#         ans = max(ans, r-l+1)
#         # print("?", l, r, ans)
#         if r == len_eis-1:
#             break
#         l += 1
#     print(ans)

# solve()


# 3020 개똥벌레
# N, H = map(int, input().split())
# ts, bs = [0]*H, [0]*H

# for i in range(N):
#     n = int(input())
#     if i % 2 == 0:
#         bs[n] += 1
#     else:
#         ts[n] += 1
# # print(ts, bs)

# for i in range(H-2, 0, -1):
#     ts[i] = ts[i]+ts[i+1]
#     bs[i] = bs[i]+bs[i+1]
# # print(ts, bs)

# sums = [0]*(H+1)
# for i in range(1, H):
#     sums[i] += ts[i]
#     sums[i+1] += bs[H-i]
# # print(sums)

# ans_sum, ans_cnt = (N+1), 0
# for i in range(1, H+1):
#     if ans_sum > sums[i]:
#         ans_sum = sums[i]
#         ans_cnt = 1
#     elif ans_sum == sums[i]:
#         ans_cnt += 1

# print(ans_sum, ans_cnt)


# 2212 센서
'''
2
1
1 3
'''
'''
3
2
1 3 5
'''
# N = int(input())
# K = int(input())
# ns = sorted(list(map(int, input().split())))
# gaps = sorted([(ns[i+1]-ns[i]) for i in range(N-1)])
# # print(gaps)

# ans = ns[N-1]-ns[0]-(sum(gaps[-K+1:]) if K >= 2 else 0)
# print(ans)


# 18405 경쟁적 전염
# import sys
# input = sys.stdin.readline
# from collections import deque

# N, K = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# q = deque()
# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# vs = [[] for _ in range(K+1)]
# for x in range(N):
#     for y in range(N):
#         if board[x][y] != 0:
#             vs[board[x][y]].append([x, y])

# for k in range(1, K+1):
#     for x, y in vs[k]:
#         q.append([x, y, k])
# # print(q)

# S, X, Y = map(int, input().split())
# for _ in range(S):
#     for _ in range(len(q)): #
#         x, y, k = q.popleft()
#         # print(x, y, k)
#         for px, py in inc_xy:
#             nx, ny = x+px, y+py
#             if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
#                 board[nx][ny] = k
#                 q.append([nx, ny, k])

# # for x in range(N):
# #     print(board[x])

# print(board[X-1][Y-1])


# 17387 선분 교차 2
# 신발끈 정리

'''
1 1 5 5
6 6 5 5
[ans] 1
'''
'''
1 1 5 5
-3 -3 10 10
[ans] 1
'''

# def ccw(x1, y1, x2, y2, x3, y3):
#     a = x1*y2 + x2*y3+ x3*y1
#     b = y1*x2 + y2*x3+ y3*x1
#     return (a-b)

# def solve():
#     x1, y1, x2, y2 = map(int, input().split())
#     x3, y3, x4, y4 = map(int, input().split())

#     ccws1 = [ccw(x1, y1, x2, y2, x3, y3), ccw(x1, y1, x2, y2, x4, y4)]
#     ccws2 = [ccw(x3, y3, x4, y4, x1, y1), ccw(x3, y3, x4, y4, x2, y2)]

#     if (ccws1[0] * ccws1[1] <= 0) and (ccws2[0] * ccws2[1] <= 0):
#         # 평행한 경우 예외처리
#         if (ccws1[0] * ccws1[1] == 0) and (ccws2[0] * ccws2[1] == 0):
#             x1, x2 = sorted([x1, x2])
#             x3, x4 = sorted([x3, x4])
#             y1, y2 = sorted([y1, y2])
#             y3, y4 = sorted([y3, y4])

#             overlapped = False
#             for tx in [x3, x4]:
#                 for ty in [y3, y4]:
#                     if x1 <= tx <= x2 and y1 <= ty <= y2:
#                         overlapped = True
#             for tx in [x1, x2]:
#                 for ty in [y1, y2]:
#                     if x3 <= tx <= x4 and y3 <= ty <= y4:
#                         overlapped = True

#             print(1 if overlapped else 0)
#             return
#         ##
#         print(1)
#     else:
#         print(0)

# solve()


# 9527 1의 개수
# def cal(cnts, s, k):
#     tot, one_cnt = 0, 0
#     for i in range(k):
#         if s[i] == '1':
#             upper = k-1-i
#             tot += cnts[upper] + one_cnt*(1 << upper) + 1
#             one_cnt += 1

#     return tot

# def solve():
#     cnts = [0]*55
#     for i in range(1, 55):
#         cnts[i] = cnts[i-1]*2 + (1 << (i-1))
#     # print(cnts)

#     A, B = map(int, input().split())
#     A -= 1

#     bin_a, bin_b = bin(A)[2:], bin(B)[2:]
#     print(cal(cnts, bin_b, len(bin_b)) - cal(cnts, bin_a, len(bin_a)))

# solve()


# 2162 선분 그룹
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# def find_parent(parent, x):
#     if x != parent[x]:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)

#     if a > b:   parent[a] = b
#     else:       parent[b] = a

# # todo -> class
# def ccw(x1, y1, x2, y2, x3, y3):
#     a = x1*y2 + x2*y3 + x3*y1
#     b = y1*x2 + y2*x3 + y3*x1
#     return a-b

# def is_overlapped(x1, y1, x2, y2, x3, y3, x4, y4):
#     ccws1 = [ccw(x1, y1, x2, y2, x3, y3), ccw(x1, y1, x2, y2, x4, y4)]
#     ccws2 = [ccw(x3, y3, x4, y4, x1, y1), ccw(x3, y3, x4, y4, x2, y2)]

#     if ccws1[0]*ccws1[1] <= 0 and ccws2[0]*ccws2[1] <= 0:
#         if ccws1[0]*ccws1[1] == 0 and ccws2[0]*ccws2[1] == 0:
#             check_overlapped = False
#             x1, x2 = sorted([x1, x2])
#             x3, x4 = sorted([x3, x4])
#             y1, y2 = sorted([y1, y2])
#             y3, y4 = sorted([y3, y4])

#             for tx in [x3, x4]:
#                 for ty in [y3, y4]:
#                     if x1 <= tx <= x2 and y1 <= ty <= y2:
#                         check_overlapped = True
#             for tx in [x1, x2]:
#                 for ty in [y1, y2]:
#                     if x3 <= tx <= x4 and y3 <= ty <= y4:
#                         check_overlapped = True

#             return check_overlapped
#         return True
#     else:
#         return False

# def solve():
#     N = int(input())
#     xys = [list(map(int, input().split())) for _ in range(N)]

#     parent = [i for i in range(N)]
#     for a in range(N-1):
#         x1, y1, x2, y2 = xys[a]
#         for b in range(a+1, N):
#             x3, y3, x4, y4 = xys[b]
#             if is_overlapped(x1, y1, x2, y2, x3, y3, x4, y4):
#                 union_parent(parent, a, b)

#     # here
#     for a in range(N):
#         find_parent(parent, a)
#     ##

#     d = defaultdict(int)
#     for k in parent:
#         d[k] += 1
#     # print(d)

#     print(len(d), max(d.values()), sep='\n')

# solve()


# 2887 행성 터널
# Prim
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# from heapq import heappush, heappop

# N = int(input())
# xyzs = [list(map(int, input().split())) for _ in range(N)]
# xs = sorted([[xyzs[i][0], i] for i in range(N)])
# ys = sorted([[xyzs[i][1], i] for i in range(N)])
# zs = sorted([[xyzs[i][2], i] for i in range(N)])
# # print(xs)
# # print(ys)
# # print(zs)

# g = defaultdict(list)
# for i in range(N):
#     if i != N-1:
#         g[xs[i][1]].append([xs[i+1][0]-xs[i][0], xs[i+1][1]])
#         g[ys[i][1]].append([ys[i+1][0]-ys[i][0], ys[i+1][1]])
#         g[zs[i][1]].append([zs[i+1][0]-zs[i][0], zs[i+1][1]])
#     if i != 0:
#         g[xs[i][1]].append([xs[i][0]-xs[i-1][0], xs[i-1][1]])
#         g[ys[i][1]].append([ys[i][0]-ys[i-1][0], ys[i-1][1]])
#         g[zs[i][1]].append([zs[i][0]-zs[i-1][0], zs[i-1][1]])
# # print(g)

# ans = 0
# heap = []
# for item in g[0]:
#     heappush(heap, item)
# # print(heap)
# visited = [False]*N
# visited[0] = True

# for _ in range(N-1):
#     while heap:
#         d, v = heappop(heap)
#         if not visited[v]:
#             visited[v] = True
#             ans += d
#             for item in g[v]:
#                 heappush(heap, item)
#             break

# print(ans)


# Kruskal
# import sys
# input = sys.stdin.readline
# from heapq import heapify, heappop

# def find_parent(parent, x):
#     if x != parent[x]:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a > b :  parent[a] = b
#     else:       parent[b] = a

# def solve():
#     N = int(input())
#     xyzs = [list(map(int, input().split())) for _ in range(N)]
#     xs = sorted([[xyzs[i][0], i] for i in range(N)])
#     ys = sorted([[xyzs[i][1], i] for i in range(N)])
#     zs = sorted([[xyzs[i][2], i] for i in range(N)])

#     heap = []
#     for ts in [xs, ys, zs]:
#         heap.extend([[ts[i+1][0]-ts[i][0], ts[i][1], ts[i+1][1]] for i in range(N-1)])
#         # heap.extend([[ts[i][0]-ts[i-1][0], ts[i][1], ts[i-1][1]] for i in range(1, N)])
#     # print(heap)
#     # print(len(heap))
#     heapify(heap)
#     parent = [i for i in range(N)]

#     ans = 0
#     for _ in range(N-1):
#         while heap:
#             d, s, e = heappop(heap)
#             if find_parent(parent, s) != find_parent(parent, e):
#                 union_parent(parent, s, e)
#                 ans += d
#                 break
#     print(ans)

# solve()


# 16566 카드 게임
'''
10 7 7
1 2 3 4 5 6 7
3 4 5 6 7 8 9
[ans]
4
5
6
7
1
2
3
'''
# import sys
# input = sys.stdin.readline

# def find_parent(parent, x):
#     if x != parent[x]:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def solve():
#     N, M, K = map(int, input().split())
#     ms = sorted(list(map(int, input().split())))
#     ks = list(map(int, input().split()))

#     parent = [i for i in range(M+1)]
#     for k in ks:
#         # binary_search
#         l, r = 0, M-1
#         bi = M-1 # base index
#         if k < ms[M-1]:
#             while l <= r:
#                 mid = (l+r)//2
#                 if ms[mid] > k:
#                     bi = mid
#                     r = mid-1
#                 else:
#                     l = mid+1

#         ti = find_parent(parent, bi) # target index
#         print(ms[ti])
#         parent[ti] = parent[(ti+1)%M]
#         # print(parent)

# solve()


# 1013 Contact
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     target = list(map(int, input().rstrip()))
#     # print(target)

#     ns, len_ns = [], 0
#     pp = [-1, 0] # prev_pattern
#     for t in target:
#         ns.append(t)
#         len_ns += 1
#         if ns[0] == 1:
#             # 100...111111...
#             if pp[0] == 0:
#                 ns = []
#                 len_ns = 0
#                 pp[1] += 1
#             # 100...1
#             if len_ns >= 2 and ns[-1] == 1:
#                 # 11 / 101
#                 if len_ns < 4: break
#                 pp = [0, 0]
#                 ns = []
#                 len_ns = 0
#         # 0...
#         elif len_ns >= 2:
#             # 01
#             if ns[1] == 1:
#                 pp = [1, 0]
#                 ns = []
#                 len_ns = 0
#             # 00...1
#             else:
#                 if pp[0] == 0 and ns[-1] == 1:
#                     if pp[1] == 0: break
#                     pp = [0, 0]
#                     ns = []
#                     len_ns = 0

#     print("NO" if ns else "YES")


# 2533 사회망 서비스(SNS)
'''
14
1 2
1 3
1 4
2 5
3 6
4 7
5 8
6 9
6 10
7 11
7 12
8 13
8 14
[ans] 5
'''
# 틀린 이유 : q의 탐색 순서가 트리의 레벨 순서로 이루어 지지 않음
# 반례 찾을 수 있음

# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque

# N = int(input())
# g = defaultdict(list)
# leaf_node = [False]*(N+1)

# for _ in range(N-1):
#     u, v = map(int, input().split())
#     g[u].append(v)
#     g[v].append(u)
# # print(g)

# # leaf_node check
# visited = [False]*(N+1)
# visited[1] = True
# q = deque([1])

# while q:
#     v = q.popleft()
#     is_leaf_node = True
#     for u in g[v]:
#         if not visited[u]:
#             visited[u] = True
#             q.append(u)
#             is_leaf_node = False
#     if is_leaf_node:
#         leaf_node[v] = True
# # print(leaf_node)

# # dp : early_adaptor check
# visited = [False]*(N+1)
# leaf_nodes = [i for i in range(1, N+1) if leaf_node[i]]
# q = deque(leaf_nodes)
# for lf in leaf_nodes:
#     visited[lf] = True
# # print(visited)

# dp = [0] + [0 if leaf_node[i] else 1 for i in range(1, N+1)]
# # print(dp)

# while q:
#     v = q.popleft()
#     # parent_node
#     for u in g[v]:
#         if not visited[u]:
#             visited[u] = True
#             q.append(u)

#     # uncheck unnecessary node
#     should_be_early_adaptor = False
#     for u in g[v]:
#         if not dp[u]:
#             should_be_early_adaptor = True
#     if not should_be_early_adaptor:
#         dp[v] = 0

# # print(dp)
# print(sum(dp))


# PyPy3 메모리 초과
# Python3 273900 KB > 256 * 1024 == 262144 (KB) / 4340 ms > 3000 ms
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# sys.setrecursionlimit(int(1e6))

# def should_be_early_adaptor_check(v, g, ans, visited):
#     should_be_early_adaptor = False
#     for u in g[v]:
#         if not visited[u]:
#             visited[u] = True
#             should_be_early_adaptor |= should_be_early_adaptor_check(u, g, ans, visited)

#     if not should_be_early_adaptor:
#         ans[v] = 0

#     return not should_be_early_adaptor

# def solve():
#     N = int(input())
#     g = defaultdict(list)

#     for _ in range(N-1):
#         u, v = map(int, input().split())
#         g[u].append(v)
#         g[v].append(u)
#     # print(g)

#     ans = [0] + [1]*N
#     visited = [True, True]+[False]*(N-1)
#     should_be_early_adaptor_check(1, g, ans, visited)
#     print(sum(ans))

# solve()


# PyPy3 메모리 초과
# Python3 231524 KB < 256 * 1024 == 262144 (KB) / 4144 ms > 3000 ms
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(int(1e6))

# def should_be_early_adaptor_check(v):
#     should_be_early_adaptor = False
#     for u in g[v]:
#         if not visited[u]:
#             visited[u] = True
#             should_be_early_adaptor |= should_be_early_adaptor_check(u)
#     if not should_be_early_adaptor: ans[v] = 0
#     return not should_be_early_adaptor

# N = int(input())
# g = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     u, v = map(int, input().split())
#     g[u].append(v)
#     g[v].append(u)
# # print(g)

# ans = [0] + [1]*N
# visited = [True, True] + [False]*(N-1)
# should_be_early_adaptor_check(1)
# print(sum(ans))


# 13334 철로
# 반례 참고 : https://www.acmicpc.net/board/view/29748
'''
4
-2 2
1 0
3 0
3 -1
4
[ans] 3
'''
# 22 퍼 틀렸습니다.. 다시 보니 보완이 필요한 코드
# import sys
# input = sys.stdin.readline
# from heapq import heappush, heappop

# n = int(input())
# lines = [sorted(list(map(int, input().split()))) for _ in range(n)]
# d = int(input())
# lines = sorted([line for line in lines if (line[1]-line[0]) <= d], key=lambda x:(x[0], x[1]))
# # print(lines)
# n = len(lines)

# xs = sorted(set([line[0] for line in lines]))
# x_idx, line_idx = 0, 0
# max_cnt, cnt = 0, 0
# now_heap, wait_heap = [], []

# while line_idx < n:
#     line = lines[line_idx]
#     s, e = xs[x_idx], xs[x_idx]+d
#     while now_heap and now_heap[0][0] < s:
#         heappop(now_heap)
#         cnt -= 1
#     while wait_heap and wait_heap[0][0] <= e:
#         heappush(now_heap, heappop(wait_heap)[::-1])
#         cnt += 1

#     # start is overlapped
#     if line[0] < e: #
#         line_idx += 1
#         # fully overlapped
#         if line[1] <= e:
#             heappush(now_heap, line)
#             cnt += 1
#             max_cnt = max(max_cnt, cnt)
#         # 범위를 벗어나는 경우
#         else:
#             heappush(wait_heap, line[::-1])
#     else:
#         x_idx += 1

# print(now_heap, wait_heap)
# max_cnt = max(max_cnt, len(now_heap))
# print(max_cnt)


# revise - code with 2 heapq
# 참고 반례 : https://www.acmicpc.net/board/view/117691
# import sys
# input = sys.stdin.readline
# from heapq import heappush, heappop

# n = int(input())
# lines = [sorted(list(map(int, input().split()))) for _ in range(n)]
# d = int(input())
# lines = sorted([line for line in lines if (line[1]-line[0]) <= d], key=lambda x:(x[0]))
# # print(lines)
# n = len(lines)

# xs = sorted(set([line[0] for line in lines]))
# line_idx = 0
# max_cnt, cnt = 0, 0
# now_heap, wait_heap = [], []

# for x in xs:
#     s, e = x, x+d
#     while now_heap and now_heap[0][0] < s:
#         heappop(now_heap)
#         cnt -= 1
#     while wait_heap and wait_heap[0][0] <= e:
#         heappush(now_heap, heappop(wait_heap)[::-1])
#         cnt += 1

#     while line_idx < n:
#         line = lines[line_idx]
#         if line[0] >= e: break
#         # fully overlapped
#         if line[1] <= e:
#             heappush(now_heap, line)
#             cnt += 1
#         # partially overlapped
#         else:
#             heappush(wait_heap, line[::-1])
#         line_idx += 1

#     max_cnt = max(max_cnt, cnt)

# print(max_cnt)


# revised - 1 heapq
# import sys
# input = sys.stdin.readline
# from heapq import heappush, heappop

# n = int(input())
# lines = [sorted(list(map(int, input().split()))) for _ in range(n)]
# d = int(input())
# lines = sorted([line for line in lines if (line[1]-line[0]) <= d])
# len_lines = len(lines)
# # print(lines)

# # starts
# ss = sorted(set([line[0] for line in lines]))
# len_ss = len(ss)
# line_idx = 0
# max_cnt, cnt = 0, 0
# wait_heap = []

# line_cnts = dict()
# for s, _ in lines:
#     if s not in line_cnts:
#         line_cnts[s] = 1
#     else: 
#         line_cnts[s] += 1

# s_idx = 0
# while s_idx < len_ss:
#     v = ss[s_idx]
#     s, e = v, v+d

#     if s_idx > 0:
#         cnt -= line_cnts[ss[s_idx-1]]
#     while wait_heap and wait_heap[0] <= e:
#         heappop(wait_heap)
#         cnt += 1

#     while line_idx < len_lines:
#         line = lines[line_idx]
#         if line[0] >= e: break
#         # fully overlapped
#         if line[1] <= e:
#             cnt += 1
#         # partially overlapped
#         else:
#             heappush(wait_heap, line[1])
#         line_idx += 1

#     max_cnt = max(max_cnt, cnt)
#     s_idx += 1

# print(max_cnt)


# 1092 배
# def solve():
#     N = int(input())
#     ns = sorted(list(map(int, input().split())), reverse=True)
#     M = int(input())
#     ms = sorted(list(map(int, input().split())), reverse=True)
#     moved = [False]*M
#     tot_cnt = 0

#     if ns[0] < ms[0]:
#         print(-1)
#         return

#     for time in range(1, 10001):
#         ni = 0
#         for mi in range(M):
#             if ms[mi] <= ns[ni] and not moved[mi]:
#                 moved[mi] = True
#                 ni += 1
#                 tot_cnt += 1
#                 if ni >= N:
#                     break
#         if tot_cnt == M:
#             print(time)
#             return

# solve()


# 6198 옥상 정원 꾸미기
'''
4
3
1
2
1
'''
# import sys
# input = sys.stdin.readline

# N = int(input())
# hs = [int(input()) for _ in range(N)]
# ans = [0]*N
# s = []

# for i in range(N):
#     while s and hs[s[-1]] <= hs[i]:
#         t = s.pop()
#         ans[t] = i-t-1
#     s.append(i)

# for i in range(len(s)):
#     ans[s[i]] = N-1-s[i]

# print(sum(ans))


# 15824 너 봄에는 캡사이신이 맛있단다
# N = int(input())
# ns = sorted(list(map(int, input().split())))
# mod = int(1e9)+7

# pws = [1]*N
# for i in range(1, N):
#     pws[i] = (pws[i-1]*2) % mod
# # print(pws)

# ans = 0
# for i in range(N):
#     ans = (ans + ns[i]*((pws[i]-1)-(pws[N-1-i]-1))) % mod
# print(ans)


# 1041 주사위
# def sum_alphas(ss: str, nd: list):
#     return sum(nd[s] for s in ss)

# def solve():
#     N = int(input())
#     ns = list(map(int, input().split()))

#     if N == 1:
#         print(sum(sorted(ns)[:5]))
#         return

#     nd = dict()
#     for i in range(6):
#         nd[chr(65+i)] = ns[i]

#     ans = (4*(N-2)*(N-1)+(N-2)**2)*min(ns)
#     min_val_on_two_sulfaces = 100
#     for ss in ['EA', 'AB', 'BF', 'FE', 'DE', 'DA', 'DB', 'DF', 'CE', 'CA', 'CB', 'CF']:
#         min_val_on_two_sulfaces = min(min_val_on_two_sulfaces, sum_alphas(ss, nd))

#     min_val_on_three_sulfaces = 150
#     for ss in ['DEA', 'DAB', 'DBF', 'DFE', 'CEA', 'CAB', 'CBF', 'CFE']:
#         min_val_on_three_sulfaces = min(min_val_on_three_sulfaces, sum_alphas(ss, nd))

#     ans += (4*((N-1)+(N-2)))*min_val_on_two_sulfaces + 4*min_val_on_three_sulfaces
#     print(ans)

# solve()


# 17206 준석이의 수학 문제
# T = int(input())
# ns = list(map(int, input().split()))

# for n in ns:
#     print(3*(n//3)*(1+n//3)//2 + 7*(n//7)*(1+(n//7))//2 - 21*(n//21)*(1+(n//21))//2)


# 16565 N포커
# def f(n):
#     val = 1
#     for a in range(2, n+1):
#         val *= a
#     return val

# def c(n, k):
#     val = 1
#     for a in range(n+1-k, n+1):
#         val *= a
#     return val//f(k)

# def solve():
#     N = int(input())
#     mod = int(1e4)+7

#     ans = 0
#     for i in range(1, (N//4)+1):
#         ans = (ans + ((-1)**(i+1)) * c(13,i) * c(52-4*i, N-4*i)) % mod
#     print(ans)

# solve()


# 12852 1로 만들기 2 - 오랜만에 retry
# def btr(dp, n, ans):
#     if n > 1:
#         if n % 2 == 0 and dp[n//2] == dp[n]-1: btr(dp, n//2, ans)
#         elif n % 3 == 0 and dp[n//3] == dp[n]-1: btr(dp, n//3, ans)
#         else: btr(dp, n-1, ans)

#     ans.append(n)
#     return ans

# def solve():
#     N = int(input())
#     INF = int(1e6)+1

#     dp = [INF]*(N+1)
#     dp[1] = 0
#     for i in range(2, N+1):
#         dp[i] = dp[i-1]+1
#         if i % 2 == 0: dp[i] = min(dp[i], dp[i//2]+1)
#         if i % 3 == 0: dp[i] = min(dp[i], dp[i//3]+1)
#     # print(dp)

#     print(dp[N])
#     print(*btr(dp, N, [])[::-1])

# solve()


# 1019 책 페이지
'''
99
[ans]

100
[ans]

101
[ans]
'''
# def solve():
#     N = int(input())
#     ans = [0]*10

#     if N <= 9:
#         for i in range(1, N+1):
#             ans[i] = 1
#         print(*ans)
#         return

#     for c in list(map(int, str(N))):
#         ans[c] += 1
#     # print(ans)

#     pw = len(str(N))-1
#     # print(pw)

#     cnts = [[0]*10 for _ in range(pw)]
#     for i in range(10):
#         cnts[0][i] = 1

#     for p in range(1, pw):
#         for i in range(10):
#             cnts[p][i] = cnts[p-1][i]*10 + 10**p
#             # else:
#             #     cnts[p][i] = cnts[p-1][i]*10 + 9*(10**(p-1) if p >= 2 else 0)
#     print(cnts)

#     for p in range(pw, -1, -1):
#         print("p", p)
#         val = 10**p
#         quo = N // val # 몫
#         print("N", N)
#         N %= val

#         if quo == 0: continue
#         # ans[0] += val if p != pw else 0

#         for i in range(quo):
#             ans[i] += val
#                 # ans[0] += (val//10) if p >= 2 else 0 # 1 ~ 8
#             for j in range(10):
#                 ans[j] += cnts[p-1][j] if p >= 1 else 0
#         # print("[1]", (val//10) if p >= 2 else 0)
#         # print("[2]", cnts[p-1][0] if p >= 1 else 0)

#         ans[quo] += N
#         print("now ans", ans)

#     print(ans)

# solve()