"""
Description:  Positional (cursor) linked list.
Author:  Emmy @emmykk
"""
from node import Node
from constants import BLUE, END_ANSI

class CursorLinkedList():
    """ Linked implementation of a positional list."""
    
    def __init__(self):
        """ Creates an empty cursor-based list with header and trailer nodes."""
        self._header = Node(None)
        self._trailer = Node(None)
        self._trailer.setPrevious(self._header)
        self._header.setNext(self._trailer)
        self._current = None
        self._size = 0

    def hasNext(self):
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        return self._current.getNext() != self._trailer

    def hasPrevious(self):
        if self.isEmpty():
            raise AttributeError("Empty list has no previous item")
        return self._current.getPrevious() != self._header
    
    def first(self):
        if self.isEmpty():
            raise AttributeError("Empty list has no first item")
        self._current = self._header.getNext()

    def last(self):
        if self.isEmpty():
            raise AttributeError("Empty list has no last item")
        self._current = self._trailer.getPrevious()

    def next(self):
        if not self.hasNext():
            raise AttributeError("This is the last item in the list!")
        self._current = self._current.getNext()

    def previous(self):
        if not self.hasPrevious():
            raise AttributeError("This is the first item in the list!")
        self._current = self._current.getPrevious()

    def insertAfter(self, item):
        newNode = Node(item)

        if self.isEmpty():
            self.insertAsOnlyItem(newNode)
            return

        newNode.setNext(self._current.getNext())
        self._current.getNext().setPrevious(newNode)
        self._current.setNext(newNode)         
        newNode.setPrevious(self._current) 

        self._current = newNode
        self._size += 1

    def insertBefore(self, item):
        newNode = Node(item)

        if self.isEmpty():
            self.insertAsOnlyItem(newNode)
            return

        self._current.getPrevious().setNext(newNode)
        newNode.setPrevious(self._current.getPrevious())
        self._current.setPrevious(newNode)
        newNode.setNext(self._current)

        self._current = newNode
        self._size += 1

    def insertAsOnlyItem(self, newNode):
        """ Helper function for insertBefore and insertAfter to handle the case of insertion when the list is empty."""
        self._header.setNext(newNode)
        self._trailer.setPrevious(newNode)
        newNode.setPrevious(self._header)
        newNode.setNext(self._trailer) 
        self._current = newNode       
        self._size += 1

    def getCurrent(self):
        if self.isEmpty():
            raise AttributeError("Empty list has no current item")
        return self._current.getData()

    def remove(self):
        if self.isEmpty():
            raise AttributeError("Can't remove the current item from an empty list!")

        temp = self._current

        if self._size == 1:
            self._header.setNext(self._trailer)
            self._trailer.setPrevious(self._header)
            self._current = None
            self._size -= 1
            return temp.getData()

        if self._current.getNext() == self._trailer:
            previousNode = self._current.getPrevious()
            previousNode.setNext(self._trailer)
            self._trailer.setPrevious(previousNode)
            self._current = previousNode
            self._size -= 1
            return temp.getData()
        
        nextNode = self._current.getNext()
        previousNode = self._current.getPrevious()

        previousNode.setNext(nextNode)
        nextNode.setPrevious(previousNode)
        self._current = nextNode
        self._size -= 1            
        return temp.getData()

    def replace(self, newItemValue):
        if self.isEmpty():
            raise AttributeError("Can't replace the current item of an empty list!")
        if newItemValue is None:
            raise ValueError("Please enter an item value!")

        self._current.setData(newItemValue)  

    def isEmpty(self):
        return True if self._size == 0 else False

    def __len__(self):
        return self._size

    def __str__(self):
        result = ""
        temp = self._header.getNext()
        while temp != self._trailer:
            if temp == self._current:                
                data = str(temp.getData())
                if ("\n" in data):
                    result += (BLUE + data.replace("\n", "") + END_ANSI + "\n")
                else:
                    result += (BLUE + data + END_ANSI + " ")
            else:
                result += (str(temp.getData()) + " ")
            temp = temp.getNext()
        return result
