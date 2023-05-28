def validate(value):
    try:
        return float(value)
    except ValueError:
        print(f'Incorrect value - {value}')
    return validate(input())
