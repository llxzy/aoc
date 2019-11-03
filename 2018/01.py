# This is not very elegant looking so might look to rewrite it some time later
# Especially the second function is rather slow so might look into optimising it a bit, if possible

def get_frequency(file):
    with open(file, "r") as f:
        flag = 0
        files = [i.strip() for i in f.readlines()]
        for i in files:
            if i[0] == "+":
                flag += int(i[1:])
            else:
                flag -= int(i[1:])
    return flag


def freq_twice(file):
    with open(file, "r") as f:
        files = [i.strip() for i in f.readlines()]
        index = tmp = 0
        result = None
        freqs = []
        while not result:
            if files[index][0] == "+":
                tmp += int(files[index][1:])
            else:
                tmp -= int(files[index][1:])
            if tmp in freqs:
                result = tmp
            else: 
                freqs.append(tmp)
                index += 1
                if index == len(files):
                    index = 0
    return result
