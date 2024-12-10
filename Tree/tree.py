class CreateNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return CreateNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)

        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        node = self.findMinNode(root.right, key)
        root.key = node.key
        root.right = self.delete(root.right, key)
        
        return root

    def findMinNode(self, root):
        while root.left is not None:
            root = root.left
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)


tree = Tree()

tree.root = tree.insert(tree.root,2)
tree.root = tree.insert(tree.root,6)


tree.inorder(tree.root)