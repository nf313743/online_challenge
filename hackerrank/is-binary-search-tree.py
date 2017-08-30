
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkRecursiveIsLesser(root, max_value):
    if root is None:
        return True

    if root.data > max_value:
        return 
    
    return checkRecursiveIsLesser(root.left, root.data) and checkRecursiveIsGreater(root.right, root.data)

def checkRecursiveIsGreater(root, max_value):
    if root is None:
        return True

    if root.data < max_value:
        return 
    
    return checkRecursiveIsLesser(root.left, root.data) and checkRecursiveIsLesser(root.right, root.data)

def checkBST(root):
    if root is None:
        return True

   return checkBST(root.left) and checkBST(root.right)


node = Node(3)
node.left =Node(2)
node.left.left =Node(1)
node.left.right = Node(4)

node.right = Node(6)
node.right.left = Node(5)
node.right.right = Node(7)


result = checkBST(node)
print(result)