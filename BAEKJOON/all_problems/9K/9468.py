for _ in range(int(input())):
    ns = list(map(int, input().split()))
    k, ns = ns[0], ns[1:]

    pre = 0
    ans = 0
    for n in ns:
        if pre > n:
            ans += 1
        pre = n

    print(k, ans)