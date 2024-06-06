ss = input()
while ss[0] != '#':
    c, ss = ss[0], ss[2:].lower()

    cnt = sum([1 if s == c else 0 for s in ss])
    print(c, cnt)

    ss = input()