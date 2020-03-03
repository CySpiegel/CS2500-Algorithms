from edge import Edge
from vertex import Vertex


class DirectedGraph(object):
	def __init__(self, num_of_vertices):
		"""
		num_of_vertices - stores number of vertices in graph.
		vertex_list - dictionary of all vertices and edges.
		"""
		self.num_of_vertices = num_of_vertices
		self.vertex_list = {}
		for index in range(self.num_of_vertices):
			new_vertex = Vertex(index)
			self.vertex_list[index] = new_vertex

	def get_vertex(self, index):
		return self.vertex_list.get(index)

	def connect_edges(self, edge):
		#add to vertex_list
		self.vertex_list[edge.vertex1].add_neighbor(edge.vertex2, edge.weight)
		# self.vertex_list[edge.vertex2].add_neighbor(edge.vertex1, edge.weight)

	def get_vertices(self):
		return self.vertex_list.keys()

	def get_vertex_list(self):
		return self.vertex_list


if __name__ == "__main__":
	graph = DirectedGraph(6)
	graph.connect_edges(Edge(0,1,5))
	graph.connect_edges(Edge(0,5,2))
	graph.connect_edges(Edge(1,2,4))
	graph.connect_edges(Edge(2,3,9))
	graph.connect_edges(Edge(3,4,7))
	graph.connect_edges(Edge(3,5,3))
	graph.connect_edges(Edge(4,0,1))
	graph.connect_edges(Edge(5,4,8))
	graph.connect_edges(Edge(5,2,1))

	#code to test a random vertex
	random_vertex = graph.get_vertex(2) #get vertex by index
	print(random_vertex)
	print(random_vertex.get_vertex_id()) #print vertex's id.
	print("Neighbors :" , random_vertex.get_connections()) #print neighbors.
	print(random_vertex.get_weight(4)) #print weight on neighbor with index 4.
