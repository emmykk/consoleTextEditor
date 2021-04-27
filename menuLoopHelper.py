from helpers import replaceWordInLine, printError, printSuccess, printGreen, printPurple, findWord, goToLineNumber
from constants import INPUT_COLOR, BLUE, END_ANSI

def printMenuOptions():
    """ Displays commands in terminal for the text editor."""
    print("\nFile Editor Menu:")
    print(f"{BLUE} H {END_ANSI} - Hide file from view")            
    print(f"{BLUE} S {END_ANSI} - Show file in editor")      
    print(f"{BLUE} F {END_ANSI} - Display first line")
    print(f"{BLUE} L {END_ANSI} - Display last line")
    print(f"{BLUE} N {END_ANSI}- Display next line")
    print(f"{BLUE} P {END_ANSI} - Display previous line")
    print(f"{BLUE} B {END_ANSI} - Insert a line before current line")
    print(f"{BLUE} A {END_ANSI} - Insert a line after current line")
    print(f"{BLUE} R {END_ANSI} - Remove current line")
    print(f"{BLUE} U {END_ANSI} - Replace current line")
    print(f"{BLUE} X {END_ANSI} - Save/write file changes and exit")
    print(f"{BLUE} XO {END_ANSI} - Exit without saving")        
    print(f"{BLUE} FIND {END_ANSI} - Find word")
    print(f"{BLUE} RP {END_ANSI} - Replace word in current line with another word")
    print(f"{BLUE} COPY {END_ANSI} - Copy current line to clipboard.")        
    print(f"{BLUE} PASTE {END_ANSI} - Pastes the copied line and inserts after current line.")    
    print(f"{BLUE} GOTO {END_ANSI} - Go to a specific line #.")  

def runMenuLoop(fileName, myList):
    """ Runs the program and displays the menu and file summary after each user action 
    until user chooses to exit with or without saving."""
    run = True
    clipboard = '' # Program clipboard for copy-paste functions.
    showFile = True # Determines whether we show or hide the current file in the editor.

    while run is True:
        displaySummary(fileName, myList, showFile)
        printMenuOptions()

        response = input("Menu Choice? ").upper()

        # menu = {
        #     'F': (lambda: myList.first() if not myList.isEmpty() else printError("Nothing is in the file yet. Add something to the file first!")),
        #     'L': (lambda: myList.last() if not myList.isEmpty() else printError("Nothing is in the file yet. Add something to the file first!")),
        #     'N': (lambda: myList.next() if (not myList.isEmpty() and myList.hasNext()) else printError("There is no next line!")),
        #     'P': (lambda: myList.previous() if (not myList.isEmpty() and myList.hasPrevious()) else printError("There is no previous line!")),
        #     'B': (lambda: myList.next() if (not myList.isEmpty() and myList.hasNext()) else printError("There is no next line!")),
        # }

        if response == 'F':
            if myList.isEmpty():
                printError("Nothing is in the file yet. Add something to the file first!")
            else:
                myList.first()
                printSuccess("Moved cursor to first line.")
        elif response == 'L':
            if myList.isEmpty():
                printError("Nothing is in the file yet. Add something to the file first!")
            else:            
                myList.last()
                printSuccess("Moved cursor to last line.")
        elif response == 'N':
            if myList.isEmpty() or not myList.hasNext():
                printError("There is no next line!")   
            else:
                myList.next()
                printSuccess("Moved to next line.")
        elif response == 'P':
            if myList.isEmpty() or not myList.hasPrevious():
                printError("There is no previous line!")
            else:      
                myList.previous()
                printSuccess("Moved to previous line.")
        elif response == 'B':
            item = str(input("Enter the line to insert before the current line: "))
            myList.insertBefore(item + "\n")
        elif response == 'A':
            item = input("Enter the line to insert after the current line: ")
            myList.insertAfter(item + "\n")
        elif response == 'R':
            if myList.isEmpty():
                printError("There's nothing to remove!")
            else:   
                item = myList.remove()
                printSuccess(f"Ths line removed: {item}")
        elif response == 'U':
            if myList.isEmpty():
                printError("There's nothing to replace. Add a line to the file first!")
            else:
                item = str(input("Enter replacement line: "))
                newLineString = "\n" if myList.hasNext() else ""
                replacement = f"{item}{newLineString}"
                myList.replace(replacement)
        elif response == 'FIND':
            if myList.isEmpty():
                printError("Can't find something in an empty list!")
            else:
                word = str(input("Enter a word to search for: "))
                findWord(word, myList)
        elif response == 'RP':
            if myList.isEmpty():
                print("The list is empty!")
            else:
                word = input("Enter a word to replace in the current line: \033[1;36;40m")
                replWord = input("\x1b[0m Enter a replacement word: \033[1;36;40m")
                print("\x1b[0m Processing...")
                replaceWordInLine(word, replWord, myList)
        elif response == 'COPY':
            if not myList.isEmpty():
                copiedLine = myList.getCurrent()
                clipboard = copiedLine
                printSuccess("Line copied to program clipboard.")
            else:
                printError("Nothing to copy.  Please write a line to the file first.")
        elif response == 'PASTE':
            if clipboard != '':
                myList.insertAfter(clipboard)
                printSuccess("Line pasted from program clipboard.")
            else:
                printError("Nothing to paste.  Please write a line to the file first.")
        elif response == 'GOTO':
            if myList.isEmpty():
                printError("The list is empty!")
            else:
                goToLineNumber(myList)
        elif response == 'H':
            showFile = False
            printSuccess("Preferences saved.")
        elif response == 'S':
            showFile = True     
            printSuccess("Preferences saved.")                  
        elif response == 'X':
            run = False
            printGreen("Saving your changes....")
            return True
        elif response == 'XO':
            return False
        else:
            printError("Invalid Menu Choice!")

def displaySummary(fileName, myList, showFile):
    """ Displays summary of the file including the current line content."""
    print("\n===============================================================")
    printPurple(f"Current File: {fileName}")
    
    if myList.isEmpty():
        printError("This is an empty file. Write something!")
    else:
        printGreen(f"# of lines: {len(myList)}")
        printPurple(f"Current line: {myList.getCurrent()}")
    if showFile:
        print(myList)