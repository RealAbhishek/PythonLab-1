from Banner import banner
from removematches import removeMatches
from railfence import railDecrypt
from railfence import railBreak
from letterfrequency1 import letterFrequency
from letterfrequency1 import readFile
from letterfrequency1 import getFreq

def session8_1():
    """
    Decrypts the given cipher text using the rail fence cipher with varying key lengths.
    """
    print("Setting the cipher text for session 8.1")
    cipherText = "n aci mreidontoowp mgorw"
    print("Decrypting the cipher text using rail fence cipher with varying key lengths")
    for i in range(2, len(cipherText) + 1):
        print(railDecrypt(cipherText, i))
    print("Making a decision to stay or go")
    decisions()
    return "Session 8.1"

def session8_2():
    """
    Breaks the rail fence cipher for the given cipher text.
    """
    print("Setting the cipher text for session 8.2")
    cipherText = "n aci mreidontoowp mgorw"
    print("Breaking the rail fence cipher")
    print(railBreak(cipherText))
    print("Making a decision to stay or go")
    decisions()
    return "Session 8.2"

def session8_3():
    """
    Removes non-letter characters from the given text.
    """
    print("Setting the text for session 8.3")
    text = 'Are there 25, 26, or 27 non-letters to remove?'
    print("Converting text to lowercase")
    text = text.lower()
    print(text)
    print("Removing non-letter characters from the text")
    nonLetters = removeMatches(text, 'abcdefghijklmnopqrstuvwxyz')
    print(nonLetters)
    text = removeMatches(text, nonLetters)
    print(text)
    print("Making a decision to stay or go")
    decisions()

def session8_4():
    """
    Reads cipher text from a file and calculates the letter frequency.
    """
    print("Reading the cipher text from file for session 8.4")
    text = readFile('cipherText.txt')
    print("Calculating letter frequency of the text")
    lf = letterFrequency(text)
    print("Printing letter frequencies")
    for letter in lf:
        print(letter, lf.get(letter))
    print("Making a decision to stay or go")
    decisions()
    return "Session 8.4"

def session8_5():
    """
    Sorts a list of numbers in descending order.
    """
    print("Setting the list for session 8.5")
    xlist = [3, 7, 4, 9]
    print("Sorting the list in descending order")
    xlist.sort(reverse=True)
    print(xlist)
    print("Making a decision to stay or go")
    decisions()
    return "Session 8.5"

def session8_6():
    """
    Reads cipher text from a file, calculates letter frequency, and sorts the frequencies in descending order.
    """
    print("Reading the cipher text from file for session 8.6")
    text = readFile('cipherText.txt')
    print("Calculating letter frequency of the text")
    lf = letterFrequency(text)
    print("Sorting letter frequencies in descending order")
    lfList = list(lf.items())
    lfList.sort(key=getFreq, reverse=True)
    print("Printing sorted letter frequencies")
    for entry in lfList:
        print("{0} {1:.3f}".format(entry[0], entry[1]))
    print("Making a decision to stay or go")
    decisions()
    return "Session 8.6"

def sessionswitcher(argument):
    """
    Switches to the selected session function based on user input.
    """
    print("Switching to the selected session function")
    switcher = menu()
    func = switcher.get(argument, "nothing")
    return func()

def decisions():
    """
    Asks the user whether to stay or go, and acts accordingly.
    """
    print("Asking the user whether to stay or go")
    stayorgo = input("Should I 'stay' or should I 'go'? stay or go? ")
    if stayorgo == "stay":
        print("User chose to stay, calling main()")
        main()
    elif stayorgo == "go":
        print("User chose to go, saying goodbye and exiting")
        print("Goodbye!")
        exit()
    print("Repeating the decision process")
    decisions()

def menu():
    """
    Creates a menu with session functions.
    """
    print("Creating the menu with session functions")
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
    """
    Displays the banner, creates the menu, and prompts the user to select a session.
    """
    print("Displaying the banner")
    banner()
    print("Creating the menu")
    mymenu = menu()
    print("Displaying assignment information")
    print("Assignment 11.2 Abhishek Dubey")
    print("Prompting the user to select a session")
    print("Please type in a number between 1 and 6 to view the output from the sessions.")
    for key, value in mymenu.items():
        print(key, ' : ', value.__name__.replace("_", "."))
    userinput = int(input("Enter the number of the session to run: "))
    print("Switching to the selected session")
    sessionswitcher(userinput)

if __name__ == "__main__":
    print("Starting the main function")
    main()
