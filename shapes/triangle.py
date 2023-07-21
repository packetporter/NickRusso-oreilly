"""
Author: PacketPorter
File: triangle.py
Purpose: Defines a triangle object, inherited from the abstract class Shape.
"""

from collections import Counter
from math import sqrt
from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and containes leghts of the sides of a triangle
    """

    def __init__(self, side_1, side_2, side_3):
        print(side_1, side_2, side_3)
        self.side_1 = int(side_1)
        self.side_2 = int(side_2)
        self.side_3 = int(side_3)
        self.all_sides = [self.side_1, self.side_2, self.side_3]

    def perimeter(self):
        """
        Compute the perimeter by adding all the sides of a triangle
        """
        return sum(self.all_sides)
    
    def area(self):
        """
        compute the area using 1/2 * base * height
        """
        print(f"Height is {self._height()} and base is {self._base()}")
        return 0.5 * self._height() * self._base()

    def _height(self):
        """
        Derive the height of a triangle, depends on type
        """
        if self.is_equilateral():
            return sqrt((self.side_1 ** 2) - ((self.side_1/2) ** 2))
        
        elif self.is_scalene():
            return sqrt((self.side_3 ** 2) - (self.side_1 ** 2 +
                                       self.side_3 ** 2 -
                                       self.side_2 ** 2)/ (2 * self.side_1))
        elif self.is_isosceles():
            base = self._base()
            hypotenuse = list(set([side for side in self.all_sides if side != base]))
            return sqrt((hypotenuse[0] ** 2 ) - (base/2 ** 2))
    
    def _base(self):
        if self.is_isosceles():
            sides_count = Counter(self.all_sides)
            for key,value in sides_count.items():
                if value == 1:
                    side_base = key
                    return side_base
        return self.all_sides[0]

    def is_equilateral(self):
        return (
            self.side_1 == self.side_2 and
            self.side_1 == self.side_3
        )
    def is_isosceles(self):
        return (
            self.side_1 == self.side_2 and self.side_1 !=self.side_3 or
            self.side_2 == self.side_3 and self.side_2 != self.side_1 or
            self.side_1 == self.side_3 and self.side_1 != self.side_2
        )
    
    def is_scalene(self):
        return (
            self.side_1 != self.side_2 and
            self.side_1 != self.side_3 and
            self.side_2 != self.side_3
        )