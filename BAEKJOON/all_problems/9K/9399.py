xys = [[-1, -1] for _ in range(10001)]
x, y = 0, 0
max_y = 1

for i in range(1, 10001):
    xys[i] = [x, y]
    y += 1
    if y == max_y:
        x += 1
        y = 0
        max_y += 1

a, b = map(int, input().split())
while a and b:
    x1, y1 = xys[a]
    x2, y2 = xys[b]
    x_gap, y_gap = abs(x1-x2), abs(y1-y2)
    print(max(x_gap, y_gap) if (x1-x2)*(y1-y2) >= 0 else x_gap + y_gap)

    # if x1 < x2:
    #     if y1 <= y2:
    #         print(max(x_gap, y_gap))
    #     else:
    #         print(x_gap + y_gap)
    # else: # x2 <= x1:
    #     if y2 <= y1:
    #         print(max(x_gap, y_gap))
    #     else:
    #         print(x_gap + y_gap)

    a, b = map(int, input().split())