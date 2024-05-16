a, b, c = map(int, input().split())
while a or b or c:
    if((b**2) == (a*c)):
        print("GP", c**2//b)
    else:
        print("AP", 2*c-b)
    a, b, c = map(int, input().split())