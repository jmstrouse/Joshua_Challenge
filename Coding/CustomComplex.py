"""
A custom type for complex numbers.

Written for: https://www.hackerrank.com/challenges/
  class-1-dealing-with-complex-numbers/problem

Uses Python 3.8.0
"""


from math import sqrt


class Complex(object):
    """A custom, hand-written complex number type."""

    def __init__(self, real, imag):
        """Sets initial values for the number, real and imaginary."""
        self.real = real
        self.imag = imag

    def __add__(self, no):
        """Provides support for the addition(+) operator."""
        return Complex(self.real + no.real, self.imag + no.imag)

    def __sub__(self, no):
        """Provides support for the subtraction(-) operator."""
        return Complex(self.real - no.real, self.imag - no.imag)

    def __mul__(self, no):
        """Provides support for the multiplication(*) operator."""
        x, y = self.real, self.imag
        u, v = no.real, no.imag
        newReal = (x * u) - (y * v)
        newImag = (x * v) + (y * u)
        return Complex(newReal, newImag)

    def __truediv__(self, no):
        """Provides support for the division(/) operator."""
        x, y = self.real, self.imag
        u, v = no.real, no.imag
        newReal = (x * u) + (y * v)
        newImag = (y * u) - (x * v)
        newReal /= u ** 2 + v ** 2
        newImag /= u ** 2 + v ** 2
        return Complex(newReal, newImag)

    def mod(self):
        """Returns the modulous of the number."""
        newReal = sqrt(self.real ** 2 + self.imag ** 2)
        return Complex(newReal, 0.0)

    def __str__(self):
        """Provides a human-readable representation of the number."""
        sign = "+" if self.imag >= 0.0 else ""
        return "%.2f%s%.2fi" % (self.real, sign, self.imag)
