# Programmer: Kayla Cashwell
# Date: 6/23/24
# Purpose: Day 8 Challenge - Program a Ticket Vending Machine
"""
Note: This program works but does not fulfill all the parameters outlined in the
prompt and lessons learned prior to the challenge. Such as Error handling and usage
of the decorator. The decorator is defined but not used here. Iteration 2 of this program
should have those components added.
"""

import numbers
import sys


def menu():
    print("[P] Perfumes\n[M] Medicine\n[C] Cosmetics\n")
    department = input("Choose department: ")
    return department


def again():
    continue_order = input("Would you like to pick another ticket? ")
    if continue_order.upper() == "Y" or continue_order == "yes":
        department = menu()
        return department

    else:
        print("ending program.")
        sys.exit(0)

def main():
    pick = menu()
    perfume_generator = numbers.perfumes()
    medicine_generator = numbers.medicine()
    cosmetics_generator = numbers.cosmetics()
    # wait = info(numbers.perfume)

    while pick:
        if pick.upper() == "P":
            print(next(perfume_generator))
            pick = again()

        if pick.upper() == "M":
            print(next(medicine_generator))
            pick = again()

        if pick.upper() == "C":
            print(next(cosmetics_generator))
            pick = again()


if __name__ == '__main__':
    main()
