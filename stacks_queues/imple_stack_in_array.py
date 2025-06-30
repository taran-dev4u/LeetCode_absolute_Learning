# class Stack:
#     def __init__(self):
#         self.items = []
    
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         if self.is_empty():
#             raise IndexError("pop from empty stack")
#         return self.items.pop()
    
#     def peek(self):
#         if self.is_empty():
#             raise IndexError("peek from empty stack")
#         return self.items[-1]
#     def is_empty(self):
#         return len(self.items) == 0
    
#     def __str__(self):
#         return "Stack(top to bottom) "+" -> ".join(map(str, reversed(self.items)))
    
#     def size(self):
#         return len(self.items)
    
# s = Stack()

# s.push(50)
# s.push(30)
# s.push(80)

# print(s)
# print(s.peek())
# print(s.pop())
# print(s.size())
# print(s.is_empty())


# stack implementation in linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLL:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    def pop(self):
        if self._isempty():
            raise IndexError("pop from empty stack")
        value = self.top.value
        self.top =self.top.next
        self._size -=1
        return value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value
    
    def is_empty(self):
        return self.top is None
    
    def __str__(self):
        result = []
        current = self.top
        while current:
            result.append(str(current.value))
            current = current.next
        return "stack (top to bottom) "+ " -> ".join(result)
    def size(self):
        return self._size



    