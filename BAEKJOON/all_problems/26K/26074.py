'''
n*m 홀수 -> GomGom Win

n*m 짝수
2 -> ChongChong win
4 -> GomGom Win
6 -> GomGom Win
8 -> GomGom Win
10 -> (2x5) GomGom Win -> by 6th block - on mid
12 -> (2x6) GomGom Win -> by 4th block - on side, and copy opponent's block
12 -> (3x4) GomGom Win -> by 1th block
'''
'''
ChongChong Win scenario
1 2
2 1
'''
'''
keyword : symmetry

even,   even    -> 4th block center
even,   odd     -> 1th block center
odd,    odd     -> 8th block center
'''
print("GomGom" if sum(map(int,input().split())) != 3 else"ChongChong")