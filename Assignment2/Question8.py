class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        return self.stack.pop()


def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)

    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

string= "hello how are you?"
reverse=reverse_string(string)
print(reverse)