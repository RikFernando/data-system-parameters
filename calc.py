# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys


def main():
    """Implement the calculator"""
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[3])
    if sys.argv[2] == "+":
        return arg1 + arg2
    if sys.argv[2] == "*":
        return arg1 * arg2
    if sys.argv[2] == "-":
        return arg1 - arg2



if __name__ == "__main__":
    print(main())
