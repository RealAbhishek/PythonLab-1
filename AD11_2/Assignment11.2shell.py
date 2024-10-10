

def session8_1():
    decisions()
    return "Session 8.1"


def session8_2():
    decisions()
    return "Session 8.2"


def session8_3():
    decisions()


def session8_4():
    decisions()
    return "Session 8.4"


def session8_5():
    decisions()
    return "Session 8.5"


def session8_6():
    decisions()
    return "Session 8.6"


def sessionswitcher(argument):
    switcher = menu()
    func = switcher.get(argument, "nothing")
    return func()


def decisions():
    stayorgo = input("Should I stay or should I go? stay or go")
    if stayorgo == "stay":
        main()
    elif stayorgo == "go":
        print("goodbye!")
        exit()
    decisions()


def menu():
    mymenu = {
        1: session8_1,
        2: session8_2,
        3: session8_3,
        4: session8_4,
        5: session8_5,
        6: session8_6
    }
    return mymenu

def main():
    banner()
    mymenu = menu()
    print("Assignment 11.2 Steven Richard")
    print("Please type in a number between 1 and 6 to view the output from the sessions.")
    for key, value in mymenu.items():
        print(key, ' : ', value.__name__.replace("_","."))
    userinput = int(input("Enter the number of the session to run"))
    sessionswitcher(userinput)


if __name__ == "__main__":
    main()
