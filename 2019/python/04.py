def parse_one(n):
    digits = []
    repeat_flag = False
    prev = None
    for i in n:
        if digits:
            if i < max(digits):
                return False
        if i == prev:
            repeat_flag = True
        digits.append(i)
        prev = i
    return repeat_flag and True

def parse_two(n):
    digits = []
    repeat_flag = False
    for i in n:
        if digits:
            if i < max(digits):
                return False
        if n.count(i) == 2:
            repeat_flag = True
        digits.append(i)
    
    return repeat_flag

def guess_password(lower, upper):
    correct_count = 0
    for i in range(lower, upper + 1):
        # part 1
        # if parse_num(str(i)):
        #     correct_count += 1
        # part 2
        if parse_two(str(i)):
            correct_count += 1
    return correct_count
