from collections import deque

# very ugly, will refactor

def read_input(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return [i.strip().split(")") for i in lines]


def init_graph(filename):
    lines = read_input(filename)
    orbits = {}
    for i in lines:
        cur = orbits.get(i[0], [])
        cur.append(i[1])
        orbits[i[0]] = cur
    return orbits


def part1(filename):
    graph = init_graph(filename)
    orbits = {"COM": 0}

    queue = deque(["COM"])
    while queue:
        item = queue.popleft()
        for i in graph[item]:
            if i in graph.keys():
                queue.append(i)
            orbits[i] = orbits.get(item, 0) + 1

    return sum(orbits.values())


def part2(filename):
    with open(filename, "r") as f:
        l = f.readlines()
    lines = [i.strip() for i in l]
    graph = {}
    
    for i in lines:
        i = i.split(")")
        cur = graph.get(i[1], [])
        cur.append(i[0])
        graph[i[1]] = cur


    you = san = ""
    for i in graph:
        if i == "YOU":
            you = graph[i]
        elif i == "SAN":
            san = graph[i]

    san_parents = {}
    san_dist = 0
    queue = deque(san)
    while queue:
        item = queue.popleft()
        for i in graph[item]:
            if i not in graph.keys():
                continue
            else:
                queue.append(i)
            san_parents[i] = san_dist
        san_dist += 1


    queue = deque(you)
    distance = 0
    while queue:
        item = queue.popleft()
        distance += 1
        for i in graph[item]:
            if i in san_parents:
                return distance + san_parents[i] + 1
            else:
                queue.append(i)
    return distance


print(part1("2019/06.txt"))