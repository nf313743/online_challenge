import unittest
from add_two_numbers import AddTwoNumbers
from add_two_numbers import ListNode

class AddTwoNumbersTest(unittest.TestCase):
    
    def setUp(self):
        self.add_two_numbers = AddTwoNumbers()

    def test_add_two_lists(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        result = self.add_two_numbers.addTwoNumbers(l1, l2)
        self.assertEqual(7, result.val)
        result = result.next
        self.assertEqual(0, result.val)
        result = result.next
        self.assertEqual(8, result.val)


if __name__ == '__main__':
    unittest.main()