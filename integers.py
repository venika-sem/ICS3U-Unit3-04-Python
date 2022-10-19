#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: oct 2022
# This program tells user if integer is positive, negative, or zero

import math


def main():
    # this function tells user if integer is positive, negative, or zero

    # input
    integer = int(input("Enter a any integer: "))
    print("")

    # process & output
    if integer > 0:
        print("{0} is a positive number.".format(integer))

    elif integer < 0:
        print("{0} is a negative number.".format(integer))

    elif integer == 0:
        print("{0} is a just zero!".format(integer))

    else:
        print("No idea!")

    print("\nDone.")


if __name__ == "__main__":
    main()
