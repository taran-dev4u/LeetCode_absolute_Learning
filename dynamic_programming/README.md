# Dynamic Programming
●	Coin Change Problem
●	Knapsack Problem
●	Binomial coefficient Problem
●	Permutation Coefficient Problem
●	Program for nth Catalan Number
●	Matrix Chain Multiplication
●	Edit Distance
●	Subset Sum Problem
●	Friends Pairing Problem
●	Gold Mine Problem
●	Assembly Line Scheduling Problem
●	Painting the Fence problem
●	Maximize The Cut Segments
●	Longest Common Subsequence
●	Longest Repeated Subsequence
●	Longest Increasing Subsequence
●	Space Optimized Solution of LCS
●	LCS (Longest Common Subsequence) of three strings
●	Maximum Sum Increasing Subsequence
●	Count all subsequences having product less than K
●	Longest subsequence such that difference between adjacent is one
●	Maximum subsequence sum such that no three are consecutive
●	Egg Dropping Problem
●	Maximum Length Chain of Pairs
●	Maximum size square sub-matrix with all 1s
●	Maximum sum of pairs with specific difference
●	Min Cost Path Problem
●	Maximum difference of zeros and ones in binary string
●	Minimum number of jumps to reach end
●	Minimum cost to fill given weight in a bag
●	Minimum removals from array to make max-min <= K
●	Longest Common Substring
●	Count number of ways to reach a given score in a game
●	Count Balanced Binary Trees of Height h
●	Largest Sum Contiguous Subarray [V>V>V>V IMP]
●	Smallest sum contiguous subarray
●	Unbounded Knapsack (Repetition of items allowed)
●	Word Break Problem
●	Largest independent Set Problem
●	Partition problem
●	Longest Palindromic Subsequence
●	Count All Palindromic Subsequence in a given String
●	Longest Palindromic Substring
●	Longest alternating subsequence
●	Weighted Job Scheduling
●	Coin game winner where every player has three choices
●	Count Derangements (Permutation such that no element appears in its original position) [IMPORTANT]
●	Maximum profit by buying and selling a share at most twice [IMP]
●	Optimal Strategy for a Game
●	Optimal Binary Search Tree
●	Palindrome Partitioning Problem
●	Word Wrap Problem
●	Mobile Numeric Keypad Problem [IMP]
●	Boolean Parenthesization Problem
●	Largest rectangular sub matrix whose sum is 0
●	Largest area rectangular sub-matrix with equal number of 1's and 0's [IMP]
●	Maximum sum rectangle in a 2D matrix
●	Maximum profit by buying and selling a share at most k times
●	Find if a string is interleaved of two other strings
●	Maximum Length of Pair Chain



### 1. Coin Change Problem

* **Problem Definition:** Given coin denominations and a target sum, count how many ways you can make that sum using unlimited coins.
* **Real‑World Analogy:** A cashier giving change with unlimited supplies of certain coins.
* **Core Concept:** Unbounded combinations; order doesn’t matter.
* **Approach/Strategy:** Use a 1D DP array `dp[0…sum]` initialized `dp[0]=1`; for each coin `c`, for `i=c…sum`: `dp[i]+=dp[i-c]`.
* **Related Concepts:** Unbounded knapsack; partition functions; generating functions.

### 2. Knapsack Problem (0/1)

* **Problem Definition:** Given weights and values for `n` items and capacity `W`, maximize total value without exceeding `W`.
* **Real‑World Analogy:** Packing a suitcase of fixed capacity to maximize worth of contents.
* **Core Concept:** Binary inclusion/exclusion; optimal substructure.
* **Approach/Strategy:** Build DP table `dp[i][w]` = best value using first `i` items and capacity `w`:
  `dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i]]+val[i])`.
* **Related Concepts:** Subset-sum; branch-and-bound; unbounded knapsack variant.

### 3. Binomial Coefficient Problem

* **Problem Definition:** Compute C(n, r) = n!/(r!·(n − r)!) for given `n`, `r`.
* **Real‑World Analogy:** Choosing `r` people from `n`.
* **Core Concept:** Pascal’s triangle identity: C(n, r)=C(n−1, r−1)+C(n−1, r).
* **Approach/Strategy:** DP triangular table `C[i][j]` for 0≤j≤i≤n with base `C[i][0]=C[i][i]=1`, else sum of two above.
* **Related Concepts:** Combinatorics; dynamic programming; modular arithmetic optimizations.

### 4. Permutation Coefficient Problem

* **Problem Definition:** Compute P(n, r) = n!/(n−r)! = number of ordered arrangements of size `r` from `n` items.
* **Real‑World Analogy:** Seating `r` people in `n` chairs.
* **Core Concept:** Permutation identity: P(n, r) = n·P(n−1, r−1).
* **Approach/Strategy:** Either compute factorials directly or fill `P[i][j]` via DP: `P[i][j] = P[i][j-1]*(i-j+1)`.
* **Related Concepts:** Factorials; binomial coefficients; combinatorial identities.

### 5. nth Catalan Number

* **Problem Definition:** Compute the nth Catalan number: Cₙ = (1/(n+1))(2n choose n).
* **Real‑World Analogy:** Number of valid parentheses sequences of length 2n.
* **Core Concept:** C₀=1, Cₙ=Σ₀≤i<ₙ(Cᵢ·Cₙ₋₁₋ᵢ).
* **Approach/Strategy:** Fill DP array `cat[0]=1`; for `n=1…N`: `cat[n]=Σ cat[i]*cat[n-1-i]`.
* **Related Concepts:** Dyck paths; binary tree shapes; Motzkin numbers.

### 6. Matrix Chain Multiplication

* **Problem Definition:** Given matrix dimensions p₀×p₁, p₁×p₂, …, pₙ₋₁×pₙ, find min scalar multiplications to multiply chain.
* **Real‑World Analogy:** Optimizing order of multiple matrix multiplications to minimize computation.
* **Core Concept:** Optimal parenthesization; associative property.
* **Approach/Strategy:** DP `m[i][j]` = min cost for chain i…j; `m[i][j]=minₖ(m[i][k]+m[k+1][j]+p[i−1]·p[k]·p[j])`.
* **Related Concepts:** Optimal binary tree; chain of operations; interval DP.

### 7. Edit Distance (Levenshtein Distance)

* **Problem Definition:** Min operations (insert, delete, replace) to transform string A into B.
* **Real‑World Analogy:** Spell-check suggestion distance.
* **Core Concept:** String alignment; DP on prefixes.
* **Approach/Strategy:** 2D DP `dp[i][j]` = min of `dp[i-1][j]+1`, `dp[i][j-1]+1`, `dp[i-1][j-1]+ cost(∂)`.
* **Related Concepts:** Needleman–Wunsch; Damerau–Levenshtein; sequence alignment.

### 8. Subset Sum Problem

* **Problem Definition:** Given array and sum S, determine if any subset sums to S.
* **Real‑World Analogy:** Partitioning items into two groups of equal weight.
* **Core Concept:** 0/1 knapsack with boolean DP.
* **Approach/Strategy:** DP table `dp[i][s]` = dp\[i-1]\[s] OR dp\[i-1]\[s−arr\[i]]; or optimize to 1D.
* **Related Concepts:** Knapsack; partition problem; bitset optimizations.

### 9. Friends Pairing Problem

* **Problem Definition:** Number of ways `n` friends can remain single or pair up.
* **Real‑World Analogy:** Seating pairs at a dance.
* **Core Concept:** Recurrence f(n)=f(n−1)+(n−1)·f(n−2).
* **Approach/Strategy:** Compute via DP or recursion with memoization.
* **Related Concepts:** Fibonacci; derangements.

### 10. Gold Mine Problem

* **Problem Definition:** Given a grid of gold values, start at any row in column 0, move right, right-up, or right-down, maximize collected gold.
* **Real‑World Analogy:** Mining expedition through terrain with constraints.
* **Core Concept:** DP on grid with local transitions.
* **Approach/Strategy:** For each cell `(i,j)`, `dp[i][j]=gold[i][j]+max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])`.
* **Related Concepts:** Maximum path in matrix; matrix DP; 2D Kadane variants.

### 11. Assembly Line Scheduling

* **Problem Definition:** Two assembly lines, each with stations and transfer times; minimize total time through stations.
* **Real‑World Analogy:** Car factory with two parallel assembly lines.
* **Core Concept:** DP with two states per station.
* **Approach/Strategy:** Maintain `T1[i]`, `T2[i]` = min time to reach station i on each line; update considering staying or transferring.
* **Related Concepts:** Pipeline scheduling; shortest path in DAG.

### 12. Painting the Fence Problem

* **Problem Definition:** Paint `n` fences with `k` colors so that no more than two adjacent share the same color, count ways.
* **Real‑World Analogy:** Avoiding monotony in fence design.
* **Core Concept:** DP on positions with last‐two‐colors state.
* **Approach/Strategy:** Track `same[i]` (i-th same as i−1) and `diff[i]` (different); `diff[i]= (same[i−1]+diff[i−1])*(k−1)`, `same[i]=diff[i−1]*1`.
* **Related Concepts:** Colorings on paths; recurrence relations.

### 13. Maximize The Cut Segments

* **Problem Definition:** Given rod length `n` and cut lengths `a, b, c`, maximize the number of segments.
* **Real‑World Analogy:** Cutting ribbon into maximum equal‐valued pieces.
* **Core Concept:** DP for maximizing count.
* **Approach/Strategy:** DP array `dp[0…n]`, `dp[i] = max(dp[i-a], dp[i-b], dp[i-c]) + 1` if valid.
* **Related Concepts:** Unbounded knapsack maximizing items; greedy fails.

### 14. Longest Common Subsequence (LCS)

* **Problem Definition:** Longest sequence appearing (not necessarily contiguous) in both strings.
* **Real‑World Analogy:** Finding common DNA subsequence between species.
* **Core Concept:** 2D DP on string prefixes.
* **Approach/Strategy:** `dp[i][j]` = if `A[i-1]==B[j-1]` then `1+dp[i-1][j-1]` else `max(dp[i-1][j],dp[i][j-1])`.
* **Related Concepts:** Edit distance; longest common substring.

### 15. Longest Repeated Subsequence

* **Problem Definition:** Longest subsequence that appears at least twice without overlapping.
* **Real‑World Analogy:** Identifying repeated patterns in a song.
* **Core Concept:** Modified LCS on same string with index mismatch constraint.
* **Approach/Strategy:** LCS of `S` with itself, but only match `i≠j`.
* **Related Concepts:** Suffix arrays; string periodicity.

### 16. Longest Increasing Subsequence (LIS)

* **Problem Definition:** Length of longest strictly increasing subsequence in an array.
* **Real‑World Analogy:** Longest chain of increasing stock prices.
* **Core Concept:** DP O(n²) or patience‐sorting O(n log n).
* **Approach/Strategy:**

  * O(n²): `dp[i]=1+max(dp[j] for j<i if a[j]<a[i])`.
  * O(n log n): Maintain `tail` array via binary search insertion.
* **Related Concepts:** Longest decreasing subsequence; patience sorting.

### 17. Space‑Optimized Solution of LCS

* **Problem Definition:** Compute LCS length using O(min(m,n)) space instead of O(mn).
* **Core Concept:** Only two rows of the DP table are needed at a time.
* **Approach/Strategy:** Alternate between two 1D arrays for current and previous rows.
* **Related Concepts:** Hirschberg’s algorithm for sequence reconstruction.

### 18. LCS of Three Strings

* **Problem Definition:** Longest common subsequence among three strings A, B, C.
* **Core Concept:** 3D DP on indices (i,j,k).
* **Approach/Strategy:** `dp[i][j][k]` = if all match then `1+dp[i-1][j-1][k-1]` else max of three pairwise subproblems.
* **Related Concepts:** Multi‑sequence alignment; k‑dimensional DP.

### 19. Maximum Sum Increasing Subsequence (MSIS)

* **Problem Definition:** Among all increasing subsequences, find one with maximum sum.
* **Core Concept:** Variation of LIS with sum instead of length.
* **Approach/Strategy:** `dp[i] = a[i] + max(dp[j] for j<i if a[j]<a[i])`.
* **Related Concepts:** Weighted LIS; longest bitonic subsequence.

### 20. Count All Subsequences Having Product < K

* **Problem Definition:** Count subsequences whose product of elements is strictly less than `K`.
* **Core Concept:** Two‑pointer on sorted array or DP/backtracking for small n.
* **Approach/Strategy:** Sort, then for each start expand end pointer maintaining product and count new subsequences.
* **Related Concepts:** Sliding window; subset enumeration.

### 21. Longest Subsequence with Adjacent Diff = 1

* **Problem Definition:** Longest subsequence where every adjacent pair differs by exactly 1.
* **Core Concept:** DP indexed by value.
* **Approach/Strategy:** `dp[val] = 1 + max(dp[val-1], dp[val+1])` encountered so far; track global max.
* **Related Concepts:** Longest arithmetic progression subsequence.

### 22. Maximum Subsequence Sum such that No Three Are Consecutive

* **Problem Definition:** Max sum of elements picking from array without selecting three consecutive picks.
* **Core Concept:** DP with state for count of consecutive picks.
* **Approach/Strategy:** Let `dp[i][c]` = max sum up to i with `c` consecutive picks at end (`0≤c≤2`). Update transitions accordingly.
* **Related Concepts:** House robber with k‑distance constraint.

### 23. Egg Dropping Problem

* **Problem Definition:** Given `k` eggs and `n` floors, find min trials to determine highest safe floor.
* **Real‑World Analogy:** Testing the strength threshold of glass panes.
* **Core Concept:** Minimize worst‑case number of moves.
* **Approach/Strategy:** DP `dp[e][f]` = 1 + min₁≤x≤f(max(dp\[e-1]\[x-1], dp\[e]\[f-x])) with binary search or optimized monotonicity.
* **Related Concepts:** Divide and conquer; binomial trials.

### 24. Maximum Length Chain of Pairs

* **Problem Definition:** Given pairs `(aᵢ,bᵢ)`, find longest chain where `bᵢ < aⱼ` for consecutive pairs.
* **Core Concept:** Interval scheduling; longest path in DAG.
* **Approach/Strategy:** Sort by second value and apply LIS on start times or greedy scheduling.
* **Related Concepts:** Activity selection; weighted interval scheduling.

### 25. Maximum‑Size Square Sub‑matrix with All 1s

* **Problem Definition:** In a binary matrix, find largest square consisting entirely of 1s.
* **Core Concept:** 2D DP on neighborhoods.
* **Approach/Strategy:** For each cell `(i,j)`: if `mat[i][j]=1`, `dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`. Track max.
* **Related Concepts:** Largest rectangle in histogram; maximal rectangle in binary matrix.

### 26. Maximum Sum of Pairs with Specific Difference

* **Problem Definition:** From array, choose disjoint pairs `(i,j)` with `|a[i]−a[j]|=K` to maximize total sum of paired elements.
* **Core Concept:** Greedy after sorting or DP matching.
* **Approach/Strategy:** Sort arr, then two‑pointer to form valid pairs and accumulate sum greedily.
* **Related Concepts:** Maximum matching in bipartite graph; weighted pairing.

### 27. Min Cost Path Problem

* **Problem Definition:** In a cost matrix, find path from `(0,0)` to `(m-1,n-1)` with min total cost, moving right/down/diag.
* **Core Concept:** Grid DP.
* **Approach/Strategy:** `dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`.
* **Related Concepts:** Shortest path in weighted grid; dynamic programming on DAG.

### 28. Maximum Difference of Zeros and Ones in Binary String

* **Problem Definition:** Flip a contiguous substring to maximize difference (#zeros−#ones).
* **Core Concept:** Transform to max‑subarray by mapping `0→1`, `1→−1`.
* **Approach/Strategy:** Use Kadane’s algorithm on the mapped array.
* **Related Concepts:** Maximum subarray; range flipping.

### 29. Minimum Number of Jumps to Reach End

* **Problem Definition:** Given array where each element indicates max jump length, find min jumps to last index.
* **Core Concept:** Greedy range expansion or BFS on array indices.
* **Approach/Strategy:** Track current reach and farthest reach in a single sweep. Increment jump when you exceed current reach.
* **Related Concepts:** BFS on graphs; interval covering.

### 30. Minimum Cost to Fill Given Weight in a Bag

* **Problem Definition:** Given item weights and costs, fill bag exactly of weight W with min cost, items unlimited.
* **Core Concept:** Unbounded knapsack minimization.
* **Approach/Strategy:** DP `dp[0…W]` initialized ∞ except `dp[0]=0`; for each weight `w`, for `i=w…W`: `dp[i]=min(dp[i], dp[i-w]+cost[w])`.
* **Related Concepts:** Coin change (min coins); rod cutting.

### 31. Minimum Removals from Array to Make max-min ≤ K

* **Problem Definition:** Remove fewest elements so that the remaining array’s max minus min ≤ K.
* **Core Concept:** Two‑pointer on sorted array.
* **Approach/Strategy:** Sort array, then slide window to find max window size where `arr[j]−arr[i]≤K`, removals = n−maxSize.
* **Related Concepts:** Longest subarray with constraint; sliding window.

### 32. Longest Common Substring

* **Problem Definition:** Longest contiguous substring common to two strings.
* **Core Concept:** 2D DP on prefixes, reset when mismatch.
* **Approach/Strategy:** `dp[i][j]=dp[i-1][j-1]+1 if A[i-1]==B[j-1] else 0`; track max.
* **Related Concepts:** Suffix automaton; suffix array; rolling hash.

### 33. Count Number of Ways to Reach a Given Score in a Game

* **Problem Definition:** Given possible scores (e.g. 2,3,5), count ways to reach total `N`.
* **Core Concept:** Unbounded combinations; order may or may not matter.
* **Approach/Strategy:** DP `dp[0]=1`; for each score `s`, for `i=s…N`: `dp[i]+=dp[i-s]`.
* **Related Concepts:** Coin change count; composition of integers.

### 34. Count Balanced Binary Trees of Height h

* **Problem Definition:** Count number of height-balanced binary trees of height `h`.
* **Core Concept:** Recurrence: `T(h)=T(h-1)·T(h-2)*2 + T(h-1)²`.
* **Approach/Strategy:** DP bottom‑up using the formula with modulo.
* **Related Concepts:** Fibonacci; AVL trees; tree enumeration.

### 35. Largest Sum Contiguous Subarray (Kadane’s)

* **Problem Definition:** Find max sum of any contiguous subarray.
* **Core Concept:** Kadane’s linear scan: track current and global max.
* **Approach/Strategy:** `current = max(a[i], current+a[i])`, `best = max(best, current)`.
* **Related Concepts:** Maximum subarray with indices; divide‑and‑conquer variant.

### 36. Smallest Sum Contiguous Subarray

* **Problem Definition:** Find min sum of any contiguous subarray.
* **Core Concept:** Kadane’s on negated array or track current min.
* **Approach/Strategy:** `current = min(a[i], current+a[i])`, `best = min(best, current)`.
* **Related Concepts:** Maximum negative subarray; prefix sums.

### 37. Unbounded Knapsack

* **Problem Definition:** Like 0/1 knapsack but unlimited copies of each item.
* **Core Concept:** Unbounded combinations; DP on capacity only.
* **Approach/Strategy:** 1D DP `dp[w] = max(dp[w], dp[w-wt[i]]+val[i])` for each item `i` and weight `w`.
* **Related Concepts:** Coin change max value; rod cutting.

### 38. Word Break Problem

* **Problem Definition:** Given string and dictionary, determine if it can be segmented into valid words.
* **Core Concept:** DP on prefixes or backtracking with memo.
* **Approach/Strategy:** `dp[0]=True`; for `i=1…n`: if any `dp[j] and s[j:i] in dict` then `dp[i]=True`.
* **Related Concepts:** Trie optimization; minimum cuts; word break II (print sentences).

### 39. Largest Independent Set Problem (Tree)

* **Problem Definition:** On a tree, select max set of nodes so none are adjacent.
* **Core Concept:** Tree‑DP with include/exclude state.
* **Approach/Strategy:** For each node, compute `incl=node.val+sum(excl(child))` and `excl=sum(max(incl,excl)(child))`.
* **Related Concepts:** Vertex cover; tree matching.

### 40. Partition Problem

* **Problem Definition:** Determine if array can be split into two subsets of equal sum.
* **Core Concept:** Subset sum to `total/2`.
* **Approach/Strategy:** Same as subset‑sum DP for target `sum/2`.
* **Related Concepts:** Balanced partition; multi-way partition.

### 41. Longest Palindromic Subsequence

* **Problem Definition:** Longest subsequence of a string that reads same forwards/backwards.
* **Core Concept:** LCS of string and its reverse.
* **Approach/Strategy:** Compute LCS(S, reverse(S)).
* **Related Concepts:** Longest palindromic substring; DP on palindromes.

### 42. Count All Palindromic Subsequences

* **Problem Definition:** Count distinct palindromic subsequences in a string.
* **Core Concept:** DP with inclusion‑exclusion on characters.
* **Approach/Strategy:** `dp[i][j]` = dp\[i+1]\[j] + dp\[i]\[j-1] − dp\[i+1]\[j-1] plus if `s[i]==s[j]` then `+1+dp[i+1][j-1]`.
* **Related Concepts:** Palindrome counting; modulo arithmetic.

### 43. Longest Palindromic Substring

* **Problem Definition:** Longest contiguous palindrome in a string.
* **Core Concept:** Expand around center or DP.
* **Approach/Strategy:** For each center (char or gap), expand pointers while match.
* **Related Concepts:** Manacher’s algorithm (O(n)); DP table.

### 44. Longest Alternating Subsequence

* **Problem Definition:** Longest subsequence where differences alternate sign.
* **Core Concept:** DP with two states (up/down).
* **Approach/Strategy:** Maintain `up[i]` and `down[i]` lengths: if `a[i]>a[j]` then `up[i]=max(up[i],down[j]+1)`.
* **Related Concepts:** Wiggle subsequence; zigzag sequence.

### 45. Weighted Job Scheduling

* **Problem Definition:** Given jobs with start, end, profit, select non‑overlapping jobs to maximize profit.
* **Core Concept:** DP with binary search on sorted end times.
* **Approach/Strategy:** Sort by finish time, `dp[i]=max(dp[i-1], profit[i]+dp[pred(i)])`.
* **Related Concepts:** Interval scheduling; knapsack.

### 46. Coin Game Winner (Three Choices)

* **Problem Definition:** Two players pick 1–3 coins per turn from a heap; last to pick wins. Determine winner under optimal play for `n` coins.
* **Core Concept:** Game theory; DP win/lose states.
* **Approach/Strategy:** `win[n]=not(all(win[n-1], win[n-2], win[n-3]))`.
* **Related Concepts:** Nim; impartial combinatorial games.

### 47. Count Derangements

* **Problem Definition:** Number of permutations of n where no element remains in original position.
* **Core Concept:** Recurrence `D(n) = (n−1)(D(n−1)+D(n−2))`.
* **Approach/Strategy:** Compute iteratively with base `D(0)=1, D(1)=0`.
* **Related Concepts:** Subfactorial; inclusion–exclusion principle.

### 48. Max Profit by Buying & Selling Stock at Most Twice

* **Problem Definition:** Given prices, perform at most two buy–sell transactions to maximize profit.
* **Core Concept:** State DP or split at midpoint.
* **Approach/Strategy:** First pass L→R compute `profit1[i]`, then R→L `profit2[i]`, max of `profit1[i]+profit2[i]`.
* **Related Concepts:** Single transaction max profit; k‑transaction DP.

### 49. Optimal Strategy for a Game (Pick Ends)

* **Problem Definition:** Two players alternately pick either end of an array; maximize your total.
* **Core Concept:** Minimax with DP.
* **Approach/Strategy:** `dp[i][j] = max(arr[i] + min(dp[i+2][j],dp[i+1][j-1]), arr[j] + min(dp[i+1][j-1],dp[i][j-2]))`.
* **Related Concepts:** Game theory; minimax; dynamic programming.

### 50. Optimal Binary Search Tree

* **Problem Definition:** Given keys with search probabilities, build BST of min expected search cost.
* **Core Concept:** DP on optimal substructure of BST cost.
* **Approach/Strategy:** `e[i][j] = min(e[i][r-1]+e[r+1][j])+sum(p[i..j])` for r in \[i,j].
* **Related Concepts:** Huffman coding; dynamic programming on intervals.

### 51. Palindrome Partitioning Problem

* **Problem Definition:** Min cuts needed to partition string into palindromic substrings.
* **Core Concept:** DP on partitions + palindrome checks.
* **Approach/Strategy:** Precompute `isPal[i][j]`, then `cuts[i] = min(cuts[j-1]+1 for j≤i if isPal[j][i])`.
* **Related Concepts:** Minimum partition; DP with preprocessed tables.

### 52. Word Wrap Problem

* **Problem Definition:** Given words and line width, minimize badness cost of line breaks.
* **Core Concept:** DP on word positions with cost function.
* **Approach/Strategy:** `dp[i] = min((width−sumLen(i,j))^2 + dp[j+1])` for j≥i.
* **Related Concepts:** Text justification; formatting algorithms.

### 53. Mobile Numeric Keypad Problem

* **Problem Definition:** Count possible numbers of length `N` using phone keypad movement rules.
* **Real‑World Analogy:** Counting valid PINs under keypad adjacency moves.
* **Core Concept:** Matrix exponentiation or DP on steps.
* **Approach/Strategy:** DP `dp[n][digit] = Σ dp[n-1][adj]` for all adjacent keys. Can optimize via exponentiation for large N.
* **Related Concepts:** Graph walks; adjacency matrices.

### 54. Boolean Parenthesization Problem

* **Problem Definition:** Given boolean expression of T/F and operators `|, &, ^`, count ways to parenthesize to true.
* **Core Concept:** DP on subexpression with two states (trueCount, falseCount).
* **Approach/Strategy:** Split at each operator: combine left/right counts according to operator truth tables.
* **Related Concepts:** Catalan‑like parenthesization; matrix chain multiplication variant.

### 55. Largest Rectangular Sub‑matrix Whose Sum Is 0

* **Problem Definition:** In a 2D matrix of ints, find largest-area submatrix summing to zero.
* **Core Concept:** Reduce 2D to multiple 1D zero‑sum subarray problems.
* **Approach/Strategy:** For each pair of rows, compress columns to sums, then find max-length zero‑sum subarray via hash map.
* **Related Concepts:** Max subarray; prefix sums; submatrix enumeration.

### 56. Largest Area Sub‑matrix with Equal Number of 1s and 0s

* **Problem Definition:** In a binary matrix, find largest-area submatrix where count(1)=count(0).
* **Core Concept:** Map 0→−1, reduce to zero-sum submatrix problem.
* **Approach/Strategy:** Same as #55 but with transformed values.
* **Related Concepts:** Kadane’s 2D; submatrix with given sum.

### 57. Maximum Sum Rectangle in a 2D Matrix

* **Problem Definition:** Find submatrix with maximum sum in a 2D array.
* **Core Concept:** Kadane’s extension to 2D.
* **Approach/Strategy:** For each row pair, compress to 1D and apply Kadane’s.
* **Related Concepts:** Largest sum contiguous subarray; prefix sums.

### 58. Max Profit by Buying & Selling Stock at Most k Times

* **Problem Definition:** At most `k` transactions allowed, maximize profit from price array.
* **Core Concept:** DP with states for transactions and holding.
* **Approach/Strategy:** Let `dp[i][t][0/1]` = max profit at day `i` with `t` transactions and holding flag; optimize space/time.
* **Related Concepts:** Transaction-state machines; 0/1 knapsack.

### 59. Check if String Is Interleaved of Two Others

* **Problem Definition:** Given `A`, `B`, `C`, check if `C` is interleaving of `A` and `B`.
* **Core Concept:** 2D DP on indices of A & B.
* **Approach/Strategy:** `dp[i][j]` = (`dp[i-1][j] and C[i+j-1]==A[i-1]`) OR (`dp[i][j-1] and C[i+j-1]==B[j-1]`).
* **Related Concepts:** Shuffle of strings; 3D LCS variant.

### 60. Maximum Length of Pair Chain

* **Problem Definition:** Given pairs `(aᵢ,bᵢ)`, chain them so each `bᵢ < aⱼ`, maximize chain length.
* **Core Concept:** Longest path in DAG or LIS on sorted pairs.
* **Approach/Strategy:** Sort by end; greedy or DP LIS on start times: `dp[i]=1+max(dp[j] if pairs[j].second<pairs[i].first)`.
* **Related Concepts:** Interval scheduling; weighted/unweighted LIS.

