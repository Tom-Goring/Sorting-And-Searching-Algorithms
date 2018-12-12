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
        # k keeps track of what slot in alist we are putting an element into
        # i keeps track of what slot in left we are currently comparing
        # j keeps track of what slot in right we are currently comparing

        # iterate through left and right one item at a time, constantly putting the smallest value from between the two
        # into the leftmost slot of alist
        while i < len(left) and j < len(right):

            # if the latest item being considered from left is smaller than the latest item on the right, we add it to
            # the current slot being vied for in alist, else we add the one from right.
            if left[i] < right[j]:

                alist[k] = left[i]
                i += 1

            else:

                alist[k] = right[j]
                j += 1

            k += 1

        # now we add all remaining items from left into alist
        while i < len(left):

            alist[k] = left[i]
            i += 1
            k += 1

        # and the same from right
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

