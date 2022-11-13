class Graph:

    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)

    """ Devuelve TRUE si existe un camino desde la fuente 's' hacia 
    el sumidero 't' en el grafo residual. Tambien llena parent[]
    para guardar el grafo."""
    # Busqueda Por Amplitud para verificar si existe camino entre fuente y sumidero
    def BFS(self, s, t, parent):

        # Marca todos los vertices como no visitados
        visited = [False] * self.ROW

        # Crea una lista para el algoritmo BPA
        queue = []

        # Marca el sumidero como visitado y lo coloca en la lista del algoritmo BPA
        queue.append(s)
        visited[s] = True

        # Algoritmo BPA
        while queue:

            u = queue.pop(0)
            for index, value in enumerate(self.graph[u]):
                if visited[index] == False and value > 0:
                    queue.append(index)
                    visited[index] = True
                    parent[index] = u
                    if index == t:
                        return True

        # No existe camino entre la fuente y el sumidero, entonces return False
        return False

    # Metodo FordFulkerson para devolver el flujo maximo entre fuente y sumidero
    def FordFulkerson(self, source, sink):

        # Arreglo rellenado por el BPA
        parent = [-1] * self.ROW

        max_flow = 0  # Flujo inicial es 0

        # Aumenta el flujo mientras va encontrando camino
        while self.BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


n = int(input("Ingresar cantidad de vertices: "))
A = []

print("\nAhora ingrese la matriz de adyacencia:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input(f"Arista [{i}-{j}]: ")))
    A.append(row)

source = int(input("Ingresar Fuente: "))
sink = int(input("Ingresar Sumidero: "))

g = Graph(A)

print(f"El flujo maximo desde la fuente '{source}' al sumidero '{sink}' es: %d " % g.FordFulkerson(source, sink))