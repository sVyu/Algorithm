import sys

dict_input_mode = True
wd = dict() # word_dict
for line in sys.stdin.readlines():
    line = line.rstrip()

    if not line:
        dict_input_mode = False
        continue

    if dict_input_mode:
        val, key = line.split()
        wd[key] = val
    else:
        key = line
        if key in wd: print(wd[key])
        else: print("eh")