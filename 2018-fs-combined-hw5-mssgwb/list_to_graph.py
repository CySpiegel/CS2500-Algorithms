from edge import Edge
from graph import DirectedGraph


def adj_list_to_graph(adj_list):
    """
    converts the given input adj_list to user defined graph format
    """
    length_of_adj_list = len(adj_list)
    g = DirectedGraph(length_of_adj_list)
    for vertex, neighbors in adj_list.items():
        # print vertex, neighbors
        for neighbor in neighbors:
            neighbor_vertex = neighbor[0]
            weight = neighbor[1]
            #creates an edge object with current_vertex, neighbor_vertex and associated weight.
            new_connecting_edge = Edge(vertex, neighbor_vertex, weight)
            g.connect_edges(new_connecting_edge)
    return g

if __name__ == "__main__":
    """
    adj_list is an array of tuples.
    First element in tuple represents the index of the neighbor
    and second index represents the weight.
    """
    adj_list =  dict([(0, [(1,1), (2,1)]), (1, [(0,1)]), (2, [(0,1)])])
    graph = adj_list_to_graph(adj_list)

    for vertex_index in range(len(adj_list)):
        vertex = graph.get_vertex(vertex_index)
        print (vertex)
