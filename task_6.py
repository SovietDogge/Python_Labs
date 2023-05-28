from sqlite3 import connect
import re as r


NUM_CHECK_PAIRED = 'num_characteristic.txt'
LEARN_P = 'learning_python.txt'


def task_1(path='numbers.txt'):
    with open(path, 'rt') as nums:
        amount = sum([float(num) for num in nums])

    with open('amount.txt', 'wt') as file:
        file.write(str(amount))
    return amount


def task_2(path=NUM_CHECK_PAIRED):
    try:
        num = int(input('Enter any number: '))
        with open(path, 'wt') as check_paired_file:
            num_status = f'Num {num} is paired' if num % 2 == 0 else f'Num {num} is not paired'
            check_paired_file.write(num_status)
    except ValueError:
        raise Exception('It must be a number')


def task_3(path=LEARN_P):
    with open(path, 'rt') as file:
        python_features = [line.rstrip('\n') for line in file]
        return python_features


def task_4(path=LEARN_P):
    with open(path, 'rt') as file:
        python_features = [line.replace('Python', 'C++').rstrip('\n') for line in file]
        return python_features


def task_5(path='guest_book.txt'):
    with open(path, 'a') as file:
        while True:
            name = input()
            if name == '0':
                break
            greeting = f'Welcome! {name}\n'
            file.write(greeting)


def task_6(path='book_1.txt'):
    with open(path, 'rt') as book:
        return book.read().lower().count('the')


def task_7(path):
    with open(path, 'rt') as book:
        formatted_book = book.read().replace('\n', ' ')
    with open('formatted_text.txt', 'wt') as file:
        file.write(formatted_book)


def task_8(path):
    with open(path, 'rt', encoding='UTF-8') as book:
        chapters = [line for line in book if r.match(r'CHAPTER ', line)]

    with open('chapters.txt', 'wt', encoding='UTF-8') as file:
        for elem in chapters:
            file.write(elem + '\n')


def task_9(path):
    with open(path, 'rt', encoding='UTF-8') as book:
        text = book.read()
    all_letters = [letter for letter in text if letter.isalpha()]
    upper_letters = [letter for letter in all_letters if letter.isupper()]

    percentage = (len(upper_letters) / len(all_letters)) * 100
    return f'Percentage of upper letters is {percentage}\n' \
           f'Percentage of lower letters is {100 - percentage}'


def task_10():
    with connect('imdb.db') as db_imdb:
        cur = db_imdb.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS ratings
        (id INTEGER PRIMARY KEY,
        title VARCHAR(20), 
        year INT, 
        rating FLOAT)
        ''')
        with open('imdb.csv', 'r') as file:
            for line in file:
                line = line.strip().rstrip('\n')
                cur.execute('INSERT INTO ratings (title,year,rating) values(?,?,?)', line.split(', '))
                db_imdb.commit()
        cur.execute('SELECT * FROM ratings')
        db_imdb.commit()
        films = cur.fetchall()
        cur.execute('''SELECT * FROM ratings
                            WHERE rating > 8.7
                            order by title''')
        db_imdb.commit()
        films += cur.fetchall()
        cur.execute('''SELECT * FROM ratings
                                order by title''')
        db_imdb.commit()
        films += cur.fetchall()
        # print(films)
        return films


if __name__ == '__main__':
    print(task_10())
