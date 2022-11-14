from os import system


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


if __name__ == '__main__':

    def pedirOpcion():
        correcto = False
        num = 0
        while (not correcto):
            try:
                num = int(input("Introduce una opcion del menu: "))
                system("cls")
                correcto = True
            except ValueError:
                print('Error, introduce un numero del menu')

        return num


    salir = False
    opcion = 0

    while not salir:

        print("Materia: Matematica Discreta 2\n")
        print("Algoritmo Ford-Fulkerson\n")
        print("Alumnos: Santiago Lugani , Tobias Grassani")
        print("Profesora: Claudia Ferreyra\n")

        print("1- Utilizar algoritmo con matriz Pre-cargada")
        print("2- Utilizar algoritmo cargando una matriz")
        print("3- Salir.")

        opcion = pedirOpcion()
        if opcion == 1:
            n = 7
            A = [[0, 7, 6, 4, 0, 0, 0],
                 [0, 0, 2, 0, 2, 0, 0],
                 [0, 0, 0, 3, 5, 2, 0],
                 [0, 0, 0, 0, 0, 5, 0],
                 [0, 0, 0, 0, 0, 0, 8],
                 [0, 0, 0, 0, 2, 0, 5],
                 [0, 0, 0, 0, 0, 0, 0]]

            source = 0
            sink = 6

            g = Graph(A)
            print("La matriz de adyacencia precargada es:", A, "\n\n")

            print(f"El flujo maximo desde la fuente '{source}' al sumidero '{sink}' es: %d " % g.FordFulkerson(source,
                                                                                                               sink) + "\n")
            system("pause")
            system("cls")
        elif opcion == 2:
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

            print(f"El flujo maximo desde la fuente '{source}' al sumidero '{sink}' es: %d " % g.FordFulkerson(source,
                                                                                                               sink))
            system("pause")
            system("cls")
        elif opcion == 3:
            salir = True
        else:
            print("Introduce un numero entre 1 y 3")

    print("Fin")