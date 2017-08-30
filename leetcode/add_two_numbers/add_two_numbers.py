import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_root = ListNode(-1)
        current = ListNode(0)
        dummy_root = current
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            value = 0
            if l1 == None and l2 == None:
                value = carry
            else:
                if l1 is not None:
                    value += l1.val
                    l1 = l1.next
                if l2 is not None:
                    value += l2.val
                    l2 = l2.next
                value += carry
            
            current.next = ListNode(int(value % 10))
            current = current.next
            carry = math.floor(value / 10)
        
        return dummy_root.next


l1 = [2,4,3]
l2= [5,6, 4]

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print("done")