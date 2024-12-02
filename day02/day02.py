def count_safe():
    with open("./sample_input", encoding="utf-8") as file:
        lines = (line.strip() for line in file.readlines())

    total_safe = 0
    for line in lines:
        int_list = list(map(int, line.split()))
        size = len(int_list) - 1

        all_increasing = all([int_list[i] < int_list[i + 1] for i in range(size)])
        all_decreasing = all([int_list[i] > int_list[i + 1] for i in range(size)])
        diff_in_range = all([0 < abs(int_list[i] - int_list[i + 1]) < 4 for i in range(size)])

        if (all_increasing or all_decreasing) and diff_in_range:
            total_safe = total_safe + 1

    return total_safe


def count_tolerate_safe():
    with open("./input", encoding="utf-8") as file:
        lines = (line.strip() for line in file.readlines())

    def is_single_list_safe(lst):
        size_minus_1 = len(lst) - 1

        all_increasing = all([lst[i] < lst[i + 1] for i in range(size_minus_1)])
        all_decreasing = all([lst[i] > lst[i + 1] for i in range(size_minus_1)])
        diff_in_range = all([0 < abs(lst[i] - lst[i + 1]) < 4 for i in range(size_minus_1)])

        if (all_increasing or all_decreasing) and diff_in_range:
            return True
        return False

    def is_list_safe(lst):
        if is_single_list_safe(lst):
            return True

        lst_to_check = [lst[:i] + lst[i + 1:] for i in range(len(lst))]

        return any([is_single_list_safe(new_lst) for new_lst in lst_to_check])

    total_safe = 0

    for line in lines:
        int_list = list(map(int, line.split()))
        if is_list_safe(int_list):
            total_safe = total_safe + 1

    return total_safe


print("count_safe:", count_safe())
print("count_tolerate_safe:", count_tolerate_safe())
