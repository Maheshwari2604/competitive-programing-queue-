from collections import defaultdict 

#from collections import defaultdict
# This class represents a directed graph 
# using adjacency list representation 

class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list)
        print(self.graph)
  
    # function to add an edge to graph 
    def addEdge(self,u,v):
        print(u+v)
        #   self.graph[u].append(v)
        a = self.graph[u].append(v)
        print(self.graph[u].append(v))
        print(self.graph)

    # Function to print a BFS of graph 
    
    def BFS(self, s): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph))
        print(visited) 
  
        # Create a queue for BFS 
        queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s) 
        print(queue)
        visited[s] = True
        print(visited)
  
        while queue: 
  
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
            print(s) 
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            print(self.graph[s])
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i)
                    print(queue) 
                    visited[i] = True
                    print(visited)
  
# Driver code 
  
# Create a graph given in 
# the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.BFS(2) 
