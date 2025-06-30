from imple_linked_list import *

def delete_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow  = slow.next
        fast = fast.next.next
        if slow is fast:
            break
        else:
            return
    ptr1 = head
    ptr2 = slow
    while ptr1 is not ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    prev = ptr2
    while prev.next is not ptr2:
        prev = prev.next
    prev.next = None
    return head

delete_loop()
