class Node:
    def __init__(self, pervious=None, data=None, next=None):
        self.previous = pervious
        self.data = data
        self.next = next

class double_linklist:
    def __init__(self):
        self.head = None

    def printlist_forward(self):
        if self.head is None:
            print("double Linklist is empty")
        else:
            point = self.head
            linklist = ""
            while point:
                linklist += str(point.data)+" --> "
                point = point.next
            print(linklist)

    def printlist_reverse(self):
        if self.head is None:
            print("double Linklist is empty")
        else:
            point = self.head
            linklist = ""
            while point.next is not None:
                point = point.next
            while point is not  None:
                linklist += str(point.data) + " --> "
                point = point.pervious
            print(linklist)

list = double_linklist()
list.printlist_forward()
list.printlist_reverse()