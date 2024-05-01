# solved
import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    n = int(input())
    ans = 0
    s = []
    len_s = 0
    h = -1
    d = defaultdict(int)

    for _ in range(n):
        h = int(input())
        if(s):
            # 오큰수와 흡사한 코드, 현재의 h보다 작은 경우 바로 ans 1 증가 등의 처리
            if(s[-1]<h):
                while(s and s[-1]<h):
                    ans += 1
                    d[s.pop()] -= 1
                    len_s -= 1

        # 4 2 2 1 2 와 같은 case가 있으면, 2 2 -- 2 에 대해서 2개만큼 더해주기 위한 코드
        if(s and s[-1]==h):
            ans += d[h]

        # 2 2 2 -- 2 (더 높은 곳이 없음) 혹은 3 (단독)처럼 더할 필요 없는 경우 제외
        if(len_s > d[h]):
            ans += 1

        s.append(h)
        len_s += 1
        d[h] += 1

    print(ans)

solve()