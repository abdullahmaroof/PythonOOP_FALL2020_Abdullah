class Node:
    def __init__(self, previous=None, data=None, next=None):
        self.previous = previous
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

    #def printlist_reverse(self):
     #   if self.head is None:
      #      print("double Linklist is empty")
      #  else:
       #     point = self.head
        #    linklist = ""
        #    while point.next is not None:
        #        point = point.next
        #    while point is not None:
        #        linklist += str(point.data)+" --> "
        #        point = point.previous

        #    print(linklist)

    def tell_length(self):
        length = 0
        point = self.head
        while point:
            length += 1
            point = point.next
        return length

    def insert_at_start(self, data):
        node = Node(self.head,data,self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(None,data, None)
        else:
            point = self.head
            while point.next:
                point = point.next
            point.next = Node(point,data,None)

    def insert_at(self, index, data):
        if index<0 or index>self.tell_length():
            print("Invalid index")
        elif index==0:
            self.insert_at_start()

        pointer = 0
        point = self.head
        while point:
            if pointer == index-1:
                print("pointer:",pointer," ",self.head,"  ",data,"  ",point.next)
                node = Node(self.head,data,point.next)
                print("data:  ",node)
                point.next = node
                node = point.previous
                point.previous = point.next
                break
            pointer += 1





list = double_linklist()
list.insert_at_start(12)
list.insert_at_start(23)
list.insert_at_start(32)
list.insert_at_start(11)
print(list.tell_length())
list.printlist_forward()
list.insert_at_end(100)
list.printlist_forward()
list.insert_at(4,140)
list.printlist_forward()

