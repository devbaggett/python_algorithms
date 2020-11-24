# SinglyLinkedList

# In a singly linked list, we have an ordered list of items as individual Nodes that have pointers to other Nodes.


class LinkedList(object):
    def __init__(self):
        self.head = None

    def __str__(self):
        return f"Head: {self.head}"
