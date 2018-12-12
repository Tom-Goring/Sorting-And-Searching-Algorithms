"""
Merge sort works by dividing a list into n sublists each of size 1, then repeatedly merging the sublists until there
is only one list remaining, which will be sorted.
"""
import random


def merge_sort(alist):

    if len(alist) > 1:

        middle = len(alist) // 2
        left = alist[:middle]
        right = alist[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # merge left and right into one sorted list
        while i < len(left) and j < len(right):

            if left[i] < right[j]:

                alist[k] = left[i]
                i += 1

            else:

                alist[k] = right[j]
                j += 1

            k += 1

        while i < len(left):

            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):

            alist[k] = right[j]
            j += 1
            k += 1


unordered_list = []

for i in range(100):

    unordered_list.append(i)

random.shuffle(unordered_list)

merge_sort(unordered_list)

print(unordered_list)

success = True

for index in range(len(unordered_list) - 1):

    if unordered_list[index] > unordered_list[index + 1]:

        success = False

if success:

    print("Merge Sort successful!")

