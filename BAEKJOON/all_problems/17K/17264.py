import sys
input = sys.stdin.readline

def solve():
    n, p = map(int, input().split())
    w, l, g = map(int, input().split())

    players_data = dict()
    for _ in range(p):
        name, win_or_lose = map(str, input().split())
        players_data[name] = w if win_or_lose == 'W' else -l
    # print(players_data)

    score = 0
    for _ in range(n):
        name = input().rstrip()
        if(name in players_data):   score = max(0, score + players_data[name])
        else:                       score = max(0, score - l)

        if score >= g:
            print("I AM NOT IRONMAN!!")
            return

    print("I AM IRONMAN!!")

solve()