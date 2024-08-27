def perfumes():
    for x in range(1, 100001):
        yield f"P-{x}"


def medicine():
    for x in range(1, 100001):
        yield  f"M-{x}"


def cosmetics():
    ticket_num = 0
    yield f"C-{ticket_num}"
    ticket_num += 1


def info(func):
    def wait_time():
        ticket = func()
        print(f"Your number is {ticket}")
        print("Wait and someone will be with you shortly.")
    return wait_time()
