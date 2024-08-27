# Programmer: Kayla Cashwell
# Date: 6/26/24
# Purpose: Day 8 -Program vending machine - Iteration #2

import store_tickets


def options():
    print("\n[P] - Perfumes\n[M] - Medicine\n[C] - Cosmetics\n")


def greeting():

    while True:
        options()
        try:
            department = input("Choose Department: ")
            if department.upper() == "C":
                store_tickets.ticket_dispense(store_tickets.c)
            if department.upper() == "P":
                store_tickets.ticket_dispense(store_tickets.p)
            if department.upper() == "M":
                store_tickets.ticket_dispense(store_tickets.m)


        except:
            print("Invalid choice, please enter the correct option")
            options()

greeting()












