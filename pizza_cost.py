#!/usr/bin/env python3
# Created by: Minab Berhane
# Created on: Oct 6, 2022
# This program asks the user for the diameter of the
# pizza. It then calculates and displays the total cost
# of the pizza with tax
import constant
import math


def main():
    # input
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # process
    subtotal = (
        constant.LABOUR_COST + constant.RENTAL_COST + (constant.INGRED_COST * diameter)
    )

    tax = constant.HST * subtotal
    total = subtotal + tax

    # output
    print("")
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
