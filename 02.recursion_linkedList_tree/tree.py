# tree demo in python

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.data) + " -> " + str(self.left) + " " + str(self.right)


root = Node(1)
left = Node(2)
right = Node(3)
left_left = Node(4)
left_right = Node(5)
right_left = Node(6)
right_right = Node(7)


root.left = left
root.right = right
left.left = left_left
left.right = left_right
right.left = right_left
right.right = right_right


# traverse the tree
# preorder traversal
def preorder_traversal(node):
    if node is not None:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)


# inorder traversal
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)

# postorder traversal


def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=" ")


print("Preorder traversal")
preorder_traversal(root)
print("\nInorder traversal")
inorder_traversal(root)
print("\nPostorder traversal")
postorder_traversal(root)
