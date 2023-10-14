from typing import Optional
from helper.simple_linked_list import ListNode, makeLinkedList
from math import gcd

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def insertGreatestCommonDivisors(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    while cur.next:
        cur.next = ListNode(gcd(cur.val,cur.next.val),cur.next)
        cur = cur.next.next
    return head

if __name__ == "__main__":
    cases = [
        [[18,6,10,3],[18,6,6,2,10,1,3]]
    ]
    heads = []
    for case in cases:
        list = makeLinkedList(case[0])
        head = insertGreatestCommonDivisors(list)
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        print('{}\n{}\n========================='.format(ans,case[1]))
        
