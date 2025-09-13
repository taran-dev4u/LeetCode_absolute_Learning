from imple_linked_list import *

def rev_ll_in_grps(head, k):
    # Step 1: Check if there are at least k nodes left
    node = head
    count = 0
    while count < k and node:
        node = node.next
        count += 1
    if count < k:
        return head  # Base case: not enough nodes to reverse, return as-is

    # Step 2: Reverse k nodes
    prev = None
    curr = head
    nxt = None
    count = 0
    while count < k and curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        count += 1

    # Step 3: Recursive call on the rest of the list
    if nxt:
        head.next = rev_ll_in_grps(nxt, k)

    # Step 4: Return new head after reversal
    return prev



arr = [3, 1, 7, 4, 9, 8, 6, 2, 1]
head = build_list(arr)
printLL(rev_ll_in_grps(head, 3))

