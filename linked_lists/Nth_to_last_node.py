# Nth_to_last_node

# Write a function that takes a linked list and returns the nth to last node in the linked list.

from Nodes import Node
from LinkedList import LinkedList


def Nth_to_last_node(linked_list, n):
    current = linked_list.head

    runner = linked_list.head
    for x in range(n):
        if not runner:
            raise LookupError('Error: n is larger than the linked list.')
        runner = runner.next
    while runner:
        current = current.next
        runner = runner.next

    return current


# Example Nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

l = LinkedList()
l.head = a

print(Nth_to_last_node(l, 1))  # returns e
