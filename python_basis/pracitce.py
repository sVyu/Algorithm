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

"""
### 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))