# 6001 출력하기01
# print("Hello")

# 6002 출력하기02
# print("Hello World")

# 6003 출력하기03
# print("Hello\nWorld")

# 6004 출력하기04
# print("\'Hello\'")

# 6005 출력하기05
# print("\"Hello World\"")

# 6006 출력하기06
# print("\"!@#$%^&*()\'")

# 6007 출력하기07
# print("\"C:\\Download\\\'hello\'.py\"")

# 6008 출력하기08
# print("print(\"Hello\\nWorld\")")

# 6009 문자 1개 입력받아 그대로 출력하기
# print(input())

# 6010 정수 1개 입력받아 int로 변환하여 출력하기
# print(int(input()))

# 6011 실수 1개 입력받아 변환하여 출력하기
# print(float(input()))

# 6012 정수 2개 입력받아 그대로 출력하기1
# a, b = [int(input()) for _ in range(2)]
# print("{0}\n{1}".format(a,b))

# 6013 문자 2개 입력받아 순서 바꿔 출력하기1
# a, b = [input() for _ in range(2)]
# print("{0}\n{1}".format(b, a))

# 6014 실수 1개 입력받아 3번 출력하기
# print("{0}\n".format(input()) *3)

# 6015 정수 2개 입력받아 그대로 출력하기2
# a, b = map(int, input().split())
# print("{0}\n{1}".format(a, b))

# 6016 문자 2개 입력받아 순서 바꿔 출력하기2
# a, b = input().split()
# print(b, a)

# 6017  문장 1개 입력받아 3번 출력하기
# temp_str = input()
# print(temp_str, temp_str, temp_str)

# 6018 시간 입력받아 그대로 출력하기
# a, b = input().split(':')
# print(a, b, sep=':')

# 6019 연월일 입력받아 순서 바꿔 출력하기
# y, m, d = input().split('.')
# print("{0}-{1}-{2}".format(d, m, y))

# 6020 주민번호 입력받아 형태 바꿔 출력하기
# front_part, back_part = input().split('-')
# print("{0}{1}".format(front_part, back_part))

# 6021 단어 1개 입력받아 나누어 출력하기
# temp_str = input()
# for i in range(len(temp_str)):
#     print(temp_str[i])

# 6022 연월일 입력받아 나누어 출력하기
# temp_str = input()
# print(temp_str[0:2])
# print(temp_str[2:4])
# print(temp_str[4:])

# 6023 시분초 입력받아 분만 출력하기
# h, m, s = input().split(':')
# print(m)

# 6024 단어 2개 입력받아 이어 붙이기
# word1, word2 = input().split()
# print(word1, word2, sep='')

# 6025 정수 2개 입력받아 합 계산하기
# num1, num2 = map(int, input().split())
# print(num1 + num2)

# 6026 실수 2개 입력받아 합 계산하기
# num_list = [float(input()) for _ in range(2)]
# print(num_list[0] + num_list[1])

# 6027 10진 정수 입력받아 16진수로 출력하기1
# num = int(input())
# print("{0:x}".format(num))

# 6028 10진 정수 입력받아 16진수로 출력하기2
# num = int(input())
# print("{0:X}".format(num))

# 6029 16진 정수 입력받아 8진수로 출력하기
# num = int(input(), 16)
# print("{0:o}".format(num))

# 6030 영문자 1개 입력받아 10진수로 변환하기
# num = ord(input())
# print(num)

# 6031 정수 입력받아 유니코드 문자로 변환하기
# print(chr(int(input())))

# 6032 정수 1개 입력받아 부호 바꾸기
# print(-int(input()))

# 6033 문자 1개 입력받아 다음 문자 출력하기
# print(chr(ord(input())+1))

# 6034 정수 2개 입력받아 차 계산하기
# num1, num2 = map(int, input().split())
# print(num1 - num2)

# 6034 실수 2개 입력받아 곱 계산하기
# num1, num2 = map(float, input().split())
# print(num1 * num2)

# 6036 단어 여러 번 출력하기
# word, num = input().split()
# print(word * int(num))

# 6037 문장 여러 번 출력하기
# temp_str = [input() for _ in range(2)]
# print(int(temp_str[0]) * temp_str[1])

# 6038 정수 2개 입력받아 거듭제곱 계산하기
# num, exp = map(int, input().split())
# print(num ** exp)

# 6039 실수 2개 입력받아 거듭제곱 계산하기
# num, exp = map(float, input().split())
# print(num ** exp)

# 6040 정수 2개 입력받아 나눈 몫 계산하기
# num, div = map(int, input().split())
# print(num // div)

# 6041 정수 2개 입력받아 나눈 나머지 계산하기
# num, div = map(int, input().split())
# print(num % div)

# 6042 실수 1개 입력받아 소숫점이하 자리 변환하기
# print("{0:.2f}".format(float(input())))
# print(format(float(input()),".2f"))

# 6043 실수 2개 입력받아 나눈 결과 계산하기
# float_list = list(map(float, input().split()))
# print("{0:.3f}".format(float_list[0]/float_list[1]))

# 6044 정수 2개 입력받아 자동 계산하기
# int_list = list(map(int, input().split()))
# print(int_list[0] + int_list[1])
# print(int_list[0] - int_list[1])
# print(int_list[0] * int_list[1])
# print(int_list[0] // int_list[1])
# print(int_list[0] % int_list[1])
# print(format((int_list[0] / int_list[1]), ".2f"))

# 6045 정수 3개 입력받아 합과 평균 출력하기
# num_list = list(map(int, input().split()))
# print(sum(num_list), format(sum(num_list)/len(num_list),".2f"))

# 6046 [비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기
# print(int(input()) << 1)

# 6047 [비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기
# num, exp = map(int, input().split())
# print(num << exp)

# 6048 정수 2개 입력받아 비교하기1
# a, b = map(int, input().split())
# print(a < b)

# 6049 정수 2개 입력받아 비교하기2
# a, b = map(int, input().split())
# print(a == b)

# 6050 정수 2개 입력받아 비교하기3
# a, b = map(int, input().split())
# print(a <= b)

# 6051 정수 2개 입력받아 비교하기4
# a, b = map(int, input().split())
# print(a != b)

# 6052 정수 입력받아 참 거짓 평가하기
# print(bool(int(input())))

# 6053 참 거짓 바꾸기
# print(not(bool(int(input()))))

# 6054 둘 다 참일 경우만 참 출력하기
# a, b = map(int, input().split())
# print(bool(a) and bool(b))

# 6055 하나라도 참이면 참 출력하기
# a, b = map(int, input().split())
# print(bool(a) or bool(b))

# 6056 참/거짓이 서로 다를 때에만 참 출력하기
# c, d = map(int, input().split())
# c, d = bool(c), bool(d)
# print((c and (not d)) or ((not c) and d))

# 6057 참/거짓이 서로 같을 때에만 참 출력하기
# c, d = map(int, input().split())
# c, d = bool(c), bool(d)
# print((c and d) or ((not c) and (not d)))

# 6058 둘 다 거짓일 경우만 참 출력하기
# c, d = map(int, input().split())
# c, d = bool(c), bool(d)
# print((not c) and (not d))

# 6059 비트단위로 NOT 하여 출력하기
# print(~int(input()))

# 6060 비트단위로 AND 하여 출력하기
# a, b = map(int, input().split())
# print(a & b)

# 6061 비트단위로 OR 하여 출력하기
# a, b = map(int, input().split())
# print(a | b)

# 6062 비트단위로 XOR 하여 출력하기
# a, b = map(int, input().split())
# print(a ^ b)

# let's take a rest ...

# 6063 정수 2개 입력받아 큰 값 출력하기
# a, b = map(int, input().split())
# print(a if(a>=b) else b)

# 6064 정수 3개 입력받아 가장 작은 값 출력하기
# num_list = list(map(int, input().split()))
# print(min(num_list))

# a, b, c = map(int, input().split())
# a = (a if (a<=b) else b)
# print(a if (a<=c) else c)

# 6065 정수 3개 입력받아 짝수만 출력하기
# num_list = list(map(int, input().split()))
# for i in range(len(num_list)):
#     if num_list[i] % 2 == 0:
#         print(num_list[i])

# 6066 정수 3개 입력받아 짝/홀 출력하기
# num_list = list(map(int, input().split()))
# for i in range(len(num_list)):
#     if num_list[i] % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# 6067 정수 1개 입력받아 분류하기
# num = int(input())

# def check_even(num):
#     if (num % 2 == 0): return True
#     else: return False

# if (num < 0):
#     if check_even(num) == True: print("A")
#     else: print("B")
# else:
#     if check_even(num) == True : print("C")
#     else: print("D")

# 6068 점수 입력받아 평가 출력하기
# num = int(input())

# if(num >= 90): print("A")
# elif(num >= 70): print("B")
# elif(num >= 40): print("C")
# else: print("D")

# 6069 평가 입력받아 다르게 출력하기
# char_input = input()

# if char_input == 'A': print("best!!!")
# elif char_input == 'B': print("good!!")
# elif char_input == 'C': print("run!")
# elif char_input == 'D': print("slowly~")
# else: print("what?")

# 6070 월 입력받아 계절 출력하기
# month = int(input())
# season_check = month // 3

# if (month == 12) | (season_check == 0): print("winter")
# elif season_check == 1: print("spring")
# elif season_check == 2: print("summer")
# else: print("fall")

# 6071 0 입력될 때까지 무한 출력하기
# while True:
#     num = int(input())
#     print(num if num != 0 else quit())

# 6072 정수 1개 입력받아 카운트다운 출력하기1
# num = int(input())
# while num:
#     print(num)
#     num -= 1

# 6073 정수 1개 입력받아 카운트다운 출력하기2
# num = int(input())
# while num:
#     num -= 1
#     print(num)

# 6074 문자 1개 입력받아 알파벳 출력하기
# input_char = ord(input())
# ord_char = ord('a')
# # print(ord_char)

# while ord_char <= input_char:
#     print(chr(ord_char), end= ' ')
#     ord_char += 1

# 6075 정수 1개 입력받아 그 수까지 출력하기1
# input_num = int(input())
# index_num = 0

# while index_num <= input_num:
#     print(index_num)
#     index_num += 1

# 6076 정수 1개 입력받아 그 수까지 출력하기2
# num = int(input())
# for i in range(num + 1):
#     print(i)

# 6077 짝수 합 구하기
# num = int(input())
# sum = 0
# for i in range(1, num+1):
#     if (i%2 == 0):
#         sum += i

# print(sum)

# 6078 원하는 문자가 입력될 때까지 반복 출력하기
# while True:
#     input_char = input()
#     print(input_char)
#     if(input_char == 'q'):
#         break

# 6079 언제까지 더해야 할까?
# num = int(input())
# num_plus, sum = 0, 0
# # print(num_plus, sum)

# while True:
#     sum += num_plus

#     if(sum >= num):
#         print(num_plus)
#         break
    
#     num_plus += 1

# 6080 주사위 2개 던지기
# n, m = map(int, input().split())
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(i, j)

# 6081 16진수 구구단 출력하기
# num = int(input(), 16)
# for i in range(1, 16):
#     print("{0:X}*{1:X}={2:X}".format(num, i, num * i))

# 6082 3 6 9 게임의 왕이 되자
# num = int(input())
# for i in range(1, num+1):
#     remain = i%10
#     if(remain == 3) | (remain == 6) | (remain == 9): print('X', end=' ')
#     else: print(i, end=' ')

# 6083 빛 섞어 색 만들기
# r, g, b = map(int, input().split())
# sum = 0
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print(i, j, k)
#             sum +=1

# print(sum)

# 6084 소리 파일 저장용량 계산하기
# h, b, c, s = map(int, input().split())
# print("{0:.1f} MB" .format(h * b* c * s/8/1024/1024))

# 6085 그림 파일 저장용량 계산하기
# w, h, b = map(int, input().split())
# print("{0:.2f} MB" .format(w * h * b/8/1024/1024))

# 6086 거기까지! 이제 그만
# num = int(input())
# num_plus, sum = 0, 0

# while True:
#     sum += num_plus
#     if sum >= num:
#         break
#     num_plus += 1

# print(sum)

# 6087 3의 배수는 통과
# num = int(input())
# num_plus = 0

# while num_plus < num:
#     num_plus +=1
#     # print(num_plus if (num_plus % 3 != 0) else '\b', end=' ')
#     if(num_plus % 3 != 0):
#         print(num_plus, end= ' ')
#     else: continue

# 6088 수 나열하기1 (등차수열)
# a, d, n = map(int, input().split())
# print(a + d*(n-1))

# 6089 수 나열하기2 (등비수열)
# a, r, n = map(int, input().split())
# print(a * r ** (n-1))

# 6090 수 나열하기3 (다음 항에 대해 곱하고 더하는 혼합 형태)
# a, m, d, n = map(int, input().split())
# for i in range(n-1):
#     a = (a * m) + d
# print(a)

# 6091 함께 푸는 날 (최소 공배수)
# a, b, c = map(int, input().split())

# def gcd(a, b):
#     # if ((a % b) > 0):
#     while b > 0:
#         a, b = b, a%b
#     else:
#         return a

# def lcm(a, b):
#     return (a * b / gcd(a, b))

# print(int(lcm(lcm(a,b),c)))

# 6092 이상한 출석번호 부르기1
# num = int(input())
# num_list = [0] * 23
# attendance_list = list(map(int, input().split()))
# for i in range(len(attendance_list)):
#     num_list[attendance_list[i]-1] += 1

# for i in range(len(num_list)):
#     print(num_list[i], end=' ')

# 6093 이상한 출석번호 부르기2
# num = int(input())
# num_list = list(map(int, input().split()))
# # num_list.reverse()
# # for i in range(len(num_list)):
# for i in range(len(num_list)-1, -1, -1):
#     print(num_list[i], end=' ')

# 6094 이상한 출석번호 부르기3
# num = int(input())
# # num_list = list(map(int, input().split()))
# # print(min(num_list))
# print(min(list(map(int, input().split()))))

# 6095 바둑판에 흰 돌 놓기
# num = int(input())
# point_list = [list(map(int, input().split())) for _ in range(num)]
# # checkboard = [[0] * 19] * 19
# checkboard = [[0] * 19 for _ in range(19)]

# for i in range(len(point_list)):
#     checkboard[point_list[i][0]-1][point_list[i][1]-1] = 1

# for i in range(19):
#     for j in range(19):
#         print(checkboard[i][j], end=' ')
    
#     print()

# 6096 바둑알 십자 뒤집기
# checkboard = [list(map(int, input().split())) for _ in range(19)]
# num = int(input())
# point_list = [list(map(int, input().split())) for _ in range(num)]

# for i in range(len(point_list)):
#     for j in range(19):
#         if(checkboard[point_list[i][0]-1][j] == 0):
#             checkboard[point_list[i][0]-1][j] = 1
#         else:
#             checkboard[point_list[i][0]-1][j] = 0
#     for j in range(19):
#         if(checkboard[j][point_list[i][1]-1] == 0):
#             checkboard[j][point_list[i][1]-1] = 1
#         else:
#             checkboard[j][point_list[i][1]-1] = 0
#     # checkboard[point_list[i][0]][point_list[i][1]]

# for i in range(19):
#     for j in range(19):
#         print(checkboard[i][j], end=' ')
    
#     print()

# 6097 설탕과자 뽑기
# board_height, board_width = map(int, input().split())
# num = int(input())
# checkboard = [[0] * board_width for _ in range(board_height)]

# for i in range(num):
#     l, d, x, y = map(int, input().split())
#     if (d == 0):
#         for j in range(l):
#             checkboard[x-1][y-1+j] = 1
#     else:
#         for j in range(l):
#             checkboard[x-1+j][y-1] = 1

# for i in range(board_height):
#     for j in range(board_width):
#         print(checkboard[i][j], end=' ')
    
#     print()

# 6098 성실한 개미
# maze = [list(map(int, input().split())) for _ in range(10)]
# x, y = 1, 1     # (2, 2)
# while True:
#     # 해당 지점에 먹이가 있으면 종료
#     if(maze[x][y] == 2):
#         maze[x][y] = 9
#         break

#     # 해당 칸 도착 시 9로 변경
#     maze[x][y] = 9

#     # 우측 칸이 벽이 아닐 때 (비었을 때, 먹이가 있을 때)
#     if(maze[x][y+1] != 1):
#         y += 1

#     # 우측 칸이 벽이고 아래가 벽이 아닐 때
#     elif(maze[x][y+1] == 1) & (maze[x+1][y] != 1):
#         x += 1

#     # 우측 칸이 벽이고, 아래도 벽일 때
#     else:
#         break

# for i in range(10):
#     for j in range(10):
#         print(maze[i][j], end=' ')
#     print()

