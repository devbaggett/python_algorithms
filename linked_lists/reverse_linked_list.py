# reverse_linked_list

# Write a function to reverse a Linked List in place. The function will take a list as input and return a new list in
# reverse.

from Nodes import Node
from LinkedList import LinkedList


def reverse_linked_list(linked_list):
    current = linked_list.head
    prev = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    linked_list.head = prev

    return linked_list


# Example Nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d

l = LinkedList()
l.head = a

print(reverse_linked_list(l))
