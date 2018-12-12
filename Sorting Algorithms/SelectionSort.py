"""
Selection Sort picks the smallest element in the list and swaps it to the first position, then the second smallest into
the second position, etc. Selection sort is an in-place sort.
"""
import random


def selection_sort(alist):

    for i in range(len(alist)):

        min_position = i
        for j in range (i + 1, len(alist)):

            if alist[min_position] > alist[j]:

                min_position = j

        alist[i], alist[min_position] = alist[min_position], alist[i]


unordered_list = []

for i in range(100):

    unordered_list.append(i)

random.shuffle(unordered_list)

selection_sort(unordered_list)

print(unordered_list)

success = True

for index in range(len(unordered_list) - 1):

    if unordered_list[index] > unordered_list[index + 1]:

        success = False

if success:

    print("Selection Sort successful!")
