class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next
def linked_list_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res
l1_input = [9,9,9,9,9,9,9]
l2_input = [9,9,9,9]
l1 = build_linked_list(l1_input)
l2 = build_linked_list(l2_input)
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print(linked_list_to_list(result))