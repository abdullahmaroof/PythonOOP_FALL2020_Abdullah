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
            point = self.head
            linklist = ""
            while point:
                linklist += str(point.data)+" --> "
                point = point.next
            print(linklist)

    def tell_length(self):
        length = 0
        point = self.head
        while point:
            length += 1
            point = point.next
        return length

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            point = self.head
            while point.next:
                point = point.next
            point.next = Node(data,None)


list = single_linklist()
list.insert_at_start(12)
list.insert_at_start(32)
list.insert_at_end(89)
print(list.tell_length())
