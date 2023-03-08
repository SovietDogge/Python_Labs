import random


def selection_sort(sortable_list):
    for i in range(len(sortable_list)):
        min_num_ind = i
        for j in range(i, len(sortable_list)):
            if sortable_list[min_num_ind] > sortable_list[j]:
                min_num_ind = j
        sortable_list[min_num_ind], sortable_list[i] = sortable_list[i], sortable_list[min_num_ind]


def bubble_sort(sortable_list):
    for i in range(0, len(sortable_list)):
        for j in range(0, len(sortable_list) - 1):
            if sortable_list[i] < sortable_list[j]:
                sortable_list[i], sortable_list[j] = sortable_list[j], sortable_list[i]


def insertion_sort(sortable_list):
    for i in range(1, len(sortable_list)):
        current_ind = i
        while sortable_list[current_ind] < sortable_list[current_ind - 1]:
            sortable_list[current_ind], sortable_list[current_ind - 1] = \
                sortable_list[current_ind - 1], sortable_list[current_ind]
            if current_ind != 1:
                current_ind = current_ind - 1


def counting_sort(sortable_list):
    max_num = 0

    for i in range(len(sortable_list)):
        if sortable_list[i] > max_num:
            max_num = sortable_list[i]

    count_nums = [0 for i in range(max_num + 1)]

    for i in range(len(sortable_list)):
        count_nums[sortable_list[i]] += 1

    sortable_list.clear()

    sortable_list = [sortable_list.append(i) for i in range(len(count_nums)) for j in range(count_nums[i])]


def merge_sort(sortable_list):

    if len(sortable_list) == 1:
        return sortable_list

    size = int(len(sortable_list) / 2)

    left_part = [sortable_list[i] for i in range(size)]
    right_part = [sortable_list[i] for i in range(size, len(sortable_list))]

    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)

    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left_part) and right_index < len(right_part):
        if left_part[left_index] < right_part[right_index]:
            sorted_list.append(left_part[left_index])
            left_index += 1
        else:
            sorted_list.append(right_part[right_index])
            right_index += 1

    while left_index < len(left_part):
        sorted_list.append(left_part[left_index])
        left_index += 1

    while right_index < len(right_part):
        sorted_list.append(right_part[right_index])
        right_index += 1

    return sorted_list


def quick_sort(sortable_list):

    if len(sortable_list) <= 1:
        return sortable_list

    end_ind = len(sortable_list) - 1
    pivot_ind = random.randint(0, end_ind)

    sortable_list[pivot_ind], sortable_list[end_ind] = sortable_list[end_ind], sortable_list[pivot_ind]

    pivot_ind = end_ind
    left_ind = 0
    right_ind = end_ind - 1
    is_bigger = False
    is_smaller = False

    while right_ind > left_ind:
        if sortable_list[left_ind] < sortable_list[pivot_ind] and not is_bigger:
            left_ind += 1
        else:
            is_bigger = True
        if sortable_list[right_ind] > sortable_list[pivot_ind] and not is_smaller:
            right_ind -= 1
        else:
            is_smaller = True
        if is_smaller and is_bigger:
            sortable_list[left_ind], sortable_list[right_ind] = sortable_list[right_ind], sortable_list[left_ind]
            is_smaller = False
            is_bigger = False

    if sortable_list[pivot_ind] < sortable_list[left_ind]:
        sortable_list[pivot_ind], sortable_list[left_ind] = sortable_list[left_ind], sortable_list[pivot_ind]
        pivot_ind = left_ind
    else:
        sortable_list[pivot_ind], sortable_list[left_ind + 1] = sortable_list[left_ind + 1], sortable_list[pivot_ind]
        pivot_ind = left_ind + 1

    sortable_list[0:pivot_ind] = quick_sort(sortable_list[0:pivot_ind])
    sortable_list[pivot_ind + 1: end_ind + 1] = quick_sort(sortable_list[pivot_ind + 1: end_ind + 1])
    return sortable_list
