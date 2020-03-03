class Vertex(object):
	def __init__(self, id):
		self.vertex_id = id
		self.connected_to = {}
		self.key = 99999999
		self.pred = -1
	
	def get_key(self):
		return self.key

	def set_key(self, newKey):
		self.key = newKey
	
	def set_pred(self, newPred):
		self.pred = newPred
	
	def get_pred(self):
		return self.pred
	
	def add_neighbor(self, neighboring_vertex, weight=1):
		self.connected_to[neighboring_vertex] = weight
	
	def __repr__(self):
		return 'Vertex : %s, Neighbors : %s' % (self.vertex_id, self.connected_to)

	def get_connections(self):
		return self.connected_to.keys()

	def get_vertex_id(self):
		return self.vertex_id
	
	def get_weight(self, neighboring_vertex):
		"""
		Returns the weight on the edge, given a neighboring vertex.
		If no vertex is found, returns None.
		"""
		return self.connected_to.get(neighboring_vertex)

	def __eq__(self, other):
		return self.key == other.key

	def __ne__(self, other):
		return not self.key == other.key

