def btr(s:str, len_s:int, idx:int, visited:list, ans:list, max_num:int) -> bool:
    if(idx >= len_s):
        return True

    # idx < len_s
    # 1 ~ 9 의 숫자
    n = int(s[idx:idx+1])
    if(n > 0 and not visited[n]):
        visited[n] = True
        ans.append(n)

        if(btr(s, len_s, idx+1, visited, ans, max_num)):
            return True

        visited[n] = False
        ans.pop()

    # 10 ~ 50의 숫자
    if(idx >= (len_s-1)): return False
    if(s[idx] == '0'): return False
    n = int(s[idx:idx+2])

    if(n <= max_num and not visited[n]):
        visited[n] = True
        ans.append(n)

        if(btr(s, len_s, idx+2, visited, ans, max_num)):
            return True

        visited[n] = False
        ans.pop()

    return False


def solve():
    s = input()
    len_s = len(s)

    max_num = 0
    for _ in range(9):
        max_num += 1
        len_s -= 1
        if(len_s <= 0): break
    while(len_s > 0):
        max_num += 1
        len_s -= 2
    # print("max_num", max_num)

    visited = [False]*(max_num+1)
    ans = []
    btr(s, len(s), 0, visited, ans, max_num)

    print(*ans)

solve()