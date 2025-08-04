# 1) Slicing: arr[::-1]
def rev(arr):
    """
    Reverse using slicing.
    Time:  O(n)      (creates a new list by copying n elements)
    Space: O(n)      (slice allocates a new list of size n)
    """
    return arr[::-1]

# 2) built‑in reversed() → list
def rev_arr(arr):
    """
    Reverse using built‑in reversed() and list().
    Time:  O(n)      (iterates n elements, appending to new list)
    Space: O(n)      (allocates a new list of size n)
    """
    return list(reversed(arr))

# 3) In‑place swap via for i in range(n//2)
def rev_array(arr):
    """
    Reverse in‑place by swapping pairs.
    Time:  O(n/2) → O(n)   (n//2 iterations, each O(1) swap)
    Space: O(1)            (only a few indices/temps)
    """
    n = len(arr)                       # O(1)
    for i in range(n // 2):            # O(n) loop
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]  # O(1) swap
    return arr                         # O(1)

# 4) Build new_arr by append in reverse index order
def rev_arrayy(arr):
    """
    Reverse by appending elements from the end.
    Time:  O(n)      (n iterations of append)
    Space: O(n)      (new list of size n)
    Note: returns original arr due to bug; should return new_arr.
    """
    n = len(arr)                       # O(1)
    new_arr = []                       # O(1)
    for i in range(n - 1, -1, -1):     # O(n) loop
        new_arr.append(arr[i])         # O(1) amortized
    return arr                         # O(1)  (likely intended new_arr)

# 5) While‑loop in‑place swap (same as 3)
def re_arr(arr):
    """
    Reverse in‑place with two‑pointer while‑loop.
    Time:  O(n)      (n/2 iterations of constant work)
    Space: O(1)
    """
    start, end = 0, len(arr) - 1       # O(1)
    while start < end:                 # O(n) loop
        arr[start], arr[end] = arr[end], arr[start]  # O(1)
        start += 1                     # O(1)
        end -= 1                       # O(1)
    return arr                         # O(1)

from functools import reduce

# 6) Using reduce with list concatenation
def rev_arr_red(arr):
    """
    Reverse via reduce and list concatenation.
    Time:  O(n^2)   (each concatenation [x] + acc costs O(k), summed k=1..n)
    Space: O(n^2)   (intermediate lists of growing size)
    """
    # reduce builds many intermediate lists of sizes 1, 2, ..., n
    rev_arr_temp = reduce(lambda acc, x: [x] + acc, arr, [])  # O(n^2)
    return rev_arr_temp
    """
    Reverse a list using reduce() and list concatenation.
    --------------------------------------------
    How it works (step by step):
      1. Start with an empty accumulator: acc = []
      2. For each element x in the original list `arr`:
           acc = [x] + acc
         i.e. prepend x to the front of the accumulated list.
      3. After processing all n elements, `acc` holds the reversed list.
    
    Example for arr = ['a','b','c']:
      - Initial acc = []
      - x = 'a' → acc = ['a']
      - x = 'b' → acc = ['b','a']
      - x = 'c' → acc = ['c','b','a']
      Final result: ['c','b','a']
    
    Time Complexity:
      - Each concatenation [x] + acc takes O(k) time when acc has length k.
      - Over n steps, k goes from 0 up to n-1, so total cost is
          1 + 2 + ... + (n-1) = O(n^2).
    
    Space Complexity:
      - Each step allocates a new list of size k+1.
      - Intermediate lists of sizes 1,2,...,n are created → O(n^2) total auxiliary space.
    """
    
# 7) Recursive (buggy – immediate return)
def rev_recursive(arr, start, end):
    """
    Supposed recursive reverse, but base condition is incorrect.
    Actual:
      Time:  O(1)
      Space: O(depth) → O(1)
    because it returns immediately when start <= end.
    """
    if start <= end:
        return
    # never reached in correct usage

# 8) Using a stack (copy + pop)
def rev_stack(arr):
    """
    Reverse by copying to a stack and popping.
    Time:  O(n)    (copy + n pops + n appends)
    Space: O(n)    (stack copy + result list of size n)
    """
    stack = arr[:]                      # O(n) copy
    rev_arr = []                        # O(1)
    while stack:                        # O(n) iterations
        rev_arr.append(stack.pop())     # pop() O(1), append() amortized O(1)
    return rev_arr                      # O(1)

# 9) Another in‑place while‑loop (identical to 5)
def rev_arrr(arr):
    """
    Reverse in‑place (duplicate of re_arr).
    Time:  O(n)
    Space: O(1)
    """
    n = len(arr)                       # O(1)
    i = 0                              # O(1)
    while i < n // 2:                  # O(n) loop
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]  # O(1)
        i += 1                         # O(1)
    return arr                         # O(1)



# print(rev([3, 2, 4, 1, 6, 7]))
# print(rev_arr([3, 2, 4, 1, 6, 7]))
print(rev_array([3, 2, 4, 1, 6, 7]))
print(rev_arrr([3, 2, 4, 1, 6, 7]))
