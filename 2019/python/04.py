def part1(n):
    digits = [n[0]]
    repeat_flag = False
    prev = None
    for digit in n:
        if digit < max(digits):
            return False
        repeat_flag = repeat_flag or digit == prev
        digits.append(digit)
        prev = digit
    return repeat_flag


def part2(n):
    digits = [n[0]]
    repeat_flag = False
    for digit in n:
        if digit < max(digits):
            return False
        repeat_flag = repeat_flag or n.count(digit) == 2
        digits.append(digit)
    return repeat_flag

def solution(lower, upper):
    correct_count = 0
    for i in range(lower, upper + 1):
        #if part1(str(i)):
        if part2(str(i)):
            correct_count += 1
    return correct_count
