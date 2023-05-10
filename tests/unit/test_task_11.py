from unittest.mock import mock_open, patch

from task_11 import task_1, task_2, task_3

DATES = '20.12.2000, jsbnidnbsind 2001/02/01fnkfonkkg0kojog ghoro or roko ok hot 2003/1/17. sdfj jaopfjwpo jwjfpwqj ,' \
        ' jsfpoqwph pw2i12049 12.4.2004, 8.8.2008'
SENTENCES = 'Web scraping is an important skill for data scientists. I have developed a number of ad hoc web' \
            ' scraping projects using Python, BeautifulSoup, ' \
            'and Scrapy in the past few years and read a few books and' \
            ' tons of online tutorials along the way. However, I have not found a simple beginner level tutorial that' \
            ' is end-to-end in the sense that covers all basic steps and concepts in a typical Scrapy web scraping' \
            ' project (therefore Minimalist in the title) — that’s why I am writing this and hope the code repo can' \
            ' serve as a template to help jumpstart your web scraping projects.Many people ask: should I use ' \
            'BeautifulSoup or Scrapy? They are different things: BeautifulSoup is a library for parsing HTML and XML ' \
            'and Scrapy is a web scraping framework. You can use BeautifulSoup instead of Scrapy build-in selectors ' \
            'if you want but comparing BeautifulSoup to Scrapy is like comparing the Mac keyboard to the iMac or' \
            ' a better metaphor as stated in the official documentation “like comparing jinja2 to Django” if you' \
            ' know what they are :) — In short, you' \
            ' should learn Scrapy if you want to do serious and systematic web scraping.'
EVENTS = 'A Song of Ice and Fire is a series of epic fantasy novels written by American novelist and screenwriter ' \
         'George Martin, he began writing the series in 1991.' \
         'A Game of Thrones is the first of seven planned novels in A Song of Ice and Fire, an epic fantasy series ' \
         'by American author George Martin, it was first published on 6 August 1996.' \
         'A Clash of Kings is the second of seven planned novels in A Song of Ice and Fire, an epic fantasy series ' \
         'by American author George Martin, it was first published on November 16, 1998.' \
         'A Storm of Swords is the third of seven planned novels in A Song of Ice and Fire, an epic fantasy series ' \
         'by American author George Martin, It was first published on August 8, 2000.'


@patch('task_11.open')
def test_task_1(mock_op):
    mock_op = mock_open(mock_op, read_data=DATES)
    user_input = 'dates.txt'
    actual = task_1(user_input)
    expected_value = ['20.12.2000', '12.04.2004', '08.08.2008', '01.02.2001', '17.01.2003']
    assert actual == expected_value


@patch('task_11.open')
def test_task_2(mock_op):
    mock_op = mock_open(mock_op, read_data=SENTENCES)
    user_input = 'some_text.txt'
    actual = task_2(user_input)
    expected_value = ['Web scraping is an important skill for data scientists.',
                      'I have developed a number of ad hoc web scraping projects using Python, BeautifulSoup,'
                      ' and Scrapy in the past few years and read a few books and tons of online'
                      ' tutorials along the way.',
                      'However, I have not found a simple beginner level tutorial that is end-to-end in the sense that '
                      'covers all basic steps and concepts in a typical Scrapy web scraping project '
                      '(therefore Minimalist in the title) — that’s why I am writing this and hope the code repo'
                      ' can serve as a template to help jumpstart your web scraping projects.',
                      'Many people ask: should I use BeautifulSoup or Scrapy?',
                      'They are different things: BeautifulSoup is a library for parsing HTML and XML and Scrapy'
                      ' is a web scraping framework.',
                      'You can use BeautifulSoup instead of Scrapy build-in selectors if you want but comparing '
                      'BeautifulSoup to Scrapy is like comparing the Mac keyboard to the iMac or a better metaphor as'
                      ' stated in the official documentation “like comparing jinja2 to Django” if you know what they '
                      'are :) — In short, you should learn Scrapy if you want to '
                      'do serious and systematic web scraping.']

    assert expected_value == actual


@patch('task_11.open')
def test_task_3(mock_op):
    mock_op = mock_open(mock_op, read_data=EVENTS)
    user_input = 'events.txt'
    actual = task_3(user_input)
    expected_value = {'1991': 'A Song of Ice and Fire is a series of epic fantasy novels written by American novelist '
                              'and screenwriter George Martin, he began writing the series in 1991.',
                      '1996': 'A Game of Thrones is the first of seven planned novels in A Song of Ice and Fire, '
                              'an epic fantasy series by American author George Martin, it was first published on '
                              '6 August 1996.',
                      '1998': 'A Clash of Kings is the second of seven planned novels in A Song of Ice and Fire, an '
                              'epic fantasy series by American author George Martin, it was first published '
                              'on November 16, 1998.',
                      '2000': 'A Storm of Swords is the third of seven planned novels in A Song of Ice and Fire, '
                              'an epic fantasy series by American author George Martin, It was first published '
                              'on August 8, 2000.'}
    assert actual == expected_value
