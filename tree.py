class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name


node = Node(10)
node.left = Node(5)
node.right = Node(15)
node.left.left = Node(3)
node.left.right = Node(6)
node.right.left = Node(13)
node.right.right = Node(100)

print(node.left.data)
print(node.right.right.data)

myTree = Tree(node)
print(myTree.root.right.data)
print(myTree.root.left.left.data)
