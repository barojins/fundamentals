# Python DSA Template Set Design

## Goal

Build two complementary Python 3.12+ data-structure and algorithm resources:

- a small `core.py` that contains only the reusable foundations worth memorizing;
- a categorized `complete/` reference that covers the major DSA families used in
  LeetCode and general coding interviews.

The set must teach reusable structures rather than present a collection of answers
to isolated Easy problems. After the Python set is stable, its organization can be
ported to TypeScript as a separate project phase.

"Complete" means complete for practical coding interviews. It does not mean every
algorithm published in computer science.

## Existing Files

The following files remain intact for compatibility and comparison:

- `python/quick_templates.py`
- `python/templates.py`
- `python/concise_templates.py`

The new package does not import from these files and does not silently change their
APIs.

## Package Structure

```text
python/dsa/
├── __init__.py
├── README.md
├── core.py
└── complete/
    ├── __init__.py
    ├── arrays_strings.py
    ├── linked_lists.py
    ├── stacks_queues.py
    ├── trees.py
    ├── graphs.py
    ├── backtracking.py
    ├── dynamic_programming.py
    ├── searching_sorting.py
    ├── range_queries.py
    └── math.py

python/tests/dsa/
├── __init__.py
├── test_core.py
└── test_complete_*.py
```

`core.py` is intentionally standalone so a learner can repeatedly rewrite it
without navigating imports. Some implementation overlap with `complete/` is
intentional because the files serve different learning goals.

## Core Selection Rule

An item belongs in `core.py` only when it meets all three criteria:

1. it appears frequently across coding-interview problem families;
2. understanding it transfers to multiple problems;
3. its essential state transition can be memorized and reconstructed.

The core set is not required to contain a predetermined number of functions. It
contains:

- hash map and frequency counting;
- stack, queue, deque, and min-heap usage;
- two pointers;
- fixed and variable sliding windows;
- prefix sums;
- exact and boundary binary search;
- interval merging;
- monotonic stack;
- Kadane's algorithm;
- linked-list reversal and fast/slow pointers;
- tree DFS traversals and level-order BFS;
- graph DFS and BFS;
- grid DFS and BFS;
- topological sort;
- Union-Find;
- Dijkstra's algorithm;
- generic backtracking plus subsets, permutations, and combinations;
- representative 1D DP, 2D/grid DP, 0/1 knapsack, and unbounded knapsack states;
- the basic greedy selection pattern.

## Complete Reference Scope

### Arrays and strings

- two-pointer variants;
- fixed and variable sliding windows;
- prefix sums in one and two dimensions;
- difference arrays;
- Kadane's algorithm;
- interval processing;
- cyclic placement and partitioning;
- matrix traversal;
- KMP, Z algorithm, and rolling hash.

### Fundamental data structures

- stack, queue, deque, and heap patterns;
- singly linked-list operations and dummy nodes;
- binary-tree and binary-search-tree nodes;
- Trie;
- Union-Find;
- monotonic stack and monotonic deque.

### Searching and sorting

- exact, lower-bound, upper-bound, and answer-space binary search;
- merge sort, quicksort, counting sort, and heap sort;
- quickselect.

### Trees

- recursive and iterative preorder, inorder, and postorder traversal;
- level-order traversal;
- BST search and insertion;
- depth, diameter, and balance calculations;
- lowest common ancestor;
- construction and serialization.

### Graphs

- DFS, BFS, grid traversal, and multi-source BFS;
- directed and undirected cycle detection;
- bipartite checking;
- topological sorting with Kahn's algorithm and DFS;
- shortest paths with unweighted BFS, 0-1 BFS, Dijkstra, Bellman-Ford, and
  Floyd-Warshall;
- minimum spanning trees with Kruskal and Prim;
- strongly connected components;
- bridges and articulation points;
- a clearly marked optional max-flow reference.

### Backtracking and dynamic programming

- generic choose/explore/undo structure;
- subsets, permutations, combinations, combination sum, grid word search, and
  N-Queens;
- 1D and 2D state transitions;
- grid DP;
- 0/1 and unbounded knapsack;
- longest increasing subsequence;
- longest common subsequence and edit distance;
- interval, tree, and bitmask DP.

### Range queries and math

- Fenwick tree, segment tree, and sparse table;
- GCD, LCM, sieve of Eratosthenes, fast exponentiation, and basic modular
  arithmetic.

## Learning Format

Every core template has a compact memory card immediately above the code:

```text
WHEN: question signals that suggest the pattern
NEED: preconditions required for correctness
INVARIANT: the statement that remains true during execution
MEMORIZE: the state and update order worth recalling
COST: time and space complexity
```

Core code avoids advanced type syntax so the algorithm remains visually dominant.
It uses short, executable Python rather than pseudocode.

Every complete-reference implementation uses modern Python 3.12+ annotations and
documents:

- input representation and return value;
- when to use and when not to use the algorithm;
- preconditions;
- a short correctness argument;
- complexity;
- common mistakes;
- important related variants.

The reference remains concise: explanations teach the decision and invariant, not
line-by-line Python syntax.

## README and Study Flow

`python/dsa/README.md` provides:

- the distinction between Core and Complete;
- a category index linking concepts to files;
- a recommended learning order;
- a recall loop: recognize, state the invariant, trace, rewrite, and vary;
- guidance on choosing BFS, Dijkstra, Bellman-Ford, or Floyd-Warshall;
- guidance on choosing a window, two pointers, prefix sum, or binary search;
- a checklist for reconstructing a forgotten template.

The recommended progression is collections, array patterns, binary search,
stack/queue, linked lists, trees, graph traversal, backtracking, dynamic
programming, weighted graphs, then advanced structures.

## Interfaces and Error Handling

- Implementations are deterministic and do not print.
- Functions return results rather than mutating caller input unless in-place
  behavior is the algorithm's explicit purpose.
- Invalid structural preconditions raise `ValueError`, such as a negative Dijkstra
  edge or an invalid window size.
- Empty inputs return the natural identity when one exists; otherwise the function
  documents and raises `ValueError`.
- Graph functions state whether all vertices must appear as keys and how unreachable
  vertices are represented.
- Functions use zero-based indexing and clearly state whether interval endpoints
  are inclusive or half-open.

## Testing and Quality

- `test_core.py` covers every executable core template with a normal example and a
  defining edge case.
- Complete tests are grouped by module and cover public implementations,
  preconditions, unreachable states, duplicates, empty inputs, and disconnected
  graphs where relevant.
- Traversal tests define whether order is part of the contract; otherwise they test
  reachability without assuming incidental ordering.
- Shortest-path and spanning-tree algorithms are checked on small graphs with known
  costs.
- Data structures are checked for insertion, lookup, removal, and empty-state
  behavior.
- All new files must pass unittest discovery, Ruff formatting and linting, and
  Pyright under the repository configuration.
- Existing TypeScript checks remain green even though the TypeScript port is outside
  this phase.

## Delivery Phases

1. Create the package, README, core templates, and core tests.
2. Implement and test the complete modules by category.
3. Run repository-wide verification and review the set for missing or duplicated
   concepts.
4. Commit and push the Python DSA set.
5. Design and implement the TypeScript mirror as a separate phase after the Python
   interfaces and curriculum are stable.

## Success Criteria

- A learner can use `core.py` alone for active recall without reading problem
  solutions.
- A learner can find a major interview DSA family quickly through the README index.
- Each complete implementation is executable, documented, tested, and explicit
  about its correctness assumptions.
- Core remains meaningfully smaller and easier to rewrite than Complete.
- Existing template files and their APIs remain unchanged.
