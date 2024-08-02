import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()
    arrs = [list(map(int, a)), list(map(int, b))]
    # print(arrs)

    bases = [10, 10]
    while bases[0] <= 15000 and bases[1] <= 15000:
        vals = [0, 0]
        for i in range(2):
            for arr in arrs[i]:
                for k in range(3):
                    vals[i] += arrs[i][k]*(bases[i]**(2-k))

        if vals[0] == vals[1]:
            print(*bases)
            break
        elif vals[0] < vals[1]: bases[0] += 1
        else:                   bases[1] += 1