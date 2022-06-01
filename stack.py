# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack.pop())
#
# top = stack[-1]
# print(top)
#
# size = len(stack)
# print(size)

# from _collections import deque
# stack = deque()
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack.pop())
#
# top = stack[-1]
# print(top)
#
# size = len(stack)
# print(size)

# import math
#
# class Node:
#     def __init__(self,d):
#         self.data = d
#         self.next = None
#
# class MyStack:
#     def __init__(self):
#         self.head = None
#         self.sz = 0
#
#     def push(self,x):
#         temp = Node(x)
#         temp.next = self.head
#         self.head = temp
#         self.sz += 1
#
#     def size(self):
#         return self.sz
#
#     def peek(self):
#         if self.head == None:
#             return math.inf
#         return self.head.data
#
#     def pop(self):
#         if self.head == None:
#             return math.inf
#         res = self.head.data
#         self.head = self.head.next
#         self.sz -= 1
#         return res
#
# s = MyStack()
# s.push(10)
# s.push(20)
# s.push(30)
#
# print(s.pop())
#
# print(s.peek())
#
# print(s.size())

# def isMatching(a,b):
#     if(a =='(' and b == ')') or (a == '{' and b == '}') or (a =='[' and b ==']'):
#         return True
#     else:
#         return False
#
# def isBalanced(expr):
#     stack = []
#     for x in expr:
#         if x in ('(','{','['):
#             stack.append(x)
#
#         else:
#             if not stack:
#                 return False
#             elif isMatching(stack[-1],x) == False:
#                 return False
#             else:
#                 stack.pop()
#
#     if stack:
#         return False
#     else:
#         return True
#
# a = input()
# print(isBalanced(a))

# Python program to convert infix expression to postfix

# Class to convert the expression

#
# class Conversion:
#
# 	# Constructor to initialize the class variables
# 	def __init__(self, capacity):
# 		self.top = -1
# 		self.capacity = capacity
# 		# This array is used a stack
# 		self.array = []
# 		# Precedence setting
# 		self.output = []
# 		self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
#
# 	# check if the stack is empty
# 	def isEmpty(self):
# 		return True if self.top == -1 else False
#
# 	# Return the value of the top of the stack
# 	def peek(self):
# 		return self.array[-1]
#
# 	# Pop the element from the stack
# 	def pop(self):
# 		if not self.isEmpty():
# 			self.top -= 1
# 			return self.array.pop()
# 		else:
# 			return "$"
#
# 	# Push the element to the stack
# 	def push(self, op):
# 		self.top += 1
# 		self.array.append(op)
#
# 	# A utility function to check is the given character
# 	# is operand
# 	def isOperand(self, ch):
# 		return ch.isalpha()
#
# 	# Check if the precedence of operator is strictly
# 	# less than top of stack or not
# 	def notGreater(self, i):
# 		try:
# 			a = self.precedence[i]
# 			b = self.precedence[self.peek()]
# 			return True if a <= b else False
# 		except KeyError:
# 			return False
#
# 	# The main function that
# 	# converts given infix expression
# 	# to postfix expression
# 	def infixToPostfix(self, exp):
#
# 		# Iterate over the expression for conversion
# 		for i in exp:
# 			# If the character is an operand,
# 			# add it to output
# 			if self.isOperand(i):
# 				self.output.append(i)
#
# 			# If the character is an '(', push it to stack
# 			elif i == '(':
# 				self.push(i)
#
# 			# If the scanned character is an ')', pop and
# 			# output from the stack until and '(' is found
# 			elif i == ')':
# 				while((not self.isEmpty()) and
# 					self.peek() != '('):
# 					a = self.pop()
# 					self.output.append(a)
# 				if (not self.isEmpty() and self.peek() != '('):
# 					return -1
# 				else:
# 					self.pop()
#
# 			# An operator is encountered
# 			else:
# 				while(not self.isEmpty() and self.notGreater(i)):
# 						# this is to pass cases like a^b^c
# 					# without if ab^c^
# 					# with if abc^^
# 					if i == "^" and self.array[-1] == i:
# 						break
# 					self.output.append(self.pop())
# 				self.push(i)
#
# 		# pop all the operator from the stack
# 		while not self.isEmpty():
# 			self.output.append(self.pop())
# 			print("".join(self.output))
#
#
# # Driver program to test above function
# exp = "a+b*(c^d-e)^(f+g*h)-i"
# obj = Conversion(len(exp))
# obj.infixToPostfix(exp)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
