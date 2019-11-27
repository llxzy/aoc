import re

def parse_lines(file):
    with open(file, "r") as f:
        return [i for i in f.readlines()]
    
def claim(file):
    fabric = 1010 * [1010 * [0]]
    lines = parse_lines(file)
    
    for i in lines:
        m = re.search("#[0-9]* @ ([0-9]*),([0-9]*): ([0-9]*)x([0-9]*)$", i)
        width_s = int(m.group(1))
        height_s = int(m.group(2))
        width_e = int(m.group(3))
        height_e = int(m.group(4))

        for j in range(width_s, width_s + width_e + 1):
            for k in range(height_s, height_s + height_e + 1):
                fabric[k][j] += 1

    return fabric

def overlap(fabric):
    count = 0
    x = 0
    for i in range(len(fabric)):
        for j in range(len(fabric)):
            if fabric[i][j] > 1:
                count += 1
            else:
                x += 1
    return x

print(overlap(claim("2018/03.txt")))