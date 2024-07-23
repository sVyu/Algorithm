from collections import defaultdict

def solve():
    size = 6
    tot_words = [input() for _ in range(size)]

    used = [False]*size
    row_words = ['']*3
    for i in range(size):
        row_words[0] = tot_words[i]
        used[i] = True
        for j in range(size):
            if i == j: continue
            row_words[1] = tot_words[j]
            used[j] = True
            for k in range(size):
                if k in [i, j]: continue
                row_words[2] = tot_words[k]
                used[k] = True

                d = defaultdict(int)
                for a in range(size):
                    if not used[a]:
                        d[tot_words[a]] += 1

                pos = True
                targets = [''.join([row_words[x][y] for x in range(3)]) for y in range(3)]
                for t in targets:
                    if (t not in d) or d[t] <= 0:
                        pos = False
                        break
                    else:
                        d[t] -= 1

                if pos:
                    print(*row_words, sep='\n')
                    return

                used[k] = False
            used[j] = False
        used[i] = False

    print(0)

solve()