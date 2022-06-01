# def addEdge(adj, u, v):
#     adj[u].append(v)
#     adj[v].append(u)
#
# def printGraph(adj):
#     for u, l in enumerate(adj):
#         print(u, l)
#
# # main
# v = 4
# adj = [[] for i in range(v)]
# addEdge(adj, 0, 1)
# addEdge(adj, 0, 2)
# addEdge(adj, 1, 2)
# addEdge(adj, 1, 3)
#
# printGraph(adj)

# from collections import deque
#
# def addEdge(adj, u, v):
#     adj[u].append(v)
#     adj[v].append(u)
#
# def BFS(adj,s):
#     visited = [False]*len(adj)
#     q= deque()
#     q.append(s)
#     visited[s] = True
#
#     while q:
#         s = q.popleft()
#         print(s,end=' ')
#
#         for u in adj[s]:
#             if visited[u] == False:
#                 q.append(u)
#                 visited[u] = True
#
# def printGraph(adj):
#     for u, l in enumerate(adj):
#         print(u, l)
#
# # main
# v = 4
# adj = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [2, 3]]
# printGraph(adj)
# s=0 # starting
# print('\nBFS path')
# BFS(adj,s)

# from collections import deque
#
# def addEdge(adj, u, v):
#     adj[u].append(v)
#     adj[v].append(u)
#
# def BFS(adj, s, visited):
#     q = deque()
#     q.append(s)
#     visited[s] = True
#     while q:
#         s = q.popleft()
#         print(s, end=' ')
#         for u in adj[s]:
#             if visited[u] == False:
#                 q.append(u)
#                 visited[u] = True
#
# def BFSDis(adj):
#     visited = [False] * len(adj)
#     for u in range(len(adj)):
#         if visited[u] == False:
#             BFS(adj, u, visited)
#
# def printGraph(adj):
#     for u, l in enumerate(adj):
#         print(u, l)
#
# # main
# v = 7
# adj = [[1, 2], [0, 3], [0, 3], [1, 2], [5, 6], [4, 6], [4, 5]]
# printGraph(adj)
# print('\nBFS path')
# BFSDis(adj)

# from collections import deque
# def addEdge(adj, u, v):
#     adj[u].append(v)
#     adj[v].append(u)
#
# def BFS(adj, s, visited):
#     q = deque()
#     q.append(s)
#     visited[s] = True
#     while q:
#         s = q.popleft()
#         print(s, end=' ')
#         for u in adj[s]:
#             if visited[u] == False:
#                 q.append(u)
#                 visited[u] = True
#     print()
#
# def BFSDis(adj):
#     visited = [False] * len(adj)
#     res = 0
#     for u in range(len(adj)):
#         if visited[u] == False:
#             res+=1
#             BFS(adj, u, visited)
#     return res
#
# def printGraph(adj):
#     for u, l in enumerate(adj):
#         print(u, l)
#
# # main
# v = 8
# adj = [[1, 2], [0, 2], [0, 1], [4], [3], [6,7], [5],[5]]
# printGraph(adj)
# print('\nconnected component')
# print('no of connected component',BFSDis(adj))

# def DFSRec(adj, s, visited):
#     visited[s] = True
#     print(s, end=' ')
#     for u in adj[s]:
#         if visited[u] == False:
#             DFSRec(adj, u, visited)
# def DFS(adj, s):
#     visited = [False] * len(adj)
#     DFSRec(adj, s, visited)
# def printGraph(adj):
#     for u, l in enumerate(adj):
#         print(u, l)
# adj = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 4], [1, 3]]
# printGraph(adj)
# DFS(adj, 0)

# def DFSRec(adj, s, visited):
#     visited[s] = True
#     print(s, end=' ')
#     for u in adj[s]:
#         if visited[u] == False:
#             DFSRec(adj, u, visited)
# def DFS(adj):
#     visited = [False] * len(adj)
#     for u in range(len(adj)):
#         if visited[u] == False:
#             DFSRec(adj, u, visited)
# def printGraph(adj):
#     for u, l in enumerate(adj):
#         print(u, l)
# adj = [[1, 2], [0, 2], [0, 1], [4], [3]]
# printGraph(adj)
# DFS(adj)

def DFSRec(adj, s, visited):
    visited[s] = True
    print(s, end=' ')
    for u in adj[s]:
        if visited[u] == False:
            DFSRec(adj, u, visited)

def DFS(adj):
    visited = [False] * len(adj)
    res = 0
    for u in range(len(adj)):
        if visited[u] == False:
            res+=1
            DFSRec(adj, u, visited)
            print()
    return res

def printGraph(adj):
    for u, l in enumerate(adj):
        print(u, l)
adj = [[1, 2], [0, 2], [0, 1], [4], [3]]
printGraph(adj)
print('connected component')
print('no of connected component ',DFS(adj))