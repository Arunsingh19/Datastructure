# #recursion
# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.left = None
#         self.right = None
#
# def searchBST(root,key):
#     if root is None:
#         return False
#     elif root.key == key:
#         return True
#     elif root.key>key:
#         return searchBST(root.left,key)
#     else:
#         return searchBST(root.right,key)
#
# root = Node(10)
# root.left = Node(5)
# root.left.left = Node(2)
# root.right = Node(30)
# root.right.left = Node(25)
# root.right.right = Node(40)
# print(searchBST(root,40))

# #iteration
# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.left = None
#         self.right = None
#
# def searchBST(root,key):
#     while root != None:
#         if root.key == key:
#             return True
#         elif root.key>key:
#             root = root.left
#         else:
#             root = root.right
#     return False
#
# root = Node(10)
# root.left = Node(5)
# root.left.left = Node(2)
# root.right = Node(30)
# root.right.left = Node(25)
# root.right.right = Node(40)
# print(searchBST(root,40))

# #insert(recursion)
# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.left = None
#         self.right = None
#
# def insert(root, key):
#     if root == None:
#         return Node(key)
#     elif root.key == key:
#         return root
#     elif root.key > key:
#         root.left = insert(root.left, key)
#     else:
#         root.right = insert(root.right, key)
#     return root
#
# # root = Node(10)
# # root.left = Node(5)
# # root.right = Node(20)
# # root.right.left = Node(15)
# # root.right.right = Node(30)
# # print(insert(root,7))
# root = None
# root = insert(root, 10)
# root = insert(root, 20)
# root = insert(root, 5)
# print(insert(root,7))

# #insert(iteration)
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
# def insert(root, key):
#     parent = None
#     curr = root
#     while curr != None:
#         parent = curr
#         if curr.key == key:
#             return root
#         elif curr.key<key:
#             curr = curr.left
#         else:
#             curr = curr.right
#     if parent == None:
#         return Node(key)
#     if parent.key > key:
#         parent.left = Node(key)
#     else:
#         parent.right = Node(key)
#     return root
#
# # root = Node(10)
# # root.left = Node(5)
# # root.right = Node(20)
# # root.right.left = Node(15)
# # root.right.right = Node(30)
# # print(insert(root,7))
# root = None
# root = insert(root, 10)
# root = insert(root, 20)
# root = insert(root, 5)
# print(itrInorder(root))

# #delete node
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
# def getSucc(curr, key):
#     while curr.left != None:
#         curr = curr.left
#     return curr.key
#
# def delNode(root, key):
#     if root == None:
#         return
#     if root.key > key:
#         root.left = delNode(root.left, key)
#     elif root.key < key:
#         root.right = delNode(root.right, key)
#     else:
#         if root.left == None:
#             return root.right
#         elif root.right == None:
#             return root.left
#         else:
#             succ = getSucc(root.right,key)
#             root.key = succ
#             root.right = delNode(root.right, succ)
#     return root
#
# # root = Node(10)
# # root.left = Node(5)
# # root.right = Node(20)
# # root.right.left = Node(15)
# # root.right.right = Node(30)
# # print(insert(root,7))
# root = Node(10)
# root.left = Node(5)
# root.right = Node(20)
# root.right.left = Node(18)
# root.right.right = Node(100)
#
# root = delNode(root,20)
#
# print(itrInorder(root))








