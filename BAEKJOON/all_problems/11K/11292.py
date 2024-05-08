import sys
input = sys.stdin.readline

n = int(input())
while n>0:
    infos = [input().rstrip().split() for _ in range(n)]
    max_h = max(infos[i][1] for i in range(n))

    for name, h in infos:
        if h == max_h:
            print(name, end=' ')
    print()

    n = int(input())