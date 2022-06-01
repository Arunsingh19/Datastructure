# #iteration
# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.left = None
#         self.right = None
#
# def itrInorder(root):
#     if root is None:
#         return
#     st = []
#     curr = root
#     while curr is not None:
#         st.append(curr)
#         curr = curr.left
#     while len(st)>0:
#         curr = st.pop()
#         print(curr.key)
#         curr = curr.right
#         while curr is not None:
#             st.append(curr)
#             curr = curr.left
#
# def bSearch(l, x):
#     low = 0
#     high = len(l) - 1
#
#     while low <= high:
#
#         mid = (low + high) // 2
#         if l[mid] == x:
#             return mid
#         elif l[mid] < x:
#             low = mid + 1
#
#         else:
#             high = mid - 1
#
#     return -1
#
# l = [10, 20, 30, 40, 50, 60]
#
# print(30, bSearch(l, 30))
# print(20, bSearch(l, 20))
# print(10, bSearch(l, 10))
# print(60, bSearch(l, 60))
# print(40, bSearch(l, 40))
# print(55, bSearch(l, 55))
# print(-50, bSearch(l, -50))

# #recursion
# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.left = None
#         self.right = None
#
# def itrInorder(root):
#     if root is None:
#         return
#     st = []
#     curr = root
#     while curr is not None:
#         st.append(curr)
#         curr = curr.left
#     while len(st)>0:
#         curr = st.pop()
#         print(curr.key)
#         curr = curr.right
#         while curr is not None:
#             st.append(curr)
#             curr = curr.left
#
# def bSearch(l, x, low, high):
#     if low > high:
#         return -1
#
#     mid = (low + high) // 2
#     if l[mid] == x:
#         return mid
#
#     elif l[mid] > x:
#         return bSearch(l, x, low, mid - 1)
#
#     else:
#         return bSearch(l, x, mid + 1, high)
#
#
# def bSearchMain(l, x):
#     return bSearch(l, x, 0, len(l) - 1)
#
#
# l = [10, 20, 30, 40, 50, 60]
#
# print(30, bSearchMain(l, 30))
# print(20, bSearchMain(l, 20))
# print(10, bSearchMain(l, 10))
# print(60, bSearchMain(l, 60))
# print(40, bSearchMain(l, 40))
# print(55, bSearchMain(l, 55))
# print(-50, bSearchMain(l, -50))

# #first occurence
class Node:
    def __init__(self,k):
        self.key = k
        self.left = None
        self.right = None

def itrInorder(root):
    if root is None:
        return
    st = []
    curr = root
    while curr is not None:
        st.append(curr)
        curr = curr.left
    while len(st)>0:
        curr = st.pop()
        print(curr.key)
        curr = curr.right
        while curr is not None:
            st.append(curr)
            curr = curr.left

def firstIndex(l, x):
    low = 0

    high = len(l) - 1

    while low <= high:

        mid = (low + high) // 2

        if l[mid] > x:
            high = mid - 1
        elif l[mid] < x:
            low = mid + 1

        else:
            if mid == 0 or l[mid - 1] != l[mid]:
                return mid
            else:
                high = mid - 1
    return -1


l = [5, 10, 10, 20, 20]

print(10, firstIndex(l, 10))
print(20, firstIndex(l, 20))
print(50, firstIndex(l, 50))

# #count occurence
# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.left = None
#         self.right = None
#
# def itrInorder(root):
#     if root is None:
#         return
#     st = []
#     curr = root
#     while curr is not None:
#         st.append(curr)
#         curr = curr.left
#     while len(st)>0:
#         curr = st.pop()
#         print(curr.key)
#         curr = curr.right
#         while curr is not None:
#             st.append(curr)
#             curr = curr.left
#
# def firstIndex(l, x):
#     low = 0
#
#     high = len(l) - 1
#
#     while low <= high:
#
#         mid = (low + high) // 2
#
#         if l[mid] > x:
#             high = mid - 1
#         elif l[mid] < x:
#             low = mid + 1
#
#         else:
#             if mid == 0 or l[mid - 1] != l[mid]:
#                 return mid
#             else:
#                 high = mid - 1
#     return -1
#
#
# def lastOccur(l, x):
#     low = 0
#     high = len(l) - 1
#
#     while low <= high:
#
#         mid = (low + high) // 2
#
#         if l[mid] < x:
#             low = mid + 1
#
#         elif l[mid] > x:
#             high = mid - 1
#
#         else:
#
#             if mid == len(l) - 1 or l[mid] != l[mid + 1]:
#                 return mid
#             else:
#                 low = mid + 1
#     return -1
#
#
# def countOccurr(l, x):
#     first = firstIndex(l, x)
#
#     if first == -1:
#         return 0
#
#     else:
#         return lastOccur(l, x) - first + 1
#
#
# l = [10, 20, 20, 20, 30, 30]
#
# print(10, countOccurr(l, 10))
# print(20, countOccurr(l, 20))
# print(30, countOccurr(l, 30))
# print(25, countOccurr(l, 25))