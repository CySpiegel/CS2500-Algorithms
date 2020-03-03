from list_to_graph import adj_list_to_graph
import heapq

def dijkstra_algorithm(graph, start):
	print("to be implemented - Dijkstra")
	Q = []
	for i in graph.get_vertices():
		u = graph.get_vertex(i)
		u.set_key(9999999999)
		u.set_pred(None)
	T = []
	r = graph.get_vertex(start)
	r.set_key(0)
	heapq.heappush(Q, (r.get_key(), r.vertex_id))
	while Q:
		u = heapq.heappop(Q)
		# T.append(u[1])
		for v in graph.get_vertex(u[1]).connected_to:
			nextVertex = graph.get_vertex(v)
			previousVertex = graph.get_vertex(u[1])
			if  v not in T and previousVertex.get_weight(v) + previousVertex.get_key() < nextVertex.get_key():
				nextVertex.set_key(previousVertex.get_weight(v) + previousVertex.get_key())
				nextVertex.set_pred(u[1])
				heapq.heappush(Q, (nextVertex.get_key(), v))
	pass

if __name__ == "__main__":
	"""
	prob 1 represented as adj_list
	First element in tuple represents the index of the neighbor
    and second index represents the weight.
	"""
	adj_list = dict([
		(0, [(1,3), (3,2)]),
		(1, [(2,1), (7,2)]),
		(2, [(5,2)]),
		(3, [(2,2), (5,4), (6,3)]),
		(4, [(1,3)]),
		(5, [(4,2), (8,1)]),
		(6, [(8,5)]),
		(7, [(4,1), (9,4)]),
		(8, [(9,2)]),
		(9, [])
	])
	graph = adj_list_to_graph(adj_list)

	for index in range(len(adj_list)):
		vertex = graph.get_vertex(index)
		print (vertex)
	dijkstra_algorithm(graph, 0)

	for i in graph.get_vertices():
		print("Vertex:", i, "Predecessor", graph.get_vertex(i).get_pred())
	print("End of Line")
