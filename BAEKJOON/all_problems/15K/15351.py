for _ in range(int(input())):
    score = 0
    for c in list(input()):
        if 65 <= ord(c) < 91:
            score += ord(c)-64
    
    print("PERFECT LIFE" if score == 100 else score)