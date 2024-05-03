X,Y,W,S = map(int, input().split())
X,Y = sorted([X, Y])

if 2*W <= S:
    print((X+Y)*W)
else:
    if(X%2 == Y%2):
        print(min(S*Y, S*X+W*(Y-X)))
    else:
        print(min(S*(Y-1)+W, S*X+W*(Y-X)))