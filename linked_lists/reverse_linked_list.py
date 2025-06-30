from imple_linked_list import *


def rev_ll(head):
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def rev_using_stack(head):
    if not head or not head.next:
        return head
    
    new_head = rev_using_stack(head.next)

    head.next.next = head
    head.next = None
    return new_head


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    head = build_list(arr)
    rev_ll(head)
