import sys
input = sys.stdin.readline

for _ in range(int(input())):
    ns = list(map(int, input().split()))
    N, ns = ns[0], ns[1:]
    # print(N, ns)

    for i in range(1, N-1):
        if (ns[i-1]+1) != ns[i]:
            print(i+1)
            break