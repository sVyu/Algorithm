import sys
lines = sys.stdin.readlines()

for line in lines:
    print(line, end='')   # AC
    print(line.rstrip())  # WA


# import sys
# input = sys.stdin.read

# print(input())


# import sys
# input = sys.stdin.read

# data = input().splitlines()
# for line in data:
#     print(line)