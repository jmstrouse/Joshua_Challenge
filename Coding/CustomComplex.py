"""
A custom type for complex numbers.

Written for: https://www.hackerrank.com/challenges/
  class-1-dealing-with-complex-numbers/problem

Uses Python 3.8.0
"""


class Complex(object):
    """A custom, hand-written complex number type."""

    def __init__(self, real, imaginary):
        """Sets initial values for the number, real and imaginary."""
        pass

    def __add__(self, no):
        """Provides support for the addition(+) operator."""
        pass

    def __sub__(self, no):
        """Provides support for the subtraction(-) operator."""
        pass

    def __mul__(self, no):
        """Provides support for the multiplication(*) operator."""
        pass

    def __truediv__(self, no):
        """Provides support for the division(/) operator."""
        pass

    def mod(self):
        """Returns the modulous of the number."""
        pass

    def __str__(self):
        """Provides a human-readable representation of the number."""
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
