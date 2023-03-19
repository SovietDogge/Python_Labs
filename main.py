import random
import copy
import sortings

num_list = [random.randint(0, 20) for i in range(8)]
num_list_copy = copy.deepcopy(num_list)

print('Num_list original', num_list)
print('Num_list_copy original', num_list_copy)

# sortings.selection_sort(num_list)
# sortings.bubble_sort(num_list)
# sortings.insertion_sort(num_list)
# sortings.counting_sort(num_list)
# num_list = sortings.merge_sort(num_list)
num_list = sortings.quick_sort(num_list)
num_list_copy.sort()

print('Comparison', num_list_copy == num_list)
print('Num_list sorted', num_list)
print('Same_list sorted', num_list_copy)
