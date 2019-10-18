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

    def _handle_test(msg, actual, expected):
        r = actual is expected
        if r:
            print(f"[ OK ] {msg}")
        else:
            print(f"[FAIL] {msg} (expected: {expected})")
        return r

    fullResult = True
    testData = [
        {
            "input_x":      (2, 1),
            "input_y":      (5, 6),
            "add_result":   "7.00+7.00i",
            "sub_result":   "-3.00-5.00i",
            "mult_result":  "4.00+17.00i",
            "div_result":   "0.26-0.11i",
            "mod_x_result": "2.24+0.00i",
            "mod_y_result": "7.81+0.00i",
        },
        {
            "input_x":      (5.9, 6),
            "input_y":      (9, 10),
            "add_result":   "14.90+16.00i",
            "sub_result":   "-3.10-4.00i",
            "mult_result":  "-6.90+113.00i",
            "div_result":   "0.62-0.03i",
            "mod_x_result": "8.41+0.00i",
            "mod_y_result": "13.45+0.00i",
        }
    ]

    print("Begin CustomComplex automated test.")
    for i, test in enumerate(testData, start=1):
        testResult = True
        print(f"Starting test {i} of {len(testData)}.")

        x = Complex(*test["input_x"])
        y = Complex(*test["input_y"])

        addResult = str(x + y)
        msg = "{x!s} + {y!s} = {addResult}"
        if not _handle_test(msg, addResult, test["add_result"]):
            testResult = False

        subResult = str(x - y)
        msg = "{x!s} - {y!s} = {subResult}"
        if not _handle_test(msg, subResult, test["sub_result"]):
            testResult = False

        multResult = str(x * y)
        msg = "{x!s} * {y!s} = {multResult}"
        if not _handle_test(msg, multResult, test["mult_result"]):
            testResult = False

        divResult = str(x / y)
        msg = "{x!s} / {y!s} = {divResult}"
        if not _handle_test(msg, divResult, test["div_result"]):
            testResult = False

        modXResult = str(x.mod())
        msg = "mod({x!s}) = {modXResult}"
        if not _handle_test(msg, modXResult, test["mod_x_result"]):
            testResult = False

        modYResult = str(y.mod())
        msg = "mod({y!s}) = {modYResult}"
        if not _handle_test(msg, modYResult, test["mod_y_result"]):
            testResult = False

        print(f"Finishing test {i} of {len(testData)}.")

        if not testResult:
            fullResult = False

    if fullResult:
        print("Full Test Result: PASS")
    else:
        print("Full Test Result: FAIL")

    return fullResult


def ManualTest():
    """
    Perform a manual test of the CustomComplex type by asking for two
    complex numbers, one per line. Do a full set of calculations and
    print results.
    """
    print("Input values for X, seperated by a space.")
    c = map(float, input().split())
    print("Input values for Y, seperated by a space.")
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')


if __name__ == "__main__":
    if "--manual" in sys.argv:
        ManualTest()
    else:
        if AutoTest():
            sys.exit(0)
        else:
            sys.exit(1)
