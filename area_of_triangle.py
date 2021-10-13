#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program calculates the area of the triangle
#   with user input


def triangle_area(base_int, height_int):
    # this function calculates the area of a triangle

    area = 0

    # process
    area = base_int * height_int / 2
    print("The area of the triangle is {0} cm²".format(area))


def main():
    # this function accept 2 parameters, base and height (cm)

    # input
    base_str = input("Enter base of the triangle (cm): ")
    height_str = input("Enter height of the triangle (cm): ")
    print("")

    # try and catch
    try:
        base_int = int(base_str)
        height_int = int(height_str)
        print("")

        # call function
        triangle_area(base_int, height_int)
        print("\nDone.")

    except Exception:
        print("{0} and {1} are invalid inputs, try again.".format(base_str, height_str))
        print("\nDone.")


if __name__ == "__main__":
    main()
