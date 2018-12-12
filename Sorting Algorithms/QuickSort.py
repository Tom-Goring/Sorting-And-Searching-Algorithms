"""
Quick Sort breaks down a given list into smaller sub-lists, and then these smaller lists are sorted either
recursively or iteratively until they are all sorted. All the lists are then appended into one fully sorted list.
"""
import random


def partition(a, low, high):

    i = low - 1  # index of smaller element
    pivot = a[high]

    for j in range(low, high):

        # if current value is smaller than or equal to pivot
        if a[j] <= pivot:

            i += 1  # increment index of smaller element
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def quicksort_inplace(a, low=0, high=None):

    if high is None:
        high = len(a) - 1

    if low < high:
        pivot = partition(a, low, high)
        quicksort_inplace(a, low, pivot - 1)
        quicksort_inplace(a, pivot + 1, high)


unordered_list = []

for i in range(100):

    unordered_list.append(i)

random.shuffle(unordered_list)

quicksort_inplace(unordered_list)

print(unordered_list)

success = True

for index in range(len(unordered_list) - 1):

    if unordered_list[index] > unordered_list[index + 1]:

        success = False

if success:

    print("In-place Quicksort successful!")
