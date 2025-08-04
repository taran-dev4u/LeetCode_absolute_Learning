#!/usr/bin/env python3
"""
Four Approaches to Huffman Coding with Complete Examples:

1. Naïve O(n^2) Scanning
2. Min‑Heap (O(n log n))
3. Two‑Queue Method (O(n log n))
4. Canonical Huffman Code Assignment (O(n log n))

Each approach builds a Huffman tree (except canonical, which
assigns codes from lengths), then extracts prefix‑free codes,
and prints them alongside total bit‑cost.
"""

import heapq
from collections import deque

# ----------------------------------------
# 1) NODE CLASS & CODE EXTRACTION ROUTINE
# ----------------------------------------
class Node:
    def __init__(self, freq, symbol=None, left=None, right=None):
        """
        A node in the Huffman tree.
        freq   : aggregated frequency
        symbol : the character (for leaves); None for internal nodes
        left   : left child (represents '0' bit)
        right  : right child (represents '1' bit)
        """
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        # Allows heapq to compare Nodes by frequency
        return self.freq < other.freq

def extract_codes(root):
    """
    Traverse the Huffman tree to build codes:
      left → '0', right → '1'
    Returns: dict symbol → binary code string
    """
    codes = {}
    def dfs(node, prefix):
        if node is None:
            return
        if node.symbol is not None:
            # Leaf: assign code; if tree has one node, code '0'
            codes[node.symbol] = prefix or '0'
        else:
            dfs(node.left,  prefix + '0')
            dfs(node.right, prefix + '1')
    dfs(root, "")
    return codes

# -------------------------------
# 2) NAÏVE O(n^2) SCANNING METHOD
# -------------------------------
def build_huffman_naive(freq_map):
    """
    Very simple, O(n^2 log n) if using sort each iteration,
    or O(n^2) if scanning min‑pairs manually.
    """
    # Create leaf nodes
    nodes = [Node(f, s) for s, f in freq_map.items()]

    # Merge until one tree remains
    while len(nodes) > 1:
        # Sort by frequency ascending
        nodes.sort(key=lambda n: n.freq)
        # Pop two smallest
        left  = nodes.pop(0)
        right = nodes.pop(0)
        # Merge and append
        merged = Node(left.freq + right.freq, None, left, right)
        nodes.append(merged)

    return nodes[0] if nodes else None

# -----------------------------
# 3) MIN‑HEAP (BINARY HEAP) METHOD
# -----------------------------
def build_huffman_heap(freq_map):
    """
    Uses heapq for O(n log n) performance.
    """
    # Build initial heap of leaves
    heap = [Node(f, s) for s, f in freq_map.items()]
    heapq.heapify(heap)  # O(n)

    # Merge until single tree
    while len(heap) > 1:
        left  = heapq.heappop(heap)  # O(log n)
        right = heapq.heappop(heap)  # O(log n)
        merged = Node(left.freq + right.freq, None, left, right)
        heapq.heappush(heap, merged) # O(log n)

    return heap[0] if heap else None

# -----------------------------
# 4) TWO‑QUEUE METHOD
# -----------------------------
def build_huffman_twoqueues(freq_map):
    """
    Two sorted queues approach for O(n log n) initial sort
    and O(n) merging.
    """
    # Q1: sorted leaves, Q2: initially empty
    leaves = sorted((Node(f, s) for s, f in freq_map.items()), key=lambda n: n.freq)
    Q1 = deque(leaves)
    Q2 = deque()

    def pop_smallest():
        # Return and remove the smaller head among Q1 and Q2
        if not Q2 or (Q1 and Q1[0].freq <= Q2[0].freq):
            return Q1.popleft()
        else:
            return Q2.popleft()

    # Merge n‑1 times
    for _ in range(len(leaves) - 1):
        x = pop_smallest()
        y = pop_smallest()
        merged = Node(x.freq + y.freq, None, x, y)
        Q2.append(merged)

    # Remaining tree root
    return (Q1 or Q2)[0]

# ---------------------------------
# 5) CANONICAL HUFFMAN ASSIGNMENT
# ---------------------------------
def canonical_huffman(lengths):
    """
    Given a dict symbol -> code length, produce canonical codes.
    """
    # Sort by (length, symbol)
    sorted_syms = sorted(lengths.items(), key=lambda kv: (kv[1], kv[0]))
    codes = {}
    code_value = 0
    prev_len = 0

    for sym, length in sorted_syms:
        # Shift left for increased length
        code_value <<= (length - prev_len)
        # Format code_value as binary, zero‑padded to 'length'
        codes[sym] = format(code_value, 'b').zfill(length)
        code_value += 1
        prev_len = length

    return codes

# -------------------------
# 6) DRIVER / EXAMPLE USAGE
# -------------------------
if __name__ == "__main__":
    # Example frequency map
    freq_map = {
        'a': 5,
        'b': 9,
        'c': 12,
        'd': 13,
        'e': 16,
        'f': 45
    }

    print("\n=== Naïve O(n^2) Huffman ===")
    root_naive = build_huffman_naive(freq_map)
    codes_naive = extract_codes(root_naive)
    for sym, code in sorted(codes_naive.items()):
        print(f"'{sym}': {code}")
    total_naive = sum(len(codes_naive[s]) * freq_map[s] for s in freq_map)
    print(f"Total bits: {total_naive}")

    print("\n=== Min‑Heap O(n log n) Huffman ===")
    root_heap = build_huffman_heap(freq_map)
    codes_heap = extract_codes(root_heap)
    for sym, code in sorted(codes_heap.items()):
        print(f"'{sym}': {code}")
    total_heap = sum(len(codes_heap[s]) * freq_map[s] for s in freq_map)
    print(f"Total bits: {total_heap}")

    print("\n=== Two‑Queue O(n log n) Huffman ===")
    root_2q = build_huffman_twoqueues(freq_map)
    codes_2q = extract_codes(root_2q)
    for sym, code in sorted(codes_2q.items()):
        print(f"'{sym}': {code}")
    total_2q = sum(len(codes_2q[s]) * freq_map[s] for s in freq_map)
    print(f"Total bits: {total_2q}")

    print("\n=== Canonical Huffman Codes ===")
    # Derive lengths from one of the above (they all produce same lengths)
    lengths = {sym: len(codes_heap[sym]) for sym in freq_map}
    codes_canon = canonical_huffman(lengths)
    for sym, code in sorted(codes_canon.items()):
        print(f"'{sym}': {code}")
    total_canon = sum(len(codes_canon[s]) * freq_map[s] for s in freq_map)
    print(f"Total bits: {total_canon}")
