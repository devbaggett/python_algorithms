# Queue2Stacks

# Given the Stack class below, implement a Queue class using two stacks! Note, this is a "classic" interview problem. Use
# a Python list data structure as your Stack.

class Queue2Stacks(object):
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def enqueue(self, element):
        self.stackA.append(element)

    def dequeue(self):
        while self.stackA:
            self.stackB.append(self.stackA.pop())
        element = self.stackB.pop()
        while self.stackB:
            self.stackA.append(self.stackB.pop())
        return element
