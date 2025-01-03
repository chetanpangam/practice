class Graph(object):
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edges(self, u, v):
        if u in self.graph and v in self.graph:
            self.graph[u].append(v)
            self.graph[v].append(u)

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex} => {self.graph[vertex]}")

# [1, 2, 3, 5]
# [2, 3, 4, 6]
graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)


graph.add_edges(1, 2)
graph.add_edges(2, 3)
graph.add_edges(3, 4)
graph.add_edges(5, 6)

graph.print_graph()

