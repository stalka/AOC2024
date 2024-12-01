from collections import Counter


def calc_dist():
    with open("./input", encoding="utf-8") as file:
        lines = (line.strip() for line in file.readlines())

    merged_list = [line.split() for line in lines]

    first_list = [pair[0] for pair in merged_list]
    second_list = [pair[1] for pair in merged_list]

    first_list.sort()
    second_list.sort()

    total_dist = 0
    for index in range(len(first_list)):
        dist = abs(int(first_list[index]) - int(second_list[index]))
        total_dist += dist
    return total_dist


def calc_similarity():
    with open("./input", encoding="utf-8") as file:
        lines = (line.strip() for line in file.readlines())

    merged_list = [line.split() for line in lines]

    first_list = [pair[0] for pair in merged_list]
    second_list = [pair[1] for pair in merged_list]

    second_list_counter = Counter(second_list)

    total_similarity = 0
    for elem in first_list:
        similarity = int(elem) * second_list_counter[elem]
        total_similarity += similarity
    return total_similarity


print("calc_dist:", calc_dist())
print("calc_similarity:", calc_similarity())
