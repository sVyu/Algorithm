s = input()
t = input()

filtered = [False]*26
for c in s:
    filtered[ord(c)-97] = True
# print(filtered)

for c in t:
    if(not filtered[ord(c)-97]):
        print(c, end='')