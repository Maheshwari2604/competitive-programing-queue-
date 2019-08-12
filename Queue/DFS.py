from collections import defaultdict

class graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self , u, v):
        self.graph[u].append(v)
    
    def DFS(self , u):
        visited = [False] * len(self.graph)
        self.DFSS(u , visited)

    def DFSS(self , u , visited):
        visited[u] = True
        print(u)
        for i in self.graph[u]:
            if visited[i] == False:
                self.DFSS(i , visited)


g = graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print('followinf elements are for DFS: ')
g.DFS(2)
