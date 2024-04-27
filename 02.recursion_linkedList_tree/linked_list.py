# linked list demo in python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data) + " -> " + str(self.next)


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

print(a)


# find mid node of linked list using tortoise and hare algorithm

def find_mid_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
