N, M = map(int, input().split())

for n in range(N):
    for m in range(1, M+1):  
        print(n*M+m, end=' 'if m != M else '')
    print()