from imple_stack_in_array import *
def valid_para(s):
    stack =[]
    mapping = {')':'(', '}':'{', ']':'['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != char:
                return False
            stack.pop()
    return not stack