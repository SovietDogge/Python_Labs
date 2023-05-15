from sqlite3 import connect
import re as r


NUM_CHECK_PAIRED = 'num_characteristic.txt'


def task_1():
    with open('numbers.txt', 'rt') as nums:
        amount = sum([float(num) for num in nums])

    with open('amount.txt', 'wt') as file:
        file.write(str(amount))
    return amount


def task_2():
    try:
        num = int(input('Enter any number: '))
        with open(NUM_CHECK_PAIRED, 'wt') as check_paired_file:
            num_status = f'Num {num} is paired' if num % 2 == 0 else f'Num {num} is not paired'
            check_paired_file.write(num_status)
    except ValueError:
        raise Exception('It must be a number')


def task_3():
    with open('learning_python.txt', 'rt') as file:
        python_features = [line.rstrip('\n') for line in file]
        return python_features


def task_4():
    with open('learning_python.txt', 'rt') as file:
        python_features = [line.replace('Python', 'C++').rstrip('\n') for line in file]
        return python_features


def task_5():
    with open('guest_book.txt', 'a') as file:
        while True:
            name = input()
            if name == '0':
                break
            greeting = f'Welcome! {name}\n'
            file.write(greeting)


def task_6():
    with open('book_1.txt', 'rt') as book:
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
    count_upper_letters = 0
    count_lower_letters = 0
    with open(path, 'rt', encoding='UTF-8') as book:
        text = book.read()

        for letter in text:
            if letter.isalpha():
                if letter in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                    count_upper_letters += 1
                elif letter in 'qwertyuiopasdfghjklzxcvbnm':
                    count_lower_letters += 1

    count_letters = count_upper_letters + count_lower_letters
    return f'Percentage of upper letters is {(count_upper_letters / count_letters) * 100}\n' \
           f'Percentage of lower letters is {(count_lower_letters / count_letters) * 100}'


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
                print(line.split(', '))
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
        return films


if __name__ == '__main__':
    print(task_10())