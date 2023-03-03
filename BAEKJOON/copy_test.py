# 얕은 복사 / 깊은 복사
# https://www.acmicpc.net/board/view/112363#comment-176983

def show(list_n):
    for x in range(len(list_n)):
        print(list_n[x])

    for x in range(len(list_n)):
        # 각 행(리스트)들의 id값
        print(id(list_n[x]), end='')
        # 각 행(리스트) 내 원소들의 id 값
        # print("|", *[id(list_n[x][y]) for y in range(len(list_n[x]))], end='')
        print()

nosol = [[0]*5]*5
# nosol = [[0]*5 for _ in range(5)]
show(nosol)
print()

nosol[1][1] = 10
show(nosol)

# nosol[2][3] = 20
# show(nosol)

print("\n", "a list !", sep='')
# [[0]*5 for _ in range(5)] 는 이하와 같습니다
a = []
for _ in range(5):
    a.append([0]*5)
show(a)

# a[1][1] = 10
# show(a)

##############################################################################


import copy

def show(a, b):
    print("id(a) :", id(a))
    print("id(b) :", id(b))

    print(*[id(na) for na in a])
    print(*[id(nb) for nb in b])

    print(*a)
    print(*b)
    print()

# b = a[:]
# b 리스트 자체는(객체 집합은) a와 다른 id, b의 각 원소들은 얕은 복사(같은 id)
# 원소들 중에 list, set 등의 객체 집합 X
a = [0, 1, 2]
b = a[:]
a[2] = 200
print("\n[ test1 ]")
show(a, b)

# 마찬가지로 b 리스트는 a와 다른 id, b의 각 원소들은 얕은 복사
# 원소들 중에 list, set 등의 객체 집합 O
a = [0, [1, 1], {2, 2}]
b = a[:]

# 원소 중 객체 집합이 아닌 데이터에 대해서 값을 바꿉니다
# 해당 원소를 통으로 바꾸는 것과 같음
# == 새로운 저장 공간에 값을 할당해서 id를 연결시킨 것과 같다
a[0] = 5
print("[ test2 ]")
show(a, b)

# 객체 집합 내부의 값을 바꿀 경우 a[1]과 b[1]의 id는 동일하기 때문에 출력 결과가 같음
a[1][0] = 10
# a[2].add(3)
print("[ test3 ]")
show(a, b)

# 해당 객체 집합을 통으로 바꿔주면 새로운 id가 할당되고 출력 결과가 다름
a[1] = [1, 1]
print("[ test4 ]")
show(a, b)

# 깊은 복사
# 각 객체 집합들에 대해서 다른 id 값을 가지게 해줍니다
b = copy.deepcopy(a)
a[1][0] = 20
print("[ test5 ]")
show(a, b)

# 동일한 id를 가지는 객체 집합 :)
a = [[0]*2]*2
# a = [[0]*2 for _ in range(2)]

b = a[:]
# 위 코드를 개선하여 각각의 행마다 복사하는 방법
# b = [a[x][:] for x in range(len(a))]
a[0][0] = 10
print("[ test6 ]")
show(a, b)