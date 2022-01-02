from collections import defaultdict
  
# function for adding edge to graph
graph = defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)



print("Enter number of vertices and edges: ")
v = int(input("Vertices: "))
e = int(input("Edges: "))

# edges = [[0,1],[1,2],[2,3]]
print("Enter edges: ")
for i in range(e):
	x = int(input("Starting node: "))
	y = int(input("Ending node: "))
	print("Next Edge..")
	addEdge(graph,x,y)

for i in range(len(graph)+1):
	print(i, " -> ",graph[i])
	

