INCORRECT_INPUT_ER = 'Incorrect input'
ENTER_CORRECT_NUM = 'Please enter num from 0 to 8: '


def nums_validation(num):
    try:
        return int(num)
    except ValueError:
        print(INCORRECT_INPUT_ER)
        return nums_validation(input())


def validation_pattern(input_value, valid_value):
    if input_value in valid_value:
        return input_value
    print('Write correct value')
    if isinstance(input_value, int):
        return validation_pattern(nums_validation(input()), valid_value)
    return validation_pattern(input(), valid_value)


def vert_coord_validation(coordinate):
    coordinate = nums_validation(coordinate)
    return coordinate if 0 < coordinate <= 8 else vert_coord_validation(input(ENTER_CORRECT_NUM))
