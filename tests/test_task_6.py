from unittest.mock import mock_open, patch, call

import pytest

from task_6 import task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10

PYTHON_FEATURES = 'In Python you can use functions\n' \
                  'In Python you can use OOP\n' \
                  'In Python you can write classes'
BOOK_1 = 'Several narrative accounts of the navy of the American Revolution have been written. These usually form' \
         ' the introductory part of a history of the American Navy since 1789. The earliest of these accounts is ' \
         'that of Thomas Clark, published in 1814, and probably the best that of James Fenimore Cooper, first ' \
         'printed in 1839. Later narratives are rather more popular than Cooper’s. Many sources of information, which' \
         ' were not accessible to the earlier writers, and were not much used by the later, were drawn upon in' \
         ' the writing of this book. Moreover, the information that is here presented is of a somewhat different ' \
         'sort from that of previous writers; and the method of treatment is new.This book is written from the point ' \
         'of view of the naval administrators; hitherto, historians have written from the point of view of the naval ' \
         'officers. Their narratives treat almost exclusively of the doings at sea, the movements of armed vessels, ' \
         'and the details of sea fights. They have the advantage of dealing primarily with picturesque, and sometimes ' \
         'dramatic, events. Their accounts, however, lack unity, since[Pg 6] they consist of a series of detached ' \
         'incidents.In the first place an attempt has been here made to restore the naval administrative ' \
         'machinery of the Revolution. The center of this narrative is the origin, organization, and work of naval ' \
         'committees, secretaries of marine, navy boards, and naval agents. Next, inasmuch as the men who served as ' \
         'naval executives administered the laws relating to naval affairs, and indeed often prepared these laws ' \
         'before their adoption by the legislative authorities, it was thought best to give a fairly complete resume' \
         ' of the naval legislation of the Revolution. Those laws with which the naval administrators were chiefly' \
         ' concerned have received most attention. The legislation with reference to prize courts and privateering' \
         ' has been treated more briefly. As the privateers do not, properly speaking, form a part of the' \
         ' Revolutionary navy, no attempt to write their history has been made. In order that the subject' \
         ' may be seen in its true relations, some statistics and other interesting facts concerning this industry have, however, been introduced. An account of the State Navies is now given for the first time.Since naval committees, navy boards, and naval agents issued written orders to the naval commanders prescribing the time, place, and manner of their cruises, it has seemed logical and proper to consider the naval policy of the administrators, and the[Pg 7] movements of the armed vessels. So detailed an account of naval movements, as would be given by those writers who proceed from the point of view of the doings of the naval officers, would obviously not be expected in this book. My plan has been to describe the various classes of naval movements, to present the sum total of their results, and to give briefly the details of a few typical cruises and sea fights. The cruises of the American vessels were much alike; they were minor affairs, and many of them scarcely merit individual treatment.It is evident that one who proposes to write the history of the navy of the American Revolution from the point of view which I have described, will not only avoid excessive detail in respect to individual naval achievements, but will be particularly determined not to allow their brilliancy or their dramatic quality to fix the amount of detail with which each shall be narrated. For instance, several historians have been inclined to dwell at some length upon the brilliant and picturesque achievements of John Paul Jones. Sometimes they have devoted more than one-third of their narratives of the Continental navy to this hero, undoubtedly the greatest naval officer of the Revolution. As a result, the pictures which they have presented are somewhat distorted, and many brave sea officers have had scant justice done their gallant services.[Pg 8] An attempt is made in this book to present a better balanced narrative, and to make a juster estimate of the work of the Revolutionary navy. The scope and method of treatment adopted by the author has compelled a certain economy of phrase, precision of statement, and sharpness of outline.TheTheI am very grateful to the many persons who have assisted me. Space does not permit me to thank each of them by name. I am under special obligations to the librarians and officials of the Library of Congress, the Library of the Department of the Navy, the Bureau of Rolls and Library of the Department of State, the State Library of Massachusetts, the Office of the Massachusetts State Archives, the Boston Public Library, the Boston Athenaeum, the library of Harvard University, the State Library of Rhode Island, the Rhode Island Historical Society, the State Library of Connecticut, the Connecticut Historical Society, the Pennsylvania Historical Society, the State Library of Virginia, the Virginia Historical Society, the Office of the Secretary of State of South Carolina, the Charleston (South Carolina) Public Library, and the Library of the University of Chicago. Far more than to any one else, I am indebted to Professor John Franklin Jameson, Director of the Department of Historical Research in the Carnegie Institution of Washington. I have had the advantage of Professor Jameson’s extensive[Pg 9] knowledge of bibliography, his fruitful suggestions as to treatment, and his painstaking care in reading and criticising my manuscript. Parts of the narrative, somewhat popularized, have appeared in the Proceedings of the United States Naval Institute and the Sewanee Review.'


def test_task_1():
    mock_op = mock_open(read_data='1\n12\n23\n54\n46\n23\n98\n32\n65\n23\n57')
    with patch('task_6.open', mock_op):
        expected = 434
        actual = task_1()

        assert actual == expected


@patch('task_6.input')
def test_task_2(mock_in):
    user_input = 22
    expected_output = [call('num_characteristic.txt', 'wt'), call().__enter__(),
                       call().write('Num 22 is paired'), call().__exit__(None, None, None)]
    mock_op = mock_open()
    with patch('task_6.open', mock_op):
        mock_in.return_value = user_input
        task_2()
        assert mock_op.mock_calls == expected_output


@patch('task_6.open')
def test_task_3(mock_op):
    mock_op = mock_open(mock_op, read_data=PYTHON_FEATURES)
    actual = task_3()
    expected_value = ['In Python you can use functions',
                      'In Python you can use OOP',
                      'In Python you can write classes']
    assert actual == expected_value


@patch('task_6.open')
def test_task_4(mock_op):
    mock_op = mock_open(mock_op, read_data=PYTHON_FEATURES)
    actual = task_4()
    expected_output = ['In C++ you can use functions',
                       'In C++ you can use OOP',
                       'In C++ you can write classes']
    assert actual == expected_output


@patch('task_6.open')
@patch('task_6.input')
@pytest.mark.parametrize('input_data, expected_data', [(['0'], [call('guest_book.txt', 'a'),
                                                                call().__enter__(),
                                                                call().__exit__(None, None, None)]),
                                                       (['bro', '0'], [call('guest_book.txt', 'a'),
                                                                       call().__enter__(),
                                                                       call().write('Welcome! bro\n'),
                                                                       call().__exit__(None, None, None)])])
def test_task_5(mock_i, mock_op, input_data, expected_data):
    mock_op = mock_open(mock_op)
    mock_i.side_effect = input_data
    task_5()
    actual = mock_op.mock_calls
    assert actual == expected_data


@patch('task_6.open')
def test_task_6(mock_op):
    mock_op = mock_open(mock_op, read_data=BOOK_1)
    actual = task_6()
    expected = 123
    assert actual == expected


@patch('task_6.open')
def test_task_7(mock_op):
    mock_op = mock_open(mock_op, read_data='theThetih\nsbhs\nkbnsk\nfmbSL:bnlsn\nthekb;nsdkgThethe')
    task_7('test_t7.txt')
    actual = mock_op.mock_calls
    expected = [call('test_t7.txt', 'rt'),
                call().__enter__(),
                call().read(),
                call().__exit__(None, None, None),
                call('formatted_text.txt', 'wt'),
                call().__enter__(),
                call().write('theThetih sbhs kbnsk fmbSL:bnlsn thekb;nsdkgThethe'),
                call().__exit__(None, None, None)]
    assert actual == expected


@patch('task_6.open')
def test_task_8(mock_op):
    mock_op = mock_open(mock_op, read_data='''CHAPTER I. START IN LIFE\n

CHAPTER II. SLAVERY AND ESCAPE

CHAPTER III. WRECKED ON A DESERT ISLAND

CHAPTER IV. FIRST WEEKS ON THE ISLAND

CHAPTER V. BUILDS A HOUSE—THE JOURNAL

CHAPTER VI. ILL AND CONSCIENCE-STRICKEN

CHAPTER VII. AGRICULTURAL EXPERIENCE

CHAPTER VIII. SURVEYS HIS POSITION

CHAPTER IX. A BOAT
wrbbwrbwb
CHAPTER X. TAMES GOATS
wwrbwrbwrb
CHAPTER XI. FINDS PRINT OF MAN’S FOOT ON THE SAND
wrbwrb
CHAPTER XII. A CAVE RETREAT
wrbrbwr
CHAPTER XIII. WRECK OF A SPANISH SHIP
wrbwrb
CHAPTER XIV. A DREAM REALISED
rbwbrw
CHAPTER XV. FRIDAY’S EDUCATION
wrbwrb
CHAPTER XVI. RESCUE OF PRISONERS FROM CANNIBALS
webwrbr
CHAPTER XVII. VISIT OF MUTINEERS
wgebweb
CHAPTER XVIII. THE SHIP RECOVERED
wrnwn
CHAPTER XIX. RETURN TO ENGLAND
wrnwrnwrn
CHAPTER XX. FIGHT BETWEEN FRIDAY AND A BEAR
wewhw
welmgwelmglwmergwmgwrmg''')
    task_8('test_t8.txt')
    actual = mock_op.mock_calls
    expected = [call('test_t8.txt', 'rt', encoding='UTF-8'),
                call().__enter__(),
                call().__iter__(),
                call().__exit__(None, None, None),
                call('chapters.txt', 'wt', encoding='UTF-8'),
                call().__enter__(),
                call().write('CHAPTER I. START IN LIFE\n\n'),
                call().write('CHAPTER II. SLAVERY AND ESCAPE\n\n'),
                call().write('CHAPTER III. WRECKED ON A DESERT ISLAND\n\n'),
                call().write('CHAPTER IV. FIRST WEEKS ON THE ISLAND\n\n'),
                call().write('CHAPTER V. BUILDS A HOUSE—THE JOURNAL\n\n'),
                call().write('CHAPTER VI. ILL AND CONSCIENCE-STRICKEN\n\n'),
                call().write('CHAPTER VII. AGRICULTURAL EXPERIENCE\n\n'),
                call().write('CHAPTER VIII. SURVEYS HIS POSITION\n\n'),
                call().write('CHAPTER IX. A BOAT\n\n'),
                call().write('CHAPTER X. TAMES GOATS\n\n'),
                call().write('CHAPTER XI. FINDS PRINT OF MAN’S FOOT ON THE SAND\n\n'),
                call().write('CHAPTER XII. A CAVE RETREAT\n\n'),
                call().write('CHAPTER XIII. WRECK OF A SPANISH SHIP\n\n'),
                call().write('CHAPTER XIV. A DREAM REALISED\n\n'),
                call().write('CHAPTER XV. FRIDAY’S EDUCATION\n\n'),
                call().write('CHAPTER XVI. RESCUE OF PRISONERS FROM CANNIBALS\n\n'),
                call().write('CHAPTER XVII. VISIT OF MUTINEERS\n\n'),
                call().write('CHAPTER XVIII. THE SHIP RECOVERED\n\n'),
                call().write('CHAPTER XIX. RETURN TO ENGLAND\n\n'),
                call().write('CHAPTER XX. FIGHT BETWEEN FRIDAY AND A BEAR\n\n'),
                call().__exit__(None, None, None)]
    assert actual == expected


@patch('task_6.open')
def test_task_9(mock_op):
    mock_op = mock_open(mock_op, read_data='''The Project Gutenberg eBook of The Count of Monte Cristo, by Alexandre Dumas, père

This eBook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this eBook or online at
www.gutenberg.org. If you are not located in the United States, you
will have to check the laws of the country where you are located before
using this eBook.

Title: The Count of Monte Cristo

Author: Alexandre Dumas, père

Release Date: January, 1998 [eBook #1184]
[Last updated: October 14, 2022]

''')
    actual = task_9('test_t9.txt')
    expected = f'Percentage of upper letters is 7.269155206286837\n' \
               f'Percentage of lower letters is 92.73084479371316'
    assert actual == expected


@patch('task_6.open')
def test_task_10(mock_op):
    mock_op = mock_open(mock_op, read_data='''The Shawshank Redemption, 1994, 9.2
The Godfather, 1972, 9.2
The Dark Knight, 2008, 9.0
V for Vendetta, 2005, 8.2
The Big Lebowski, 1998, 8.1
Ratatouille, 2007, 8.0
''')
    expected = [(1, 'The Shawshank Redemption', 1994, 9.2), (2, 'The Godfather', 1972, 9.2),
                (3, 'The Dark Knight', 2008, 9.0), (4, 'V for Vendetta', 2005, 8.2), (5, 'The Big Lebowski', 1998, 8.1),
                (6, 'Ratatouille', 2007, 8.0), (3, 'The Dark Knight', 2008, 9.0), (2, 'The Godfather', 1972, 9.2),
                (1, 'The Shawshank Redemption', 1994, 9.2), (6, 'Ratatouille', 2007, 8.0),
                (5, 'The Big Lebowski', 1998, 8.1), (3, 'The Dark Knight', 2008, 9.0), (2, 'The Godfather', 1972, 9.2),
                (1, 'The Shawshank Redemption', 1994, 9.2), (4, 'V for Vendetta', 2005, 8.2)]
    print(len(expected))
    actual = task_10()
    assert actual == expected
