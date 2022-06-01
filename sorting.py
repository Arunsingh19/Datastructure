# #bubblesort(1)
# def bubble_sort(l):
#     n = len(l)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if l[j] > l[j+1]:
#                 l[j],l[j+1] = l[j+1],l[j]
#
# l = [10,8,20,5]
# bubble_sort(l)
# print(*l)

# #bubblesort(2)
# def bubble_sort(l):
#     n = len(l)
#     for i in range(n-1):
#         swapped = False
#         for j in range(n-i-1):
#             if l[j] > l[j+1]:
#                 l[j],l[j+1] = l[j+1],l[j]
#                 swapped = True
#         if swapped == False:
#             return
#
# l = [3,5,10,20,40]
# bubble_sort(l)
# print(*l)

# #selectsort
def selectSort(l):
    n = len(l)

    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):

            if l[j] < l[min_ind]:
                min_ind = j

        l[min_ind], l[i] = l[i], l[min_ind]


l = [10, 5, 8, 20, 2, 18]
selectSort(l)
print(*l)

# #merge two sorted list
# def merge(a, b):
#     res = []
#     m = len(a)
#     n = len(b)
#     i = j = 0
#     while i < m and j < n:
#         if a[i] < b[j]:
#             res.append(a[i])
#             i += 1
#         else:
#             res.append(b[j])
#             j += 1
#     while i < m:
#         res.append(a[i])
#         i += 1
#     while j < n:
#         res.append(b[j])
#         j += 1
#     return res
#
# a = [10, 15]
# b = [5, 6, 6, 30, 40]
#
# print(*merge(a, b))

# #merge subarrays
# def merge(a, low, mid, high):
#     left = a[low:mid + 1]
#     right = a[mid + 1:high + 1]
#     i = j = 0
#     k = low
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             a[k] = left[i]
#             k += 1
#             i += 1
#         else:
#             a[k] = right[j]
#             k += 1
#             j += 1
#     while i < len(left):
#         a[k] = left[i]
#         i += 1
#         k += 1
#     while j < len(right):
#         a[k] = right[j]
#         j += 1
#         k += 1
# a = [10, 15, 20, 40, 8, 11, 55]
# merge(a, 0, 3, 6)
# print(*a)

#merge sort algorithm
# def merge(a, low, mid, high):
#     left = a[low:mid + 1]
#     right = a[mid + 1:high + 1]
#
#     i = j = 0
#     k = low
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             a[k] = left[i]
#             k += 1
#             i += 1
#         else:
#             a[k] = right[j]
#             k += 1
#             j += 1
#
#     while i < len(left):
#         a[k] = left[i]
#         i += 1
#         k += 1
#
#     while j < len(right):
#         a[k] = right[j]
#         j += 1
#         k += 1
#
# def mergeSort(arr, l, r):
#     if r > l:
#         m = (r + l) // 2
#         mergeSort(arr, l, m)
#         mergeSort(arr, m + 1, r)
#         merge(arr, l, m, r)
#
# arr = [10, 5, 30, 15, 7]
#
# mergeSort(arr, 0, 4)
# print(*arr)

# #qsort using lamutopartition
# def lomutoPartition(arr, l, h):
#     pivot = arr[h]
#     i = l - 1
#     for j in range(l, h):
#         if arr[j] <= pivot:  # error
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[h] = arr[h], arr[i + 1]
#     return i + 1
#
# def qSort(arr, l, h):
#     if l < h:
#         p = lomutoPartition(arr, l, h)
#         qSort(arr, l, p - 1)
#         qSort(arr, p + 1, h)
#
# arr = [8, 4, 7, 9, 3, 10, 5]
# qSort(arr, 0, 6)
# print(*arr)