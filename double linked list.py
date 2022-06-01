
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None
#
# def printlist(head):
#     curr = head
#     while curr != None:
#         print(curr.data,end=" ")
#         curr = curr.next
#
# head = Node(10)
# temp1 = Node(20)
# temp2 = Node(30)
# temp3 = Node(40)
# head.next = temp1
# temp1.prev = head
# temp1.next = temp2
# temp2.prev = temp1
# temp3.prev = temp2
# temp2.next = temp3
# printlist(head)

# #insert at the begining
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None
#
# def insertBegin(head,x):
#     temp = Node(x)
#     if head != None:
#         head.prev = temp
#         temp.next = head
#     return temp
#
# def printlist(head):
#     curr = head
#     while curr != None:
#         print(curr.data,end=" ")
#         curr = curr.next
#
# head = None
# head = insertBegin(head,10)
# head = insertBegin(head,20)
# head = insertBegin(head,30)
# head = insertBegin(head,40)
# printlist(head)

# #insert at the end
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None
#
# def insertEnd(head,x):
#     if head == None:
#         return Node(x)
#     curr = head
#     while curr.next != None:
#         curr = curr.next
#     temp = Node(x)
#     curr.next = temp
#     temp.prev = curr
#     return head
#
# def printlist(head):
#     curr = head
#     while curr != None:
#         print(curr.data,end=" ")
#         curr = curr.next
#
# head = None
# head = insertEnd(head,10)
# head = insertEnd(head,20)
# head = insertEnd(head,30)
# head = insertEnd(head,40)
# head = insertEnd(head,50)
# printlist(head)

# #delete at the beginning
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None
#
# def delBegin(head):
#     if head == None:
#         return None
#     if head.next == None:
#         return None
#     else:
#         head = head.next
#         head.prev = None
#         return head
#
# def printlist(head):
#     curr = head
#     while curr != None:
#         print(curr.data,end=" ")
#         curr = curr.next
#     print()
#
# head = Node(10)
# temp1 = Node(20)
# temp2 = Node(30)
# temp3 = Node(40)
# head.next = temp1
# temp1.prev = head
# temp1.next = temp2
# temp2.prev = temp1
# temp3.prev = temp2
# temp2.next = temp3
# printlist(head)
# head = delBegin(head)
# printlist(head)

# #delete at the end
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None
#
# def delEnd(head):
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
# def printlist(head):
#     curr = head
#     while curr != None:
#         print(curr.data,end=" ")
#         curr = curr.next
#     print()
#
# head = Node(10)
# temp1 = Node(20)
# temp2 = Node(30)
# temp3 = Node(40)
# head.next = temp1
# temp1.prev = head
# temp1.next = temp2
# temp2.prev = temp1
# temp3.prev = temp2
# temp2.next = temp3
# printlist(head)
# head = delEnd(head)
# printlist(head)







