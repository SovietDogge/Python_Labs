import re


def task_1(path):
    with open(path, 'rt', encoding='utf-8') as file:
        text = file.read()
        dates = re.findall(r'(?:\d{1,2})\.(?:\d{1,2})\.\d{4}', text)
        dates += re.findall(r'\d{4}[/](?:\d{1,2})[/](?:\d{1,2})', text)
        print(dates)

    for i, _ in enumerate(dates):
        dates[i] = re.sub(r'(\d{4})[/](\d{1,2})[/](\d{1,2})', r'\3.\2.\1', dates[i])

    for i, date in enumerate(dates):
        correct_date = date.split('.')
        for j, _ in enumerate(correct_date):
            correct_date[j] = correct_date[j].zfill(2)
        dates[i] = '.'.join(correct_date)

    return dates


def task_2(path):
    with open(path, 'rt', encoding='utf-8') as file:
        return re.findall(r'[A-Z][^\.!?]*[\.!?]', file.read())


def task_3(path):
    with open(path, 'rt', encoding='utf-8') as file:
        text = file.read()
        descriptions = re.findall(r'[A-Z][^\.!?]*[\.!?]', text)
        dates = re.findall(r'\d{3,4}', text)
        events = dict(zip(dates, descriptions))
        return events


if __name__ == '__main__':
    print(task_1('dates.txt'))
    # print(task_2('some_text.txt'))
    # print(task_3('events.txt'))
    # dates_file_path = 'dates.txt'
