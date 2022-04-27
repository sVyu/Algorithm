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
