# this took me way longer than it should
# and the result is not as pretty as it should be

def read_input(filename):
    with open(filename, "r") as f:
        line = f.read().strip()
    return [i for i in line.split(",")]


def computer(lines):
    i = 0
    while i < len(lines):
        opcode = lines[i][-2:]
        opcode = str(int(opcode)%10)
        mode = ["0", "0", "0", "0"]
        rest = lines[i][:-2]
        rest = rest[::-1]
        for j in range(len(rest)):
            mode[j] = rest[j]

        md = {"1": 3, "2": 3, "3":1, "4":1, "5": 2, "6": 2, "7":3, "8": 3, "99": 0}
        nxt = []

        for a in range(1, md.get(opcode, 0) + 1):
            if mode[a-1] == "0":
                nxt.append(int(lines[i+a]))
            elif mode[a-1] == "1":
                nxt.append(i+a)
            else:
                print('error')

        opcode = int(opcode)
        if opcode == 1:
            tmp = int(lines[nxt[1]]) + int(lines[nxt[0]])
            lines[nxt[2]] = str(tmp)
            i += 4
        elif opcode == 2:
            tmp = int(lines[nxt[0]]) * int(lines[nxt[1]])
            lines[nxt[2]] = str(tmp) 
            i += 4
        elif opcode == 3:
            num = int(input("enter num: "))
            lines[nxt[0]] = str(num)
            i += 2
        elif opcode == 4:
            print(lines[nxt[0]])
            i += 2
        elif opcode == 5:
            code = lines[nxt[0]]
            if code != "0":
                i = int(lines[nxt[1]])
            else:
                i += 3
        elif opcode == 6:
            code = lines[nxt[0]]
            if code == "0":
                i = int(lines[nxt[1]])
            else:
                i += 3
        elif opcode == 7:
            tmp = "0"
            if lines[nxt[0]] < lines[nxt[1]]:
                tmp = "1"
            lines[nxt[2]] = tmp
            i += 4
        elif opcode == 8:
            tmp = "0"
            if lines[nxt[0]] == lines[nxt[1]]:
                tmp = "1"
            lines[nxt[2]] = tmp
            i += 4
        else:
            break
    return 


def part1(filename):
    lines = read_input(filename)
    return computer(lines)

part1("2019/05.txt")