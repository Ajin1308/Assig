class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def is_empty(self):
        return len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) > 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  
print(queue.dequeue())  
print(queue.is_empty())