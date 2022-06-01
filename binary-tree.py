# #create Node:
# class Node:
#     def __init__(self,k):
#         self.left = None
#         self.right = None
#         self.key = k
#
# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.left.left = Node(40)

#Inorder
# class Node:
#     def __init__(self,k):
#         self.left = None
#         self.right = None
#         self.key = k
#
# def inorder(root):
#     if root != None:
#         inorder(root.left)
#         print(root.key)
#         inorder(root.right)
#
# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.right.left = Node(40)
# root.right.right = Node(50)
# inorder(root)

# #preorder
# class Node:
#     def __init__(self,k):
#         self.left = None
#         self.right = None
#         self.key = k
# def inorder(root):
#     if root != None:
#         print(root.key)
#         inorder(root.left)
#         inorder(root.right)
#
# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.right.left = Node(40)
# root.right.right = Node(50)
# inorder(root)

# #postorder
# class Node:
#     def __init__(self,k):
#         self.left = None
#         self.right = None
#         self.key = k
# def inorder(root):
#     if root != None:
#         inorder(root.left)
#         inorder(root.right)
#         print(root.key)
#
# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.right.left = Node(40)
# root.right.right = Node(50)
# inorder(root)

# #size of binary tree:
# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.left = None
#         self.right = None
#
# def treesize(root):
#     if root == None:
#         return 0
#
#     else:
#         return 1 + treesize(root.left) + treesize(root.right)
#
# def searchkey(root,key):
#     if root is None:
#         return False
#     elif root.key == key:
#         return True
#     elif searchkey(root.left,key):
#         return True
#     else:
#         return searchkey(root.right,key)
#
# def height(root):
#     if root == None:
#         return 0
#     else:
#         return max(height(root.left),height(root.right)) + 1
#
# root = Node(10)
# root.left = Node(20)
# root.left.left = Node(30)
# root.left.right = Node(40)
# root.right = Node(50)
# root.right.left = Node(60)
# root.right.right = Node(70)
# root.right.right.right = Node(80)
# print(treesize(root))
# print(searchkey(root,30))
# print(searchkey(root,15))
# print(height(root))

# #MAX of binary tree:
# import math
# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.left = None
#         self.right = None
#
# def getMax(root):
#     if root == None:
#         return -math.inf
#     else:
#         return max(root.key,getMax(root.left),getMax(root.right))
#
# root = Node(10)
# root.left = Node(20)
# root.left.left = Node(90)
# root.left.right = Node(40)
# root.right = Node(50)
# root.right.left = Node(60)
# root.right.right = Node(70)
# root.right.right.right = Node(80)
# print(getMax(root))

# #itrInorder of binary tree:
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
# root = Node(10)
# root.left = Node(20)
# root.left.left = Node(40)
# root.left.right = Node(50)
# root.right = Node(30)
# itrInorder(root)

# #level order
# from collections import deque
# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.left = None
#         self.right = None
#
# def printlo(root):
#     if root is None:
#         return
#     q = deque()
#     q.append(root)
#     while len(q)>0:
#         node = q.popleft()
#         print(node.key)
#         if node.left is not None:
#             q.append(node.left)
#         if node.right is not None:
#             q.append(node.right)
#
# root = Node(10)
# root.left = Node(20)
# root.left.left = Node(40)
# root.right = Node(30)
# root.right.left = Node(50)
# root.right.right = Node(60)
# root.right.left.left = Node(70)
# root.right.right.left = Node(80)
# printlo(root)

# #itrPreorder:
class Node:
    def __init__(self,k):
        self.key = k
        self.left = None
        self.right = None

def itrPreorder(root):
    if root is None:
        return

    st = [root]

    while len(st)>0:
        curr = st.pop()
        print(curr.key)
        if curr.right is not None:
            st.append(curr.right)
        if curr.left is not None:
            st.append(curr.left)

root = Node(10)
root.left = Node(20)
root.left.left = Node(40)
root.left.right = Node(50)
root.right = Node(30)
root.right.left = Node(60)
itrPreorder(root)


