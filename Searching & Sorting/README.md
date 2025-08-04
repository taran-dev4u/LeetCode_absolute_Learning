# Searching and sorting
●	Find first and last positions of an element in a sorted array
●	Find a Fixed Point (Value equal to index) in a given array
●	Search in a rotated sorted array
●	square root of an integer
●	Maximum and minimum of an array using minimum number of comparisons
●	Optimum location of point to minimize total distance
●	Find the repeating and the missing
●	find majority element
●	Searching in an array where adjacent differ by at most k
●	find a pair with a given difference
●	find four elements that sum to a given value
●	maximum sum such that no 2 elements are adjacent
●	Count triplet with sum smaller than a given value
●	merge 2 sorted arrays
●	print all subarrays with 0 sum
●	Product array Puzzle
●	Sort array according to count of set bits
●	minimum no of swaps required to sort the array
●	Bishu and Soldiers
●	Rasta and Kheshtak
●	Kth smallest number again
●	Find pivot element in a sorted array
●	K-th Element of Two Sorted Arrays
●	Aggressive cows
●	Book Allocation Problem
●	EKO SPOJ
●	Job Scheduling Algo
●	Missing Number in AP
●	Smallest number with atleast n trailing zeroes in factorial
●	Painters Partition Problem
●	ROTI Prata SPOJ
●	Double Helix SPOJ
●	Subset Sums
●	Find the inversion count
●	Implement Merge-sort in place
●	Partitioning and Sorting Arrays with Many Repeated Entries

---

### 1. Find First and Last Positions of an Element in a Sorted Array

* **Problem Definition**
  Given a sorted array and a target `x`, return the indices of its first and last occurrences (or `[-1, -1]` if absent).
* **Real‑World Analogy**
  Locating when a TV show starts and ends in a time‑sorted guide.
* **Core Concept**
  Two variants of binary search (lower‑bound and upper‑bound).
* **Approach/Strategy**

  1. Binary‑search to find the leftmost index where `arr[mid] ≥ x`.
  2. Binary‑search to find the rightmost index where `arr[mid] ≤ x`.
     Each in O(log n), total O(log n), O(1) extra space.
* **Related Concepts**
  C++ `std::lower_bound`/`upper_bound`, bisect in Python.

---

### 2. Find a Fixed Point (Value Equal to Index)

* **Problem Definition**
  Given a sorted array of distinct integers, find any index `i` such that `arr[i] == i`. Return `−1` if none.
* **Real‑World Analogy**
  Finding a book whose shelf number matches its label.
* **Core Concept**
  Binary search on the function `f(i)=arr[i]−i` (strictly increasing).
* **Approach/Strategy**
  If `arr[mid] < mid`, search right; if `arr[mid] > mid`, search left. O(log n), O(1) space.
* **Related Concepts**
  Monotonic functions, order‑statistic binary search.

---

### 3. Search in a Rotated Sorted Array

* **Problem Definition**
  A sorted array has been rotated at some pivot. Search for a target value in O(log n).
* **Real‑World Analogy**
  Finding a time on a clock that’s been “reset” at an unknown hour.
* **Core Concept**
  Modified binary search by identifying which half is sorted.
* **Approach/Strategy**
  At each `mid`, check if left half `[low…mid]` is sorted (compare `arr[low] ≤ arr[mid]`) else right half sorted; then decide which half could contain the target. O(log n), O(1) space.
* **Related Concepts**
  Finding the rotation pivot, circular arrays.

---

### 4. Integer Square Root

* **Problem Definition**
  Compute ⌊√n⌋ for nonnegative integer `n`, without using floating‑point.
* **Real‑World Analogy**
  Determining how many whole square tiles fit in a room of area `n`.
* **Core Concept**
  Binary search on the answer in range `[0…n]`.
* **Approach/Strategy**
  Maintain `low=0, high=n`; while `low ≤ high`, pick `mid=(low+high)//2`, compare `mid*mid` to `n`, adjust bounds. O(log n), O(1).
* **Related Concepts**
  Newton’s (Heron’s) method for integer square roots.

---

### 5. Maximum & Minimum with Minimum Comparisons

* **Problem Definition**
  Find both min and max of an array in fewer than 2(n−1) comparisons.
* **Real‑World Analogy**
  Determining the lightest and heaviest package in one pass.
* **Core Concept**
  Pairwise “tournament” comparisons.
* **Approach/Strategy**
  Process elements in pairs: compare the two in each pair (1 cmp), then compare the smaller to current min and larger to current max (2 cmps), for \~3⌊n/2⌋ total comparisons. O(n), O(1).
* **Related Concepts**
  Divide‑and‑conquer min/max; selection algorithm.

---

### 6. Optimum Location to Minimize Total Distance

* **Problem Definition**
  Given points on a line, find the point minimizing the sum of absolute distances to all points.
* **Real‑World Analogy**
  Placing a warehouse to minimize delivery distances.
* **Core Concept**
  The 1‑dimensional geometric median = median of the points.
* **Approach/Strategy**
  Sort the points (O(n log n)) and choose the median (or any point between the two middle points if even count). O(1) extra space.
* **Related Concepts**
  Fermat‑Weber problem in higher dimensions (requires iterative methods).

---

### 7. Find the Repeating and the Missing

* **Problem Definition**
  Array of size `n` contains numbers `1…n`, one is missing and one is duplicated. Identify both.
* **Real‑World Analogy**
  Attendance sheet with one person signed twice and one not at all.
* **Core Concept**
  Use arithmetic sums and sums of squares (or XOR).
* **Approach/Strategy**
  Let `S1 = sum(arr) − n(n+1)/2 = dup−miss`;
  `S2 = sum(arr²) − n(n+1)(2n+1)/6 = dup²−miss²`.
  Solve the two equations to recover `dup` and `miss`. O(n), O(1).
* **Related Concepts**
  XOR‑based missing‑number algorithms.

---

### 8. Find Majority Element

* **Problem Definition**
  Element that appears more than ⌊n/2⌋ times in an array (guaranteed to exist or not).
* **Real‑World Analogy**
  Winning candidate in an election with over half the votes.
* **Core Concept**
  Boyer‑Moore Voting algorithm.
* **Approach/Strategy**
  First pass to find a candidate by canceling pairs, second pass to verify count. O(n), O(1).
* **Related Concepts**
  Misra‑Gries “kth frequent” generalization.

---

### 9. Search in an Array Where Adjacent Differ by at Most k

* **Problem Definition**
  Given array `A` where |A\[i]−A\[i+1]| ≤ k, search for key `x` faster than O(n).
* **Real‑World Analogy**
  Temperature readings that change gradually hour‑to‑hour.
* **Core Concept**
  Jump search using the known bound.
* **Approach/Strategy**
  At index `i`, if `A[i] != x`, skip ahead by `steps = max(1, |A[i]−x|/k)`. Total jumps ≈ O(n/k).
* **Related Concepts**
  Interpolation search; skip lists.

---

### 10. Find a Pair with a Given Difference

* **Problem Definition**
  In array, find any two elements whose difference is a given `d`.
* **Real‑World Analogy**
  Two clocks showing times exactly one hour apart.
* **Core Concept**
  Two‑pointer on sorted array, or hash table lookup.
* **Approach/Strategy**
  Sort (O(n log n)) then use two pointers `i,j`: if `A[j]−A[i] < d` increment `j`, if `>d` increment `i`, else found. Or hash: for each `a`, check if `a+d` (or `a−d`) in set.
* **Related Concepts**
  Two‑sum family; counting pairs.

---

### 11. Find Four Elements That Sum to a Given Value

* **Problem Definition**
  Given array and target `T`, find four distinct elements whose sum equals `T`.
* **Real‑World Analogy**
  Bundling four grocery items to exactly match a discount threshold.
* **Core Concept**
  Extension of 3‑sum; pair‑sum hashing.
* **Approach/Strategy**

  1. Sort the array.
  2. Two nested loops fix first two elements, then two‑pointer to find remaining two that sum to `T − (a[i]+a[j])`. O(n³).
     Or store all pair sums in a hash map (O(n²) time & space), then look for complementary pair sums.
* **Related Concepts**
  k‑sum problem; meet‑in‑the‑middle.

---

### 12. Maximum Sum with No Two Adjacent

* **Problem Definition**
  Select a subset of array elements (not adjacent) to maximize their sum.
* **Real‑World Analogy**
  Scheduling non‑overlapping jobs for maximum profit.
* **Core Concept**
  Linear DP with two states: include/exclude.
* **Approach/Strategy**
  Let `incl = max sum including prev element`, `excl = max sum excluding prev`.
  For each `x`:

  ```
  new_excl = max(incl, excl)
  incl = excl + x
  excl = new_excl
  ```

  Final answer = `max(incl, excl)`. O(n), O(1).
* **Related Concepts**
  House‑robber problem; weighted interval scheduling on a path.

---

### 13. Count Triplets with Sum Smaller than a Given Value

* **Problem Definition**
  Count all triplets `(i,j,k)` such that `arr[i]+arr[j]+arr[k] < S`.
* **Real‑World Analogy**
  Selecting three investments whose total risk score remains under threshold.
* **Core Concept**
  Two‑pointer inside a loop.
* **Approach/Strategy**
  Sort the array. For each `i` from `0` to `n−3`, set `l = i+1`, `r = n−1`.
  While `l<r`, if `arr[i]+arr[l]+arr[r] < S`, then all elements between `l` and `r` with `l` form valid triplets: `count += (r−l)`, and `l++`; else `r--`. O(n²).
* **Related Concepts**
  3‑sum problem; combinatorial counting.

---

### 14. Merge Two Sorted Arrays

* **Problem Definition**
  Merge two sorted arrays into one sorted array (possibly in-place if extra capacity is available).
* **Real‑World Analogy**
  Merging two sorted contact lists.
* **Core Concept**
  Two‑pointer merge.
* **Approach/Strategy**
  Maintain pointers `i,j` on each array and copy the smaller element to result. If in‑place (one array has extra slots), merge from the end backwards. O(n+m), O(1) extra for in‑place or O(n+m) extra for new array.
* **Related Concepts**
  Merge sort’s merge step.

---

### 15. Print All Subarrays with 0 Sum

* **Problem Definition**
  Print (or count) every contiguous subarray whose elements sum to zero.
* **Real‑World Analogy**
  Time intervals where net cash flow is zero.
* **Core Concept**
  Prefix sums + hash‑map of occurrences.
* **Approach/Strategy**
  As you iterate, maintain `prefix_sum`. Use a hash map from sum→list of indices where it occurred. Whenever the same `sum` reappears at index `j` that first appeared at indices `i₁,…,iₖ`, each subarray `(iₜ+1…j)` sums to zero. O(n+M) where M is number of zero‑sum subarrays.
* **Related Concepts**
  Subarray sum equals k; counting subarrays with given sum.

---

### 16. Product Array Puzzle

* **Problem Definition**
  Given array `A`, build output `B` such that `B[i] = ∏_{j≠i} A[j]`, without using division.
* **Real‑World Analogy**
  Impact on total product when removing one factor.
* **Core Concept**
  Prefix and suffix products.
* **Approach/Strategy**

  1. Compute `L[i] = ∏_{j< i} A[j]` in one pass.
  2. Compute `R[i] = ∏_{j > i} A[j]` in reverse pass.
  3. `B[i] = L[i] * R[i]`.
     O(n) time, O(n) space. Can optimize to O(1) extra if allowed to overwrite.
* **Related Concepts**
  Prefix sums/products; exclusion logic; division alternative.

---

### 17. Sort Array According to Count of Set Bits

* **Problem Definition**
  Sort integers by ascending number of 1‑bits in binary form; break ties by numeric value.
* **Real‑World Analogy**
  Prioritizing tasks by the number of resource flags set.
* **Core Concept**
  Custom comparator based on bit‑count.
* **Approach/Strategy**

  1. Precompute `popcount(x)` for each element (built‑in e.g. `__builtin_popcount`).
  2. Sort with key `(popcount(x), x)`. O(n log n) time and O(n) extra for keys.
* **Related Concepts**
  Radix sort by bit‑counts; bucket sort if range small.

---

### 18. Minimum Number of Swaps Required to Sort the Array

* **Problem Definition**
  Given an array of distinct elements, compute min swaps to sort it.
* **Real‑World Analogy**
  Swapping books in minimal moves to arrange in order.
* **Core Concept**
  Cycle decomposition of the permutation.
* **Approach/Strategy**

  1. Create array of `(value, original_index)` and sort it.
  2. Maintain visited array; for each unvisited index, follow the cycle, count cycle length `L`, require `L−1` swaps.
     Total swaps = Σ(Lᵢ−1). O(n log n) time, O(n) space.
* **Related Concepts**
  Permutation cycles; graph cycle decomposition.

---

### 19. Bishu and Soldiers

* **Problem Definition**
  Given soldier strengths array and queries `q`, for each query count how many soldiers have strength ≤ `q`.
* **Real‑World Analogy**
  Ranking participants within skill threshold.
* **Core Concept**
  Sorting + binary search.
* **Approach/Strategy**
  Sort strengths (O(n log n)), then for each query use upper\_bound to get count in O(log n).
* **Related Concepts**
  Order‑statistics; prefix sums for strength totals.

---

### 20. Rasta and Kheshtak

> (Hackerearth “Rasta and Kheshtak” is a 0‑1 weighted shortest‑path problem on a grid.)

* **Problem Definition**
  In a grid, “Rasta” edges cost 0, “Kheshtak” edges cost 1. From source to destination, find minimum total cost path.
* **Real‑World Analogy**
  Traveling on toll roads (cost) vs free roads.
* **Core Concept**
  0‑1 BFS (deque‑based Dijkstra for weights 0/1).
* **Approach/Strategy**
  Use a double‑ended queue: when traversing a 0‑cost edge, push front; when 1‑cost, push back. Track distances; O(V+E).
* **Related Concepts**
  Dijkstra’s algorithm; BFS on weighted graphs.

---

### 21. Kth Smallest Number Again

* **Problem Definition**
  Find the kᵗʰ smallest element in an unsorted array (multiple queries or streaming).
* **Real‑World Analogy**
  Selecting the kᵗʰ fastest runner’s time.
* **Core Concept**
  Quickselect (average O(n)) or heap.
* **Approach/Strategy**

  * **Quickselect:** Partition around pivot as in quicksort, recurse into the side containing the kᵗʰ element.
  * **Heap:** Maintain a max‑heap of size k (O(n log k)).
* **Related Concepts**
  Order‑statistics trees; median of medians for worst‑case O(n).

---

### 22. Find Pivot Element in a Sorted Rotated Array

* **Problem Definition**
  In a sorted array rotated at unknown pivot, find index of the smallest element (the pivot).
* **Real‑World Analogy**
  Locating midnight on a 24‑hour clock displayed starting at a random hour.
* **Core Concept**
  Binary search for the inflection point (`arr[mid] > arr[mid+1]`).
* **Approach/Strategy**
  Compare `arr[mid]` to `arr[high]`: if `arr[mid] ≤ arr[high]`, pivot is in left half; else in right half. O(log n).
* **Related Concepts**
  Search in rotated array; minimum in rotated array.

---

### 23. K‑th Element of Two Sorted Arrays

* **Problem Definition**
  Given two sorted arrays, find their combined kᵗʰ smallest element in O(log k) time.
* **Real‑World Analogy**
  Merging two sorted scoreboards and picking the kᵗʰ rank.
* **Core Concept**
  Divide & conquer on k.
* **Approach/Strategy**
  Compare the k/2ᵗʰ element of each array (or end of array), discard that many from one side, adjust k, recurse. O(log k) time, O(1) space.
* **Related Concepts**
  Median of two sorted arrays.

---

### 24. Aggressive Cows

* **Problem Definition**
  Given stall positions and `C` cows, place each cow in a stall to maximize the minimum pairwise distance.
* **Real‑World Analogy**
  Placing cell towers to maximize coverage separation.
* **Core Concept**
  Binary search on the answer (distance) + greedy feasibility check.
* **Approach/Strategy**

  1. Sort stall positions.
  2. Binary search `d` in `[0, max_distance]`.
  3. Greedily place cows: first in stall\[0], then each next in the first stall ≥ last\_position + d.
  4. If you can place ≥ C cows, `d` is feasible.
     O(n log n + log D × n).
* **Related Concepts**
  Max‑min optimization; book allocation.

---

### 25. Book Allocation Problem

* **Problem Definition**
  Partition `n` books (pages) among `k` students (contiguously) so that the maximum pages assigned to any student is minimized.
* **Real‑World Analogy**
  Distributing chapters among editors to balance workload.
* **Core Concept**
  Binary search on the maximum pages + greedy check.
* **Approach/Strategy**
  Low = max single book pages; High = sum of pages.
  While `low ≤ high`, set `mid = (low+high)//2`, greedily assign books to students without exceeding `mid`; if students required ≤ k, reduce `high`, else increase `low`. O(n log sum).
* **Related Concepts**
  Painters partition problem; load balancing.

---

### 26. EKO SPOJ (Woodcutters)

* **Problem Definition**
  Given tree heights and required wood amount `M`, choose saw height `H` so that sum of `(height_i − H)` for trees taller than `H` ≥ `M`.
* **Real‑World Analogy**
  Setting saw height to fulfill a wood order.
* **Core Concept**
  Monotonic “wood collected” vs `H`, searchable via binary search.
* **Approach/Strategy**
  Low = 0; High = max height.
  While `low ≤ high`, `mid=(low+high)//2`, compute wood = Σ max(0, h\_i−mid); if wood ≥ M search higher `H`, else lower. O(n log H).
* **Related Concepts**
  Aggressive cows; partition by threshold.

---

### 27. Job Scheduling Algorithm (with Deadlines & Profits)

* **Problem Definition**
  Given jobs each with deadline and profit, schedule jobs (one per unit time) to maximize total profit before deadlines.
* **Real‑World Analogy**
  Assigning tasks to a single processor with deadlines and profits.
* **Core Concept**
  Greedy by profit + disjoint‑set or priority queue.
* **Approach/Strategy**

  1. Sort jobs by profit descending.
  2. For each job, attempt to schedule it at the latest possible free slot ≤ deadline (using a DSU union‑find to track free slots).
  3. If slot found, assign; else skip.
     O(n log n + n α(n)).
* **Related Concepts**
  Interval scheduling; maximum weighted matching in unit‑time slots.

---

### 28. Missing Number in AP

* **Problem Definition**
  An arithmetic progression of `n` terms has one term missing. Given the remaining `n−1` terms (sorted), find the missing term.
* **Real‑World Analogy**
  Identifying the missing page number in a numbered booklet.
* **Core Concept**
  Common difference `(last−first)/(n−1)`, binary search for mismatch.
* **Approach/Strategy**

  1. Compute `d = (arr[n−2]−arr[0])/(n−1)`.
  2. Binary search: at `mid`, expected value = `arr[0] + mid⋅d`; if `arr[mid] == expected`, missing in right half, else left.
     O(log n), O(1).
* **Related Concepts**
  Sum of AP check; simple iteration (O(n)).

---

### 29. Smallest Number with ≥ n Trailing Zeroes in Factorial

* **Problem Definition**
  Given `n`, find the smallest `x` such that `x!` has at least `n` trailing zeros.
* **Real‑World Analogy**
  Determining how large a factorial you need to guarantee `n` zeros at the end.
* **Core Concept**
  Trailing zeros = Σ⌊x/5ᵏ⌋, a nondecreasing function of `x`.
* **Approach/Strategy**
  Binary search on `x` in `[0, 5n]`; for each mid compute zeros; adjust low/high. O(log(5n)⋅log x) ≈ O(log² n).
* **Related Concepts**
  Legendre’s formula; monotonic binary search.

---

### 30. Painters Partition Problem

* **Problem Definition**
  Given `n` boards lengths and `k` painters (each paints contiguous boards at unit speed), minimize time to paint all boards.
* **Real‑World Analogy**
  Assigning painting sections to teams to finish as quickly as possible.
* **Core Concept**
  Same as book allocation (binary search on maximum workload).
* **Approach/Strategy**
  Low = max(board lengths), High = sum(lengths).
  Binary search mid; greedily assign boards to painters without exceeding mid; check ≤ k painters needed. O(n log sum).
* **Related Concepts**
  Book allocation; load balancing.

---

### 31. ROTI Prata SPOJ

* **Problem Definition**
  Given cooks of ranks `R[i]`, each cook takes `R[i]` minutes for first prata, `2R[i]` for second, … find minimum time `T` so that total prata cooked ≥ `P`.
* **Real‑World Analogy**
  Multiple machines with different speeds producing units over time.
* **Core Concept**
  Cumulative production function vs time is monotonic; binary search on time.
* **Approach/Strategy**
  Low = 0, High = `max(R)*P*(P+1)/2`.
  For mid, compute total = Σ max `k` such that `R[i]*(k(k+1)/2) ≤ mid` (`k` = (√(1+8 mid/R\[i])−1)/2).
  Adjust bounds. O(n log T).
* **Related Concepts**
  Aggressive cows; binary search on answer.

---

### 32. Double Helix SPOJ

* **Problem Definition**
  Two strictly increasing sequences; you can switch from one to the other only at common elements. Maximize sum of visited elements until both sequences end.
* **Real‑World Analogy**
  Hiking two parallel trails with bridges at common points; want max scenic value.
* **Core Concept**
  Two‑pointer merge with segment sums.
* **Approach/Strategy**
  Maintain pointers `i,j`, running sums `sum1,sum2`.
  While both arrays:

  * If `A[i]<B[j]`, `sum1+=A[i++]`.
  * If `A[i]>B[j]`, `sum2+=B[j++]`.
  * If equal, add `max(sum1,sum2)+A[i]` to result, reset `sum1=sum2=0`, `i++,j++`.
    After loop add remaining sums to result. O(n+m), O(1).
* **Related Concepts**
  Merge step; maximum path in DAG.

---

### 33. Subset Sums

* **Problem Definition**
  Compute all possible sums from subsets of a given set (or count them).
* **Real‑World Analogy**
  All possible purchase totals from items on sale.
* **Core Concept**
  Bitmask enumeration or DP by inclusion/exclusion.
* **Approach/Strategy**

  * **Enumeration:** For mask `0…(1<<n)-1`, sum bits. O(n·2ⁿ).
  * **DP:** Boolean `dp[s] = True` if sum `s` is achievable, update for each element. O(n·sum).
* **Related Concepts**
  Power set; knapsack decision problem.

---

### 34. Find the Inversion Count

* **Problem Definition**
  Count pairs `(i,j)` with `i<j` and `A[i]>A[j]`.
* **Real‑World Analogy**
  Measuring how “unsorted” a list is (# swaps to sort).
* **Core Concept**
  Modified merge sort counting cross‑inversions.
* **Approach/Strategy**
  During merge, when an element from right half is placed before left half, add `(mid–i+1)` to count. O(n log n), O(n) extra.
* **Related Concepts**
  Fenwick tree (BIT) or segment tree counting; Kendall τ distance.

---

### 35. Implement Merge‑Sort In‑Place

* **Problem Definition**
  Implement merge sort without O(n) temporary array – i.e. O(1) extra space.
* **Real‑World Analogy**
  Sorting logs in a pile by only swapping adjacent logs.
* **Core Concept**
  In‑place merging via block rotations or the “gap” method.
* **Approach/Strategy**
  Use an in‑place merge algorithm (e.g. the Galli–Shonik method) that swaps elements using constant extra storage, or iterative shell‑sort‑style gap merging. Time remains O(n log n), space O(1).
* **Related Concepts**
  In‑place quicksort; stable vs unstable sorts.

---

### 36. Partitioning & Sorting Arrays with Many Repeated Entries

* **Problem Definition**
  Sort an array efficiently when there are many duplicates.
* **Real‑World Analogy**
  Organizing ballots by candidate when many voters chose the same candidate.
* **Core Concept**
  Three‑way partition (Dutch national flag) + quicksort, or counting sort if range small.
* **Approach/Strategy**

  * **Dutch flag:** Partition into `< pivot`, `= pivot`, `> pivot`, recurse on outer partitions. Achieves O(n) average for many duplicates.
  * **Counting sort:** If values in small range \[0…k], count frequencies and reconstruct. O(n+k).
* **Related Concepts**
  Radix sort; multikey quicksort.


