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
            # ��ū���� ����� �ڵ�, ������ h���� ���� ��� �ٷ� ans 1 ���� ���� ó��
            if(s[-1]<h):
                while(s and s[-1]<h):
                    ans += 1
                    d[s.pop()] -= 1
                    len_s -= 1

        # 4 2 2 1 2 �� ���� case�� ������, 2 2 -- 2 �� ���ؼ� 2����ŭ �����ֱ� ���� �ڵ�
        if(s and s[-1]==h):
            ans += d[h]

        # 2 2 2 -- 2 (�� ���� ���� ����) Ȥ�� 3 (�ܵ�)ó�� ���� �ʿ� ���� ��� ����
        if(len_s > d[h]):
            ans += 1

        s.append(h)
        len_s += 1
        d[h] += 1

    print(ans)

solve()