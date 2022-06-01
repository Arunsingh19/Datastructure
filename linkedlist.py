# # 1.simple linked list
# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.next = None
#
# def printlist(head):
#     curr = head
#     while curr != None:
#         print(curr.key,end=" ")
#         curr = curr.next
#
# # Driver code
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(15)
# head.next.next.next = Node(30)
# printlist(head)

# # 2.search in linked list
# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.next = None
#
# def search(head,x):
#     pos = 1
#     curr =head
#     while curr != None:
#         if curr.key == x:
#             print(pos)
#         pos = pos+1
#         curr = curr.next
# # Driver code
# head = Node(10)
# head.next = Node(15)
# head.next.next = Node(20)
# head.next.next.next = Node(25)
# x=20
# search(head,x)

# # 3.insert at the beginning
# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.next = None
#
# def insertBegin(head,key):
#     temp = Node(key)
#     temp.next = head
#     return temp
#
# def printlist(head):
#     curr = head
#     while curr != None:
#         print(curr.key,end=" ")
#         curr = curr.next
# # Driver code
# head = None
# head = insertBegin(head,10)
# head = insertBegin(head,20)
# head = insertBegin(head,30)
# printlist(head)

# #4. insert at the end
# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.next = None
#
# def insertEnd(head,key):
#     if head == None:
#         return Node(key)
#     curr = head
#     while curr.next != None:
#         curr = curr.next
#     curr.next = Node(key)
#     return head
#
# def printlist(head):
#     curr = head
#     while curr != None:
#         print(curr.key,end=" ")
#         curr =curr.next
#
# # Driver code
# head = None
# head = insertEnd(head,10)
# head = insertEnd(head,20)
# head = insertEnd(head,30)
# head = insertEnd(head,40)
# printlist(head)

# # #5.insert at given position in singly linked list
# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.next = None
#
# def insertPos(head, data, pos):
#     temp = Node(data)
#     if pos == 1:
#         temp.next = head
#         return temp
#     curr = head
#     for i in range(pos-2):
#         curr = curr.next
#         if curr == None:
#             return head
#     temp.next = curr.next
#     curr.next = temp
#     return head
#
# def printlist(head):
#     curr = head
#     while curr != None:
#         print(curr.key,end=" ")
#         curr = curr.next
# # Driver code
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# head.next.next.next.next = Node(50)
# data = 45
# pos = 2
# head = insertPos(head,data,pos)
# printlist(head)
# head = None
# data = 10
# pos = 1
# head = insertPos(head,data,pos)
# data = 20
# pos = 2
# head = insertPos(head,data,pos)
# data = 30
# pos = 3
# head = insertPos(head,data,pos)
# data = 40
# pos = 4
# head = insertPos(head,data,pos)
# data = 45
# pos = 4
# head = insertPos(head,data,pos)
# printlist(head)

# # #6.delete first node of the linked list
# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.next = None
#
# def delfirst(head):
#     if head == None:
#         return None
#     else:
#         return head.next
# def printlist(head):
#     curr = head
#     while curr != None:
#         print(curr.key,end=" ")
#         curr = curr.next
# # #Driver code
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# head = delfirst(head)
# printlist(head)

# #7.Delete last node of linked list
# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.next = None
#
# def delLastNode(head):
#     if head == None:
#         return None
#     if head.next == None:
#         return None
#     curr = head
#     while curr.next.next != None:
#         curr = curr.next
#     curr.next = None
#     return head
#
# def printList(head):
#     curr = head
#     while curr != None:
#         print(curr.key,end=" ")
#         curr = curr.next
#
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# head = delLastNode(head)
# printList(head)

# #8.sorted insert for linked list
# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.next = None
#
# def sortedInsert(head,x):
#     temp = Node(x)
#     if head == None:
#         return temp
#     elif x < head.key:
#         temp.next = head
#         return temp
#     else:
#         curr = head
#         while curr.next != None and curr.next.key < x:
#             curr = curr.next
#         temp.next = curr.next
#         curr.next = temp
#         return head
#
# def printlist(head):
#     curr = head
#     while curr != None:
#         print(curr.key,end=" ")
#         curr = curr.next
# Driver code
# head = Node(10)
# head.next = Node(15)
# head.next.next = Node(20)
# head.next.next.next = Node(30)
# x = 25
# # head = None
# # x = 10
# # head = sortedInsert(head,x)
# # head = sortedInsert(head,5)
# # head = sortedInsert(head,15)
# # head = sortedInsert(head,2)
# # head = sortedInsert(head,27)
# printlist(head)

# # # 9.Reverse a linked list
# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.next = None
#
# def reverselist(head):
#     stack = []
#     curr = head
#     while curr is not None:
#         stack.append(curr.key)
#         curr = curr.next
#     curr = head
#     while curr is not None:
#         curr.key = stack.pop()
#         curr = curr.next
#     return head
#
# def printlist(head):
#     curr = head
#     while curr != None:
#         print(curr.key,end=" ")
#         curr = curr.next
#
# # Driver code
# # head = None
# head = Node(10)
# head.next = Node(15)
# head.next.next = Node(20)
# head.next.next.next = Node(30)
# printlist(head)
# print()
# head = reverselist(head)
# printlist(head)

# # 10.Reverse a linked list(efficient solution)
# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.next = None
#
# def reverseList(head):
#    curr = head
#    prev = None
#    while curr != None:
#        next = curr.next
#        curr.next = prev
#        prev = curr
#        curr = next
#    return prev
#
# def printlist(head):
#     curr = head
#     while curr != None:
#         print(curr.key,end=" ")
#         curr = curr.next
# # Driver code
# # head = None
# head = Node(10)
# head.next = Node(15)
# head.next.next = Node(20)
# head.next.next.next = Node(30)
# printlist(head)
# print()
# head = reverseList(head)
# printlist(head)

# #recursion (reverse)
# class Node:
#     def __init__(self, k):
#         self.key = k
#         self.next = None
#
# def reverseList(head):
#     if head == None:
#         return head
#
#     if head.next == None:
#         return head
#
#     rest_head = reverseList(head.next)
#     rest_tail = head.next
#     rest_tail.next = head
#     head.next = None
#
#     return rest_head
#
# def printList(head):
#     curr = head
#     while curr != None:
#         print(curr.key, end=" ")
#         curr = curr.next
#     print()
#
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
#
# printList(head)
#
# head = reverseList(head)
#
# printList(head)

# class Node:
#     def __init__(self, k):
#         self.key = k
#         self.next = None
#
# def reverseList(curr,prev = None):
#     if curr == None:
#         return prev
#
#     next = curr.next
#     curr.next = prev
#
#     return reverseList(next,curr)
#
# def printList(head):
#     curr = head
#     while curr != None:
#         print(curr.key, end=" ")
#         curr = curr.next
#     print()
#
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
#
# printList(head)
#
# head = reverseList(head)
#
# printList(head)

