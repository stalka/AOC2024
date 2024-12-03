import re


def calc_mul():
    with open("./sample_input", encoding="utf-8") as file:
        file_content = file.read()

    pattern = r"mul\((\d{1,3},\d{1,3})\)"
    matches = re.findall(pattern, file_content)
    mul_list = [tuple(map(int, match.split(','))) for match in matches]
    return sum([x * y for x, y in mul_list])


def calc_mul_with_instruction():
    with open("./input", encoding="utf-8") as file:
        file_content = file.read()

    pattern = r"mul\((\d{1,3},\d{1,3})\)|(don't)|(do)"
    matches = re.findall(pattern, file_content)

    total = 0
    take_value = True

    for x, y, z in matches:
        if x and take_value:
            x1, x2 = x.split(',')
            total = total + (int(x1) * int(x2))
        if y: take_value = False
        if z: take_value = True

    return total


print("calc_mul:", calc_mul())
print("calc_mul_with_instruction:", calc_mul_with_instruction())
