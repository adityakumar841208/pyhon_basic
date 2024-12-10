class CreateNode():
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key

class Tree():
    def __init__(self):
        self.root = None

    def insert(self,root,key):
        if root is None:
            return CreateNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)

        return root

    def traversal(self, root):
        if root:
            self.traversal(root.left)
            print(root.key, end=' ')
            self.traversal(root.right)


tree = Tree()

tree.root = tree.insert(tree.root,5)
tree.root = tree.insert(tree.root,3)
tree.root = tree.insert(tree.root,6)
tree.root = tree.insert(tree.root,9)

tree.traversal(tree.root)




        