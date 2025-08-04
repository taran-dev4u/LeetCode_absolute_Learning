# Greedy
●	Activity Selection Problem
●	Job Sequencing Problem
●	Huffman Coding
●	Water Connection Problem
●	Fractional Knapsack Problem
●	Greedy Algorithm to find Minimum number of Coins
●	Maximum trains for which stoppane can be provided
●	Minimum Platforms Problem
●	Buy Maximum Stocks if i stocks can be bought on i-th day
●	Find the minimum and maximum amount to buy all N candies
●	Minimize Cash Flow among a given set of friends who have borrowed money from each other
●	Minimum Cost to cut a board into squares
●	Check if it is possible to survive on Island
●	Find maximum meetings in one room
●	Maximum product subset of an array
●	Maximize array sum after K negations
●	Maximize the sum of arr[i]*i
●	Maximum sum of absolute difference of an array
●	Maximize sum of consecutive differences in a circular array
●	Minimum sum of absolute difference of pairs of two arrays
●	Program for Shortest Job First (or SJF) CPU Scheduling
●	Program for Least Recently Used (LRU) Page Replacement algorithm
●	Smallest subset with sum greater than all other elements
●	Chocolate Distribution Problem
●	DEFKIN - Defense of a Kingdom
●	DIEHARD - DIE HARD
●	GERGOVIA - Wine trading in Gergovia
●	Picking Up Chicks
●	CHOCOLA - Chocolate
●	ARRANGE - Arranging Amplifiers
●	K Centers Problem
●	Minimum Cost of ropes
●	Find smallest number with given number of digits and sum of digits
●	Rearrange characters in a string such that no two adjacent are same
●	Find maximum sum possible equal sum of three stacks

---

### 1. Activity Selection Problem

* **Problem Definition:** Given `n` activities each with a start and finish time, select the maximum‑size subset of mutually non‑overlapping activities.
* **Real‑World Analogy:** Scheduling the maximum number of non‑conflicting meetings in one conference room.
* **Core Concept:** Greedy choice by earliest finish time.
* **Approach/Strategy:**

  1. Sort activities by finish time ascending.
  2. Always pick the first activity, then for each next, if its start ≥ last selected finish, select it.
  3. This yields optimal maximal count.
* **Related Concepts:** Interval scheduling; matroid theory; DP yields same result but slower.

---

### 2. Job Sequencing with Deadlines

* **Problem Definition:** Given `n` jobs each with a deadline and profit, schedule at most one job per unit time to maximize total profit.
* **Analogy:** Assigning paid tasks to a single processor under deadline constraints.
* **Core Concept:** Greedy by profit + slot allocation.
* **Approach/Strategy:**

  1. Sort jobs in descending profit.
  2. For each job, try to schedule it in the latest free slot before its deadline (use an array or disjoint‑set to track free slots).
  3. Sum profits of scheduled jobs.
* **Related Concepts:** Disjoint‑set; earliest‑deadline‑first.

---

### 3. Huffman Coding

* **Problem Definition:** Given characters and frequencies, build a prefix‑free binary code that minimizes total encoded length.
* **Analogy:** Creating optimal Morse‑like codes for letters to minimize transmission time.
* **Core Concept:** Greedy merge of least‑frequent trees.
* **Approach/Strategy:**

  1. Insert all characters as leaf nodes into a min‑heap keyed by frequency.
  2. Repeatedly extract two smallest nodes, merge into new node with summed frequency, re‑insert.
  3. The resulting tree gives optimal codes by path.
* **Related Concepts:** Optimal merge patterns; prefix codes; Shannon–Fano (suboptimal).

---

### 4. Water Connection Problem

* **Problem Definition:** Given a tree of houses and pipes (some with taps), find for every component its source tap and the minimal pipe diameter along the path.
* **Analogy:** Ensuring water flows from source tanks through the narrowest constriction.
* **Core Concept:** Greedy traversal from each unvisited node to its sink, tracking min edge.
* **Approach/Strategy:**

  1. Build adjacency.
  2. For each house with no incoming pipe (a source), DFS/BFS down until a house with no outgoing (a sink), tracking minimum capacity.
  3. Record triplets `(source, sink, min_capacity)`.
* **Related Concepts:** Tree DP; max‑flow bottleneck.

---

### 5. Fractional Knapsack Problem

* **Problem Definition:** Given items with weights and values and knapsack capacity `W`, maximize value; you may take fractions of items.
* **Analogy:** Filling a cargo plane with divisible goods by highest value density first.
* **Core Concept:** Greedy by value/weight ratio.
* **Approach/Strategy:**

  1. Compute ratio `v[i]/w[i]`.
  2. Sort items descending ratio.
  3. Take as much as possible of highest‑ratio items until capacity exhausted (possibly fractional last).
* **Related Concepts:** Continuous relaxation of 0/1 knapsack; priority queues.

---

### 6. Greedy Algo to Find Minimum Number of Coins

* **Problem Definition:** Given coin denominations (e.g. U.S. coins) and a target amount, find min coins needed (assuming canonical system).
* **Analogy:** Cashier giving change with largest coins first.
* **Core Concept:** Greedy by largest denomination.
* **Approach/Strategy:**

  1. Sort denominations descending.
  2. For each coin, take as many as fit into remaining amount.
  3. Works optimally if coin system is canonical (e.g. standard currency); fails for arbitrary sets.
* **Related Concepts:** Coin‑change DP for arbitrary denominations; canonical coin systems.

---

### 7. Maximum Trains for Which Stoppage Can Be Provided

* **Problem Definition:** Given arrival and departure times of trains at a station, find max trains that can be handled without conflict.
* **Analogy:** Platform assignment; here only one platform, so non‑overlapping intervals.
* **Core Concept:** Activity selection on train schedules.
* **Approach/Strategy:**

  1. Treat each train as interval `[arrival, departure]`.
  2. Sort by departure time, then select non‑overlapping as in activity selection.
* **Related Concepts:** Interval scheduling; multiple platforms leads to min‑platform problem.

---

### 8. Minimum Platforms Problem

* **Problem Definition:** Given arrival & departure times of trains, find the minimum number of platforms needed so no train waits.
* **Analogy:** Scheduling runways for airplanes.
* **Core Concept:** Sweep‑line / min‑heap of end times.
* **Approach/Strategy:**

  1. Sort arrivals and departures.
  2. Use two‑pointer: increment platform count on arrival, decrement on departure.
  3. Or maintain a min‑heap of departure times; push on arrival, pop all departures ≤ arrival, track heap size max.
* **Related Concepts:** Interval coloring; resource allocation.

---

### 9. Buy Maximum Stocks if i Stocks Can Be Bought on iᵗʰ Day

* **Problem Definition:** Given price on day `i` and a max transaction limit `i`, maximize shares bought with given money.
* **Analogy:** Investment opportunity with day‑by‑day purchase caps.
* **Core Concept:** Greedy buy cheapest available days first, subject to day limit.
* **Approach/Strategy:**

  1. Build list of `(price, day_limit)`.
  2. Sort ascending by price.
  3. For each entry, buy up to `min(day_limit, remaining_money/price)` shares, subtract cost until money exhausted.
* **Related Concepts:** Fractional knapsack variant; priority scheduling.

---

### 10. Min & Max Amount to Buy All N Candies

* **Problem Definition:** Given `N` prices, on each buy you pick one candy and pay sum of remaining, find min and max total cost over optimal orderings.
* **Analogy:** Buying items when each subsequent purchase discounts or penalizes based on remaining items.
* **Core Concept:** Greedy: to minimize pay largest prices early (sort descending), to maximize pay smallest first (sort ascending).
* **Approach/Strategy:**

  * **Min cost:** Sort prices descending, repeatedly pay `sum_remaining` → largest removed first.
  * **Max cost:** Sort ascending.
* **Related Concepts:** Huffman cost interpretation; prefix sums.

---

### 11. Minimize Cash Flow Among Friends (revisited)

* **Same as earlier** (#42 in Graph section) – settle debts by always matching max creditor with max debtor greedily.
* **Related Concepts:** Flow simplification; netting transactions.

---

### 12. Minimum Cost to Cut a Board into Squares

* **Problem Definition:** Given a board and lists of vertical & horizontal cut costs, determine min total cost to cut into unit squares (cost of each cut multiplies remaining segments).
* **Analogy:** Cutting a chocolate bar with varying edge costs.
* **Core Concept:** Greedy — cut highest‑cost lines first to minimize multiplier effect.
* **Approach/Strategy:**

  1. Sort horizontal and vertical costs descending.
  2. Maintain counts of segments in both directions.
  3. At each step, pick larger next cost: if horizontal, cost × current vertical segments; vice versa.
* **Related Concepts:** Kruskal’s MST dual; matrix partitioning.

---

### 13. Check if It Is Possible to Survive on Island

* **Problem Definition:** Given resource gains at grid cells, can you traverse from start to extraction point without health dropping below zero?
* **Analogy:** Video‑game character collecting health packs while moving.
* **Core Concept:** Greedy to maximize minimal health → binary search on initial health + BFS feasibility.
* **Approach/Strategy:**

  1. Binary search initial health `H`.
  2. For each `H`, BFS/DFS track health at each cell (`new_health = curr + gain[cell]`); ensure always >0.
  3. Check reachability of extraction.
* **Related Concepts:** Min‑max path; feasibility under budget.

---

### 14. Find Maximum Meetings in One Room

* **Problem Definition:** Given start/end times of meetings, schedule max non‑overlapping in a single room.
* **Analogous to #1 and #7** – interval scheduling by earliest finish time.
* **Related Concepts:** Activity selection, train stoppage.

---

### 15. Maximum Product Subset of an Array

* **Problem Definition:** Choose a subset of elements whose product is maximized (can exclude negatives/zeros).
* **Analogy:** Picking portfolio assets to maximize compound growth.
* **Core Concept:** Greedy handling of negatives and zeros.
* **Approach/Strategy:**

  1. Count negatives, zeros, track smallest absolute neg.
  2. If count of negatives is odd, exclude the one with smallest absolute value.
  3. Exclude zeros unless the entire product would be zero.
* **Related Concepts:** Sign tracking; special‑case handling.

---

### 16. Maximize Array Sum After K Negations

* **Problem Definition:** Given `K` operations of flipping sign of any element, maximize array sum.
* **Analogy:** Applying limited coupons that invert item costs.
* **Core Concept:** Greedy flip negatives first, then smallest absolute value.
* **Approach/Strategy:**

  1. Build min‑heap of absolute values.
  2. While `K>0`, extract smallest absolute val, flip its sign, push back, decrement `K`.
  3. Sum heap elements.
* **Related Concepts:** Priority queues; local-optimum greedy.

---

### 17. Maximize ∑ arr\[i] × i

* **Problem Definition:** Permute array to maximize weighted sum with weights = index.
* **Analogy:** Assign more valuable items to positions with higher multipliers.
* **Core Concept:** Greedy sort ascending so largest values at largest indices.
* **Approach/Strategy:** Sort array ascending, compute sum of `a[i]*i`.
* **Related Concepts:** Rearrangement inequality; majorization.

---

### 18. Maximum Sum of Absolute Differences

* **Problem Definition:** Arrange elements to maximize ∑|arr\[i]−arr\[i+1]|.
* **Analogy:** Seating guests so argumentative pairs sit together (max conflict).
* **Core Concept:** Greedy placing extremes alternately.
* **Approach/Strategy:**

  1. Sort array.
  2. Build new sequence by taking smallest, largest, second smallest, second largest, …
  3. Compute sum of adjacent differences.
* **Related Concepts:** Two‑pointer arrangement; rearrangement inequality.

---

### 19. Maximize Sum of Consecutive Differences (Circular)

* **Problem Definition:** Like #18 but treat array as circular (include |last−first|).
* **Approach/Strategy:** Same alternating extremes arrangement on circle.
* **Related Concepts:** Necklace arrangement; circular permutations.

---

### 20. Minimum Sum of Absolute Differences of Pairs of Two Arrays

* **Problem Definition:** Given two arrays of size `n`, pair elements one‑to‑one to minimize ∑|aᵢ−bᵢ|.
* **Analogy:** Matching workers to jobs by skill level gap.
* **Core Concept:** Greedy sort‑and‑pair.
* **Approach/Strategy:** Sort both arrays ascending, then pair in order, sum absolute differences.
* **Related Concepts:** Minimum bipartite matching on line; Earth‑mover’s distance in 1D.

---

### 21. Shortest Job First (SJF) CPU Scheduling

* **Problem Definition:** Schedule jobs on a single CPU, always pick the waiting job with smallest duration to minimize average wait time.
* **Analogy:** Serving customers with the fewest items first to shorten queue.
* **Core Concept:** Greedy selection by processing time.
* **Approach/Strategy:** Use a min‑heap of job durations; when CPU free, pop shortest job. For non‑preemptive, same; for preemptive (SRTF), if new arrival shorter, preempt.
* **Related Concepts:** Priority queues; fair scheduling.

---

### 22. Least Recently Used (LRU) Page Replacement

* **Problem Definition:** In a cache of capacity `C`, on page requests, evict the least recently used page when full.
* **Analogy:** Library returns least‑read book to make space.
* **Core Concept:** Greedy eviction of LRU.
* **Approach/Strategy:** Maintain ordered dictionary or doubly‑linked list + hash map: on access move page to front; on miss if full, remove tail.
* **Related Concepts:** Cache eviction policies; MRU, LFU.

---

### 23. Smallest Subset with Sum Greater Than All Other Elements

* **Problem Definition:** From array, find smallest subset (fewest elements) whose sum > sum of remaining elements.
* **Analogy:** Choose minimal team of stars whose combined performance surpasses everyone else.
* **Core Concept:** Greedy pick largest elements first.
* **Approach/Strategy:**

  1. Sort descending.
  2. Accumulate from largest until `sum_selected > total_sum − sum_selected`.
* **Related Concepts:** Minimal covering; majority sum.

---

### 24. Chocolate Distribution Problem

* **Problem Definition:** Given packets of chocolates with various counts, distribute to `m` students such that difference between max and min in chosen `m` packets is minimized.
* **Analogy:** Fairly handing out gift boxes of different values.
* **Core Concept:** Greedy on sorted list.
* **Approach/Strategy:**

  1. Sort packet sizes ascending.
  2. For each window of size `m`, track `arr[i+m−1] − arr[i]`, take minimum.
* **Related Concepts:** Sliding window; min‑range covering.

---

### 25. DEFKIN – Defense of a Kingdom (SPOJ)

* **Problem Definition:** Given `n×m` grid and positions of `k` towers, find largest undefended rectangle area (max gap between towers minus one).
* **Analogy:** Finding largest blind spot in a fortress’s defenses.
* **Core Concept:** Greedy on sorted coordinates.
* **Approach/Strategy:**

  1. Collect tower X‐coords, add 0 and n+1 borders, sort. Find max diff −1.
  2. Same for Y‐coords.
  3. Area = max\_dx × max\_dy.
* **Related Concepts:** Largest empty rectangle in histogram.

---

### 26. DIEHARD (SPOJ)

* **Problem Definition:** Given 5 types of water containers and total demand, maximize demand met using greedy filling.
* **Core Concept:** Greedy use biggest containers first.
* **Approach/Strategy:** Sort container capacities descending, for each, use as many as possible, decrement remaining need.
* **Related Concepts:** Coin change greedy.

---

### 27. GERGOVIA – Wine Trading in Gergovia (SPOJ)

* **Problem Definition:** Given net wine demands/supplies at houses in a line, minimize total work of carrying wine to meet demands.
* **Analogy:** Delivering supplies along a street.
* **Core Concept:** Greedy cumulative flow.
* **Approach/Strategy:**
  Maintain running `net` = sum of supplies/demands so far; total work += |net| at each step.
* **Related Concepts:** Minimum transportation cost on line; earth‑mover’s distance.

---

### 28. Picking Up Chicks (Google Code Jam)

* **Problem Definition:** Chicks on a line must reach barn in time; only those that can swap past slower ones count. Count min swaps or fail.
* **Core Concept:** Greedy from farthest chick.
* **Approach/Strategy:**
  Iterate from end: count how many can reach in time; track number of slower blocking chicks; total swaps += blockers for each good chick until `C` reached.
* **Related Concepts:** Inversion counting; sliding window.

---

### 29. CHOCOLA – Chocolate (Spoj)

* **Problem Definition:** Minimize cost of breaking chocolate bar of size `m×n` with given horizontal & vertical cut costs; each cut cost multiplied by current segments.
* **Core Concept:** Same as “Minimum Cost to Cut Board” (#12 above).
* **Related Concepts:** See Board‑cutting.

---

### 30. ARRANGE – Arranging Amplifiers (Spoj)

* **Problem Definition:** Given chain of bulbs and operations, maximize number of bulbs on with minimal amplifier placements.
* **Core Concept:** Greedy placement at farthest reach.
* **Approach/Strategy:**
  Scan positions, maintain current coverage; when leaving coverage, place amplifier at farthest reachable position among available, increment count.
* **Related Concepts:** Interval covering; jump game.

---

### 31. K‑Centers Problem

* **Problem Definition:** Choose `k` centers from points to minimize the maximum distance of any point to its nearest center. NP‑hard, but 2‑approx greedy.
* **Analogy:** Placing `k` fire stations to minimize worst response time.
* **Core Concept:** Farthest‑first traversal.
* **Approach/Strategy:**

  1. Pick arbitrary first center.
  2. Repeatedly choose the point farthest from all chosen centers as next center, until `k`.
* **Related Concepts:** k‑means seeding (k‑means++); clustering approximation.

---

### 32. Minimum Cost of Ropes

* **Problem Definition:** Given `n` ropes, combine them into one rope; each connection costs sum of two ropes; minimize total cost.
* **Analogy:** Optimal way to merge files with minimal disk I/O.
* **Core Concept:** Greedy merge of smallest lengths first.
* **Approach/Strategy:**

  1. Push all lengths into min‑heap.
  2. While heap size >1: pop two smallest, cost += sum, push sum back.
* **Related Concepts:** Huffman coding; optimal merge patterns.

---

### 33. Smallest Number with Given #Digits & Sum of Digits

* **Problem Definition:** Form smallest positive integer with `d` digits whose digits sum to `s`.
* **Analogy:** Minimal account number meeting digit‑sum constraint.
* **Core Concept:** Greedy fill digits from most significant with minimal possible.
* **Approach/Strategy:**

  1. If `s=0` and `d=1`, answer = 0; if `s>9d`, impossible.
  2. For pos=1…d: choose smallest digit `x` from `(0 or 1 if first) to 9` such that remaining sum `(s−x) ≤ 9*(d−pos)`. Subtract `s−=x`. Append `x`.
* **Related Concepts:** Constructive greedy; digit DP inverse.

---

### 34. Rearrange Characters so No Two Adjacent Are Same

* **Problem Definition:** Same as string greedy (#34 earlier).
* **Related Concepts:** Max‑heap of char frequencies.

---

### 35. Find Maximum Sum Equal Sum of Three Stacks

* **Problem Definition:** Given three stacks of positive integers, remove zero or more from top to maximize equal sum across all three.
* **Analogy:** Balancing workloads by trimming top‑heavy sections.
* **Core Concept:** Greedy reduce the tallest stack.
* **Approach/Strategy:**

  1. Compute total sums of each stack and store as arrays.
  2. While not all equal: remove top element from the stack with greatest sum, update sum.
  3. Stop when sums equal or one stack empties (then zero).
* **Related Concepts:** Prefix sums; three‑way balancing.

---
