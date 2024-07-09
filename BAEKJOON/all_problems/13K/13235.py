s = list(input())
len_s = len(s)

for i in range(len_s//2):
    if s[i] != s[len_s-1-i]:
        print('false')
        exit(0)

print('true')