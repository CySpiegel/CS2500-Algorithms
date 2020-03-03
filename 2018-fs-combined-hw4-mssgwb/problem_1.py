from list_to_graph import adj_list_to_graph
def pPrint(parrent):
	counter = 0
	for i in parrent:
		print("Node", counter, ': predecessor', i)
		counter += 1


def bfs(start, graph):
	# print("to be implemented - BFS")
	visited = [False]*(graph.num_of_vertices)
	parrent = [0]*(graph.num_of_vertices)
	Q = []
	s = graph.get_vertex(start)
	Q.append(s)
	visited[s.get_vertex_id()] = True
	parrent[s.get_vertex_id()] = "Source"
	print("BFS Q order")
	while Q:
		U = Q.pop(0)
		print(U.get_vertex_id())
		for i in U.get_connections():
			if visited[i] == False:
				visited[i] = True
				parrent[i] = U.get_vertex_id()
				Q.append(graph.get_vertex(i))		

	# print(parrent)
	pPrint(parrent)
		

def dfs(start, graph):
	print("to be implemented - DFS")
	visited = [0]*(graph.num_of_vertices)
	parrent = [-1]*(graph.num_of_vertices)
	Q = []
	s = graph.get_vertex(start)
	Q.append(s)
	visited[s.get_vertex_id()] = 1
	parrent[s.get_vertex_id()] = "Source"
	print("DFS Q order")
	while Q:
		U = Q.pop(len(Q) - 1)
		print(U.get_vertex_id())
		for i in U.get_connections():
			if visited[i] == 0:
				Q.append(graph.get_vertex(i))
				visited[i] = 1
				parrent[i] = U.get_vertex_id()		
		visited[U.get_vertex_id()] = 1
	# print(parrent)
	pPrint(parrent)

if __name__ == "__main__":
	"""
	prob 1 represented as adj_list
	First element in tuple represents the index of the neighbor 
    and second index represents the weight.
	"""

	adj_list = dict([
		(0, [(1,1), (2,1)]),
		(1, [(0,1), (3,1), (4,1), (5,1)]),
		(2, [(0,1), (3,1), (4,1), (5,1)]),
		(3, [(1,1), (2,1), (6,1), (7,1)]),
		(4, [(1,1), (2,1), (6,1), (7,1)]),
		(5, [(1,1), (2,1), (6,1), (7,1)]),
		(6, [(3,1), (4,1), (5,1), (8,1)]),
		(7, [(3,1), (4,1), (5,1), (8,1)]),
		(8, [(6,1), (7,1)])
	])
	graph = adj_list_to_graph(adj_list)
	# print("Print Graph",graph)
	# for index in range(9):
	# 	vertex = graph.get_vertex(index)
	# 	print (vertex)
	bfs(4, graph)
	dfs(4, graph)