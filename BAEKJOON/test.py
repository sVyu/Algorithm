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
# how solve is this
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
# num = int(input())

# cannon_balls_list = [0]*200
# for i in range(1, 200):
#     cannon_balls_list[i] = i*(i+1)*(i+2)//6
# cannon_balls_list[0], cannon_balls_idx = 1, 1
# # print(cannon_balls_list)

# dp_list = [0] * (num+1)
# for i in range(num+1):
#     dp_list[i] = i
# # print(dp_list)

# for i in range(1, num+1):
#     while cannon_balls_idx < 199:
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
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    num_list = [list(map(int, input().split())) for _ in range(n)]
    dp_list = [[0] * (n+1) for _ in range(n+1)]
    
    for x in range(1, n+1):
        sum_of_num = 0
        for y in range(1, n+1):
            sum_of_num += num_list[x-1][y-1]
            dp_list[x][y] = sum_of_num + dp_list[x-1][y]
    # for y in range(n+1):
    #     print(dp_list[y])

    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        ans = dp_list[x2][y2] - dp_list[x2][y1-1] - dp_list[x1-1][y2] + dp_list[x1-1][y1-1]
        print(ans)

solve()