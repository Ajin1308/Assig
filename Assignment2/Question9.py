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

def operation(expression):
    stack = Stack()
    operators={
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }
    for i in expression:
        if i.isdigit():
            stack.push(int(i))
        elif i in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            operate = operators[i]
            result = operate(operand1, operand2)
            stack.push(result)

    return stack.pop()

expression = "4 5 + 3 *"
example = operation(expression)
print(example)