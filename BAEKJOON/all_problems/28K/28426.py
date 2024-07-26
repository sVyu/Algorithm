N = int(input())

print(3, end=' ')
for i in range(1, N-1):
    print(2*i, end=' ')

if N >= 2:
    # tot = 3+((2*N-2)*(N-2)//2)
    tot = 3+(N-1)*(N-2)
    for k in range(int(2e5), int(1e6), 2):
        if (tot+k)%3 == 0:
            print(k)
            break