from edge import Edge
from graph import Graph


def adj_matrix_to_graph(adj_matrix):
    """
    converts the given input adj_matrix to user defined graph format
    """
    length_of_adj_matrix = len(adj_matrix)
    g = Graph(length_of_adj_matrix)
    for row in range(length_of_adj_matrix):
        for col in range(len(adj_matrix[0])):
            weight = adj_matrix[row][col]
            if weight>0:
                vertex = row
                neighbor_vertex = col
                #creates an edge object with current_vertex, neighbor_vertex and associated weight.  
                new_connecting_edge = Edge(vertex, neighbor_vertex, weight)
                g.connect_edges(new_connecting_edge)
    return g


if __name__ == "__main__":
    #adj_matrix is a two dimensional array.
    adj_matrix = [
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 0]
    ]
    graph = adj_matrix_to_graph(adj_matrix)
    
    for vertex_index in range(len(adj_matrix)):
        vertex = graph.get_vertex(vertex_index)
        print (vertex)