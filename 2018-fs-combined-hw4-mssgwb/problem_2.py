from matrix_to_graph import adj_matrix_to_graph
import queue as queue
import heapq 


def prims_algorithm(graph, start):
	print("to be implemented - Prim's algorithm")
	Q = []
	for i in graph.get_vertices():
		u = graph.get_vertex(i)
		u.set_key(9999999999)
		u.set_pred(None)
		heapq.heappush(Q, (u.get_key(), u.vertex_id))
	T = []
	r = graph.get_vertex(start)
	r.set_key(0)
	heapq.heappush(Q, (r.get_key(), r.vertex_id))
	while Q:
		u = heapq.heappop(Q)
		T.append(u[1])
		for v in graph.get_vertex(u[1]).connected_to:
			nextVertex = graph.get_vertex(v)
			previousVertex = graph.get_vertex(u[1])
			if v not in T and previousVertex.get_weight(v) < nextVertex.get_key():
				nextVertex.set_key(previousVertex.get_weight(v))
				nextVertex.set_pred(u[1])
				heapq.heappush(Q, (nextVertex.get_key(), v))
	pass


def kruskal_algorithm(graph):
	print("to be implemented - Kruskal's algorithm")
	pass


if __name__ == "__main__":
	"""
	prob 2 represented as adj_matrix
	Each entry in the following matrix represents the weight of the connecting edge.
	If there is no edge, it is represents by 0.
	"""
	adj_matrix = [
		[0, 3, 0, 0, 3, 1, 0, 0, 0, 0],  
		[3, 0, 3, 0, 0, 0, 1, 0, 0, 0],  
		[0, 3, 0, 3, 0, 0, 0, 1, 0, 0],  
		[0, 0, 3, 0, 3, 0, 0, 0, 1, 0],  
		[3, 0, 0, 3, 0, 0, 0, 0, 0, 1],  
		[1, 0, 0, 0, 0, 0, 0, 2, 2, 0],  
		[0, 1, 0, 0, 0, 0, 0, 0, 2, 2],  
		[0, 0, 1, 0, 0, 2, 0, 0, 0, 2],  
		[0, 0, 0, 1, 0, 2, 2, 0, 0, 0],  
		[0, 0, 0, 0, 1, 0, 2, 2, 0, 0]
	]

	graph = adj_matrix_to_graph(adj_matrix)

	# for index in range(len(adj_matrix)):
	# 	vertex = graph.get_vertex(index)
	# 	print (vertex)
	prims_algorithm(graph, 0)
	kruskal_algorithm(graph)
	v = graph.get_vertex(0)
	v.set_key(42)
	
	for i in graph.get_vertices():
		print("Vertex:", i, "Predecessor", graph.get_vertex(i).get_pred())
	print("End of Line")