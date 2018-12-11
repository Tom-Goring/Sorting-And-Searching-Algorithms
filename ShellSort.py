"""
Shell Sort Information

Worst Case Performance: O(n^2) for worst gap sequence, O(nlogn) for best known.
Best Case Performance: O(n)
Average Performance: dependant on gaps

Shell sort is an improvement/variant on Insertion Sort. Instead of comparing only adjacent values as in IS, it performs
comparisons across long gaps. The gaps change in size as the list becomes more ordered. The method used to change the
gap size has a huge impact on the average running time of the algorithm.
"""
import random


def gap_insertion_sort(alist, start, gap):

    for index in range(start + gap, len(alist), gap):

        currentvalue = alist[index]
        position = index

        # find location to put new card, and swap it backwards until it gets there
        while position >= gap and alist[position - gap] > currentvalue:

            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


def shell_sort(alist):

    length = len(alist)
    gap = length//2

    while gap > 0:

        for startposition in range(gap):

            gap_insertion_sort(alist, startposition, gap)

        gap = gap // 2


rand_list = []

for i in range(100):
    rand_list.append(i)

random.shuffle(rand_list)

print(rand_list)

shell_sort(rand_list)

print(rand_list)

success = True

for index in range(len(rand_list) - 1):

    if rand_list[index] > rand_list[index + 1]:

        success = False

if success:

    print("Insertion Sort successful!")
