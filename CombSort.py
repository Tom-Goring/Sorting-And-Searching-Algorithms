"""
Comb sort extends Bubble Sort to solve the turtle problem. It's slightly faster on average than bubble sort. Comb
sort works by comparing elements with a gap in-between, and slowly decreasing the size of the gap as the algorithm
progresses. The final run of comb should be the same as that of bubble, albeit with greater efficiency due to the
removal of turtles.
"""
import random
from math import floor


def comb_sort(alist):

    gap = len(alist)
    shrink = 1.3
    sorted = False

    while not sorted:

        gap = floor(gap // shrink)

        if gap <= 1:

            gap = 1
            sorted = True

        i = 0

        while i + gap < len(alist):

            if alist[i] > alist[i + gap]:

                alist[i], alist[i + gap] = alist[i + gap], alist[i]
                sorted = False

            i += 1


unordered_list = []

for i in range(100):

    unordered_list.append(i)

random.shuffle(unordered_list)

comb_sort(unordered_list)

print(unordered_list)

success = True

for index in range(len(unordered_list) - 1):

    if unordered_list[index] > unordered_list[index + 1]:

        success = False

if success:

    print("Comb Sort successful!")
