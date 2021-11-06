class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found it!")
            return self
        if self.left and self.data > target:
            return self.left.search(target)
        if self.right and self.data < target:
            return self.right.search(target)

        print("Value is not found in the tree")

    def traverse_preorder(self):
        print(self.data)

        if self.left:
            self.left.traverse_preorder()

        if self.right:
            self.right.traverse_preorder()

    def traverse_inorder(self):
        if self.left:
            self.left.traverse_inorder()
        print(self.data)

        if self.right:
            self.right.traverse_inorder()

    def traverse_postorder(self):
        if self.left:
            self.left.traverse_postorder()

        if self.right:
            self.right.traverse_postorder()

        print(self.data)


class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

    def traverse_preorder(self):
        return self.root.traverse_preorder()

    def traverse_inorder(self):
        return self.root.traverse_inorder()


    def traverse_postorder(self):
        return self.root.traverse_postorder()



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


found = node.search(100)
print(found.data)

print("Using Tree class method")
exists_in_tree = myTree.search(15)
print(exists_in_tree.data)

print("--------Pre order Traversal")
myTree.root.traverse_preorder()

print("-----------Inorder Traversal")
myTree.root.traverse_inorder()

print("------------Postorder Traversal")
myTree.root.traverse_postorder()