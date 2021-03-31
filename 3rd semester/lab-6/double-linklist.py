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

    def tell_length(self):
        length = 0
        point = self.head
        while point:
            length += 1
            point = point.next
        return length


list = double_linklist()
print(list.tell_length())
