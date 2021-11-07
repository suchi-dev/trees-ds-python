class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_height(self, h =0):
        left_ht = self.left.get_height(h+1) if self.left else h
        right_ht = self.right.get_height(h+1) if self.right else h
        return max(left_ht, right_ht)

    def add_node(self, data):
        if self.data == data:
            return
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add_node(data)

        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add_node(data)

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data


    def delete(self, target):
        if self.data == target:
            # do the deletion here
            # Case where both children exists for the target node to be deleted
            if self.left and self.right:
                # RTFM - Right Tree Find Minimum
                min_value = self.right.find_min()
                # min_value will replace the target value to be deleted
                self.data = min_value
                # delete the min value from the right side
                self.right = self.right.delete(min_value)
                return self
            else:
                # Case where either left or right child exists for the target node to be deleted
                # or it is a leaf node having no children
                return self.left or self.right

        if self.right and target > self.data:
            self.right = self.right.delete(target)
        if self.left and target < self.data:
            self.left = self.left.delete(target)
        return self

    def traverse_inorder(self):
        if self.left:
            self.left.traverse_inorder()
        print(self.data)

        if self.right:
            self.right.traverse_inorder()

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

    def traverse_inorder(self):
        return self.root.traverse_inorder()

    def add_node(self, data):
        self.root.add_node(data)

    def delete(self, target):
        self.root = self.root.delete(target)

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
print("Before adding a new node")
myNewTree.traverse_inorder()
myNewTree.add_node(45)
print("After adding a new node")
myNewTree.traverse_inorder()

delete_node = Node(50)
delete_node.left = Node(25)
delete_node.right = Node(75)
delete_node.right.left = Node(67)
delete_node.right.right = Node(100)
delete_node.right.right.left = Node(80)
delete_node.right.right.right = Node(120)
delete_node.right.right.left.right = Node(92)
myDeleteTree = Tree(delete_node, "Beautiful Tree")
print("Inorder Traversal before deletion")
myDeleteTree.traverse_inorder()
myDeleteTree.delete(75)
print("After deletion inorder traversal")
myDeleteTree.traverse_inorder()
print("Deleting root node")
myDeleteTree.delete(50)
print("After deletion of root node inorder traversal")
myDeleteTree.traverse_inorder()



