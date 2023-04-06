#Implement a Queue

class Node:
    def __init__(self, next, data):
        self.next = next
        self.data = data

class Queue:
    def __init__(self):
        self.elements = []

    def add(self, data):
        self.elements.append(data)

    def remove(self):
        if len(self.elements) == 0:
            return None
        return self.elements.pop(0)

q = Queue()
q.add(10)
q.add(20)
q.add(30)
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())