class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class single_linklist:
    def __init__(self):
        self.head = None

    def printlist(self):
        if self.head is None:
            print("Single Linklist is empty")
        else:
            pass


list = single_linklist()
list.printlist()