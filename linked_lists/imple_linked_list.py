class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(arr):
    if not arr:
        return None 
    head = Node(arr[0])
    node = head
    for i in range(1, len(arr)):
        node.next = Node(arr[i])
        node = node.next
    return head

def printLL(head):
    node = head
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print(" -> ".join(vals) + " -> None")

def add_to_start(head, val):
    return Node(val , head)

def add_to_last(head, val):
    node = head
    while node.next:
        node = node.next
    node.next = Node(val)
    return head
def add_to_pos(head, val,pos):
    if pos<=1:
        return add_to_start(head, val)
    else:
        node = head
        i=2
        while node.next and pos>i:
            node = node.next
            i+=1
        node.next = Node(val, node.next)
    return head
def del_val_by_pos(head, pos):
    node = head
    if pos<=1:
        return node.next
    else:
        i = 2
        while node.next and i<pos:
            node = node.next
            i +=1
        node.next = node.next.next
    return head
def del_by_val(head, val):
    node = head
    prev= Node(0, head)
    dele = False
    while node:
        if node.val == val:
            prev.next = node.next
            dele = True
            break
        node = node.next
        prev = prev.next
    if dele:
        return head
    else:
        return None



# if __name__=="__main__":
#     arr = [4, 2, 6, 8, 3, 5]
#     head = build_list(arr)
    # printLL(add_to_start(head, 34))
    # printLL(add_to_last(add_to_start(head, 90), 45))
    # printLL(add_to_pos(head, 34, 3))
    # printLL(del_val_by_pos(head, 1))
    # printLL(del_by_val(head, 57))