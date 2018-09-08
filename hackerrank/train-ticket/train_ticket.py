#!/usr/bin/env python3
import unittest


class IsBinarySearchTreeTest(unittest.TestCase):
    # def setUp(self):
    #     self.binary_search_tree = IsBinarySearchTree()

    def test_type_LB(self):
        result = berth_type(1)
        self.assertEqual('LB', result)
        result = berth_type(4)
        self.assertEqual('LB', result)
        result = berth_type(36)
        self.assertEqual('LB', result)
        result = berth_type(60)
        self.assertEqual('LB', result)

    def test_type_SUB(self):
        result = berth_type(8)
        self.assertEqual('SUB', result)
        result = berth_type(56)
        self.assertEqual('SUB', result)
        result = berth_type(72)
        self.assertEqual('SUB', result)
        
    def test_type_UB(self):
        self.assertEqual('UB', berth_type(70))


berths = ['UB', 'LB', 'MB']

def berth_type(seat_number):
    seat_mod = seat_number % 8
    if seat_mod == 0:
        return 'SUB'
    elif seat_mod == 7:
        return 'SLB'
    else:
        return berths[seat_mod % 3]


if __name__ == '__main__':
    unittest.main()
