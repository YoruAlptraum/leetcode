from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 243 
def createList(arr: List[int]) -> Optional[ListNode]:
    prev = None
    head = None
    for i in arr:
        node = ListNode(i)
        if not head:
            head = node
        if prev:
            prev.next = node
        prev = node
    return head

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    head = ListNode()
    current = head
    while l1 or l2 or carry:
        sum = carry
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry = sum // 10
        current.next = ListNode(sum % 10)
        current = current.next
    return head.next

l1 = createList([2,4,3]) # 342
l2 = createList([5,6,4]) # 465
l3 = addTwoNumbers(l1, l2) # expected 807

while l3:
    print(l3.val)
    l3 = l3.next
