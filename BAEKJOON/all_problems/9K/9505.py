import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def solve():
    inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    INF = int(1e12)

    t = int(input())
    for _ in range(t):
        k, w, h = map(int, input().split())
        battle_ship_dict = dict()
        for _ in range(k):
            name, val = input().split()
            battle_ship_dict[name] = int(val)
        # print(battle_ship_dict)

        board = [list(input().rstrip()) for _ in range(h)]
        costs = [[INF]*w for _ in range(h)]

        start = []
        for x in range(h):
            for y in range(w):
                if(board[x][y] == 'E'):
                    start = [x, y]
                    costs[x][y] = 0
        # print(start)

        heap = [[0, start[0], start[1]]]
        while(heap):
            cost, x, y = heappop(heap)
            if((x == 0) | (x == (h-1)) | (y == 0) | (y == (w-1))):
                print(cost)
                break

            if(costs[x][y] < cost): continue

            for px, py in inc_xy:
                nx, ny = x+px, y+py
                if((nx < 0) | (nx >= h) | (ny < 0) | (ny >= w)): continue
                if(board[nx][ny] == 'E'): continue

                new_cost = cost + battle_ship_dict[board[nx][ny]]
                if(costs[nx][ny] > new_cost):
                    costs[nx][ny] = new_cost
                    heappush(heap, [new_cost, nx, ny])

solve()