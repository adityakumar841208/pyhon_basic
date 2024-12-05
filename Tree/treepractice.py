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
    
    def delete(self,root, key):
        if root == None:
            return root
    

        if key < root.key:
            root.left = self.delete(root.left,key)
        elif key > root.key:
            root.right = self.delete(root.right,key)

        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
        
            # go to the smallest number at the root right and get it's data and make this to the root data
            temp = self.findMinRoot(root.right)
            root.key = temp.key
            root.right = self.delete(root.right,temp.key)
        return root

    def findMinRoot(self,root):
        while root.left:
            root = root.left
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

tree.root = tree.delete(tree.root,2)
tree.root = tree.delete(tree.root,7)
tree.inorder(tree.root)
