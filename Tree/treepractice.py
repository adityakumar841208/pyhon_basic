class CreateNode:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, root, key):
        if root is None:
            return CreateNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right) 


a = [4, 2, 5, 7, 1]

tree = Tree()

for data in a:
    tree.root = tree.insert(tree.root, data)

tree.inorder(tree.root)
