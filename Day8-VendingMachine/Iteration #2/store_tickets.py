# Programmer: Kayla Cashwell
# Date: 6/26/24
# Purpose: Day 8 -Program vending machine - Iteration #2

"""
Note: This program should include concepts such as decorators, generators and error handling.
"""

# generator definition yields the results
def perfume():
    for x in range(1, 10001):
        yield f"P - {x}"

def medicine():
    for x in range(1, 10001):
        yield f"M - {x}"

def cosmetic():
    for x in range(1, 10001):
        yield f"C - {x}"

# generators require the next keyword
p = next(perfume())
m = next(medicine())
c = next(cosmetic())


# decorator definition
def ticket_dispense(func):

    if func == p:
        print(f"Your number is {p}.")
        print(f"Please wait to be seated")

    elif func == m:
        print(f"Your number is {m}.")
        print(f"Please wait to be seated.")

    else:
        print(f"Your number is {c}.")
        print(f"Please wait to be seated.")