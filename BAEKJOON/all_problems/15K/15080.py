a = list(map(int, input().split(':')))
b = list(map(int, input().split(':')))

tot_a = a[0]*3600+a[1]*60+a[2]
tot_b = b[0]*3600+b[1]*60+b[2]

# 86400 == 24*60*60
print((86400+tot_b-tot_a)%86400)