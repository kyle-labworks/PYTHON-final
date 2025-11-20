# TUPLE EXAMPLE
coordinates = (5, 10, 15)
print("Tuple:", coordinates)
print("Second element:", coordinates[1])

# SET EXAMPLE
fruits = {"apple", "banana", "orange", "apple"}  # duplicates removed
fruits.add("grape")
print("\nSet:", fruits)
print("Contains 'banana':", "banana" in fruits)

# LINKED LIST EXAMPLE
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

print("\nLinked List:")
ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.display()

# STACK EXAMPLE
stack = []
stack.append("red")
stack.append("green")
stack.append("blue")
print("\nStack (LIFO):", stack)
print("Popped:", stack.pop())
print("Stack after pop:", stack)

# QUEUE EXAMPLE
from collections import deque
queue = deque()
queue.append("first")
queue.append("second")
queue.append("third")
print("\nQueue (FIFO):", queue)
print("Dequeued:", queue.popleft())
print("Queue after dequeue:", queue)

# TREE EXAMPLE
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

root = TreeNode("root")
root.left = TreeNode("left")
root.right = TreeNode("right")
root.left.left = TreeNode("left.left")
root.left.right = TreeNode("left.right")

print("\nTree Inorder Traversal:")
inorder(root)
print()
