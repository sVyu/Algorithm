import sys
input = sys.stdin.readline

mod = int(1e9)+7

def matrix_multi(N, mat_a, mat_b):
    new_mat = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for k in range(N):
                new_mat[x][y] = (new_mat[x][y]+mat_a[x][k]*mat_b[k][y]) % mod
    return new_mat

def matrix_divide_and_conquer(cnt, N, mat):
    if cnt == 0:
        base_mat = [[0]*N for _ in range(N)]
        for n in range(N):
            base_mat[n][n] = 1
        return base_mat
    elif cnt == 1:
        return mat
    elif(cnt%2 == 0):
        half_powered_mat = matrix_divide_and_conquer(cnt//2, N, mat)
        return matrix_multi(N, half_powered_mat, half_powered_mat)
    else:
        half_powered_mat = matrix_divide_and_conquer(cnt//2, N, mat)
        return matrix_multi(N, half_powered_mat, matrix_multi(N, half_powered_mat, mat))

def solve():
    T, N, D = map(int, input().split())
    matrixs = [[[0]*N for _ in range(N)] for _ in range(T)]

    for t in range(T):
        for _ in range(int(input())):
            a, b, c = map(int, input().split())
            a-=1; b-=1
            matrixs[t][a][b] = c

    one_cycled_mat, res_mat = [[0]*N for _ in range(N)], [[0]*N for _ in range(N)]
    res = D % T
    for n in range(N):
        one_cycled_mat[n][n] = 1
        res_mat[n][n] = 1

    for t in range(T):
        one_cycled_mat = matrix_multi(N, one_cycled_mat, matrixs[t])
        if t < res:
            res_mat = matrix_multi(N, res_mat, matrixs[t])

    ans_mat = matrix_multi(N, matrix_divide_and_conquer((D-res)//T, N, one_cycled_mat), res_mat)
    for x in range(N):
        print(*ans_mat[x])

solve()