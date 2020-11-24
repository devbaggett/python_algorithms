# Node

# Creates a node with reference to object (value) and next node if not None

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class DLLNode(Object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
