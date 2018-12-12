# Sorting-And-Searching-Algorithms
A collection of sorting and searching algorithms implemented in Python - Basically revision for DADSA module, but perhaps useful to others.

Sorting algorithms can be described with a number of qualities that enables them to be
efficiently compared:

1. Computational complexity (worst, average, and best behaviour) - Usually described in terms of "Big O Notation" The ideal behaviour for a sort would be O(n), but this is not possible for the average case. The worst behaviour displayed is O(n^2).
2. Memory usage - Some algorithms are "in-place", meaning that they do not use extra memory beyond the storage of the list being sorted itself plus O(1) memory.
3. Recursion - Some algorithms are recursive, some can be both recursive and non recursive.
4. Stability - A stable algorithm is one where the relative order of items with the same value are maintained - if say item 1 and 4 had the same value of 5 and 1 occured before 4 in the list, they would not be sorted such that 4 was before than 1 at any point.
5. Comparative - If the algorithm uses a simple comparison (< or > etc.) to sort the list. Pigeonhole Sort is an example of a non-comparison sort.
6. General method - exchanging values, inserting values, selecting values, etc.
7. Adaptability - Whether or not the degree of sortedness affects the running time of the algorithm - attractive due to the high frequency of nearly sorted lists in real scenarios.

A link to a spreadsheet of sorting algorithm characteristics can be found [here](https://docs.google.com/spreadsheets/d/1GPdLRkJgQvLW5tWaqKwAx7EOX-uma_g8q0vQzqQL2Pk/edit?usp=sharing).


## Bubble Sort

Due to its comparatively awful performances, bubble sort is a fairly impractical choice for sorting. Even on the best
case scenarios, Insertion Sort still outperforms Bubble Sort due to its low number of swaps on mostly sorted lists.

Cocktail Shaker Sort is a variation of this algorithm which sorts from either end.

## Cocktail Sort Information

As with Bubble Sort, this algorithm has fairly awful performances, and thus is typically of no real world use. It deals
with "turtles" (small values that travel to the front of the list) better than Bubble Sort, but has no real improvement
in performance. Again, Insertion Sort is superior in similar deployment scenarios.

## Insertion Sort Information

Insertion sort scales badly with a complexity of O(n<sup>2</sup>), but is efficient on very small lists and lists that have already been mostly sorted. It is similar to the way people sort cards one at a time.

## Shell Sort Information

Shell sort is an improvement/variant on Insertion Sort. Instead of comparing only adjacent values as in IS, it performs
comparisons across long gaps. The gaps change in size as the list becomes more ordered. The method used to change the
gap size has a huge impact on the average running time of the algorithm.

## Quick Sort Information

Quick Sort breaks down a given list into smaller sub-lists, and then these smaller lists are sorted either recursively or iteratively until they are all sorted. All the lists are then appended into one fully sorted list.

## Selection Sort Information

Selection Sort picks the smallest element in the list and swaps it to the first position, then the second smallest into
the second position, etc. Selection sort is an in-place sort.

## Comb Sort Information

Comb sort extends Bubble Sort to solve the turtle problem. It's slightly faster on average than bubble sort. Comb
sort works by comparing elements with a gap in-between, and slowly decreasing the size of the gap as the algorithm
progresses. The final run of comb should be the same as that of bubble, albeit with greater efficiency due to the
removal of turtles.

## Merge Sort Information

Merge sort works by dividing a list into n sublists each of size 1, then repeatedly merging the sublists until there
is only one list remaining, which will be sorted.
