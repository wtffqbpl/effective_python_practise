#!/usr/bin/env python
# coding:utf-8
# Author: Yuanjun Ren


class Meta(type):
    def __new__(mcs, name, bases, class_dict):
        print((mcs, name, bases, class_dict))
        return type.__new__(mcs, name, bases, class_dict)


class MyClass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass


class ValidatePolygon(type):
    def __new__(mcs, name, bases, class_dict):
        # Don't validate the abstract Polygon class.
        if bases != (object, ):
            if class_dict['sides'] < 3:
                raise ValueError("Polygons need 3+ sides.")
        return type.__new__(mcs, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None  # Specified by subclasses

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3
    pass


if __name__ == "__main__":
    pass
