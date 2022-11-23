<br>
<hr>

# 코딩테스트를 위한 파이썬 tip 정리
<br>

# 입력 받기
파이썬의 경우, input() 으로 쉽게 입력받을 수 있음
```python
line = input()
```
여기서 만약 받아야하는 `lines의 수가 많은 경우` (ex 1000 줄 이상)  
다음과 같이 sys 모듈을 import해서 `직접적으로 readline 함수를 사용`하는 것이 시간 효율에서 유리하다
```python
import sys
input = sys.stdin.readline

N = int(input())    # N : input line의 수
for _ in range(N):
    line = input().rstrip()
```
readline을 활용할 경우, 개행문자까지 받기때문에 `rstrip()은 개행문자 처리`를 위해 필요하다  
int(input())의 경우 int()함수가 자동으로 처리해서 문제가 없다  
또한 파이썬은 웬만한 경우에 대해서 one-line 변수 선언 및 초기화가 가능하다
```python
a, b = map(int, input().split())
# input : 1 2
# a : 1, b : 2
```
```python
list_a = list(map(int, input().split()))
# input : 1 2 3
# list_a : [1, 2, 3]
```
```python
list_b = [i for i in range(5)]
# list_b : [0, 1, 2, 3, 4]
```
```python
list_c = [list(map(int, input().split())) for _ in range(3)]

# input
1 2 3
4 5 6
7 8 9

# list_c : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

위의 list_c와 같은 2차원 list의 경우,  
아래와 같이 활용하면 초기화가 제대로 됐는지 수월하게 파악이 가능하다
```python
for x in range(3):
    print(list_c[x])
    
# output:
1 2 3
4 5 6
7 8 9
```
input()을 쓰지 않는 2차원 list 초기화의 경우
```python
list_d = [[ 0 ] * m for _ in range(n)]
```
와 같은 형태로 진행한다 (리스트 컴프리헨션)
```python
list_e = [[0] * m] * n
```
`절대 list_e와 같이 초기화하지 않도록 주의!`  
이렇게 하면 레퍼런스를 공유하는 초기화 방법이기 때문에  
값을 변경했을 때 여러 인덱스의 원소가 동시에 바뀐다

<br>

가끔 특별한 종료조건이 없이 파일의 끝까지 입력을 받아서 처리하는 경우가 있는데  
이 경우 크게 2가지 방법이 있다
> 1번째 방법
>```python
>import sys
>lines = sys.stdin.readlines
>for line in lines:
>    print(line)
>```
> readline`s`로 한 번에 입력 받고 각 line 별로 처리하는 접근

> 2번째 방법
>```python
>import sys
>input = sys.stdin.readline
>
>while True:
>    try:
>        line = input()
>    # except:
>    except EOFError:
>         break
>```
> 이와 같이 EOFError에 대해 try-except로 처리하는 방법이 있다

<br>

# 몫, 나머지 연산
몫, 나머지 연산도 가능하다
```python
n = 100 // 9
print(n)

# output : 11
```
```python
n = 100
n //= 9
print(n)

# output : 11
```
```python
n = 100 % 9
print(n)

# output : 1
```
`n //= 9` 와 같은 형태로 사용 가능함

<br>

# for문 - range() 함수
```python
for i in range(3):
    print(i, end = ' ')

# output : 1 2 3
```
```python
for i in range(3, 10):
    print(i, end = ' ')

# output : 3 4 5 6 7 8 9
```
```python
for i in range(3, 10, 2):
    print(i, end = ' ')

# output : 3 5 7 9
```
[docs 참고][ref_docs_range]  
for _ in `range(a, b)에서 b는 포함이 안 된다`는 거 꼭 기억!
list 슬라이스의 경우도 `list_n[a:b]에서 b가 포함 안 됨`  
딱 b 바로 전 인덱스까지만 접근

<br>

# 역순에 대해 sort로 접근
```python
a = [1, 2, 3]
a.sort(reverse=True)
print(a)

# output : [3, 2, 1]
```

```python
a = [1, 2, 3]
a = sorted(a, reverse=True)
print(a)

# output : [3, 2, 1]
```

[ `주의`! ]
> sorted의 경우 꼭 받는 변수를 지정해야 한다
> ```python
> a = [1, 2, 3]
> sorted(a, reverse=True)
> print(a)
>
> # output : [1, 2, 3]
> ```
> 위 경우 a에 대한 갱신이 이루어지지 않았음

> sort의 경우 아래와 같은 one-line 접근은 안 된다  
> ```python
> a = [3, 2, 1].sort()  
> print(a)
>
> # output : None
> ```

> 아래와 같은 접근은 가능하다
> ```python
> a = sorted([1, 2, 3], reverse=True)
> print(a)
>
> # output : [3, 2, 1]
> ```
개인적으로 sorted를 애용 중
<br><br>

# 역순을 sort 없이 [::-1]로 접근 가능
```python
a = [1, 2, 3]
print(a[::-1])

# output : [3, 2, 1]
```
<br>

# in, not in
list, dict, set 등에서 사용 가능한 함수  
특히 그래프에서 해당 지점을 갔는지 안 갔는지 좌표를 set에 저장하고 확인할 때 굉장히 유용
```python
a = list([1, 2, 3])
print("O" if 1 in a else "X")

# output : O
```

```python
a = dict()
a[0] = "zero!"

for i in range(2): # 0, 1
    if i in a:
        print(a[i])
    else:
        print(f'there_isn\'t {i}')

# output:
zero!
there_isn't 1
```

```python
a = set()
a.add(1)

for i in range(2): # 0, 1
    if i in a:
        print(i)
    else:
        print(f'there_isn\'t {i}')
# output:
there_isn't 0
1
```
<br>

# 출력 format
```python
a = 77
print(f'num is {a}')
print('num is {0}'.format(a))
print('num is', a)
print('num is',\
       a)

# output :
num is 77
num is 77
num is 77
num is 77
```
[코드 한 줄을 여러 줄에 걸쳐서][ref_multi_line_code]
<br><br>

# print(*a), print(''.join(a)), sep, end
```python
a = [1, 2, 3, 4, 5]
print(*a)

# output : 1 2 3 4 5
```
```python
a = ["h", "i", "_", "h","e","l","l","o","!"]
print(''.join(a))
print(' '.join(a))

# output :
hi_hello!
h i _ h e l l o !
```
```python
a = [1, 2, 3, 4]
print(*a, sep = '_')

# output : 1_2_3_4
```
```python
a = [1, 2, 3, 4]
print(*a, end = '_')

# output : 1 2 3 4_
```
<br>

# 리스트를 대입한 변수를 다시 다른 변수에 대입한 경우
`동일한 레퍼런스를 참조하게 되므로 주의`
```python
b = [1, 2, 3]
a = b

a[0] = 0
print(b)

# expectation  : [1, 2, 3]
# output       : [0, 2, 3]
```
다음과 같은 방법으로 해결할 수 있다
```python
a = b.copy()
a = b[::] # 이 방법을 권장
```
<br>

# 리스트 이어붙이기
```python
a = [1, 2, 3]
b = [4, 5, 6]
```
위와 같이 a, b가 정의되어 있을 때 이하의 방법으로 적용 가능
```python
for n in b:
    a.append(n)
print(a)

# output : [1, 2, 3, 4, 5, 6]
```
```python
a.extend(b)
print(a)

# output : [1, 2, 3, 4, 5, 6]
```
<br>

# dict와 defaultdict의 차이
`[ 기본적으로 dict 대신 defaultdict 사용 권장 ]`
```python
a = dict()
a[0] = 1

for i in range(2):
    a[i] += 1

print(a)

# output : KeyError: 1
```
a[1]이 없어서 Error가 발생

```python
from collections import defaultdict
a = defaultdict(int)

for i in range(2):
    a[i] += 1

print(a)

# output : defaultdict(<class 'int'>, {0: 1, 1: 1})
```
defaultdict() 괄호 안에 어떤 변수형인지 지정해놓으면  
접근할 원소가 없을 때 `int의 경우 0, list의 경우 빈 list를 자동으로 할당`
<br><br>

# sum 함수
```python
a = 1, 2, 3
print(sum(a))

# output : 6
```
다음과 같이 sum과 같은 특정 함수의 이름을 변수로 지정하지 않기 (의외로 실수하는 부분)
```python
sum = [1,2,3]
print(sum(sum))

# output :
TypeError: 'list' object is not callable
```
<br>

# 알파벳에 대해 인덱스 관점으로 접근해야 할 때
ord, chr, import string - string.ascii-uppercase/lowercase
```python
alpha = ord('A')
print(alpha)

# output : 65
```
```python
alpha = chr(65)
print(alpha)

# output : A
```
```python
import string

upper_case = list(string.ascii_uppercase)[:7]
print(upper_case)

# output : ['A', 'B', 'C', 'D', 'E', 'F', 'G']
```

<br>

# 리스트 (스택처럼 사용 가능 ex. pop())
```python
a = [1, 2, 3]
a.pop()
a.append(4)
print(a)

# output : [1, 2, 4]
```

# PriorityQueue, deque(덱)
```python
from queue import PriorityQueue

pq = PriorityQueue()
pq.put(3)
pq.put(2)
pq.put(4)
print(pq.get())

# output : 2
```
```python
from queue import PriorityQueue

pq = PriorityQueue()
pq.put([3, 4, 4])
pq.put([2, 3, 3])
pq.put([4, 2, 2])

print(pq.get())
print(pq.queue)
n, a, b = pq.get()
print(n, a, b)

# output :
[2, 3, 3]
[[3, 4, 4], [4, 2, 2]]
3 4 4
```
[PriorityQue][ref_priority_que] 참고 링크

```python
from collections import deque

que = deque()
que.appendleft(2)
que.appendleft(1)
que.append(3)

print(que)
print(que.pop())
print(que.popleft())

# output:
deque([1, 2, 3])
3
1
```
deque(덱)의 경우 왼쪽, 오른쪽 양방향으로 접근이 가능
<br><br>

# 최대공약수, 최소공배수, math 함수
```python
# 유클리드 호제법

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def lcd(a, b):
    return a * b // gcd(a, b)

a, b = 10, 35
print(gcd(a,b), lcd(a,b))

# output : 5 70
```
[math 모듈을 활용한 최대공약수, 최소공배수][ref_math] 계산도 가능하다 !
<br><br>

# 이분탐색
```python
bot, top = 0, 100
n = 55

cnt = 0
while bot <= top:
    mid = (bot + top)//2
    cnt += 1

    if mid > n:
        top = mid - 1
    elif mid < n:
        bot = mid + 1
    else: # mid == n
        print("탐색 횟수 : ", cnt)
        break
    
# output :
탐색 횟수 :  7
```
이분탐색의 경우, 백준의 [나무자르기][boj_2805] 문제를 풀 줄 알면 일단은 충분하다고 생각
<br><br>

# itertools - permutations, combinations
```python
# a = [1, 2, 3]
a = [i for i in range(1, 4)]
```

```python
for i in itertools.combinations(a, 2):
    print(i)

# output :
(1, 2)
(1, 3)
(2, 3)
```
```python
# 중복 허용
for i in itertools.combinations_with_replacement(a, 2):
    print(i)

# output:
(1, 1)
(1, 2)
(1, 3)
(2, 2)
(2, 3)
(3, 3)
```
```python
for i in itertools.permutations(a, 2):
    print(i)

# output:
(1, 2)
(1, 3)
(2, 1)
(2, 3)
(3, 1)
(3, 2)
```
<br>

# 그리드
탐욕적인 접근!  
그리드 활용 문제임을 캐치할 수만 있으면 비교적 쉽게 풀 수 있음  
당장 앞에 있는 거에 대해서 최대한 많이 가져간다는 접근
<br><br>

# 그래프
기본적으로 이하와 같은 모듈이 기본적으로 들어감
```python
import sys
input = sys.stdin.readline
from collections import defaultdict
# from collections import deque #BFS
```

그래프가 넓은 경우 시간초과 방지를 위해 꼭 set으로 좌표를 확인할 것  
안 그러면 시뮬레이션에서 루프에 빠진 경우를 볼 수 있음
```python
xy_set = set()
```
<br>

# dp
- dynamic programming  
`[tip] input 크기가 10만 대면 dp일 수 있다 !`  
dp 문제는 해당 문제에 맞춰서 식을 정리하는 게 오래 걸리고 풀고 나면 코드 자체는 얼마 안 되는 경우가 많다  
점화식을 세운다는 접근이 바람직하다고 생각한다
<br><br>

# Python3보다 PyPy3가 더 빠를 때가 있음
로직은 괜찮은 것 같은데 시간 초과가 날 경우, 한 번 활용해볼 여지가 있음
<br><br>

# 에러가 났을 때
- 에러 문구로 구글링
- 구간 별로 print( ) 찍어서 디버깅
<br><br>

### 2022/11/23 작성 완료

[ref_docs_range]: https://docs.python.org/ko/3/tutorial/controlflow.html#the-range-function
[ref_multi_line_code]: https://hashcode.co.kr/questions/281/%EC%BD%94%EB%93%9C-%ED%95%9C-%EC%A4%84%EC%9D%84-%EC%97%AC%EB%9F%AC-%EC%A4%84%EB%A1%9C-%EB%82%98%EB%88%A0-%EC%93%B0%EA%B8%B0
[ref_priority_que]: https://www.daleseo.com/python-priority-queue/
[ref_math]: https://blockdmask.tistory.com/525
[boj_2805]: https://www.acmicpc.net/problem/2805