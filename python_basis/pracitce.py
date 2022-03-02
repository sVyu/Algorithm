# 참고 (인프런)
# 나도코딩 - 파이썬 기초(6시간)
# https://inf.run/w1Bs

#################### 자료형
"""
### 숫자
print(5)
print(-10)

### 문자
print('풍선')
print(type('풍선'))
print("ㅋ"*9)   # 파이썬은 이런 게 되서 좋아 ~

### boolean
print(5 > 10)
print(5 < 10)
print(True)
print(not True) # False

### 변수
# 애완동물을 소개해 주세요 ~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
hobby = "공놀이"
is_adult = age >= 3     # 이게 돌아가는 파이썬..
print("우리집 " + animal + "의 이름은 " + name + "에요")
print(name + "는 "+ str(age) +"이며, " + hobby +"을 아주 좋아해요")
print(name, "는 어른일까요? " + str(is_adult))
# name, 처럼 사용 시 name 뒤에 자동으로 빈 칸이 들어감

### Quiz 1
# 변수를 이용하여 다음 문장을 출력하시오
# 변수명 : station
# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력
# 출력 문장 : XX 행 열차가 들어오고 있습니다.

station = "사당"
print(station+"행 열차가 들어오고 있습니다.")

station = "신도림"
print(station+"행 열차가 들어오고 있습니다.")

station = "인천공항"
print(station+"행 열차가 들어오고 있습니다.")
"""

#################### 연산자
"""
### 연산자
print(1+1)
print(6/3)

print(2**3) # 2^3 == 8
print(5 % 3) # 2 (나머지)
print(5//3) # 1 (몫)

print(10 > 3)   # True
print(3==3)     # True
print(1 != 3)   # True
print(not(1 != 3)) # False
print(".")

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

### 간단한 수식
number = 2 + 3 * 4
print(number)   # 14
number += 2     # 16
print(number)

### 숫자처리함수
print(abs(-5))  # 5
print(pow(4, 2)) # 4^2 = 4*4 == 16
print(max(5,12)) # 12
print(min(5,12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99))  # 4, 내림
print(ceil(3.14))   # 4, 올림
print(sqrt(17))     # 4.123..., 제곱근

### 랜덤함수
from random import *
print(random())     # 0.0 이상 1.0 미만의 임의의 값
print(random() * 10)  # 0.0 이상 10.0 미만
print(int(random() * 10))   # 0 이상 10 미만 자연수
print(int(random() * 10))   # 0 이상 10 미만 자연수
print(int(random() * 10))   # 0 이상 10 미만 자연수

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # randint는 endpoint도 포함

### Quiz2
# 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다
# 월 4회 스터디를 하는데 3번은 온라인, 1번은 오프라인
# 아래 조건에 맞는 오프라인 모임 날짜를 정하는 프로그램 작성

# 조건 1 : 랜덤으로 날짜를 뽑아야 함
# 조건 2 : 월별 날짜는 다름을 최소 일수 28 이내로 정함
# 조건 3 : 매월 1 ~ 3일은 제외

# 출력문 예시
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

from random import * 
day = randrange(4, 29)
#day = randint(4, 28)

print("오프라인 스터디 모임 날짜는 매월 " + str(day) + "일로 설정되었습니다")

"""

#################### 문자열 처리
"""
### 문자열
sentence = '나는 청년입니다'
print(sentence)
sentence2 = '파이썬은 쉬워요'
print(sentence2)
sentence3 = '''
나는 청년이고,
파이썬은 쉬워요
'''
print(sentence3)

### 슬라이싱
jumin = "960123-1234567"
print("성별 : " + jumin[7])
print("생년 : " + jumin[0:2]) # 0부터 2 전까지 (0, 1)
print("생월 : " + jumin[2:4])
print("생일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:])

print("뒤 7자리(뒤에부터) : " + jumin[-7:])

### 문자열처리함수
string1 = "Python is Amazing"
print(string1.lower())
print(string1.upper())
print(string1[0].isupper()) # P → True
print(string1[1].isupper()) # y → False
print(len(string1)) # 문자열 길이 == 17
print(string1.replace("Python", "Java"))

index = string1.index("n") # 5
print(index)
index = string1.index("n", index + 1) # 6부터
print(index)               # 15

print(string1.find("n"))
print(string1.find("Java"))
# print(string1.index("Java"))

# find도 index도 문자를 찾아주지만
# find는 없으면 -1, index는 없으면 error

print(string1.count("n")) # n이 몇 번 등장하는지

### 문자열포맷

# print("a" + "b")
# print("a", "b")

# # 방법 1
# print("나는 %d살입니다." %27)
# print("나는 %s을 좋아해요." %"파이썬")
# print("Apple 은 %c로 시작해요." % "A")
# print("나는 %s색과 %s색을 좋아해요.\n" %("주황", "파란"))

# # 방법2
# print("나는 {}살입니다." .format(27))
# print("나는 {}색과 {}색을 좋아해요" .format("주황", "파란"))
# print("나는 {0}색과 {1}색을 좋아해요" .format("주황", "파란"))
# print("나는 {1}색과 {0}색을 좋아해요" .format("주황", "파란"))

# 방법3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 27, color = "주황"))
print("나는 {age}살이며, {color}색을 좋아해요" .format(color = "주황", age = 27))

# 방법 4 (v3.6 이상~)
age = 27
color = "주황"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

### 탈출문자

# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")
# 저는 'YBH'입니다
print("저는 \"YBH\"입니다.")
# \\ : 문장 내에서 \
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")    # PineApple

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : tab
print("Red\tApple")

### Quiz3
# 사이트별로 비밀번호를 만들어 주는 프로그램 작성

# ex ) http://naver.com
# 규칙1 : http:// 부분은 제외 → naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 → naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 개수 + "!"로 구성
#                       (nav)         (5)           (1)          (!)

# ex) 생성된 비밀번호 : nav51!

domain_example = "http://naver.com"
# domain_example = "http://daum.net"
# my_str = domain_example.replace("http://", "") # 이렇게도 가능

index_dot = domain_example.find(".")
domain_name = domain_example[7:index_dot]
# my_str = mystr[:my_str.index(".")]    # 이렇게도 가능
# print(domain_name)    # daum

password = domain_name[:3] + str(len(domain_name))+ str(domain_name.count("e")) + "!"
print(f"{domain_example}의 비밀번호는 {password}입니다")
"""


# 2022/02/28 try
# point : no check, it's count
"""
url_temp = "http://naver.com"
url_temp = url_temp.replace("http://","")

string_temp = url_temp[:url_temp.index(".")]
string_output = string_temp[:3] + str(len(string_temp)) + str(string_temp.count("e")) +'!'
print(string_output)
"""


### Quiz3
# 사이트별로 비밀번호를 만들어 주는 프로그램 작성

# ex ) http://naver.com
# 규칙1 : http:// 부분은 제외 → naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 → naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 개수 + "!"로 구성
#                       (nav)         (5)           (1)          (!)

# ex) 생성된 비밀번호 : nav51!


#################### 자료구조
### 리스트 []
"""
# 지하철 칸별로 10명, 20명, 30명
subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸인지
# index
print(subway.index("조세호"))

# 하하씨가 다음 정류장에 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.append(2.2)
num_list.sort()
print(num_list)

# 다양한 자료형 함께 사용 가능 !
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

### 사전(dictionary..인데 명령어는 cabinet)
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# index range 벗어나는 경우
# print(cabinet[5]) # 오류나고 프로그램 종료
print(cabinet.get(5)) # None 출력
print(cabinet.get(5,"사용 가능")) # 이런 식으로도 사용 가능

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)

### 튜플
# 내용 변경이나 추가를 할 수 없는데 속도가 리스트보다 빠르다
# 변경되지 않는 경우, 튜플 사용이 유리

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
# menu.add("생선까스") # error

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
print(name)

### 집합(set)
# 중복 안 됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 까먹음
java.remove("김태호")
print(java)

### 자료구조의 변경
# ex) 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# Quiz) 당신의 학교에서 파이썽 코딩 대회를 주최합니다
# 참석률을 높이기 위해 댓글 이벤트를 진행
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰
# 추천 프로그램을 작성 ~

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample 활용

# 출력 예제
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --

# 활용 예제
# from random import *
# lst = [1,2,3,4,5]
# print(lst)

# shuffle(lst)
# print(lst)
# print(sample(lst, 1)) #lst에서 1개만큼 뽑음

# Do it !!
# my solution
# from random import *
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(type(lst))

# shuffle(lst)
# print(lst)

# # 치킨 1명
# # print(sample(lst, 1))
# winner_chicken = sample(lst, 1)
# print(winner_chicken)

# lst_set = set(lst)
# # print(lst_set)

# lst_set = lst_set.difference(set(winner_chicken))
# # print(lst_set)
# lst = list(lst_set)

# # 이거 아니야 ~
# # lst.reverse()
# # lst.pop()
# # lst.reverse()

# # 커피 쿠폰 3명
# # print(sample(lst, 3))
# winner_coffee = sample(lst, 3)

# print(f'''
# -- 당첨자 발표 --
# 치킨 당첨자 : {winner_chicken}
# 커피 당첨자 : {winner_coffee}
# -- 축하합니다 --
# ''')

# 풀이
from random import *
users = range(1, 21) # 1부터 20까지 생성  # type : <class 'range'>
users = list(users)

# print(users)
shuffle(users)
# print(users)

winners = sample(users, 4) # 1명 치킨 + 3명 커피

print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")

# Quiz) 당신의 학교에서 파이썽 코딩 대회를 주최합니다
# 참석률을 높이기 위해 댓글 이벤트를 진행
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰
# 추천 프로그램을 작성 ~

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample 활용

# day2
from random import *
lst = range(1,21)
lst = list(lst)

shuffle(lst)
# print(lst)

lst_winner = sample(lst,4)
print(lst_winner)

print(f'''
-- 당첨자 발표 --
치킨 당첨자 : {lst_winner[0]}
커피 당첨자 : {lst_winner[1:]}
-- 축하합니다 -- 
''')

"""
# Quiz) 당신의 학교에서 파이썽 코딩 대회를 주최합니다
# 참석률을 높이기 위해 댓글 이벤트를 진행
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰
# 추천 프로그램을 작성 ~

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample 활용


#################### 제어문
"""
### if

# weather = '맑아요'
# weather = input("오늘 날씨는 어때요? ")
# if weather == '비' or weather == '눈':
#     print("우산을 챙기세요")
# elif weather == '미세먼지':
#     print('마스크를 챙기세요')
# else:
#     print('준비물 필요 없어요')

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp <30:
#     print("괜찮은 날씨예요")
# elif 0 <= temp <10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")


# for

# for waiting_no in [0,1,2,3,4]:
# for waiting_no in range(5):   # 0 ~ 4
# for waiting_no in range(1,6): # 1 ~ 5
    # print("대기번호 : {0}" .format(waiting_no))

# starbucks = ["아이언맨","토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다." .format(customer))


# while

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요".format(customer,index))
#     index -= 1
#     if index ==0:
#         print("커피는 폐기처분되었습니다.")

# (roop)
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출{1}회" .format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"
# while person != customer :
#     print("{0}, 커피가 준비 되었습니다." .format(customer))
#     person = input("이름이 어떻게 되세요? ")

# continue와 break
# absent = [2, 5] # 결석
# no_book = [7] # 책을 깜빡했음
# for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10,11
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와" .format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))


# 한 줄 for
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 → 101, 102, 103, 104.
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# my code
# students = ["Iron man", "Thor", "I am groot"]
# len_name = [len(name_of_students) for name_of_students in students]
# print(len_name)

# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# 모두 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

"""

# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성

# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분

# my_code
# from random import *
# total_passenger = 0
# list_passenger = []
# for i in range(1,51):   # no 50, it's 51
#     drival_time = int(5 + random()*45)  # randrange(5, 51)
#     # print(drival_time)

#     if drival_time <= 15:   # 어차피 최소 시간이 5분이라 15분 이하인 조건만
#         check = "O"
#         total_passenger += 1
#         list_passenger.append(i)
#     else:
#         check = " "
#     print('[{0}] {1}번째 손님 (소요시간 : {2}분)'.format(check, i, drival_time))
# print("총 탑승 승객 : {0} 분".format(total_passenger))
# print(list_passenger)


# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성

# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분


#################### 함수
"""
### 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")
# open_account()

### 전달값과 반환값
def deposit(balance, money):    #입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다." .format(balance + money))
    return balance + money

def withdraw(balance, money):   #출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다." .format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다." .format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금
    commission = 100    # 수수료 100원
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1500)
print(balance)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다." .format(commission, balance))


### 기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교, 같은 학년, 같으 반, 같은 수업일 경우
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))
profile("유재석")
profile("김태호")


### 키워드값

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age =20)
# profile(main_lang="자바", age=25, name="김태호")


### 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이 : {1}\t" .format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")

# 이거 많이 유용할 듯
def profile(name, age, *language):
    print("이름: {0}\t나이 : {1}\t" .format(name, age), end=" ")
    for lang in language:
        print(lang, end= " ")
    print() #줄바꿈

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")


### 지역변수와 전역변수
gun = 10
def checkpoint(soldiers):   # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    # 일반적으로는 전역 변수를 많이 쓰면 코드 관리에 어려우니
    # 파라미터로 전달해서 사용하는 방식을 권장
    gun -= soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))

def checkpoint_ret(gun, soldiers):
    gun -=soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}" .format(gun))
# checkpoint(2)   # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}" .format(gun))

"""

### Quiz) 표준 체중을 구하는 프로그램을 작성하시오
# 표준 체중 : 각 개인의 키에 적당한 체중

# 성별에 따른 공식
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계싼
#       * 함수명 : std_weight
#       * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘때자리까지 표시

# 출력 예제
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if(gender=='male'):
        bmi_weight = 22
    elif(gender=='female'):
        bmi_weight = 21

    height_m = height/100

    return height_m * height_m * bmi_weight

sample_man_height = 175
gender = "male"
print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다."\
    .format(sample_man_height, round(std_weight(sample_man_height, 'male'),2) ))

# 반올림은 round 함수