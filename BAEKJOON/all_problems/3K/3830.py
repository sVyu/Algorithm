import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def fp(parent, v, vals):
    if(parent[v] != v):
        pre_parent_v = parent[v]
        parent[v] = fp(parent, parent[v], vals)
        vals[v] += vals[pre_parent_v]
    return parent[v]

# union 시 부모는 숫자 작은 vertex
def up(parent, a, b, vals, val):
    pa = fp(parent, a, vals)
    pb = fp(parent, b, vals)
    # 위 과정으로 a, b의 vals가 갱신

    # accuracy is maintained
    # if(pa == pb): return

    if(pa > pb):
        parent[pa] = pb
        current_gap = vals[b]-vals[a]
        correction_val = val-current_gap
        vals[pa] -= correction_val
    else:
        parent[pb] = pa
        current_gap = vals[b]-vals[a]
        correction_val = val-current_gap
        vals[pb] += correction_val

def solve():
    n, m = map(int, input().split())
    while n and m:
        parent = [i for i in range(n+1)]
        vals = [0]*(n+1)

        for _ in range(m):
            cmds = input().split()
            # print(cmds)

            if(cmds[0] == '!'):
                a, b, val = map(int, cmds[1:])
                up(parent, a, b, vals, val)
            else: # '?'
                a, b = map(int, cmds[1:])
                pa = fp(parent, a, vals)
                pb = fp(parent, b, vals)

                if(pa != pb):
                    print("UNKNOWN")
                    continue

                # pa == pb
                print(vals[b]-vals[a])

        n, m = map(int, input().split())

solve()