"""
Insertion Sort Information

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
"""

import random


def insertion_sort(alist):

    for index in range(len(alist)):

        currentvalue = alist[index]
        position = index

        # find location to put new card, and swap it backwards until it gets there
        while position > 0 and alist[position - 1] > currentvalue:

            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue


rand_list = []

for i in range(100):
    rand_list.append(i)

random.shuffle(rand_list)

print(rand_list)

insertion_sort(rand_list)

print(rand_list)

success = True

for index in range(len(rand_list) - 1):

    if rand_list[index] > rand_list[index + 1]:

        success = False

if success:

    print("Insertion Sort successful!")
