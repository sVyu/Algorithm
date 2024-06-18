'''
왜 WA지..
'''

def solve():
    N, M, K = map(int, input().split())
    orders = list(map(int, input().split()))
    orders_idx = M-1
    # print(orders)

    arr = [0]*(N+1)
    fixed = [False]*(N+1)
    for i in range(K):
        c, idx = map(int, input().split())
        if c == 1:
            print(idx)
            return

        arr[idx] = c
        fixed[c] = True
    # print(arr)
    # print(fixed)

    for i in range(N, 0, -1):
        if orders_idx >= 0:
            if arr[i] != 0:
                num = orders[orders_idx]
                # 고정인 숫자면
                if arr[i] == num: # 
                    orders_idx -= 1
            else:
                # 현재 order의 숫자가 고정이 아니면 값 넣어주고 고정인 경우 continue
                if not fixed[num]:
                    arr[i] = num
                    orders_idx -= 1
        else:
            break
    # print(arr)
    # print(fixed)

    for target in [1, 0]:
        for i in range(1, N+1):
            if arr[i] == target:
                print(i)
                return

solve()

'''
6 3 2
2 4 5
1 6
6 1
'''
'''
6 2 2
2 4
5 5
6 1
'''
'''
6 5 1
2 3 4 5 6
3 2
'''
'''
6 6 1
1 2 3 4 5 6
3 3
'''
'''
6 3 2
5 3 6
6 5
5 1
'''
'''
4 3 1
2 3 1
3 2
[ans] 3
'''
# 이거 바꾸면 될 것 같은데
'''
7 2 2
2 1 3
2 5
3 7
[ans] 6
'''