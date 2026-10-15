# Student Merge Sort — Scholarship Ranking

## What is this program?
A program that ranks students by their marks — highest to lowest — and then picks out who qualifies for a scholarship, using the classic Merge Sort algorithm to do the sorting.

## Description
Starting with a fixed list of students and their marks, the program keeps splitting the list in half over and over until each piece has just one student left (which is trivially "sorted"). Then it merges those tiny pieces back together, always picking the higher mark first, so the final list comes out in descending order. Once sorted, it goes through the list again and picks out everyone whose marks meet or beat the scholarship cutoff (85).

## Input
- A fixed, hardcoded list of `(name, marks)` pairs — no user typing involved in this version.

## Output
- All students printed out in descending order of marks.
- A separate list showing only the students who qualify for the scholarship.

## Time Complexity
**O(n log n)** — the classic merge sort cost. The list gets split in half `log n` times, and merging everything back together at each level takes `O(n)` work, so it multiplies out to `n log n`.

## Space Complexity
**O(n)** — merging isn't done in-place here; new lists get created at every merge step, and there's also the recursion stack to account for (about `log n` deep).

## Problem Decomposition
1. **Base case:** a list of 0 or 1 students is already sorted — nothing to do.
2. **Divide:** split the list into two halves.
3. **Conquer:** recursively sort each half the same way.
4. **Combine:** merge the two sorted halves back into one list, always taking whichever front element has the higher marks first.
5. **Filter:** once sorted, walk through and keep only students at or above the cutoff.

## Pattern Recognition
This is **Divide and Conquer** in its purest form — the same big idea behind binary search, just applied to sorting instead of searching. Specifically, it's the **Merge Sort pattern**: split, solve the small pieces, merge them back smartly. Worth noticing how naturally it pairs with a **filter step** afterward — sort first, then pick out what you actually need.
