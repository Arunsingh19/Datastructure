# # circular list
# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.next = None
#
# def printcircular(head):
#     if head == None:
#          return head
#     print(head.key,end = " ")
#     curr = head.next
#     while curr != head:
#         print(curr.key,end=" ")
#         curr = curr.next
#
# # Driver code
# # head = None
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(15)
# head.next.next.next = Node(30)
# head.next.next.next.next = head
# printcircular(head)

# #insert at the begining o(n)
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# def insertBeg(head, x):
#     temp = Node(x)
#     if head == None:
#         temp.next = temp
#         return temp
#     curr = head
#     while curr.next != head:
#         curr = curr.next
#     curr.next = temp
#     temp.next = head
#     return temp
#
# def printCircular(head):
#     if head == None:
#         return
#     print(head.data, end=" ")
#     curr = head.next
#     while curr != head:
#         print(curr.data, end=" ")
#         curr = curr.next
#     print()
#
# head = Node(20)
# head.next = Node(30)
# head.next.next = Node(40)
# head.next.next.next = head
# printCircular(head)
#
# head = insertBeg(head, 10)
#
# printCircular(head)

# #constant time
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# def insertBeg(head, x):
#     temp = Node(x)
#     if head == None:
#         temp.next = temp
#         return  temp
#     else:
#         temp.next = head.next
#         head.next = temp
#
#         head.data,temp.data = temp.data,head.data
#         return head
#
# def printCircular(head):
#     if head == None:
#         return
#     print(head.data, end=" ")
#     curr = head.next
#     while curr != head:
#         print(curr.data, end=" ")
#         curr = curr.next
#     print()
#
# head = Node(15)
# head.next = Node(20)
# head.next.next = Node(25)
# head.next.next.next = head
# printCircular(head)
#
# head = insertBeg(head, 10)
#
# printCircular(head)

# #delete at the begining(1)
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# def deleteBeg(head):
#     if head == None:
#         return None
#     elif head.next == head:
#         return None
#
#     curr = head
#     while curr.next != head:
#         curr = curr.next
#     curr.next = head.next
#     return curr.next
#
# def printCircular(head):
#     if head == None:
#         return
#     print(head.data, end=" ")
#     curr = head.next
#     while curr != head:
#         print(curr.data, end=" ")
#         curr = curr.next
#     print()
#
# head = Node(15)
# head.next = Node(20)
# head.next.next = Node(25)
# head.next.next.next = head
# printCircular(head)
#
# head = deleteBeg(head)
#
# printCircular(head)

# #delete at the begining(2)
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# def deleteBeg(head):
#     if head == None:
#         return None
#     elif head.next == head:
#         return None
#     else:
#         head.data = head.next.data
#         head.next = head.next.next
#         return head
# def printCircular(head):
#     if head == None:
#         return
#     print(head.data, end=" ")
#     curr = head.next
#     while curr != head:
#         print(curr.data, end=" ")
#         curr = curr.next
#     print()
#
# head = Node(15)
# head.next = Node(20)
# head.next.next = Node(25)
# head.next.next.next = head
# printCircular(head)
# head = deleteBeg(head)
# printCircular(head)

# #delete at the k th node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteBeg(head):
    if head == None:
        return None
    elif head.next == head:
        return None
    else:
        head.data = head.next.data
        head.next = head.next.next
        return head

def delkth(head,k):
    if head == None:
        return head
    elif k == 1:
        return deleteBeg(head)
    else:
        curr = head
        for i in range(k-2):
            curr = curr.next
        curr.next = curr.next.next
        return head

def printCircular(head):
    if head == None:
        return
    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next
    print()

head = Node(15)
head.next = Node(20)
head.next.next = Node(25)
head.next.next.next= Node(30)
head.next.next.next.next = head
printCircular(head)
head = delkth(head,3)
printCircular(head)







