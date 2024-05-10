s = list(input())

word = ''
for c in s:
    if c == '<':
        print(word[::-1], end='')
        word = '<'
    elif c == '>':
        print(word+'>', end='')
        word = ''
    elif c == ' ':
        if word and word[0] == '<':
            word += c
        else:
            print(word[::-1], end=' ')
            word=''
    else:
        word += c

if word:
    print(word[::-1], end='')