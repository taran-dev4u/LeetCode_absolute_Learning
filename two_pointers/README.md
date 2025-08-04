# Two Pointers
●	Create a Graph print it
●	Implement BFS algorithm
●	Implement DFS Algo
●	Detect Cycle in Directed Graph using BFS/DFS Algo
●	Detect Cycle in UnDirected Graph using BFS/DFS Algo
●	Search in a Maze
●	Minimum Step by Knight
●	flood fill algo
●	Clone a graph
●	Making wired Connections
●	word Ladder
●	Dijkstra algo
●	Implement Topological Sort
●	Minimum time taken by each job to be completed given by a Directed Acyclic Graph
●	Find whether it is possible to finish all tasks or not from given dependencies
●	Find the no. of Islands
●	Given a sorted Dictionary of an Alien Language, find order of characters
●	Implement Kruskal's Algorithm
●	Implement Prim's Algorithm
●	Total no. of Spanning tree in a graph
●	Implement Bellman Ford Algorithm
●	Implement Floyd warshall Algorithm
●	Travelling Salesman Problem
●	Graph Colouring Problem
●	Snake and Ladders Problem
●	Find bridge in a graph
●	Count Strongly connected Components (Kosaraju Algo)
●	Check whether a graph is Bipartite or Not
●	Detect Negative cycle in a graph
●	Longest path in a Directed Acyclic Graph
●	Journey to the Moon
●	Cheapest Flights Within K Stops
●	Oliver and the Game
●	Water Jug problem using BFS (This question appears twice consecutively in the source)
●	Find if there is a path of more than k length from a source
●	M-Colouring Problem
●	Minimum edges to reverse to make path from source to destination
●	Paths to travel each nodes using each edge (Seven Bridges)
●	Vertex Cover Problem
●	Chinese Postman or Route Inspection
●	Number of Triangles in a Directed and Undirected Graph
●	Minimise the cashflow among a given set of friends who have borrowed money from each other
●	Two Clique Problem

---

### 1. Create & Print a Graph

* **Problem Definition:** Represent a set of vertices and edges in code and output its structure.
* **Real‑World Analogy:** Drawing and labeling a city map of intersections and roads.
* **Core Concept:** Adjacency list vs. adjacency matrix representations.
* **Approach/Strategy:**

  1. Choose representation (list or matrix).
  2. Initialize empty structure for `V` vertices.
  3. For each edge `(u,v)`, update structures (`adj[u].append(v)` and, if undirected, `adj[v].append(u)`).
  4. Print by iterating vertices and listing their neighbors (or matrix rows).
* **Related Concepts:** Directed vs. undirected graphs; sparse vs. dense representations.

---

### 2. Breadth‑First Search (BFS)

* **Problem Definition:** Visit all vertices reachable from a start vertex in order of increasing distance.
* **Real‑World Analogy:** Ripples spreading in a pond from a dropped stone.
* **Core Concept:** Queue-based “level” traversal, marking visited nodes to avoid repeats.
* **Approach/Strategy:**

  1. Enqueue source, mark visited.
  2. While queue not empty: dequeue `u`, process it, enqueue each unvisited neighbor and mark visited.
* **Related Concepts:** Shortest path in unweighted graph; flood-fill; bipartiteness check.

---

### 3. Depth‑First Search (DFS)

* **Problem Definition:** Explore as far as possible along each branch before backtracking.
* **Analogy:** Solving a maze by always taking a new unexplored corridor until a dead end, then backtracking.
* **Core Concept:** Recursion or explicit stack; backtracking.
* **Approach/Strategy:**

  1. From source, visit node, mark visited.
  2. Recursively (or via stack) visit each unvisited neighbor.
* **Related Concepts:** Topological sort; cycle detection; connected components.

---

### 4. Detect Cycle in Directed Graph

* **Problem Definition:** Determine if a directed graph contains any cycle.
* **Analogy:** Tasks with circular dependencies preventing completion.
* **Core Concept:** DFS visitation states (unvisited, visiting, visited) or Kahn’s algorithm (in‑degree reduction).
* **Approach/Strategy:**

  * **DFS method:** Maintain recursion stack; if you revisit a “visiting” node, a cycle exists.
  * **BFS (Kahn’s):** Compute in‑degrees; repeatedly remove zero‑in‑degree nodes; if nodes remain, cycle.
* **Related Concepts:** Topological sort; deadlock detection.

---

### 5. Detect Cycle in Undirected Graph

* **Problem Definition:** Check if any cycle exists in an undirected graph.
* **Analogy:** Finding a looped trail in a hiking network.
* **Core Concept:** DFS with parent tracking or Union‑Find (disjoint sets).
* **Approach/Strategy:**

  * **DFS:** For each node, DFS to neighbors; if neighbor is visited and not the parent, cycle.
  * **Union‑Find:** For each edge, if endpoints already in same set, cycle; else union them.
* **Related Concepts:** Spanning trees; Kruskal’s algorithm checks.

---

### 6. Search in a Maze

* **Problem Definition:** Given a 2D grid with walls and open cells, determine if a path exists from start to end.
* **Analogy:** Navigating a labyrinth.
* **Core Concept:** Graph on grid; BFS/DFS on 4 (or 8) directions.
* **Approach/Strategy:** Treat each cell as node; edges to adjacent open cells; run BFS/DFS from start to check reachability of end.
* **Related Concepts:** Shortest path in grid; flood fill.

---

### 7. Minimum Steps by Knight

* **Problem Definition:** On an `N×N` chessboard, find the minimum moves for a knight to reach target square.
* **Analogy:** Finding shortest route with fixed movement rules.
* **Core Concept:** BFS on implicit graph of board positions.
* **Approach/Strategy:** Enqueue start with distance=0; for each dequeued position, generate all 8 knight moves within board, enqueue unvisited with `dist+1` until target reached.
* **Related Concepts:** Unweighted shortest path; 0–1 BFS variants.

---

### 8. Flood Fill Algorithm

* **Problem Definition:** Given a starting pixel in an image, replace its color and all connected same‑color pixels with a new color.
* **Analogy:** Filling a region with paint in a paint program.
* **Core Concept:** BFS or DFS on 4‑ or 8‑connected grid.
* **Approach/Strategy:** From start cell, recursively or via queue visit neighbors of same original color, change color, continue.
* **Related Concepts:** Connected components; boundary fill.

---

### 9. Clone a Graph

* **Problem Definition:** Given a reference to a node in a graph, create a deep copy of the entire graph.
* **Analogy:** Duplicating a network topology.
* **Core Concept:** DFS/BFS with hash map from original to clone.
* **Approach/Strategy:**

  1. Use map `orig→copy`.
  2. Starting at given node, BFS/DFS: for each neighbor, if not cloned, clone and recurse/enqueue; add cloned neighbor to current clone’s adjacency.
* **Related Concepts:** Deep vs. shallow copy; serialization.

---

### 10. Making Wired Connections

* **Problem Definition:** Given `n` computers and a list of cables connecting pairs, determine min operations to connect all computers.
* **Analogy:** Ensuring every office PC has network access by rewiring.
* **Core Concept:** Count connected components; need at least `components−1` extra cables.
* **Approach/Strategy:** Build graph; use DFS/BFS to count components; if total edges < n−1 impossible; else answer = `components−1`.
* **Related Concepts:** Spanning forest; Union‑Find connectivity.

---

### 11. Word Ladder

* **Problem Definition:** Transform `beginWord` to `endWord` by changing one letter at a time, each intermediate word must be in given dictionary. Return shortest transformation length.
* **Analogy:** Gradual mutation from one DNA sequence to another.
* **Core Concept:** BFS on implicit word‑graph.
* **Approach/Strategy:** Precompute patterns (`h_t` with one letter replaced by `*`) mapping to words; BFS from `begin`, for each word generate neighbors via patterns, enqueue unvisited, track levels.
* **Related Concepts:** Bidirectional BFS; generic state graphs.

---

### 12. Dijkstra’s Algorithm

* **Problem Definition:** Single‑source shortest paths in graph with nonnegative edge weights.
* **Analogy:** GPS finding fastest route on roads with travel times.
* **Core Concept:** Greedy relaxation using a min‑priority queue.
* **Approach/Strategy:** Initialize distances infinite except source=0; push source into min‑heap; while heap, pop `(d,u)`, if `d>dist[u]` skip; for each edge `u→v` with weight `w`, if `dist[v]>d+w`, update and push `(dist[v],v)`.
* **Related Concepts:** Bellman–Ford (handles negative); A\* (with heuristic).

---

### 13. Topological Sort

* **Problem Definition:** Linear ordering of vertices in a DAG such that for every edge `u→v`, `u` comes before `v`.
* **Analogy:** Course scheduling respecting prerequisites.
* **Core Concept:** Kahn’s algorithm (BFS on in‑degree zero) or DFS post‑order.
* **Approach/Strategy:**

  * **Kahn:** Compute in‑degrees, enqueue zeros, dequeue `u`, append to result, decrement neighbors’ in‑deg, enqueue any new zeros.
  * **DFS:** Recursively DFS unvisited nodes, push node onto stack after visiting all neighbors; pop stack for order.
* **Related Concepts:** Cycle detection; DAG shortest paths.

---

### 14. Min Time for Jobs in DAG

* **Problem Definition:** Given DAG with job durations on nodes, compute earliest completion time for each job assuming parallel execution but respecting dependencies.
* **Analogy:** Project tasks with prerequisites and individual durations.
* **Core Concept:** DP on topological order.
* **Approach/Strategy:**

  1. Topologically sort DAG.
  2. Initialize `time[u] = duration[u]`.
  3. For each `u` in topo order, for each `v` dependent on `u`, `time[v] = max(time[v], time[u] + duration[v])`.
* **Related Concepts:** Critical path method; longest path in DAG.

---

### 15. Can All Tasks Finish? (Course Schedule)

* **Problem Definition:** Given prerequisites as directed edges, decide if you can complete all tasks (i.e., graph is acyclic).
* **Analogy:** Checking if a set of university courses has circular prerequisites.
* **Core Concept:** Cycle detection in DAG.
* **Approach/Strategy:** Detect cycle via Kahn’s algorithm (if processed nodes < n, cycle) or DFS with recursion stack.
* **Related Concepts:** Topological sort feasibility.

---

### 16. Number of Islands

* **Problem Definition:** Given 2D grid of `0` (water) and `1` (land), count connected components of land (4‑connected).
* **Analogy:** Counting islands on a map.
* **Core Concept:** Grid graph DFS/BFS.
* **Approach/Strategy:** For each cell `1` not yet visited, BFS/DFS mark its entire island visited, increment count.
* **Related Concepts:** Flood fill; connected components.

---

### 17. Alien Dictionary (Sorted Dictionary)

* **Problem Definition:** Given sorted list of words in unknown alphabetic order, derive the character ordering.
* **Analogy:** Decoding an unfamiliar language’s alphabet from its dictionary.
* **Core Concept:** Build precedence graph of letters → topological sort.
* **Approach/Strategy:**

  1. Compare adjacent words, find first differing character pair `(u,v)`, add edge `u→v`.
  2. Topologically sort the resulting graph of characters.
* **Related Concepts:** Course schedule; precedence constraints.

---

### 18. Kruskal’s MST Algorithm

* **Problem Definition:** Find minimum‑weight spanning tree in a weighted undirected graph.
* **Analogy:** Laying cables to connect all cities with minimum cost.
* **Core Concept:** Greedy edge selection + Union‑Find to avoid cycles.
* **Approach/Strategy:**

  1. Sort edges by weight.
  2. Initialize Union‑Find.
  3. For each edge `(u,v)`, if `find(u)≠find(v)`, union and include edge in MST.
* **Related Concepts:** Prim’s algorithm; cycle detection; disjoint sets.

---

### 19. Prim’s MST Algorithm

* **Problem Definition:** Like Kruskal, build MST but growing one tree from a start vertex.
* **Core Concept:** Greedy nearest‑neighbor using a min‑heap of edges crossing the cut.
* **Approach/Strategy:**

  1. Pick arbitrary start vertex, add to MST set.
  2. Push all edges from that vertex into min‑heap.
  3. While heap not empty & MST incomplete: pop smallest edge; if it connects to new vertex, add edge and push that vertex’s outgoing edges.
* **Related Concepts:** Dijkstra’s algorithm (similar structure).

---

### 20. Count of Spanning Trees

* **Problem Definition:** Compute total number of distinct spanning trees in a connected graph.
* **Core Concept:** Matrix‑Tree Theorem (Kirchhoff’s theorem).
* **Approach/Strategy:**

  1. Build Laplacian matrix `L` (degree on diagonal, −1 for edges).
  2. Delete any one row & column from `L`.
  3. Compute determinant of resulting `(n−1)×(n−1)` matrix.
* **Related Concepts:** Kirchhoff’s laws; graph Laplacian; determinants.

---

### 21. Bellman–Ford Algorithm

* **Problem Definition:** Single‑source shortest paths with negative weights; detect negative cycles.
* **Core Concept:** Relax all edges up to `V−1` times.
* **Approach/Strategy:**

  1. Initialize `dist[source]=0`, others `∞`.
  2. Repeat `V−1` times: for each edge `u→v` with weight `w`, if `dist[v]>dist[u]+w`, update.
  3. One more pass: if any edge can still relax, negative cycle exists.
* **Related Concepts:** Dijkstra; SPFA; difference constraints.

---

### 22. Floyd–Warshall Algorithm

* **Problem Definition:** All‑pairs shortest paths in weighted graph (can have negative edges, no negative cycles).
* **Core Concept:** Dynamic programming on triples of vertices.
* **Approach/Strategy:**
  `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])` for all `i,j,k`.
* **Related Concepts:** Transitive closure; repeated squaring.

---

### 23. Travelling Salesman Problem (TSP)

* **Problem Definition:** Given weighted complete graph, find shortest Hamiltonian cycle. NP‑hard.
* **Core Concept:** NP‑completeness; DP on subsets (Held–Karp) or heuristics.
* **Approach/Strategy:**

  * **Exact (Held–Karp):** DP over subsets: `dp[mask][i]` = min cost to reach subset `mask` ending at `i`. Complexity O(n²·2ⁿ).
  * **Approx/Heuristic:** Nearest neighbor, Christofides’ algorithm (3/2‑approx).
* **Related Concepts:** Hamiltonian cycle; bitmask DP; approximation algorithms.

---

### 24. Graph Coloring Problem

* **Problem Definition:** Assign up to `M` colors to vertices so adjacent vertices differ; decide if possible. NP‑complete for general `M`.
* **Core Concept:** Backtracking or DSATUR heuristic.
* **Approach/Strategy:**

  1. DFS/backtrack assign colors 1…M to vertex `i`, checking no neighbor conflict.
  2. Prune when no color fits.
* **Related Concepts:** Map coloring; register allocation; clique cover.

---

### 25. Snake & Ladders Problem

* **Problem Definition:** On `N×N` board with snakes (move down) and ladders (move up), find min dice throws from start to finish.
* **Analogy:** Board game shortest‑path.
* **Core Concept:** BFS on implicit graph of squares (edges = dice outcomes + jumps).
* **Approach/Strategy:**

  1. Build array `move[]` mapping square→destination (after snake/ladder).
  2. BFS from 0: for each dequeued square `u`, for dice=1…6, let `v=u+dice`, `final = move[v]` if exists; enqueue unvisited, `dist[final]=dist[u]+1`.
* **Related Concepts:** Unweighted shortest path; board game simulation.

---

### 26. Find Bridges in a Graph

* **Problem Definition:** Identify edges whose removal increases the number of connected components.
* **Core Concept:** DFS time stamps + low‑link values (Tarjan’s algorithm).
* **Approach/Strategy:**

  1. DFS numbering `disc[u]` and compute `low[u]` = earliest discovery reachable from subtree of `u`.
  2. For each edge `(u,v)`, if `low[v] > disc[u]`, it’s a bridge.
* **Related Concepts:** Articulation points; biconnected components.

---

### 27. Count Strongly Connected Components (Kosaraju)

* **Problem Definition:** In a directed graph, find maximal sets where each vertex reachable from each other.
* **Core Concept:** Two‑pass DFS on original and transposed graph.
* **Approach/Strategy:**

  1. DFS on original graph, push nodes onto stack by finish time.
  2. Transpose graph.
  3. Pop stack, DFS from each unvisited node in transpose; each DFS marks one SCC.
* **Related Concepts:** Tarjan’s SCC algorithm; condensation graph.

---

### 28. Check Bipartiteness

* **Problem Definition:** Determine if a graph’s vertices can be 2‑colored so no edge joins same color.
* **Analogy:** Splitting teams into two rival groups with no internal matches.
* **Core Concept:** BFS/DFS coloring and conflict detection.
* **Approach/Strategy:**
  For each unvisited node, BFS: assign color 0; for each neighbor, if uncolored assign `1−color[u]`; if colored same as `u`, not bipartite.
* **Related Concepts:** Odd‑cycle detection; 2‑SAT reduction.

---

### 29. Detect Negative Cycle in Graph

* **Problem Definition:** Check if any cycle has negative total weight.
* **Core Concept:** Bellman–Ford extra iteration.
* **Approach/Strategy:** After `V−1` relaxations, one more pass: if any edge can relax further, negative cycle reachable from source exists.
* **Related Concepts:** Arbitrage detection; difference constraints.

---

### 30. Longest Path in a DAG

* **Problem Definition:** Find the maximum‑weight or longest simple path in a weighted DAG.
* **Core Concept:** DP on topological order.
* **Approach/Strategy:**

  1. Topo sort vertices.
  2. Initialize `dist[source]=0`, others `−∞`.
  3. For each `u` in topo order, for each `u→v` with weight `w`, `dist[v] = max(dist[v], dist[u]+w)`.
* **Related Concepts:** Critical path method; longest path in general is NP‑hard.

---

### 31. Journey to the Moon

* **Problem Definition:** On HackerRank: given astronaut pairs from same country, count ways to choose 2 astronauts from different countries.
* **Analogy:** Pairing people from different teams.
* **Core Concept:** Connected components + combinatorics.
* **Approach/Strategy:**
  BFS/DFS to find sizes of each component (country).
  Count valid pairs = Σ over all pairs of components `size[i]×size[j]`. Or maintain running sum.
* **Related Concepts:** Combination counting; union‑find.

---

### 32. Cheapest Flights Within K Stops

* **Problem Definition:** Given flights (edges with price) between cities, find minimum cost from src to dst with ≤K stops.
* **Analogy:** Cheapest itinerary with limited layovers.
* **Core Concept:** Modified BFS (level = stops) or Bellman–Ford limited to K+1 iterations.
* **Approach/Strategy:**

  * **Bellman‑Ford style:** Relax all edges up to `K+1` times, tracking two arrays for previous and current iteration.
  * **Dijkstra variant:** Use priority queue storing `(cost, city, stops)` and only push if `stops ≤ K`.
* **Related Concepts:** Constrained shortest path; stateful Dijkstra.

---

### 33. Oliver and the Game

* **Problem Definition:** CodeChef problem where Oliver plays on a circular board with cards; find max score.
* **Analogy:** Circular path with rewards and penalties.
* **Core Concept:** Prefix sums on circular array + two‑pointer or deque optimization.
* **Approach/Strategy:**
  Transform to linear via doubling array; maintain sliding window and monotonic deque to track best gains under constraints.
* **Related Concepts:** Maximum subarray on circular array; deque optimization.

---

### 34. Water Jug Problem (BFS)

* **Problem Definition:** Given two jugs of capacities `m` and `n` and target `d`, find min steps to measure exactly `d`.
* **Analogy:** Measuring exact volume using two unmarked containers.
* **Core Concept:** BFS on state graph `(x,y)` jug contents.
* **Approach/Strategy:**
  Enqueue initial `(0,0)`; from `(x,y)` generate all 6 possible operations (fill, empty, pour), enqueue unvisited states until reaching a state with `x==d` or `y==d`.
* **Related Concepts:** State‑space search; water pouring puzzles.

---

### 35. Path of Length > K

* **Problem Definition:** Decide if there exists a simple path from source of total weight > K.
* **Core Concept:** DFS with pruning when accumulated weight > K.
* **Approach/Strategy:**
  Recursively explore neighbors, passing remaining `K−w(u,v)`, mark visited, if remaining ≤0 return True, backtrack visited.
* **Related Concepts:** NP‑complete in general graphs; backtracking.

---

### 36. M‑Coloring Problem

* **Problem Definition:** Can we color vertices of a graph with `M` colors so no adjacent share a color?
* **Core Concept:** Backtracking search.
* **Approach/Strategy:**
  Recursively assign to vertex `v` any color `1…M` not used by neighbors; if reach `n`, success.
* **Related Concepts:** Graph coloring; Welsh–Powell heuristic.

---

### 37. Min Edges to Reverse to Make Path

* **Problem Definition:** In directed graph, find minimum edges to reverse so there is a path from `src` to `dst`.
* **Core Concept:** 0–1 BFS on augmented graph.
* **Approach/Strategy:**
  Build adjacency where original edges cost `0`, reversed edges cost `1`; run 0–1 BFS from `src`, result distance to `dst`.
* **Related Concepts:** Shortest path with edge‑reversal penalty; deque BFS.

---

### 38. Seven Bridges (Eulerian Path)

* **Problem Definition:** Determine a path using every edge exactly once and return to start (Eulerian circuit) or start ≠ end (Eulerian path).
* **Analogy:** Königsberg bridge problem.
* **Core Concept:** Eulerian trail conditions:

  * Undirected: all vertices with nonzero degree belong to single component; either 0 or 2 vertices of odd degree.
* **Approach/Strategy:**
  Check degree conditions and connectivity; if exists, Hierholzer’s algorithm to construct the path in O(E).
* **Related Concepts:** Chinese Postman problem; De Bruijn sequences.

---

### 39. Vertex Cover Problem

* **Problem Definition:** Find the smallest set of vertices such that every edge has at least one endpoint in the set. NP‑complete.
* **Analogy:** Minimal guard placement to watch every corridor in a museum.
* **Core Concept:** NP‑completeness; 2‑approximation via maximal matching.
* **Approach/Strategy:**

  * **Exact:** Backtracking or reduction to SAT for small graphs.
  * **Approx:** Find any maximal matching; take both endpoints of each matched edge → 2‑approx.
* **Related Concepts:** Independent set; clique cover; approximations.

---

### 40. Chinese Postman (Route Inspection)

* **Problem Definition:** Find shortest closed walk that visits every edge at least once in a (strongly) connected graph.
* **Analogy:** Mail carrier delivering mail on every street and returning to depot.
* **Core Concept:** Eulerian augmentation: make all vertices even degree by pairing odd‑degree vertices with minimum‑weight paths.
* **Approach/Strategy:**

  1. Find vertices of odd degree (2k of them).
  2. Compute all‑pairs shortest paths (Floyd–Warshall).
  3. Compute minimum‑weight perfect matching among odd vertices.
  4. Augment graph edges accordingly; then Eulerian circuit via Hierholzer.
* **Related Concepts:** Matching; Eulerian trails; metric TSP.

---

### 41. Number of Triangles in Graph

* **Problem Definition:** Count all distinct 3‑cycles in directed or undirected graph.
* **Core Concept:** Matrix multiplication or node‑ordering enumeration.
* **Approach/Strategy:**

  * **Adjacency matrix:** Trace of `A³/6` for undirected.
  * **List approach:** Order vertices by degree, for each `u`, for each `(u,v)` and `(u,w)` check if `(v,w)` exists.
* **Related Concepts:** Clustering coefficient; combinatorial enumeration.

---

### 42. Minimize Cashflow Among Friends

* **Problem Definition:** Given net balances of friends, settle debts with minimum transactions.
* **Analogy:** Group of friends splitting bills and settling later.
* **Core Concept:** Greedy settle largest creditor with largest debtor.
* **Approach/Strategy:**

  1. Compute net amount each person owes/gets.
  2. While any nonzero: pick max creditor `p` and max debtor `q`, settle `min(amount[p], -amount[q])`, update balances, recurse.
* **Related Concepts:** Flow net; transfer minimization.

---

### 43. Two‑Clique Problem

* **Problem Definition:** Decide if a graph’s vertices can be partitioned into two cliques.
* **Analogy:** Splitting guests into two tables where each table’s guests all know each other.
* **Core Concept:** Complement graph bipartiteness.
* **Approach/Strategy:**

  1. Build complement graph (edges become non‑edges).
  2. Check if complement is bipartite (see #28).
  3. If yes, original can be two cliques.
* **Related Concepts:** Clique cover; graph complements; split graphs.

---
