import pytest

from task_7 import validate, Line, Point


@pytest.mark.parametrize('input_value, output_value', [(23, 23.0),
                         ('12', 12.0)])
def test_validate(input_value, output_value):
    actual = validate(input_value)
    assert actual == output_value


@pytest.fixture()
def test_point_a():
    return Point(6, 10)


@pytest.fixture()
def test_point_b():
    return Point(12, 20)


@pytest.fixture()
def test_line():
    return Line(Point(6, 10), Point(12, 20))


def test_add(test_point_a, test_point_b):
    summary_point = Point(18, 30)
    actual = test_point_a + test_point_b
    assert actual == summary_point


def test_sub(test_point_a, test_point_b):
    expected_point = Point(-6, -10)
    actual = test_point_a - test_point_b
    assert actual == expected_point


def test_str(test_point_a):
    expected_output = 'x = 6.0, y = 10.0'
    actual = str(test_point_a)
    assert actual == expected_output


def test_find_middle_point(test_line):
    expected_output = Point(3, 5)
    actual = test_line.find_middle_point()
    assert actual == expected_output


def test_find_length(test_line):
    expected_output = 11.66
    actual = test_line.find_length()
    assert actual == expected_output


def test_find_x_projection(test_line):
    expected_output = 6
    actual = test_line.find_x_projection()
    assert actual == expected_output


def test_find_y_projection(test_line):
    expected_output = 10
    actual = test_line.find_y_projection()
    assert actual == expected_output
