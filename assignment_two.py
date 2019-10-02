#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: October 2019
# This program calculates the area of a sector of a circle

import math


def main():
    # This function calculates the area of a sector of a circle

    # input
    radius = int(input("Enter the radius: "))
    angle_θ = int(input("Enter the angle θ: "))

    # process
    area = math.pi * radius ** 2 * angle_θ / 360

    # output
    print("")
    print("The area is: {:,.2f}cm^2 "
          .format(area))


if __name__ == "__main__":
    main()
