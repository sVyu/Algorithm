line = input().split()
# print(line)

# d: data_type
d, vars = line[0], line[1:]
# print(d, vars)

for var in vars:
    var = list(var)[:-1]
    # additional data_type
    ad = ''
    while var and var[-1] in "]&*":
        if var[-1] == ']':
            ad += '[]'
            for _ in range(2):
                var.pop()
            continue
        ad += var.pop()

    print(d+ad, ''.join(var)+';')