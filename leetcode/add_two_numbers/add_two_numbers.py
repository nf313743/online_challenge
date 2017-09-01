import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class AddTwoNumbers:

    def addTwoNumbers(self, node1, node2):
        dummy_root = ListNode(-1)
        current = ListNode(0)
        dummy_root = current
        carry = 0

        while node1 is not None or node2 is not None or carry != 0:
            value = 0
            if node1 is None and node2 is None:
                value = carry
            else:
                if node1 is not None:
                    value += node1.val
                    node1 = node1.next
                if node2 is not None:
                    value += node2.val
                    node2 = node2.next
                value += carry

            current.next = ListNode(int(value % 10))
            current = current.next
            carry = math.floor(value / 10)

        return dummy_root.next
