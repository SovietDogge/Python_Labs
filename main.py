import random
import sortings

num_list = []
same_num_list = []
for i in range(0, 8):
    num_list.append(random.randint(0, 20))
    same_num_list.append(num_list[i])

print("Num_list original", num_list)
print("Same_list original", same_num_list)

# sortings.selection_sort(num_list)
# sortings.bubble_sort(num_list)
# sortings.insertion_sort(num_list)
# sortings.counting_sort(num_list)
# num_list = sortings.merge_sort(num_list)
# num_list = sortings.quick_sort(num_list)
same_num_list.sort()

print("Comparison", same_num_list == num_list)
print("Num_list sorted", num_list)
print("Same_list sorted", same_num_list)
