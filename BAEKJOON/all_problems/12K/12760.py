n, m = map(int, input().split())

cards = [sorted(list(map(int, input().split()))) for _ in range(n)]
scores = [0]*n

for i in range(m):
    t = max([cards[r][i] for r in range(n)])    
    
    for r in range(n):
        if cards[r][i] == t:
            scores[r] += 1

#print(scores)

t = max(scores)
ns = [i+1 for i in range(n) if scores[i] == t]
print(*ns)