class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = QueueNode(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            popped_item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return popped_item
        else:
            print("Queue is empty")

    def size(self):
        current = self.front
        count = 0
        while current:
            count += 1
            current = current.next
        return count

# Example usage
queue_linked_list = QueueLinkedList()
queue_linked_list.enqueue(1)
queue_linked_list.enqueue(2)
queue_linked_list.enqueue(3)
print("Queue using Linked List:")
print("Dequeue:", queue_linked_list.dequeue())
print("Size:", queue_linked_list.size())
