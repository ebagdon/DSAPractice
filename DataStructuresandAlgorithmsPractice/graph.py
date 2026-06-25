class Graph:
    def __init__(self):
        self.vertices_and_edges = {}

    def add_vertex(self, vertex):
        if vertex in self.vertices_and_edges:
            raise Exception(f"Vertex of value {vertex} already exists in graph.")

        self.vertices_and_edges[vertex] = {}

    def remove_vertex(self, vertex):
        for vert in self.vertices_and_edges:
            for edge in self.vertices_and_edges[vert]:
                if edge == vertex:
                    del self.vertices_and_edges[vert][edge]
                    break

        del self.vertices_and_edges[vertex]

    def add_edge(self, from_vertex, to_vertex, weight = 0, directed = False):
        if from_vertex not in self.vertices_and_edges or to_vertex not in self.vertices_and_edges:
            raise Exception("A vertex doesn't currently exist. Check to make sure your from_vertex and to_vertex exist.")
        if from_vertex is to_vertex:
            raise Exception("The from_vertex and to_vertex cannot be the same.")

        self.vertices_and_edges[from_vertex][to_vertex] = weight
        if not directed:
            self.vertices_and_edges[to_vertex][from_vertex] = weight
        elif self.vertices_and_edges[to_vertex][from_vertex] != None:
            del self.vertices_and_edges[to_vertex][from_vertex]

    def remove_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.vertices_and_edges or to_vertex not in self.vertices_and_edges:
            raise Exception("A vertex doesn't currently exist. Check to make sure your from_vertex and to_vertex exist.")
        if from_vertex is to_vertex:
            raise Exception("The from_vertex and to_vertex cannot be the same.")

        if to_vertex in self.vertices_and_edges[from_vertex]:
            del self.vertices_and_edges[from_vertex][to_vertex]
            if from_vertex in self.vertices_and_edges[to_vertex]:
                del self.vertices_and_edges[to_vertex][from_vertex]
        else:
            raise Exception("Edge does not exist.")

    def print_graph(self):
        for vertex in list(self.vertices_and_edges.keys()):
            print(f'{vertex}:', self.vertices_and_edges[vertex])
        print("---------------------------------END OF GRAPH---------------------------------")

#myGraph = Graph()
#myGraph.add_vertex("Home")
#myGraph.add_vertex("Chick-Fil-A")
#myGraph.add_vertex("Beach")
#myGraph.print_graph()
#myGraph.add_edge("Home", "Chick-Fil-A")
#myGraph.add_edge("Home", "Chick-Fil-A", 5, True)
#myGraph.add_edge("Home", "Beach", 3)
#myGraph.print_graph()
#myGraph.remove_edge("Beach", "Home")
#myGraph.print_graph()
#myGraph.remove_edge("Home", "Chick-Fil-A")
#myGraph.print_graph()
#myGraph.remove_vertex("Beach")
#myGraph.print_graph()
#myGraph.remove_vertex("Chick-Fil-A")
#myGraph.print_graph()
#myGraph.remove_vertex("Home")
#myGraph.print_graph()