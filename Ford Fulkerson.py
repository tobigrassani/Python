class Graph:

    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)

    """ Devuelve TRUE si existe un camino desde la fuente 's' hacia 
    el sumidero 't' en el grafo residual. Tambien llena parent[]
    para guardar el grafo."""
    # Busqueda Por Amplitud - BPA
    def BFS(self, s, t, parent):

        # Marca todos los vertices como no visitados
        visited = [False] * self.ROW

        # Crea una lista para la BPA
        queue = []

        # Marca el sumidero como visitado y lo coloca en la lista del BPA
        queue.append(s)
        visited[s] = True

        # Algoritmo BPA
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for index, value in enumerate(self.graph[u]):
                if visited[index] == False and value > 0:
                    # If we find a connection to the sink node,
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(index)
                    visited[index] = True
                    parent[index] = u
                    if index == t:
                        return True

        # We didn't reach sink in BFS starting
        # from source, so return false
        return False

    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


# Create a graph given in the above diagram

graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 130, 19, 0, 0],
         [0, 34, 0, 0, 14, 0],
         [0, 0, 93, 0, 0, 20],
         [0, 0, 0, 7, 0, 43],
         [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0
sink = 5

print("The maximum possible flow is %d " % g.FordFulkerson(source, sink))