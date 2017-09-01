import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class IsBinarySearchTree:
   
    def is_lesser(self, root, prev_root_val, lower_limit, upper_limit):
        if root is None:
            return True

        if root.data > prev_root_val:
            return False

        if root.data < lower_limit:
            return False
    
        return self.is_lesser(root.left, root.data, lower_limit, upper_limit) and self.is_greater(root.right, root.data, lower_limit, upper_limit)

    def is_greater(self, root, prev_root_val, lower_limit, upper_limit):
        if root is None:
            return True

        if root.data < prev_root_val:
            return False

        if root.data > upper_limit:
            return False
    
        return self.is_lesser(root.left, root.data,lower_limit, upper_limit) and self.is_greater(root.right, root.data,lower_limit, upper_limit)


    def is_bst(self, root):
        if root is None:
            return True

        return self.is_lesser(root.left, root.data, -sys.maxsize, root.data) and self.is_greater(root.right, root.data, root.data, sys.maxsize)
