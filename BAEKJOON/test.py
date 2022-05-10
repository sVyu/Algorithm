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
num = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

index = 0
while True:
    for i in range(num + 1):
        if(num_list[i])