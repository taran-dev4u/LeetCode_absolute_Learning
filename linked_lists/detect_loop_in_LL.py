from imple_linked_list import *
# Floyd’s Tortoise and Hare

def detect_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow  = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

if __name__ == "__main__":
    arr = [1, 2, 3, 4, ]
    head = build_list(arr)
    print(detect_loop(head))