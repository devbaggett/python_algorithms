# is_circular

# Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a
# boolean indicating if the linked list contains a "cycle".

# A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known
# as a circularly linked list.

from Nodes import Node
from LinkedList import LinkedList


def is_circular(linked_list):
    slow = linked_list.head
    fast = linked_list.head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


# Example Nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = b  # circular node

l = LinkedList()
l.head = a

print(is_circular(l))  # returns true
