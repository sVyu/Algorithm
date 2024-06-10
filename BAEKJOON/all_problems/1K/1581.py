ff, fs, sf, ss = map(int, input().split())

if not (ff+fs):
    print(ss+min(sf,1))
else:
    ans = ff
    if fs:
        ans += ss+min(fs,sf)*2
        if fs > sf:
            ans += 1
    print(ans)