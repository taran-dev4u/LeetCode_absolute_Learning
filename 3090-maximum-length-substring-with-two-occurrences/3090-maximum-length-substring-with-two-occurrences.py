from collections import defaultdict

class Solution:
    """
    Problem Analysis:
    - Input: A string `s` consisting of lowercase English letters, with length between 2 and 100.
    - Output: The maximum length of a substring such that every character in the substring appears at most twice.
    - Constraints:
      - len(s) <= 100, which is extremely small. An O(N^2) or even O(N^3) approach would pass, but an O(N) sliding window approach is optimal and extremely fast.
    
    Optimal Algorithm Choice:
    - Sliding Window (Two Pointers):
      - Maintain a window defined by pointers `left` and `right`.
      - Expand the window by moving `right` to the right and adding `s[right]` to a frequency count map.
      - If any character's frequency exceeds 2, shrink the window from the left by moving `left` forward and decrementing the frequency of `s[left]` until all character frequencies are <= 2.
      - At each step, update the maximum length encountered.

    Time Complexity:
    - O(N) where N is the length of the string `s`, because each character is visited at most twice (once by `right`, once by `left`).
    
    Space Complexity:
    - O(1) auxiliary space, since the alphabet size is fixed at 26 lowercase English letters.
    
    Edge Cases:
    - All characters are the same (e.g., "aaaa"): max length should be 2.
    - All characters are unique (e.g., "abcd"): max length should be the length of the string.
    - Minimum length string (len = 2).
    """

    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            char = s[right]
            freq[char] += 1
            
            while freq[char] > 2:
                freq[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len