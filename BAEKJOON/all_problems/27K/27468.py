n = int(input())
ans = [0]*(n+1)

if((n%4) != 2):
    for i in range(1, n+1):
        if((i%4)==1):   ans[i] = ans[i-1]+1
        elif(i%2):      ans[i] = ans[i-1]-1
        else:           ans[i] = ans[i-1]+2
else:
    for i in range(1, n+1):
        if((i%4)==0):   ans[i] = ans[i-1]+1
        elif(i%2):      ans[i] = ans[i-1]+2
        else:           ans[i] = ans[i-1]-1

print("YES")
print(*ans[1:])