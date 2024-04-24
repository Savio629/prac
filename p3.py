from collections import defaultdict 
class Graph: 
    def __init__(self):  
        self.graph = defaultdict(list) 
        self.visited = []
    def addEdge(self,u,v): 
        self.graph[u].append(v)
    def BFS(self, s): 
        queue = [] 
        queue.append(s) 
        self.visited.append(s) 
        while queue: 
            s = queue.pop(0) 
            print (s, end = " ") 
            for i in self.graph[s]: 
                if i not in self.visited: 
                    queue.append(i) 
                    self.visited.append(s) 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
g.addEdge(2, 5)
g.addEdge(1, 6)
print ("Following is Breadth First Traversal of Graph (starting from vertex 0) -") 
g.BFS(0) 
tree = Graph()
tree.addEdge(0, 1) 
tree.addEdge(0, 2) 
tree.addEdge(1, 4) 
tree.addEdge(2, 3) 
tree.addEdge(4, 5) 
print ("\nFollowing is Breadth First Traversal of Tree (starting from vertex 0) -") 
tree.BFS(0) 