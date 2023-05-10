import re


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

    return dates


def task_2(path):
    with open(path, 'rt', encoding='utf-8') as file:
        text = file.read()
        sentences = re.findall(r'[A-Z][^\.!?]*[\.!?]', text)
        return sentences


def task_3(path):
    with open(path, 'rt', encoding='utf-8') as file:
        text = file.read()
        descriptions = re.findall(r'[A-Z][^\.!?]*[\.!?]', text)
        dates = re.findall(r'\d{3,4}', text)
        events = dict(zip(dates, descriptions))
        return events


if __name__ == '__main__':
    # print(task_1('dates.txt'))
    print(task_2('some_text.txt'))
    print(task_3('events.txt'))
    # dates_file_path = 'dates.txt'
