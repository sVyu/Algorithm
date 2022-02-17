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

# find도 indeex도 문자를 찾아주지만
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

### Quiz3
# 사이트별로 비밀번호를 만들어 주는 프로그램 작성

# ex ) http://naver.com
# 규칙1 : http:// 부분은 제외 → naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 → naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 개수 + "!"로 구성
#                       (nav)         (5)           (1)          (!)

# ex) 생성된 비밀번호 : nav51!
