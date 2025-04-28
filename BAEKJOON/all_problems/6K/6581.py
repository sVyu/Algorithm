import sys
# lines = sys.stdin
# lines = sys.stdin.readlines()

# input ref : https://jamie2779.tistory.com/32

def solve():
    curr_line = ''
    words = []
    for line in sys.stdin:
        words += line.split()
    # print(words)

    for word in words:
        if(word == ''): continue
        if(word == '<br>'):
            print(curr_line)
            curr_line = ''
            continue
        if(word == '<hr>'):
            if(curr_line != ''):
                print(curr_line)
            print('-'*80)   
            curr_line = ''
            continue

        if(curr_line == ''):
            curr_line = word
            continue

        if((len(curr_line)+len(word)+1) > 80):
            print(curr_line)
            curr_line = word
        else:
            curr_line += ' '+word

    if(curr_line != ''):
        print(curr_line)

solve()