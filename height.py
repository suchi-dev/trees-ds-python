class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_height(self, h =0):
        left_ht = self.left.get_height(h+1) if self.left else h
        right_ht = self.right.get_height(h+1) if self.right else h
        return max(left_ht, right_ht)

    def get_nodes_at_depth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self.data)
            return nodes
        if self.left:
            self.left.get_nodes_at_depth(depth-1, nodes)
        else:
            nodes.extend([None] * 2 ** (depth-1))

        if self.right:
            self.right.get_nodes_at_depth(depth-1, nodes)
        else:
            nodes.extend([None] * 2 ** (depth-1))
        return nodes


class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def get_height(self):
        return self.root.get_height()

    def get_nodes_at_depth(self, depth):
        return self.root.get_nodes_at_depth(depth)


node = Node(50)
node.left = Node(25)
node.right = Node(75)
node.left.left = Node(10)
node.left.right = Node(35)
node.left.left .left = Node(5)
node.left.left.right = Node(13)
node.left.right.left = Node(30)
node.left.right.right = Node(42)
node.left.left.left.left = Node(2)

myTree = Tree(node)
print("Height of the tree is :", myTree.root.get_height())
newNode = Node(50)
newNode.left = Node(25)
newNode.right = Node(75)
newNode.left.left = Node(13)
newNode.left.right = Node(35)
newNode.right.left = Node(55)
newNode.right.right = Node(103)
newNode.left.left.left = Node(2)
newNode.left.left.right = Node(20)
newNode.left.right.right = Node(37)
newNode.right.right.right = Node(256)
myNewTree = Tree(newNode, 'A very tall tree')
print("Nodes at depth 3 are : ", myNewTree.get_nodes_at_depth(3))




