"""
Bubble Sort Information

Worst Case Performance: O(n^2) comparisons + O(n^2 swaps)
Best Case Performance: O(n) comparisons + O(1) swaps.
Average Performance: O(n^2) comparisons + O(n^2 swaps)

Due to its comparatively awful performances, bubble sort is a fairly impractical choice for sorting. Even on the best
case scenarios, Insertion Sort still outperforms Bubble Sort due to its low number of swaps on mostly sorted lists.

Cocktail Shaker Sort is a variation of this algorithm which sorts from either end.
"""

import random


def bubble_sort(alist):

    swaps = 1

    while swaps:

        swaps = 0

        for index in range(len(alist) - 1):

            if alist[index] > alist[index + 1]:

                alist[index], alist[index + 1] = alist[index + 1], alist[index]
                swaps += 1


unordered_list = []

for i in range(100):

    unordered_list.append(i)

random.shuffle(unordered_list)


bubble_sort(unordered_list)


print(unordered_list)

success = True

for index in range(len(unordered_list) - 1):

    if unordered_list[index] > unordered_list[index + 1]:

        success = False

if success:

    print("Bubble Sort successful!")
