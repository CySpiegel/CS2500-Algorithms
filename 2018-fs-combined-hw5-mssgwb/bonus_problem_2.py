from list_to_graph import adj_list_to_graph
import collections

def bfsold(graph, s, t, parent):
	visited = [False] * graph.num_of_vertices
	queue = collections.deque()
	queue.append(s)
	visited[s] = True
	while queue:
		u = queue.popleft()
		for ind in graph.get_vertex(u).connected_to:
			val = graph.get_vertex(u).get_weight(ind)
			print(ind, val)
			if (visited[ind] == False) and (val > 0):
				queue.append(ind)
				visited[ind] = True
				parent[ind] = u
	return True if visited[t] else False

def bfs(graph, start, sink, parent):
	# print("to be implemented - BFS")
	visited = [False]*(graph.num_of_vertices)
	# parent = [0]*(graph.num_of_vertices)
	Q = []
	s = graph.get_vertex(start)
	Q.append(s)
	visited[s.get_vertex_id()] = True
	parent[s.get_vertex_id()] = -1
	while Q:
		U = Q.pop(0)
		# print(U.get_vertex_id())
		for i in U.get_connections():
			if visited[i] == False:
				visited[i] = True
				parent[i] = U.get_vertex_id()
				Q.append(graph.get_vertex(i))
	return True if visited[sink] else False

def edmonds_karp_algorithm(graph, source, sink):
	print("to be implemented - Edmonds-Karp")
	parent = [-1] * graph.num_of_vertices
	max_flow = 0
	count = 0
	while bfs(graph, source, sink, parent) and count < 100:
		path_flow = float("Inf")
		s = sink
		while s != source:
			# print("First While loop")
			path_flow = min(path_flow, graph.get_vertex(parent[s]).get_weight(s))
			s = parent[s]

		max_flow += path_flow
		v = sink
		while v !=  source:
			# print("Second while loop")
			u = parent[v]
			print("Old weight", graph.get_vertex(u).get_weight(v))
			lower_weight = graph.get_vertex(u).get_weight(v) - path_flow
			graph.get_vertex(u).add_neighbor(v, lower_weight)
			print("new weight", graph.get_vertex(u).get_weight(v))
			rais_weight = graph.get_vertex(u).get_weight(v) + path_flow
			graph.get_vertex(u).add_neighbor(v, rais_weight)
			v = parent[v]
		count += 1
	print(parent)
	for index in range(len(adj_list)):
		vertex = graph.get_vertex(index)
		print (vertex)
	return max_flow
	pass

if __name__ == "__main__":
	"""
	prob 2 represented as adj_list
	First element in tuple represents the index of the neighbor
    and second index represents the weight.

	For the purpose of this assignment, we will represent the nodes with following indices.
	s -> 0
	a -> 1
	b -> 2
	c -> 3
	d -> 4
	e -> 5
	f -> 6
	t -> 7
	"""
	adj_list = dict([
		(0, [(1,9), (2,15)]),
		(1, [(3,6), (5,6)]),
		(2, [(3,2), (6,8)]),
		(3, [(4,4)]),
		(4, [(5,3), (6,6)]),
		(5, [(7,11)]),
		(6, [(7,7)]),
		(7, [])
	])
	graph = adj_list_to_graph(adj_list)

	for index in range(len(adj_list)):
		vertex = graph.get_vertex(index)
		print (vertex)
	edmonds_karp_algorithm(graph, 0, 7)

