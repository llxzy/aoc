from copy import deepcopy

def foo(lines):
    for i in range(0, len(lines), 4):
        if lines[i] == 1:
            lines[lines[i+3]] = lines[lines[i+1]] + lines[lines[i+2]]
        elif lines[i] == 2:
            lines[lines[i+3]] = lines[lines[i+1]] * lines[lines[i+2]]
    return lines

def opcodes(filename):
    with open(filename, "r") as f:
        line = f.read().strip()
    lines = [int(i) for i in line.split(",")]
    
    lines[1] = 12
    lines[2] = 2

    return foo(lines)

def output(filename):
    with open(filename, "r") as f:
        line = f.read().strip()
    lines = [int(i) for i in line.split(",")]

    for i in range(100):
        for j in range(100):
            arr = deepcopy(lines)
            arr[1] = i
            arr[2] = j
            if foo(arr)[0] == 19690720:
                return 100 * i + j
