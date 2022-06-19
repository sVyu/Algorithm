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
# # print(num_list)

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
# 자중의 필요가 있다 !
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


# 14652
n, m, k = map(int, input().split())
print(k//m, k%m)