#!/usr/bin/env python3
import unittest
from arrays_left_rotation import ArrayLeftRotation

class ArrayLeftRotationTest(unittest.TestCase):
    def setUp(self):
        self.array_rotation = ArrayLeftRotation()

    def test_rotation1(self):
        list1 = [1,2,3,4,5]
        list2 = self.array_rotation.array_left_rotation1(list1, len(list1), 4)
        self.assertEqual(5, list2[0])
        self.assertEqual(1, list2[1])
        self.assertEqual(2, list2[2])
        self.assertEqual(3, list2[3])
        self.assertEqual(4, list2[4])
    
    def test_rotation2(self):
        list1 = [1,2,3,4,5]
        list2 = self.array_rotation.array_left_rotation2(list1, len(list1), 4)
        self.assertEqual(5, list2[0])
        self.assertEqual(1, list2[1])
        self.assertEqual(2, list2[2])
        self.assertEqual(3, list2[3])
        self.assertEqual(4, list2[4])

if __name__ == '__main__':
    unittest.main()
