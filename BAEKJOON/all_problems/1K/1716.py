n, k = map(int, input().split())
while n != -1 and k != -1:
    ns = list(map(int, input().split()))
    for i in range(n, k-1, -1):
        ns[i-k] -= ns[i]
        ns[i] = 0
    # print(ns)

    all_zero = True
    for val in ns:
        if val:
            all_zero = False
            break

    print(*ns[:k]) if not all_zero else print(0)
    n, k = map(int, input().split())