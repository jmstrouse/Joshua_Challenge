"""
Provides automated and manual testing of the CustomComplex type.

Written for: https://www.hackerrank.com/challenges/
  class-1-dealing-with-complex-numbers/problem

Uses Python 3.8.0
"""


import sys

from CustomComplex import Complex


def AutoTest():
    """
    Perform a series of automatic tests on the CustomComplex type.

    Return True if all tests succeeded, False otherwise.
    """


def ManualTest():
    """
    Perform a manual test of the CustomComplex type by asking for two
    complex numbers, one per line. Do a full set of calculations and
    print results.
    """
    pass


if __name__ == "__main__":
    if '--manual' in sys.argv:
        ManualTest()
    else:
        if AutoTest():
            sys.exit(0)
        else:
            sys.exit(1)
