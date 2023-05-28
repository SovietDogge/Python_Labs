import math as m

from utils import validate


class Point:
    def __init__(self, x_value, y_value):
        self.__x = validate(x_value)
        self.__y = validate(y_value)

    def __str__(self):
        return f'x = {self.__x}, y = {self.__y}'

    def __sub__(self, other):
        coord_x = self.__x - other.x
        coord_y = self.__y - other.y
        return Point(coord_x, coord_y)

    def __add__(self, other):
        coord_x = self.__x + other.__x
        coord_y = self.__y + other.__y
        return Point(coord_x, coord_y)

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    @property
    def coord_x(self):
        return self.__x

    @coord_x.setter
    def coord_x(self, value):
        self.__x = validate(value)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = validate(value)


class Line:

    def __init__(self, first_point, second_point):
        self.__start_point = first_point
        self.__end_point = second_point

    def find_middle_point(self):
        return Point(((self.__end_point.x - self.__start_point.x) / 2),
                     (self.__end_point.y - self.__start_point.y) / 2)

    def find_length(self):
        return round(m.sqrt((self.__end_point.x - self.__start_point.x) ** 2 +
                            (self.__end_point.y - self.__start_point.y) ** 2), 2)

    def find_x_projection(self):
        return abs(self.__end_point.x - self.__start_point.x)

    def find_y_projection(self):
        return abs(self.__end_point.y - self.__start_point.y)


if __name__ == '__main__':
    a = Point('6', 10)
    b = Point(12, 20)
    print(a == b)
    exmpl = Line(a, b)
    # print(exmpl.find_middle_point())
    # print(exmpl.find_length())
    # print(exmpl.find_x_projection())
    # print(exmpl.find_y_projection())
