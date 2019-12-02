import math

def read_file(filename):
    with open(filename, "r") as f:
        return [int(i.strip()) for i in f.readlines()]


def count(filename):
    total = 0
    for i in read_file(filename):
        total += math.floor(i / 3) - 2
    return total


def count_with_fuel(filename):
    total = 0
    for i in read_file(filename):
        fuel = math.floor(i / 3) - 2
        while fuel > 0:
            total += fuel
            fuel = math.floor(fuel / 3) - 2
    return total
