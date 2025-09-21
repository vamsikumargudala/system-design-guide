# 🚀 DSA Pattern Recognition Cheat Sheet

## 🎯 Quick Pattern Identification

### 30-Second Pattern Recognition Flowchart

```
📋 READ PROBLEM → Ask these questions:

1. "What type of data structure?"
   → Array/String: Consider Two Pointers, Sliding Window, Binary Search
   → Tree: Consider DFS/BFS traversal patterns
   → Graph: Consider DFS/BFS, shortest path

2. "What's the goal?"
   → Find pair/triplet: Two Pointers, Hashing
   → Optimize subarray/substring: Sliding Window
   → Search in sorted: Binary Search
   → All combinations: Backtracking
   → Shortest/optimal path: DP, Greedy

3. "Any special constraints?"
   → Sorted array: Binary Search, Two Pointers
   → Need O(1) space: Two Pointers, Greedy
   → Tree/Graph traversal: DFS/BFS
   → Parentheses/brackets: Stack
```

---

## 🔍 Pattern Recognition Keywords

| **Keywords** | **Pattern** | **Example Problem** |
|-------------|-------------|-------------------|
| "contiguous subarray", "window" | Sliding Window | Max sum subarray |
| "sorted array", "search", "target" | Binary Search | Search in rotated array |
| "two elements sum to", "pair" | Two Pointers | Two Sum II |
| "all combinations", "permutations" | Backtracking | Generate parentheses |
| "shortest path", "minimum cost" | BFS, DP | Word Ladder |
| "top K", "Kth largest" | Heap | K closest points |
| "parentheses", "brackets", "nested" | Stack | Valid parentheses |
| "prefix", "suffix", "word search" | Trie | Word Search II |
| "cycle", "duplicate", "unique" | Hashing, Linked List | Find duplicate |
| "optimal substructure", "overlapping" | Dynamic Programming | Coin change |

---

## 📊 Pattern Templates & Time Complexities

### 1. 🔗 Two Pointers Template
```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        if condition_met(arr[left], arr[right]):
            return result
        elif need_larger_sum:
            left += 1
        else:
            right -= 1

    return default_result

# Time: O(n), Space: O(1)
```

### 2. 🪟 Sliding Window Template
```python
def sliding_window(arr):
    left = 0
    result = 0
    window_data = {}  # or counter

    for right in range(len(arr)):
        # Expand window
        window_data[arr[right]] = window_data.get(arr[right], 0) + 1

        # Contract window if needed
        while window_invalid():
            window_data[arr[left]] -= 1
            if window_data[arr[left]] == 0:
                del window_data[arr[left]]
            left += 1

        # Update result
        result = max(result, right - left + 1)

    return result

# Time: O(n), Space: O(k) where k is window size
```

### 3. 🔍 Binary Search Template
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Time: O(log n), Space: O(1)
```

### 4. 🔄 Backtracking Template
```python
def backtrack(candidates, path, result):
    if is_valid_solution(path):
        result.append(path[:])  # Make copy
        return

    for candidate in candidates:
        if is_valid_candidate(candidate, path):
            # Choose
            path.append(candidate)
            # Explore
            backtrack(get_next_candidates(), path, result)
            # Unchoose
            path.pop()

# Time: Exponential - O(2^n) or O(n!)
```

### 5. 🌳 Tree DFS Template
```python
def dfs(root):
    if not root:
        return base_case

    # Process current node (preorder)
    result = process(root.val)

    # Recurse on children
    left_result = dfs(root.left)
    right_result = dfs(root.right)

    # Combine results (postorder)
    return combine(result, left_result, right_result)

# Time: O(n), Space: O(h) where h is height
```

### 6. 🕸️ Graph BFS Template
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        process(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Time: O(V + E), Space: O(V)
```

---

## 🎮 Common Interview Patterns by Company

### 🍎 Apple Favorites:
- Tree traversals (DFS/BFS)
- Dynamic Programming (1D/2D)
- Array manipulation
- **Focus**: Clean code, edge cases

### 🏢 Google Favorites:
- Graph algorithms
- Dynamic Programming
- System design integration
- **Focus**: Scalability, optimization

### 💙 Facebook/Meta Favorites:
- BFS/DFS on graphs
- Dynamic Programming
- String manipulation
- **Focus**: Social graph problems

### 🚗 Uber/Lyft Favorites:
- Geospatial algorithms
- Sliding window
- Priority queues
- **Focus**: Real-time optimization

### 💰 Finance (Goldman, JPMorgan):
- Mathematical algorithms
- Dynamic Programming
- Greedy algorithms
- **Focus**: Precision, edge cases

---

## ⚡ Quick Decision Tree

```
🤔 "How do I know which pattern to use?"

📊 ARRAY/STRING PROBLEM?
├─ Sorted? → Binary Search / Two Pointers
├─ Find subarray/substring? → Sliding Window
├─ Pair/triplet sum? → Two Pointers / Hashing
└─ Count/frequency? → Hashing

🌳 TREE/GRAPH PROBLEM?
├─ Path problems? → DFS
├─ Level-by-level? → BFS
├─ All paths? → Backtracking
└─ Shortest path? → BFS / Dijkstra

🔢 OPTIMIZATION PROBLEM?
├─ Overlapping subproblems? → Dynamic Programming
├─ Greedy choice works? → Greedy
├─ Multiple constraints? → Backtracking
└─ Top K elements? → Heap

📚 DATA STRUCTURE PROBLEM?
├─ LIFO behavior? → Stack
├─ Fast lookups? → Hash Table
├─ Prefix matching? → Trie
└─ Min/Max queries? → Heap
```

---

## 🚨 Red Flags & Anti-Patterns

### ❌ DON'T Use Sliding Window If:
- Array is not contiguous problem
- Need to find pairs from different parts
- Problem requires sorting first

### ❌ DON'T Use Two Pointers If:
- Array is not sorted (unless you sort first)
- Need to process elements independently
- Looking for all combinations

### ❌ DON'T Use Binary Search If:
- Array is not sorted
- Search space is not monotonic
- Need to find all occurrences in unsorted data

### ❌ DON'T Use Backtracking If:
- Only need one solution (not all)
- Problem has optimal substructure (use DP)
- Can be solved greedily

---

## 🎯 Pattern Mastery Checklist

### 📊 Arrays & Hashing
- [ ] Can identify when to use HashMap vs Set
- [ ] Know prefix sum technique
- [ ] Understand frequency counting patterns

### ↔️ Two Pointers
- [ ] Can apply to sorted arrays
- [ ] Know fast/slow pointer technique
- [ ] Understand when to use opposite ends

### 🪟 Sliding Window
- [ ] Can implement fixed and variable windows
- [ ] Know when to expand vs contract
- [ ] Master the expand-contract pattern

### 📚 Stack
- [ ] Recognize nested structure problems
- [ ] Know monotonic stack applications
- [ ] Understand LIFO property usage

### 🔍 Binary Search
- [ ] Can handle different boundary conditions
- [ ] Know when search space is monotonic
- [ ] Master template variations

### 🌳 Trees
- [ ] Comfortable with recursion
- [ ] Know all traversal methods
- [ ] Can apply to BST properties

### 🕸️ Graphs
- [ ] Can implement DFS and BFS
- [ ] Know when to use adjacency list vs matrix
- [ ] Understand topological sort

### 💎 Dynamic Programming
- [ ] Can identify optimal substructure
- [ ] Know memoization vs tabulation
- [ ] Understand state transitions

---

## 📱 Quick Reference Mobile Card

```
🔥 EMERGENCY PATTERN RECOGNITION

See "contiguous" or "subarray"? → SLIDING WINDOW
See "sorted array"? → BINARY SEARCH or TWO POINTERS
See "all combinations"? → BACKTRACKING
See "shortest/minimum"? → BFS or DP
See "parentheses"? → STACK
See "top K"? → HEAP
See "prefix/suffix"? → TRIE
See "tree traversal"? → DFS/BFS

💡 When stuck: Start with brute force, then optimize!
```

---

## 🏆 Master's Mindset

### Before Solving Any Problem:
1. **Read twice** - Understand requirements clearly
2. **Identify pattern** - Use the keywords and flowchart
3. **Think edge cases** - Empty input, single element, duplicates
4. **Start simple** - Brute force first, then optimize
5. **Trace through** - Walk through your solution with examples

### During Implementation:
- **Name variables clearly** - `left`, `right`, not `i`, `j`
- **Handle edge cases first** - Empty arrays, null pointers
- **Use helper functions** - Keep main logic clean
- **Test with examples** - Trace through manually

### After Solving:
- **Analyze complexity** - Time and space
- **Consider alternatives** - Could another pattern work?
- **Explain approach** - Practice verbalizing solution
- **Note lessons learned** - Update your pattern recognition

---

**Remember**: Patterns are tools, not rigid rules. Sometimes problems combine multiple patterns or require creative adaptations. The key is recognizing the core structure and applying the most appropriate technique!

**Master's Secret**: The best engineers don't just solve problems—they recognize patterns instantly and choose optimal approaches before writing a single line of code. 🚀