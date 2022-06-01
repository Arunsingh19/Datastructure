# #
# from collections import deque
#
# d = deque()
# d.append(10)
# d.append(20)
# d.append(30)
# d.appendleft(40)
# print(d)
# print(d.pop())
# print(d.popleft())
# print(d)

# from collections import deque
#
# d = deque([10,20,30,40])
# d.insert(2,10)
# print(d.count(10))
# d.remove(10)
# print(d)
# d.extend([50,60])
# print(d)
# d.extendleft([15,25])
# print(d)

# from collections import  deque
#
# d = deque([10,20,30,40,50])
# d.rotate(2)
# print(d)
# d.rotate(-2)
# print(d)
# d.reverse()
# print(d)

# from collections import deque
#
# d = deque([10,20,30,40,50])
# print(d[2])
# d[2] = 100
# print(d)
# print(d[0])
# print(d[-1])

# from collections import deque
# class MyDS:
#     def __init__(self):
#         self.dq = deque()
#
#     def insertMin(self,x):
#         self.dq.appendleft(x)
#
#     def insertMax(self,x):
#         self.dq.append(x)
#
#     def extractMin(self):
#         return self.dq.popleft()
#
#     def extractMax(self):
#         return self.dq.pop()
#
#     def getMin(self):
#         return self.dq[0]
#
#     def getMax(self):
#         return self.dq[-1]
#
# d = MyDS()
# d.insertMin(10)
# d.insertMin(5)
# d.insertMax(20)
# d.insertMin(3)
# print(d.extractMin())
# print(d.extractMax())
# print(d.getMin())
# print(d.getMax())

# class Node:
#     def __init__(self,k):
#         self.key = k
#         self.next = None
#         self.pre = None
#
# class MyDeque:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#         self.sz = 0
#
#     def size(self):
#         return self.sz
#
#     def isEmpty(self):
#         return self.sz == 0
#
#     def insertRear(self,x):
#         temp = Node(x)
#         if self.rear == None:
#             self.front = temp
#         else:
#             self.rear.next = temp
#             temp.pre = self.rear
#         self.rear = temp
#         self.sz += 1
#
#     def deleteFront(self):
#         if self.front == None:
#             return None
#         else:
#             res = self.front.key
#             self.front = self.front.next
#             if self.front == None:
#                 self.rear = None
#             else:
#                 self.front.pre = None
#             self.sz -= 1
#             return res
#
# d = MyDeque()
# d.insertRear(10)
# d.insertRear(20)
# d.insertRear(30)
# print(d)
# print(d.isEmpty())
# d.deleteFront()
# print(d.size())

# class MyDeque:
#     def __init__(self,c):
#         self.l = [None]*c
#         self.cap = c
#         self.sz = 0
#         self.front = 0
#
#     def deleteFront(self):
#         if self.sz == 0:
#             return None
#         else:
#             res = self.l[self.front]
#             self.front = (self.front+1)%self.cap
#             self.sz = self.sz-1
#             return res
#
#     def deleteRear(self):
#         sz = self.sz
#         if sz == 0:
#             return None
#         else:
#             rear = (self.front+sz-1)%self.cap
#             self.sz -= 1
#             return self.l[rear]
#
#     def insertFront(self,x):
#         if self.sz == self.cap:
#             return
#         else:
#             self.front = (self.front-1)%self.cap
#             self.l[self.front] = x
#             self.sz = self.sz+1
#
#     def insertRear(self,x):
#         if self.sz == self.cap:
#             return
#         new_rear = (self.front + self.sz) % self.cap
#         self.l[new_rear] = x
#         self.sz += 1
#
#     def frontEle(self):
#         return self.l[self.front]
#
#     def rearEle(self):
#         rear = (self.front + self.sz - 1) % self.cap
#         return self.l[rear]
#
# dq = MyDeque(4)
# dq.insertRear(10)
# print(dq.frontEle(), dq.rearEle())
# dq.insertFront(20)
# print(dq.frontEle(), dq.rearEle())
# dq.insertFront(30)
# print(dq.frontEle(), dq.rearEle())
# dq.deleteRear()
# print(dq.frontEle(), dq.rearEle())
# dq.insertRear(40)
# print(dq.frontEle(), dq.rearEle())
# dq.deleteRear()
# print(dq.frontEle(), dq.rearEle())
