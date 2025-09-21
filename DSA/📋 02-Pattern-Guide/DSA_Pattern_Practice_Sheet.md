# 🚀 DSA Pattern-Based Practice Sheet

## 📋 Pattern Recognition Guide

### How to Identify Patterns:
1. **Arrays/Strings with contiguous elements** → Sliding Window
2. **Sorted array with target search** → Binary Search
3. **Two elements sum/difference** → Two Pointers
4. **Parentheses/brackets matching** → Stack
5. **Tree/graph traversal** → DFS/BFS
6. **Find all combinations/permutations** → Backtracking
7. **Optimal substructure** → Dynamic Programming

---

## 1. 📊 Arrays & Hashing
**Pattern Recognition**: Count frequencies, lookups, duplicates
**When to Use**: Need O(1) lookup time, frequency counting

### Problems (Easy → Hard):
1. [Two Sum](https://leetcode.com/problems/two-sum/) - Easy
2. [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) - Easy
3. [Valid Anagram](https://leetcode.com/problems/valid-anagram/) - Easy
4. [Group Anagrams](https://leetcode.com/problems/group-anagrams/) - Medium
5. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) - Medium
6. [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) - Medium
7. [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) - Medium
8. [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) - Medium
9. [3Sum](https://leetcode.com/problems/3sum/) - Medium
10. [4Sum](https://leetcode.com/problems/4sum/) - Medium

**Key Concepts**: HashMap usage, prefix sums, frequency counting
**Time Complexity**: O(n), Space: O(n)

---

## 2. ↔️ Two Pointers
**Pattern Recognition**: Sorted array, palindrome check, pair finding
**When to Use**: Opposite ends moving inward, slow/fast pointers

### Problems (Easy → Hard):
1. [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) - Easy
2. [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) - Easy
3. [3Sum](https://leetcode.com/problems/3sum/) - Medium
4. [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) - Medium
5. [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) - Easy
6. [Move Zeroes](https://leetcode.com/problems/move-zeroes/) - Easy
7. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) - Hard
8. [3Sum Closest](https://leetcode.com/problems/3sum-closest/) - Medium
9. [Sort Colors](https://leetcode.com/problems/sort-colors/) - Medium
10. [4Sum](https://leetcode.com/problems/4sum/) - Medium

**Key Concepts**: Left/right pointers, fast/slow pointers
**Time Complexity**: O(n) or O(n²), Space: O(1)

---

## 3. 🪟 Sliding Window
**Pattern Recognition**: Subarray/substring problems, "maximum/minimum in window"
**When to Use**: Contiguous sequence optimization

### Problems (Easy → Hard):
1. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) - Easy
2. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) - Easy
3. [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) - Medium
4. [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) - Medium
5. [Permutation in String](https://leetcode.com/problems/permutation-in-string/) - Medium
6. [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) - Hard
7. [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) - Hard
8. [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) - Medium
9. [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) - Medium
10. [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) - Hard

**Key Concepts**: Fixed/variable window, expand/contract technique
**Time Complexity**: O(n), Space: O(k) where k is window size

---

## 4. 📚 Stack
**Pattern Recognition**: Parentheses, nested structures, monotonic sequences
**When to Use**: LIFO behavior needed, matching problems

### Problems (Easy → Hard):
1. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) - Easy
2. [Min Stack](https://leetcode.com/problems/min-stack/) - Easy
3. [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) - Medium
4. [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) - Medium
5. [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) - Medium
6. [Car Fleet](https://leetcode.com/problems/car-fleet/) - Medium
7. [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) - Hard
8. [Valid Parentheses String](https://leetcode.com/problems/valid-parentheses-string/) - Medium
9. [Decode String](https://leetcode.com/problems/decode-string/) - Medium
10. [Basic Calculator](https://leetcode.com/problems/basic-calculator/) - Hard

**Key Concepts**: LIFO operations, monotonic stack, expression parsing
**Time Complexity**: O(n), Space: O(n)

---

## 5. 🔍 Binary Search
**Pattern Recognition**: Sorted array, search space reduction, "find target/condition"
**When to Use**: Search in sorted space, optimization problems

### Problems (Easy → Hard):
1. [Binary Search](https://leetcode.com/problems/binary-search/) - Easy
2. [Search Insert Position](https://leetcode.com/problems/search-insert-position/) - Easy
3. [Find First and Last Position](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) - Medium
4. [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) - Medium
5. [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) - Medium
6. [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) - Medium
7. [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) - Hard
8. [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) - Medium
9. [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) - Medium
10. [Find Peak Element](https://leetcode.com/problems/find-peak-element/) - Medium

**Key Concepts**: Left/right boundaries, condition checking
**Time Complexity**: O(log n), Space: O(1)

---

## 6. 🔗 Linked List
**Pattern Recognition**: Sequential access, cycle detection, merging
**When to Use**: Dynamic size, insertion/deletion operations

### Problems (Easy → Hard):
1. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) - Easy
2. [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) - Easy
3. [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) - Easy
4. [Remove Nth Node From End](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) - Medium
5. [Reorder List](https://leetcode.com/problems/reorder-list/) - Medium
6. [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) - Medium
7. [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) - Medium
8. [Find Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) - Medium
9. [LRU Cache](https://leetcode.com/problems/lru-cache/) - Medium
10. [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) - Hard

**Key Concepts**: Fast/slow pointers (Floyd's), dummy nodes
**Time Complexity**: O(n), Space: O(1) typically

---

## 7. 🌳 Trees
**Pattern Recognition**: Hierarchical data, path problems, level-order traversal
**When to Use**: Tree/binary tree problems, recursive solutions

### Problems (Easy → Hard):
1. [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) - Easy
2. [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) - Easy
3. [Same Tree](https://leetcode.com/problems/same-tree/) - Easy
4. [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) - Easy
5. [Lowest Common Ancestor of BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) - Easy
6. [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) - Medium
7. [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) - Medium
8. [Kth Smallest Element in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) - Medium
9. [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) - Hard
10. [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) - Hard

**Key Concepts**: DFS (preorder, inorder, postorder), BFS, recursion
**Time Complexity**: O(n), Space: O(h) where h is height

---

## 8. 🔤 Tries (Prefix Trees)
**Pattern Recognition**: Prefix matching, word search, autocomplete
**When to Use**: String prefix operations, word games

### Problems (Easy → Hard):
1. [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) - Medium
2. [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) - Medium
3. [Word Search II](https://leetcode.com/problems/word-search-ii/) - Hard
4. [Replace Words](https://leetcode.com/problems/replace-words/) - Medium
5. [Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) - Medium
6. [Maximum XOR of Two Numbers](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) - Medium
7. [Word Squares](https://leetcode.com/problems/word-squares/) - Hard
8. [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) - Hard
9. [Stream of Characters](https://leetcode.com/problems/stream-of-characters/) - Hard
10. [Short Encoding of Words](https://leetcode.com/problems/short-encoding-of-words/) - Medium

**Key Concepts**: Trie node structure, prefix operations
**Time Complexity**: O(m) for operations, where m is word length

---

## 9. 🏔️ Heap / Priority Queue
**Pattern Recognition**: "Top K", "Kth largest/smallest", merge operations
**When to Use**: Need min/max elements efficiently

### Problems (Easy → Hard):
1. [Kth Largest Element in Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) - Easy
2. [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) - Easy
3. [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) - Medium
4. [Kth Largest Element in Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) - Medium
5. [Task Scheduler](https://leetcode.com/problems/task-scheduler/) - Medium
6. [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) - Medium
7. [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) - Hard
8. [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) - Hard
9. [Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) - Hard
10. [IPO](https://leetcode.com/problems/ipo/) - Hard

**Key Concepts**: Min/max heap operations, heap properties
**Time Complexity**: O(log n) for insert/delete, O(1) for peek

---

## 10. 🔄 Backtracking
**Pattern Recognition**: "Find all", combinations, permutations, constraint satisfaction
**When to Use**: Generate all possible solutions, decision tree exploration

### Problems (Easy → Hard):
1. [Subsets](https://leetcode.com/problems/subsets/) - Medium
2. [Combination Sum](https://leetcode.com/problems/combination-sum/) - Medium
3. [Permutations](https://leetcode.com/problems/permutations/) - Medium
4. [Subsets II](https://leetcode.com/problems/subsets-ii/) - Medium
5. [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) - Medium
6. [Word Search](https://leetcode.com/problems/word-search/) - Medium
7. [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) - Medium
8. [Letter Combinations of Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) - Medium
9. [N-Queens](https://leetcode.com/problems/n-queens/) - Hard
10. [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) - Hard

**Key Concepts**: Choose/explore/unchoose pattern, pruning
**Time Complexity**: Exponential - O(2^n) or O(n!)

---

## 11. 🕸️ Graphs
**Pattern Recognition**: Connected components, shortest path, cycle detection
**When to Use**: Relationship between entities, network problems

### Problems (Easy → Hard):
1. [Number of Islands](https://leetcode.com/problems/number-of-islands/) - Medium
2. [Clone Graph](https://leetcode.com/problems/clone-graph/) - Medium
3. [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) - Medium
4. [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) - Medium
5. [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) - Medium
6. [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) - Medium
7. [Course Schedule](https://leetcode.com/problems/course-schedule/) - Medium
8. [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) - Medium
9. [Word Ladder](https://leetcode.com/problems/word-ladder/) - Hard
10. [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) - Hard

**Key Concepts**: DFS, BFS, topological sort, adjacency list/matrix
**Time Complexity**: O(V + E) where V=vertices, E=edges

---

## 12. 💎 Dynamic Programming
**Pattern Recognition**: Overlapping subproblems, optimal substructure, "count ways"
**When to Use**: Optimization problems, counting problems

### Problems (Easy → Hard):
1. [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) - Easy
2. [House Robber](https://leetcode.com/problems/house-robber/) - Medium
3. [Coin Change](https://leetcode.com/problems/coin-change/) - Medium
4. [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) - Medium
5. [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) - Medium
6. [Word Break](https://leetcode.com/problems/word-break/) - Medium
7. [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) - Medium
8. [House Robber II](https://leetcode.com/problems/house-robber-ii/) - Medium
9. [Decode Ways](https://leetcode.com/problems/decode-ways/) - Medium
10. [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) - Medium

**Key Concepts**: Memoization, tabulation, state transitions
**Time Complexity**: Varies - often O(n²) or O(n*m)

---

## 13. ⏰ Intervals
**Pattern Recognition**: Overlapping intervals, merging, scheduling
**When to Use**: Time-based problems, calendar applications

### Problems (Easy → Hard):
1. [Merge Intervals](https://leetcode.com/problems/merge-intervals/) - Medium
2. [Insert Interval](https://leetcode.com/problems/insert-interval/) - Medium
3. [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) - Medium
4. [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) - Easy (Premium)
5. [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) - Medium (Premium)
6. [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) - Medium
7. [Car Pooling](https://leetcode.com/problems/car-pooling/) - Medium
8. [My Calendar I](https://leetcode.com/problems/my-calendar-i/) - Medium
9. [Employee Free Time](https://leetcode.com/problems/employee-free-time/) - Hard (Premium)
10. [Range Module](https://leetcode.com/problems/range-module/) - Hard

**Key Concepts**: Sorting by start/end time, sweep line algorithm
**Time Complexity**: O(n log n) for sorting-based solutions

---

## 14. 💰 Greedy
**Pattern Recognition**: Local optimal choices, scheduling, optimization without DP
**When to Use**: When local optimum leads to global optimum

### Problems (Easy → Hard):
1. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) - Easy
2. [Jump Game](https://leetcode.com/problems/jump-game/) - Medium
3. [Jump Game II](https://leetcode.com/problems/jump-game-ii/) - Medium
4. [Gas Station](https://leetcode.com/problems/gas-station/) - Medium
5. [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) - Medium
6. [Partition Labels](https://leetcode.com/problems/partition-labels/) - Medium
7. [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) - Medium
8. [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) - Medium
9. [Candy](https://leetcode.com/problems/candy/) - Hard
10. [Create Maximum Number](https://leetcode.com/problems/create-maximum-number/) - Hard

**Key Concepts**: Greedy choice property, optimal substructure
**Time Complexity**: Often O(n) or O(n log n)

---

## 15. 🔢 Bit Manipulation
**Pattern Recognition**: Powers of 2, XOR properties, bit operations
**When to Use**: Optimize space, mathematical properties, unique elements

### Problems (Easy → Hard):
1. [Single Number](https://leetcode.com/problems/single-number/) - Easy
2. [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) - Easy
3. [Counting Bits](https://leetcode.com/problems/counting-bits/) - Easy
4. [Reverse Bits](https://leetcode.com/problems/reverse-bits/) - Easy
5. [Missing Number](https://leetcode.com/problems/missing-number/) - Easy
6. [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) - Medium
7. [Single Number II](https://leetcode.com/problems/single-number-ii/) - Medium
8. [Single Number III](https://leetcode.com/problems/single-number-iii/) - Medium
9. [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) - Medium
10. [Maximum XOR of Two Numbers in Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) - Medium

**Key Concepts**: XOR properties, bit masking, powers of 2
**Time Complexity**: O(1) for bit operations, O(n) for array processing

---

## 📅 Daily Practice Schedule

### Week 1-2: Foundation Patterns
- **Day 1-3**: Arrays & Hashing (3 easy problems)
- **Day 4-6**: Two Pointers (3 easy problems)
- **Day 7**: Review & solve 1 medium from either pattern

### Week 3-4: Core Techniques
- **Day 8-10**: Sliding Window (3 problems)
- **Day 11-13**: Stack (3 problems)
- **Day 14**: Mixed review day

### Week 5-6: Search & Traversal
- **Day 15-17**: Binary Search (3 problems)
- **Day 18-20**: Linked List (3 problems)
- **Day 21**: Algorithm analysis day

### Week 7-8: Tree & String Patterns
- **Day 22-24**: Trees (3 problems)
- **Day 25-27**: Tries (3 problems)
- **Day 28**: Pattern recognition practice

### Week 9-12: Advanced Patterns
- Continue with remaining patterns, 2-3 problems per pattern per week
- Focus on medium difficulty problems
- Practice pattern recognition speed

## 🎯 Success Metrics

### Daily Goals:
- [ ] Solve 1-2 problems (30-60 min)
- [ ] Identify pattern before coding
- [ ] Achieve target time complexity
- [ ] Explain solution approach

### Weekly Goals:
- [ ] Complete assigned pattern problems
- [ ] Review previous week's patterns
- [ ] Practice 1 mock interview problem
- [ ] Update progress tracker

### Monthly Goals:
- [ ] Master 4-5 new patterns
- [ ] Solve 50+ problems total
- [ ] Improve pattern recognition speed
- [ ] Complete mock interview sessions

---

**Remember**:
- Focus on understanding patterns, not memorizing solutions
- Practice explaining your approach out loud
- Time yourself to build interview confidence
- Review and refine solutions for optimal complexity

**Daily Mantra**: "I'm not just solving problems, I'm mastering patterns!"