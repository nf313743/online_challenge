#!/usr/bin/env python3
import unittest
from is_binary_search_tree import IsBinarySearchTree
from is_binary_search_tree import Node

class IsBinarySearchTreeTest(unittest.TestCase):
    def setUp(self):
        self.binary_search_tree = IsBinarySearchTree()

    def test_is_bst_emptyNode_True(self):
        result = self.binary_search_tree.is_bst(None)
        self.assertTrue(result)

    def test_is_bst_onlyleftnodes_true(self):
        node = Node(200)
        node.left = Node(150)
        node.left.left = Node(100)
        result = self.binary_search_tree.is_bst(node)
        self.assertTrue(result)

    def test_is_bst_onlyleftnodes_false(self):
        node = Node(200)
        node.left = Node(205)
        node.left.left = Node(100)
        result = self.binary_search_tree.is_bst(node)
        self.assertFalse(result)

    def test_is_bst_onlyrightnodes_true(self):
        node = Node(200)
        node.right = Node(250)
        node.right.right = Node(300)
        result = self.binary_search_tree.is_bst(node)
        self.assertTrue(result)

    def test_is_bstT_onlyrightnodes_false(self):
        node = Node(200)
        node.right = Node(205)
        node.right.right = Node(100)
        result = self.binary_search_tree.is_bst(node)
        self.assertFalse(result)

    def test_is_bst_true(self):
        node = Node(4)
        node.left = Node(2)
        node.left.left =Node(1)
        node.left.right = Node(3)
        node.right = Node(6)
        node.right.left = Node(5)
        node.right.right = Node(7)
        result = self.binary_search_tree.is_bst(node)
        self.assertTrue(result)

    def test_is_bst_false(self):
        node = Node(3)
        node.left = Node(2)
        node.left.left = Node(1)
        node.left.right = Node(8)
        node.right = Node(6)
        node.right.left = Node(5)
        node.right.right = Node(7)
        result = self.binary_search_tree.is_bst(node)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
