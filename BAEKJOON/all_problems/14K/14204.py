import sys
input = sys.stdin.readline

def cal_idxs(zs, m):
    new_zs = [[i, zs[i]] for i in range(m)]
    new_zs.sort(key=lambda x:(x[1]))
    # print(new_zs)

    idxs = [new_zs[i][0] for i in range(m)]
    return idxs

def is_valid_row(zs, m):
    appeared = [False]*m
    quo = (zs[0]-1)//m

    for z in zs:
        if((quo != ((z-1)//m)) or (appeared[z%m])):
            return False
        appeared[z%m] = True
    return True

def solve():
    n, m = map(int, input().split())
    if(n == 1):
        print(1)
        return

    zs = list(map(int, input().split()))
    idxs = cal_idxs(zs, m)
    if(not is_valid_row(zs, m)):
        print(0)
        return
    # print(idxs)

    for _ in range(n-1):
        zs = list(map(int, input().split()))
        new_idxs = cal_idxs(zs, m)
        if(idxs != new_idxs):
            print(0)
            return
        if(not is_valid_row(zs, m)):
            print(0)
            return

    print(1)

solve()