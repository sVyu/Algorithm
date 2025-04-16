import sys
input = sys.stdin.readline

# find_parent
def fp(parent, x, vals):
    if(parent[x] != x):
        pre_parent_x = parent[x]
        parent[x] = fp(parent, parent[x], vals)
        vals[x] += vals[pre_parent_x]
    return parent[x]

# union_parent
def up(parent, a, b, vals):
    pa = fp(parent, a, vals)
    parent[pa] = b
    vals[pa] += abs(pa-b)%1000

def solve():
    n = int(input())

    parent = [i for i in range(n+1)]
    vals = [0]*(n+1)

    cmds = list(input().split())
    while cmds[0] != 'O':
        # print(cmds)
        if cmds[0] == 'E':
            v = int(cmds[1])
            fp(parent, v, vals)
            print(vals[v])
        else: # I
            a, b = int(cmds[1]), int(cmds[2])
            up(parent, a, b, vals)

        cmds = list(input().split())

t = int(input())
for _ in range(t):
    solve()