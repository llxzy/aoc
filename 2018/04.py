### util
def input_sort(file):
    with open(file, "r") as f:
        lines = [i.strip() for i in f.readlines()]
    lines.sort()
    return lines

def calc_guards(lst):
    

print(input_sort("2018/04.txt"))