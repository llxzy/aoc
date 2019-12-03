def get_input(filename):
    with open(filename, "r") as f:
        lines = [i.strip().split(",") for i in f.readlines()]
    return lines

def dist(a, b):
    return abs(a[0] - b[0]) + abs(b[1] - a[1])

def solution(filename):
    lines = get_input(filename)
    center = (0, 0)
    temp = []
    temp2 = []
    moveX = {"D": 0, "U": 0, "L": -1, "R": 1}
    moveY = {"D": -1, "U": 1, "L": 0, "R": 0}
    for wire in lines:
        last = (0, 0)
        wire_points = set()
        inter_steps = {}
        stepcounter = 1
        for cmd in wire:
            drc = cmd[0]
            steps = int(cmd[1:])
            for i in range(steps):
                x = (last[0]+moveX[drc], last[1]+moveY[drc])
                wire_points.add(x)
                inter_steps[x] = stepcounter
                stepcounter += 1
                last = x
        temp.append(wire_points)
        temp2.append(inter_steps)

    intersections = set.intersection(*temp)
    workset = [dist(center, i) for i in intersections]

    out = {}
    for a in temp2:
        for i in a:
            if i in intersections:
                out[i] = out.get(i, 0) + a[i]

    result = []
    for i in out:
        result.append(out[i])


    #part1
    # return min(workset)
    #part2
    return min([out[item] for item in out])
