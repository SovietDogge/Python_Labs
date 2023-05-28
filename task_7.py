import math as m

from utils import validate


class Point:
    def __init__(self, x_value, y_value):
        self.__x = validate(x_value)
        self.__y = validate(y_value)

    def __str__(self):
        return f'x = {self.__x}, y = {self.__y}'

    def __sub__(self, other):
        coord_x = self.__x - other.coord_x
        coord_y = self.__y - other.coord_y
        return Point(coord_x, coord_y)

    def __add__(self, other):
        coord_x = self.__x + other.coord_x
        coord_y = self.__y + other.coord_y
        return Point(coord_x, coord_y)

    def __eq__(self, other):
        return self.__x == other.coord_x and self.__y == other.coord_y

    @property
    def coord_x(self):
        return self.__x

    @coord_x.setter
    def coord_x(self, value):
        self.__x = validate(value)

    @property
    def coord_y(self):
        return self.__y

    @coord_y.setter
    def coord_y(self, value):
        self.__y = validate(value)


class Line:

    def __init__(self, first_point, second_point):
        self.__start_point = first_point
        self.__end_point = second_point

    def find_middle_point(self):
        return Point(((self.__end_point.coord_x - self.__start_point.coord_x) / 2),
                     (self.__end_point.coord_y - self.__start_point.coord_y) / 2)

    def find_length(self):
        return round(m.sqrt((self.__end_point.coord_x - self.__start_point.coord_x) ** 2 +
                            (self.__end_point.coord_y - self.__start_point.coord_y) ** 2), 2)

    def find_x_projection(self):
        return abs(self.__end_point.coord_x - self.__start_point.coord_x)

    def find_y_projection(self):
        return abs(self.__end_point.coord_y - self.__start_point.coord_y)


if __name__ == '__main__':
    a = Point('6', 10)
    b = Point(12, 20)
    print(a == b)
    exmpl = Line(a, b)
    # print(exmpl.find_middle_point())
    # print(exmpl.find_length())
    # print(exmpl.find_x_projection())
    # print(exmpl.find_y_projection())
