from cursorLinkedList import CursorLinkedList
import os
from helpers import replaceWordInLine, saveToFileFromList, printError, printSuccess, printGreen, printPurple, findWord, goToLineNumber
from menuLoopHelper import runMenuLoop 
from constants import INPUT_COLOR

def main():
    fileName = getFilenameFromUser()
    editor = CursorLinkedList()

    if not os.path.isfile(fileName):
        printGreen(f"That file does not exist! Creating new file called: {fileName}")
        shouldSaveChanges = runMenuLoop(fileName, editor) # When the loop terminates, it returns False if changes are not to be saved
        if shouldSaveChanges:
            f = open(fileName, "x")
            f.close()
            saveToFileFromList(fileName, editor)
            return
    else:
        chosenFile = open(fileName, "r+")
        fileContent = chosenFile.readlines()

        for line in fileContent:
            editor.insertAfter(line)

        chosenFile.close()
        shouldSaveChanges = runMenuLoop(fileName, editor)

        if shouldSaveChanges:
            chosenFile = open(fileName, "w")
            saveToFileFromList(fileName, editor)
            return
    printSuccess("Youve chosen to exit without saving. Goodbye!")

def getFilenameFromUser():
    """ Solicits a .txt file name from the user.
    If a file with a .txt extension is not entered, we repeat the prompt until the user enters one."""
    fileName = ""
    while fileName == "":
        # Only accept .txt file names!
        fileName = str(input(f"Please enter a file name with a .txt extension to edit: {INPUT_COLOR}"))
        ext = os.path.splitext(fileName)[-1]
        if ext != ".txt":
            printError("The file you entered is not a .txt file. Please enter a txt file name including the .txt extension.")
            fileName = ""    
    return fileName

main()