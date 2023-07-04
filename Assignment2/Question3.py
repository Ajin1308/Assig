class Node:
    def __init__(self, data, next =None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insertion(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node


    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print() 

        

    def merge(self, other_list):
        if not self.head or not other_list.head:
            return

        current1 = self.head
        current2 = other_list.head

        while current1 and current2:
            next1 = current1.next
            next2 = current2.next

            current1.next = current2
            current2.next = next1

            current1 = next1
            current2 = next2

        if current1 is None and current2:
            current2.next = current2


lst1=LinkedList()
lst1.insertion(1)
lst1.insertion(3)
lst1.insertion(5)

lst1.display()

lst2=LinkedList()
lst2.insertion(2)
lst2.insertion(4)
lst2.insertion(6)
lst2.display()

lst1.merge(lst2)
lst1.display()