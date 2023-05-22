from copy import deepcopy


class MyMultiSet:

    def __init__(self, start_dict=None):
        self.__count_nums = {} if start_dict is None else start_dict

    def clear(self):
        self.__count_nums = {}

    def add_num(self, number):

        if number in self.__count_nums.keys():
            self.__count_nums[number] += 1
        else:
            self.__count_nums[number] = 1

    def get_count(self, number):
        return self.__count_nums[number] if number in self.__count_nums.keys() else None

    @property
    def count_nums(self):
        return self.__count_nums

    @count_nums.setter
    def count_nums(self, value):
        self.__count_nums = value

    def remove(self, number):
        if number in self.__count_nums.keys():
            if self.__count_nums[number]:
                self.__count_nums[number] -= 1
            else:
                raise Exception(f'The {number} has 0 entries in set')
        else:
            raise Exception(f'{number} isn\'t in set')

    def check_empty(self):
        return False if len(self.__count_nums.keys()) else True

    def union(self, set_to_unite):
        new_set = deepcopy(set_to_unite.count_nums)
        for key, value in self.count_nums.items():

            if key in new_set.keys():
                if value > new_set[key]:
                    new_set[key] = value
            else:
                new_set[key] = value

        return MyMultiSet(new_set)

    def intersection(self, set_to_intersect):
        new_set = {set_to_intersect.count_nums[key] if (key in set_to_intersect.count_nums.keys())
                   and (self.__count_nums[key] > set_to_intersect.count_nums[key]) else self.__count_nums[key] for key in self.__count_nums}
        # for key in self.__count_nums.keys():
        #     if key in set_to_intersect.count_nums.keys():
        #         if self.__count_nums[key] > set_to_intersect.count_nums[key]:
        #             new_set[key] = set_to_intersect.count_nums[key]
        #         else:
        #             new_set[key] = self.__count_nums[key]

        return MyMultiSet(new_set)
