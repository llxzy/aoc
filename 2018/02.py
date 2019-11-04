# This feels rather ugly as well

def checksum(file):
    with open(file, "r") as f:
        line_list = []
        lines = [i.strip() for i in f.readlines()]
        for i in lines:
            letters = {}
            for j in i:
                if not j in letters:
                    letters[j] = 1
                else:
                    letters[j] += 1
            line_list.append(letters)

    def get_nums(lines):
        count_two = 0
        count_three = 0
        for i in lines:
            two_flag = False
            three_flag = False
            for key, value in i.items():
                if value == 2 and not two_flag:
                    count_two += 1
                    two_flag = True
                if value == 3 and not three_flag:
                    count_three += 1
                    three_flag = True
        return count_two * count_three

    return get_nums(line_list)


def match(str1, str2):
    flag = False
    for k, m in zip(str1,str2):
        if k != m:
            if flag:
                return False
            else:
                flag = True
    return flag


def get_common(str1, str2):
    common = ""
    for i, j in zip(str1, str2):
        if i == j:
            common += i
    return common


def off_by_one(file):
    word_1 = ""
    word_2 = ""
    with open(file, "r") as f:
        lines = [i.strip() for i in f.readlines()]
        for i in lines:
            for j in lines:
                if i == j:
                    continue
                if match(i, j):
                    word_1 = i
                    word_2 = j
    return get_common(word_1, word_2)
                