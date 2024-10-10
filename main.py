from AD8_2.AbhishekDubey_8_2 import nmap_scan


def option_1():
   target = "apache.org"
   port = 22
   nmap_scan(target, port, 1)

def option_2():
    return "Option 2 selected"


def option_3():
    return "Option 3 selected"


def option_4():
    return "Option 4 selected"


def option_5():
    return "Option 5 selected"


def option_6():
    return "Option 6 selected"


def option_7():
    return "Option 7 selected"


def option_8():
    return "Option 8 selected"


def option_9():
    return "Option 9 selected"


def option_10():
    return "Option 10 selected"


def option_11():
    return "Option 11 selected"


def option_12():
    return "Option 12 selected"


def main():
    switch = {
        1: option_1,
        2: option_2,
        3: option_3,
        4: option_4,
        5: option_5,
        6: option_6,
        7: option_7,
        8: option_8,
        9: option_9,
        10: option_10,
        11: option_11,
        12: option_12
    }

    choice = int(input("Enter a number between 1 and 12: "))
    result = switch.get(choice, lambda: "Invalid option")()
    print(result)


if __name__ == "__main__":
    main()
