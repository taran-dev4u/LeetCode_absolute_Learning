**String**
●	Reverse a String
●	Check whether a String is Palindrome or not
●	Find Duplicate characters in a string
●	Why are strings immutable in Java?
●	Write a Code to check whether one string is a rotation of another
●	Write a Program to check whether a string is a valid shuffle of two strings or not
●	Count and Say problem
●	Write a program to find the longest Palindrome in a string [Longest palindromic Substring]
●	Find Longest Recurring Subsequence in String
●	Print all Subsequences of a string
●	Print all the permutations of the given string
●	Split the Binary string into two substring with equal 0's and 1's
●	Word Wrap Problem [VERY IMPL]
●	EDIT Distance [Very Imp]
●	Find the next greater number with the same set of digits. [Very Very IMPI]
●	Balanced Parenthesis problem
●	Word break Problem [Very imp]
●	Rabin Karp Algo
●	KMP Algo
●	Convert a Sentence into its equivalent mobile numeric keypad sequence
●	Minimum number of bracket reversals needed to make an expression balanced.
●	Count All Palindromic Subsequences in a given String.
●	Count of number of given string in 2D character array
●	Search a Word in a 2D Grid of characters
●	Boyer Moore Algorithm for Pattern Searching
●	Converting Roman Numerals to Decimal
●	Longest Common Prefix
●	Number of flips to make binary string alternate
●	Find the first repeated word in the string.
●	Minimum number of swaps for bracket balancing.
●	Find the longest common subsequence between two strings.
●	Program to generate all possible valid IP addresses from given string.
●	Write a program to find the smallest window that contains all characters of the string itself.
●	Rearrange characters in a string such that no two adjacent are same
●	Minimum characters to be added at front to make string palindrome
●	Given a sequence of words, print all anagrams together
●	Find the smallest window in a string containing all characters of another string
●	Recursively remove all adjacent duplicates
●	String matching where one string contains wildcard characters
●	Function to find Number of customers who could not get a computer
●	Transform One String to Another using Minimum Number of Given Operation
●	Check if two given strings are isomorphic to each other
●	Recursively print all sentences that can be formed from list of word lists

---

### 1. Reverse a String

* **Problem Definition:** Given a string `s`, produce a new string that is `s` in reverse order.
* **Real‑World Analogy:** Reading a sentence backwards, like decoding a mirrored sign.
* **Core Concept:** Two‑pointer swapping or stack/LIFO behavior.
* **Approach/Strategy:**

  * **In‑place (if mutable):** Swap characters at `i` and `n−1−i` for `i=0…⌊n/2⌋−1`.
  * **New string:** Traverse from end to start, appending each character.
* **Related Concepts:** String slicing (`s[::-1]` in Python); stacks; array reversal.

---

### 2. Check Whether a String Is a Palindrome

* **Problem Definition:** Determine if `s` reads the same forwards and backwards.
* **Real‑World Analogy:** “RADAR” or “LEVEL” in English.
* **Core Concept:** Symmetry check via two‑pointer.
* **Approach/Strategy:** Compare `s[i]` to `s[n−1−i]` for all `i< n/2`. Optionally skip non‑alphanumeric and lowercase to handle sentences.
* **Related Concepts:** Reverse string; sanitization (lowercasing, removing punctuation).

---

### 3. Find Duplicate Characters in a String

* **Problem Definition:** Identify characters that occur more than once in `s`.
* **Real‑World Analogy:** Spotting repeated letters in a ransom note.
* **Core Concept:** Frequency counting via hash map or fixed‑size array.
* **Approach/Strategy:** Traverse `s`, increment `count[c]`; then collect those with `count[c]>1`.
* **Related Concepts:** Anagrams; character histograms.

---

### 4. Why Are Strings Immutable in Java?

* **Problem Definition:** Explain the design rationale behind Java’s `String` immutability.
* **Real‑World Analogy:** A printed page that cannot be altered once published.
* **Core Concept:** Security, thread‑safety, caching/hashCode consistency.
* **Approach/Strategy:**

  * **Security:** Safe for classloading and network operations (e.g. `String` used in file paths).
  * **Performance:** Enables string interning and cached hash codes.
  * **Thread‑Safety:** Safe to share across threads without synchronization.
* **Related Concepts:** Java `StringBuilder`/`StringBuffer` for mutable operations; flyweight pattern.

---

### 5. Check Whether One String Is a Rotation of Another

* **Problem Definition:** Given `s1` and `s2` of equal length, determine if `s2` is a rotation of `s1` (e.g. “erbottlewat” is rotation of “waterbottle”).
* **Real‑World Analogy:** Rotating a dial so the sequence wraps around.
* **Core Concept:** Substring search on concatenated string.
* **Approach/Strategy:** Check `s2` length equals `s1`; then test if `s2` is a substring of `s1 + s1`. Use KMP/Rabin–Karp for O(n).
* **Related Concepts:** String matching; circular buffers.

---

### 6. Check Whether a String Is a Valid Shuffle of Two Strings

* **Problem Definition:** Given `A`, `B`, and `C`, determine if `C` is an interleaving (shuffle) of `A` and `B`, preserving character order within each.
* **Core Concept:** 2D DP on prefixes.
* **Approach/Strategy:**
  Build `dp[i][j] = True` if `C[0…i+j−1]` can be formed by interleaving `A[0…i−1]` and `B[0…j−1]`. Transitions from `dp[i−1][j]` or `dp[i][j−1]` when characters match.
* **Related Concepts:** LCS; string interleaving; 2D DP.

---

### 7. Count and Say Problem

* **Problem Definition:** Generate the nth term of the “count-and-say” sequence, where each term describes the previous term’s digits.
* **Real‑World Analogy:** Verbal telephone game: describe counts of repeated items.
* **Core Concept:** String building by run‑length encoding.
* **Approach/Strategy:** Iteratively build from term 1 (“1”): read current string, group consecutive identical chars, append count+character. Repeat `n−1` times.
* **Related Concepts:** Run‑length encoding; sequence generation.

---

### 8. Longest Palindromic Substring

* **Problem Definition:** Given `s`, find the longest contiguous substring that is a palindrome.
* **Real‑World Analogy:** Finding the longest symmetric segment in a text.
* **Core Concept:** Expand‑around‑center or DP or Manacher’s algorithm.
* **Approach/Strategy:**

  * **Expand:** For each index (and between indices), expand pointers while `s[l]==s[r]`, track max length. O(n²).
  * **Manacher’s:** Transform with separators and compute palindromic radii in O(n).
* **Related Concepts:** Longest palindromic subsequence; string transformation.

---

### 9. Longest Recurring Subsequence in String

* **Problem Definition:** Longest subsequence of `s` that appears at least twice without overlapping indices.
* **Core Concept:** LCS of `s` with itself, forbidding same‑index matches.
* **Approach/Strategy:** Build DP table `dp[i][j]` = LCS of `s[0…i−1]` and `s[0…j−1]`, but only if `i≠j`. Answer = `dp[n][n]`.
* **Related Concepts:** LCS; repetition detection; suffix arrays.

---

### 10. Print All Subsequences of a String

* **Problem Definition:** List every possible subsequence (not necessarily contiguous) of `s`.
* **Real‑World Analogy:** All possible playlists drawn from a set of songs.
* **Core Concept:** Recursion/backtracking or bitmask enumeration.
* **Approach/Strategy:**

  * **Recursive:** At each pos `i`, branch include or exclude `s[i]`.
  * **Bitmask:** For mask `0…(1<<n)−1`, build subsequence by checking each bit.
* **Related Concepts:** Power set; combinatorial explosion (2ⁿ outputs).

---

### 11. Print All Permutations of the Given String

* **Problem Definition:** Generate every ordering of characters in `s`.
* **Real‑World Analogy:** All seating arrangements around a table.
* **Core Concept:** Recursion with swapping or backtracking.
* **Approach/Strategy:**

  * Fix each character at position `start` by swapping with indices `start…n−1`, recurse on `start+1`.
  * Backtrack swaps to restore original.
* **Related Concepts:** Heap’s algorithm; factorial growth.

---

### 12. Split the Binary String into Two Substrings with Equal 0’s and 1’s

* **Problem Definition:** Partition a binary string into two non‑empty parts so each has the same count of ‘0’ and ‘1’. Count ways.
* **Core Concept:** Prefix counts and simple arithmetic.
* **Approach/Strategy:** Precompute total zeros/ones. Iterate split point, maintain prefix zeros/ones and check if `prefix0 == total0-prefix0` and similarly for ones. O(n).
* **Related Concepts:** Prefix sums; string partitioning.

---

### 13. Word Wrap Problem

* **Problem Definition:** Given words and a max line width, break lines to minimize total badness (`(remaining spaces)²`).
* **Core Concept:** DP on word positions with cost function.
* **Approach/Strategy:**
  Precompute extras\[i]\[j] = spaces left when words i…j in one line.
  `dp[j] = min(dp[i−1] + extras[i][j]²)` for all `i ≤ j`.
* **Related Concepts:** Text justification; line‑breaking algorithms (Knuth–Plass).

---

### 14. Edit Distance

* **Problem Definition:** Minimum insert/delete/replace ops to transform `A` into `B`.
* **Core Concept:** DP on string prefixes.
* **Approach/Strategy:** 2D `dp[i][j]`: if `A[i−1]==B[j−1]` then `dp[i−1][j−1]`; else `1+min(dp[i−1][j], dp[i][j−1], dp[i−1][j−1])`.
* **Related Concepts:** Sequence alignment; Levenshtein vs Damerau–Levenshtein.

---

### 15. Next Greater Number with Same Digits

* **Problem Definition:** Given a number as digit array, find the next lexicographically greater permutation, or report none.
* **Core Concept:** “Next permutation” algorithm.
* **Approach/Strategy:**

  1. From right, find first `i` with `a[i] < a[i+1]`.
  2. Find smallest digit to right of `i` greater than `a[i]`, swap.
  3. Reverse suffix `i+1…end`.
* **Related Concepts:** Permutation generation; lexicographic order.

---

### 16. Balanced Parenthesis Problem

* **Problem Definition:** Generate all strings of `n` pairs of well‑formed parentheses.
* **Real‑World Analogy:** Valid HTML/XML tag nesting.
* **Core Concept:** Backtracking with count constraints.
* **Approach/Strategy:** Recursively add ‘(’ if `open < n`, add ‘)’ if `close < open`, track `open`/`close` counts.
* **Related Concepts:** Catalan numbers; stack validation.

---

### 17. Word Break Problem

* **Problem Definition:** Determine if `s` can be segmented into space‑separated dictionary words.
* **Core Concept:** DP on prefixes or trie+DFS with memo.
* **Approach/Strategy:**
  `dp[0]=True`; for `i=1…n`, `dp[i]=True` if there exists `j<i` with `dp[j] and s[j:i] in dict`.
* **Related Concepts:** String segmentation; minimum cuts.

---

### 18. Rabin–Karp Algorithm

* **Problem Definition:** Find occurrences of pattern `P` in text `T` using rolling hash.
* **Core Concept:** Rolling hash for substring comparison.
* **Approach/Strategy:**
  Compute hash of `P` and initial window of `T`. Slide window: update hash in O(1), if hashes match, verify characters to avoid collision. O(n+m) average.
* **Related Concepts:** Karp–Rabin fingerprint; string hashing.

---

### 19. Knuth–Morris–Pratt (KMP) Algorithm

* **Problem Definition:** Search pattern `P` in text `T` in O(n+m) worst‑case time.
* **Core Concept:** Failure function (lps array) to skip comparisons.
* **Approach/Strategy:**
  Precompute `lps[i]` = length of longest prefix of `P` that’s a suffix ending at `i`. Then scan `T`, on mismatch jump `j = lps[j−1]` instead of resetting to 0.
* **Related Concepts:** Finite automata string matching; Z‑algorithm.

---

### 20. Convert Sentence to Mobile Numeric Keypad Sequence

* **Problem Definition:** Map each letter to its phone digit sequence (e.g. ‘c’ → “222”), output concatenated digits for a sentence, inserting pauses when consecutive letters map to same key.
* **Real‑World Analogy:** Old T9 texting.
* **Core Concept:** Lookup table + handling collisions.
* **Approach/Strategy:** Predefine mapping `'a'→"2"`, `'b'→"22"`,… track last digit; if new sequence’s first digit equals last, insert a separator (e.g. space).
* **Related Concepts:** Finite mapping; run‑length logic.

---

### 21. Minimum Bracket Reversals to Balance Expression

* **Problem Definition:** Given a string of only ‘{’ and ‘}’, find min reversals to make it balanced.
* **Core Concept:** Stack or scan counting unmatched opens/closes.
* **Approach/Strategy:**
  Remove balanced pairs via stack or counter. Let `m` = unmatched ‘{’, `n` = unmatched ‘}’. Answer = `ceil(m/2) + ceil(n/2)`.
* **Related Concepts:** Bracket validation; greedy.

---

### 22. Count All Palindromic Subsequences

* **Problem Definition:** Count distinct palindromic subsequences in `s`.
* **Core Concept:** DP with inclusion–exclusion.
* **Approach/Strategy:**
  `dp[i][j]` = if `s[i]==s[j]`: `dp[i+1][j] + dp[i][j-1] +1` else `dp[i+1][j]+dp[i][j-1]−dp[i+1][j-1]`.
* **Related Concepts:** Palindromic substring counting; modulo arithmetic.

---

### 23. Count of a Given String in 2D Character Array

* **Problem Definition:** Count occurrences of word `W` in a 2D grid along allowed directions (e.g. horizontal, vertical, diagonal).
* **Core Concept:** DFS from each cell with backtracking.
* **Approach/Strategy:** For each grid cell that matches `W[0]`, recursively explore all 8 (or allowed) directions, matching subsequent chars, marking visited as needed.
* **Related Concepts:** Word search puzzles; backtracking.

---

### 24. Search a Word in a 2D Grid of Characters

* **Problem Definition:** Similar to above but return True/False if at least one occurrence exists.
* **Approach/Strategy:** Same DFS/backtracking, stop on first match.
* **Related Concepts:** Boggle solver; trie optimization for multiple words.

---

### 25. Boyer–Moore Algorithm for Pattern Searching

* **Problem Definition:** String search using bad‑character and good‑suffix heuristics to skip ahead.
* **Core Concept:** Precomputed shift tables to maximize jumps on mismatches.
* **Approach/Strategy:**

  1. **Bad character:** On mismatch at `i`, shift pattern so mismatched text char aligns with its last occurrence in pattern.
  2. **Good suffix:** If a suffix matches, shift pattern to align next possible match of that suffix.
* **Related Concepts:** Horspool’s algorithm; Sunday’s quick search.

---

### 26. Converting Roman Numerals to Decimal

* **Problem Definition:** Parse a string of Roman numerals into its integer value.
* **Core Concept:** Add/subtract pairs based on ordering.
* **Approach/Strategy:** Traverse left→right, if current symbol value < next symbol’s, subtract it; else add it.
* **Related Concepts:** Finite mapping; greedy parsing.

---

### 27. Longest Common Prefix

* **Problem Definition:** Given an array of strings, find longest prefix common to all.
* **Real‑World Analogy:** Common folder path among file paths.
* **Core Concept:** Vertical or horizontal scanning, or divide‑and‑conquer.
* **Approach/Strategy:**

  * **Horizontal:** Compare prefix of first two, then with third, etc.
  * **Vertical:** For char position `i`, check all strings’ `s[j][i]`; stop on mismatch.
* **Related Concepts:** Trie for multi-string prefix queries; binary search on prefix length.

---

### 28. Number of Flips to Make Binary String Alternate

* **Problem Definition:** Given binary string, compute min flips to make it alternating (`0101…` or `1010…`).
* **Core Concept:** Compare with the two patterns.
* **Approach/Strategy:** Compute mismatches with pattern1 (`0,1,0,1…`) and pattern2 (`1,0,1,0…`), answer = min(mismatches1, mismatches2).
* **Related Concepts:** Greedy flips; bitwise operations.

---

### 29. Find the First Repeated Word in a String

* **Problem Definition:** In a sentence, find the earliest word that occurs more than once.
* **Core Concept:** Hash set and tokenization.
* **Approach/Strategy:** Split on whitespace/punctuation, iterate words in order, track seen; first time you see a word already in set, that’s the answer.
* **Related Concepts:** Case normalization; punctuation stripping.

---

### 30. Minimum Number of Swaps for Bracket Balancing

* **Problem Definition:** Given a string of `[` and `]`, find min swaps to balance it.
* **Core Concept:** Two‑pointer or counting imbalance.
* **Approach/Strategy:** Track balance = 0, swaps = 0, unbalanced = 0; for each char: if `[` then balance++; else balance--; if balance<0, unbalanced++, balance=0; at end swaps = ceil(unbalanced/2).
* **Related Concepts:** Bracket reversal; greedy fix.

---

### 31. Longest Common Subsequence Between Two Strings

* **Problem Definition:** Standard LCS problem (see #14 above).
* **Related Concepts:** See LCS entry.

---

### 32. Generate All Possible Valid IP Addresses from a String

* **Problem Definition:** Given digits only, insert 3 dots to form all valid IPv4 addresses (each segment 0–255, no leading zeros).
* **Core Concept:** Backtracking with pruning.
* **Approach/Strategy:** Recursively place dots: track segment count and start index; for each segment try lengths 1–3, validate numeric range and leading‑zero rule, recurse.
* **Related Concepts:** String partitioning; backtracking.

---

### 33. Smallest Window Containing All Characters of Itself

* **Problem Definition:** Find the shortest substring of `s` that contains every distinct character present in `s`.
* **Core Concept:** Sliding window + hash counts.
* **Approach/Strategy:**
  Expand right pointer, counting chars; once window contains all unique chars, shrink left pointer until it no longer does; track min window size.
* **Related Concepts:** Minimum window substring (general s, t); two‑pointer technique.

---

### 34. Rearrange Characters so No Two Adjacent Are the Same

* **Problem Definition:** Given `s`, rearrange its letters so no identical letters are adjacent, or report impossible.
* **Core Concept:** Greedy with max‑heap of character counts.
* **Approach/Strategy:**
  Build max‑heap of `(count, char)`. Repeatedly pop top two, append them in order, decrement counts, push back if still positive.
* **Related Concepts:** Rearrange string by frequency; reorganize string problem.

---

### 35. Minimum Characters to Add at Front to Make String Palindrome

* **Problem Definition:** Find fewest chars prepended to `s` to make it a palindrome.
* **Core Concept:** Compute longest palindromic prefix.
* **Approach/Strategy:**
  Build `T = s + ‘#’ + reverse(s)`, compute LPS array (KMP) for `T`; value at end = length of longest palindromic prefix. Answer = `n − LPS[last]`.
* **Related Concepts:** KMP preprocessing; palindrome augmentation.

---

### 36. Given a Sequence of Words, Print All Anagrams Together

* **Problem Definition:** Group words that are anagrams of each other.
* **Core Concept:** Canonical key by sorted letters or letter count.
* **Approach/Strategy:**
  Build hash map `key → list of words`, where `key = sorted(word)` or 26‑length count tuple. Then output each group.
* **Related Concepts:** Grouping by signature; multimap.

---

### 37. Smallest Window Containing All Characters of Another String

* **Problem Definition:** Standard minimum window substring: given `s` and `t`, find minimum substring of `s` containing all chars of `t` (with multiplicities).
* **Core Concept:** Sliding window with two hash maps and a counter of required matches.
* **Approach/Strategy:**
  Expand right, decrement needed counts; once all matched, shrink left while maintaining match, track minimal window.
* **Related Concepts:** Same as #33 but with distinct source and target strings.

---

### 38. Recursively Remove All Adjacent Duplicates

* **Problem Definition:** Repeatedly delete adjacent duplicate characters until none remain.
* **Core Concept:** Stack or recursion.
* **Approach/Strategy:**
  Traverse string, use stack: if top equals current, pop (removes both), else push. Convert stack to string.
* **Related Concepts:** String reduction; elimination games.

---

### 39. String Matching with Wildcard Characters

* **Problem Definition:** Given pattern `p` with `?` (match any single char) and `*` (match any sequence), test if it matches entire string `s`.
* **Core Concept:** DP on indices or two‑pointer with backtracking.
* **Approach/Strategy:**
  2D DP `dp[i][j]` = match up to `s[0…i−1]` and `p[0…j−1]`; handle cases for normal char, `?`, and `*` (zero or more). O(nm).
* **Related Concepts:** Regex matching; wildcard expansion.

---

### 40. Number of Customers Who Could Not Get a Computer

* **Problem Definition:** Given entry/exit events for customers and limited computers, count how many were turned away.
* **Core Concept:** Event sorting + greedy allocation.
* **Approach/Strategy:**
  Create events `(time, +1 for entry/-1 for exit)`, sort by time (exit before entry on tie), track `in_use`; on entry if `in_use < total` increment, else increment turned\_away.
* **Related Concepts:** Sweep‑line; interval scheduling.

---

### 41. Transform One String to Another with Minimum Operations

* **Problem Definition:** Convert `A` to `B` using insert/delete/replace, count min ops. (Essentially Edit Distance.)
* **Related Concepts:** See #14 above.

---

### 42. Check if Two Strings Are Isomorphic

* **Problem Definition:** Two strings are isomorphic if the characters in one can be replaced to get the other, preserving order and uniqueness of mapping.
* **Core Concept:** Bi‑directional mapping check.
* **Approach/Strategy:**
  Maintain two hash maps `map_s_t` and `map_t_s`. For each `i`, if `s[i]`→`t[i]` inconsistent or `t[i]` already mapped to different `s[j]`, return False.
* **Related Concepts:** Pattern matching; bijections.

---

### 43. Recursively Print All Sentences from List of Word Lists

* **Problem Definition:** Given a list of lists `[[w1,w2], [w3], [w4,w5,w6], …]`, print all sentences by picking one word from each list in order.
* **Core Concept:** Cartesian product via recursion.
* **Approach/Strategy:** Backtrack with an index `i` over lists, append each word in `lists[i]` to current sentence, recurse to `i+1`.
* **Related Concepts:** Nested loops; product in Python’s itertools.

---

