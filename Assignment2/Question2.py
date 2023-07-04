class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def inserting_at_end(self, data):
        new_node = Node(data)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        else:
            self.head = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("Linked List:", elements)

    def reverse_in_groups(self, k, head, length):
        if length < k:
            return head

        prev = None
        current = head
        next_node = None
        count = 0

        while current!= None and count < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1

        if next_node:
            head.next = self.reverse_in_groups(k, next_node, length - k)

        return prev

    def reverseKGroup(self, k):
        length = self.lengthOfLinkedList(self.head)
        self.head = self.reverse_in_groups(k, self.head, length)

    def lengthOfLinkedList(self, head):
        length = 0
        temp = head
        while temp is not None:
            temp = temp.next
            length += 1

        return length


item = LinkedList()
item.inserting_at_end(1)
item.inserting_at_end(2)
item.inserting_at_end(3)
item.inserting_at_end(4)
item.inserting_at_end(5)
item.inserting_at_end(6)
item.inserting_at_end(7)
item.inserting_at_end(8)
item.display()

item.reverseKGroup(3)
item.display()
