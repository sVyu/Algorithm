import sys
input = sys.stdin.readline

def find_parent(parent:list, x:int) -> int:
    if(x != parent[x]):
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent:list, a:int, b:int) -> None:
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)

    if(pa > pb):    parent[pa] = pb
    else:           parent[pb] = pa

def solve():
    n, m, k = map(int, input().split())
    friend_costs = [0] + list(map(int, input().split()))

    # union_find
    parent = [i for i in range(n+1)]
    for _ in range(m):
        v, w = map(int, input().split())
        union_parent(parent, v, w)
    for v in range(1, n+1):
        find_parent(parent, v)
    # print(parent)

    # find_min_costs
    INF = int(1e12)
    min_costs = [INF]*(n+1)
    for v in range(1, n+1):
        min_costs[parent[v]] = min(min_costs[parent[v]], friend_costs[v])
    # print(min_costs)

    # print ans
    ans_cost = sum([cost for cost in min_costs if cost != INF])
    print(ans_cost if ans_cost <= k else "Oh no")

solve()