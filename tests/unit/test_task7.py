import pytest

from task_7 import validate, Line, Point


@pytest.mark.parametrize('input_value, output_value', [(23, 23.0),
                         ('sdvs', None),
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
    return Line(test_point_a, test_point_b)


@pytest.mark.parametrize('first_point, second_point, summary_point',
                         [(Point(6, 10), Point(12, 20), Point(18, 30))])
def test_add(first_point, second_point, summary_point):
    actual = first_point + second_point
    assert actual.x == summary_point.x and actual.y == summary_point.y


@pytest.mark.parametrize('first_point, second_point, expected_point',
                         [(Point(6, 10), Point(12, 20), Point(-6, -10))])
def test_sub(first_point, second_point, expected_point):
    actual = first_point - second_point
    assert actual.x == expected_point.x and actual.y == expected_point.y


@pytest.mark.parametrize('point, expected_output',
                         [(Point(6, 10), 'x = 6.0, y = 10.0')])
def test_str(point, expected_output):
    actual = str(point)
    assert actual == expected_output


@pytest.mark.parametrize('test_line, expected_output',
                         [(Line(Point(6, 10), Point(12, 20)), 'x = 3.0, y = 5.0')])
def test_find_middle_point(test_line, expected_output):
    actual = test_line.find_middle_point()
    assert str(actual) == expected_output


@pytest.mark.parametrize('test_line, expected_output',
                         [(Line(Point(6, 10), Point(12, 20)), 11.66)])
def test_find_length(test_line, expected_output):
    actual = test_line.find_length()
    assert actual == expected_output


@pytest.mark.parametrize('test_line, expected_output',
                         [(Line(Point(6, 10), Point(12, 20)), 6)])
def test_find_x_projection(test_line, expected_output):
    actual = test_line.find_x_projection()
    assert actual == expected_output


@pytest.mark.parametrize('test_line, expected_output',
                         [(Line(Point(6, 10), Point(12, 20)), 10)])
def test_find_x_projection(test_line, expected_output):
    actual = test_line.find_y_projection()
    assert actual == expected_output
