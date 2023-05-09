import re


def write_correct_dates(path):
    current_date = '25.04.2023'
    with open(path, 'rt', encoding='utf-8') as file:
        text = re.sub(r'\d{2}\.\d{2}\.\d{4}', current_date, file.read())

    with open('updated.txt', 'wt') as file:
        file.write(text)


def task_1(path):
    with open(path, 'rt', encoding='utf-8') as file:
        dates = re.findall(r'(?:\d{1,2})\.(?:\d{1,2})\.\d{4}', file.read())
        dates += re.findall(r'(\d{4})[\/](?:\d{1,2})[\/](?:\d{1,2})', file.read())
        print(dates)


if __name__ == '__main__':
    task_1('dates.txt')
    # dates_file_path = 'dates.txt'
    # write_correct_dates(dates_file_path)

