# Node

# Creates a node with reference to object (value) and next node if not None

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"\nValue: {self.value}, Next: {self.next}"


class DLLNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
