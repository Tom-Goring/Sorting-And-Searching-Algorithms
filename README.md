# Sorting-And-Searching-Algorithms
A collection of sorting and searching algorithms implemented in Python.

## Bubble Sort

Worst Case Performance: O(n^2) comparisons + O(n^2 swaps)
Best Case Performance: O(n) comparisons + O(1) swaps.
Average Performance: O(n^2) comparisons + O(n^2 swaps)

Due to its comparatively awful performances, bubble sort is a fairly impractical choice for sorting. Even on the best
case scenarios, Insertion Sort still outperforms Bubble Sort due to its low number of swaps on mostly sorted lists.

Cocktail Shaker Sort is a variation of this algorithm which sorts from either end.

## Cocktail Sort Information

Worst Case Performance: O(n^2)
Best Case Performance: O(n)
Average Performance: O(n^2)

As with Bubble Sort, this algorithm has fairly awful performances, and thus is typically of no real world use. It deals
with "turtles" (small values that travel to the front of the list) better than Bubble Sort, but has no real improvement
in performance. Again, Insertion Sort is superior in similar deployment scenarios.

## Insertion Sort Information

Worst Case Performance: O(n^2) comparisons + O(n^2 swaps)
Best Case Performance: O(n) comparisons + O(1) swaps.
Average Performance: O(n^2) comparisons + O(n^2 swaps)

Insertion sort scales very badly with a worst case performance of O(n^2) (similarly to Bubble Sort), but holds a number
of advantages over other O(n^2) algorithms:
1. Normally very simple to implement.
2. Efficient for very small data sets.
3. Adaptive - efficient with lists that are already mostly sorted.
4. Stable - doesn't sort items with equal keys
5. In-place - Requires constant memory of O(1) space.
6. Online - can sort a list when given items one at a time.

## Shell Sort Information

Worst Case Performance: O(n^2) for worst gap sequence, O(nlogn) for best known.
Best Case Performance: O(n)
Average Performance: dependant on gaps

Shell sort is an improvement/variant on Insertion Sort. Instead of comparing only adjacent values as in IS, it performs
comparisons across long gaps. The gaps change in size as the list becomes more ordered. The method used to change the
gap size has a huge impact on the average running time of the algorithm.