"""
Author: Emmy @emmykk
"""

def findWord(word, cbl):
    """ Finds the first occurrence of the word in the file and 
    returns the line & line # it is in with the word highlighted.
    Variable 'cbl' is a CursorLinkedList. """
    cbl.first()
    lineNumber = 1
    currentLine = cbl.getCurrent()
    found = False

    while currentLine is not None and found is False:
        currentLine = cbl.getCurrent()
        if word.lower() in currentLine.lower():
            found = True
            print("\nWord found here: ", currentLine.replace(word, '\033[44;33m{}\033[m'.format(word)))
            print("Found on line", lineNumber)
            return
        else:
            if cbl.hasNext():
                cbl.next()
                lineNumber += 1
            else:
                currentLine = None
    if not found:
        printError("Word not found")
    return

def replaceWordInLine(word, replWord, cbl):
    """ Replaces a given word on the current line with another word, replWord, in the given cursor based list.
        Variable 'cbl' is a CursorLinkedList. """
    currentLine = cbl.getCurrent()
    modifiedLine = f"{currentLine.replace(word, replWord)}" if word in currentLine else None

    if modifiedLine is not None:
        cbl.replace(modifiedLine)
        print("\x1b[0m Word replaced! \x1b[0m ")
        print(modifiedLine.replace(replWord, '\033[1;36;40m{}\033[m'.format(replWord)))    
    else:
        print("\x1b[0m The word you entered isn't in this line!")
    return cbl

def goToLineNumber(myList):
    """ Moves the cursor to the specified line number."""
    lineNumber = None
    while type(lineNumber) is not int:
        try:
            lineNumber = int(input("Enter the line number you'd like to go to."))
            myList.first() # Start our search at the first node in the list.
            currLineNumber = 1
            found = False

            while myList.hasNext() and found is False and lineNumber <= len(myList):
                if currLineNumber == lineNumber:
                    printSuccess(f"Moved to line {lineNumber}")
                    printGreen(myList.getCurrent())

                    found = True
                else:
                    myList.next()
                    currLineNumber += 1

            printError("Line does not exist.") if found is False else None
        except ValueError:
            printError("Please enter an integer for your line #.")
            continue

def saveToFileFromList(fileName, cursorLinkedList):
    """ Saves and writes contents of a given CursorLinkedList to a specified file."""
    chosenFile = open(fileName, "w")
    resultFileString = ""
    fileAsList = cursorLinkedList

    if not fileAsList.isEmpty():
        fileAsList.first()
        curr = fileAsList.getCurrent()

        while curr is not None:
            curr = fileAsList.getCurrent()
            lineToAdd = fileAsList.getCurrent()
            isNotLastLine = fileAsList.hasNext()

            if "\n" not in lineToAdd and isNotLastLine:
                lineToAdd += "\n"
            resultFileString += (lineToAdd)
            if isNotLastLine:
                fileAsList.next()
            else:
                curr = None

    chosenFile.write(resultFileString)
    chosenFile.close()
    printSuccess(f"Successfully saved changes to {fileName}. Goodbye!")

""" Console printing helpers with highlighting using ANSI escape sequences."""
def printError(message):
    print('\033[1;33;31m{}\033[m'.format(message))
def printSuccess(message):
    print('\033[1;33;34m{}\033[m'.format(message))
def printPurple(message):
    print('\033[1;33;35m{}\033[m'.format(message))    
def printGreen(message):
    print('\033[1;33;32m{}\033[m'.format(message))      
