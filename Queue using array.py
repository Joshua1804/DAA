class QueueArray:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)

# Example usage
queue_array = QueueArray()
queue_array.enqueue(1)
queue_array.enqueue(2)
queue_array.enqueue(3)
print("Queue using Array:", queue_array.items)
print("Dequeue:", queue_array.dequeue())
print("Size:", queue_array.size())
