"""
Cocktail Sort Information

Worst Case Performance: O(n^2)
Best Case Performance: O(n)
Average Performance: O(n^2)

As with Bubble Sort, this algorithm has fairly awful performances, and thus is typically of no real world use. It deals
with "turtles" (small values that travel to the front of the list) better than Bubble Sort, but has no real improvement
in performance. Again, Insertion Sort is superior in similar deployment scenarios.
"""

import random


def cocktail_sort(alist):

    while True:

        swapped = False

        for i in range(len(alist) - 2):

            if alist[i] > alist[i + 1]:

                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                swapped = True

        for i in range(len(alist) - 2, -1, -1):

            if alist[i] > alist[i + 1]:

                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                swapped = True

        if not swapped:

            break


rand_list = []

for i in range(100):
    rand_list.append(i)

random.shuffle(rand_list)

print(rand_list)

cocktail_sort(rand_list)

print(rand_list)

success = True

for index in range(len(rand_list) - 1):

    if rand_list[index] > rand_list[index + 1]:

        success = False

if success:

    print("Cocktail Sort successful!")
