import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())

    # if K == 0:
    #     print((N+1)//2)
    #     continue

    divider = 1
    for _ in range(K):
        divider *= 2
        if divider > N:
            break

    # 2**K가 N보다 큰 경우
    # if divider > N:
    #     print(0)
    #     continue

    cnt = N//divider
    print(cnt - N//(divider*2))