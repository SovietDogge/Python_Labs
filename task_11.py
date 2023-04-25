import re


def write_correct_dates(path):
    current_date = '25.04.2023'
    with open(path, 'rt', encoding='utf-8') as file:
        text = re.sub('\d{2}\.\d{2}\.\d{4}',current_date, file.read())

    with open('updated.txt', 'wt') as file:
        file.write(text)


if __name__ == '__main__':
    file_path = 'dates.txt'
    write_correct_dates(file_path)
