import re


def write_correct_dates(path):
    current_date = '25.04.2023'
    with open(path, 'rt', encoding='utf-8') as file:
        text = re.sub(r'\d{2}\.\d{2}\.\d{4}', current_date, file.read())

    with open('updated.txt', 'wt') as file:
        file.write(text)


def task_1(path):
    with open(path, 'rt', encoding='utf-8') as file:
        text = file.read()
        dates = re.findall(r'(?:\d{1,2})\.(?:\d{1,2})\.\d{4}', text)
        dates += re.findall(r'\d{4}[/](?:\d{1,2})[/](?:\d{1,2})', text)

    for i, date in enumerate(dates):
        date = date.replace('/', '.')

        correct_date = date.split('.')
        for j, num in enumerate(correct_date):
            if len(num) < 2:
                correct_date[j] = f'0{correct_date[j]}'

        if len(correct_date[0]) > len(correct_date[-1]):
            correct_date[0], correct_date[-1] = correct_date[-1], correct_date[0]

        dates[i] = '.'.join(correct_date)

    print(dates)


if __name__ == '__main__':
    task_1('dates.txt')
    # dates_file_path = 'dates.txt'
    # write_correct_dates(dates_file_path)

