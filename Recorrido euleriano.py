import random

Grafo = dict()
Grafo_variable = dict()
nodos = []
Conversion_nodos = []

print("Cantidad de NODOS: ")
num_de_nodos = int(input())

print('Ingrese la lista de adyacencia para cada nodo y separe los elementos con comas (,)')

for i in range(num_de_nodos):
    print("nodo", i + 1)
    nodos = str(input())
    Conversion_nodos = list(nodos)
    Grafo[i + 1] = Conversion_nodos

print("Fin de input lista adyacencia. ")

Grafo_variable = Grafo
num_aristas = 0

num_elementos_list = len(Grafo)
nodo_inicio = random.randint(1, num_elementos_list)
Solucion = []

print('El nodo de inicio del circuito es', nodo_inicio)

valencia_nodos = 0
ultimo_nodo_borrado = 0

Solucion.append(nodo_inicio)
for i in Grafo:
    num_aristas += len(Grafo[i])

num_aristas = num_aristas / 2
num_aristas_var = num_aristas

while (num_aristas_var != 0):
    nodo = nodo_inicio
    valencia_nodos = 0
    check_nodo = 0

for i in Grafo_variable[nodo]:
    for j in Grafo_variable[nodo]:
        if j != 0:
            valencia_nodos += 1

    if valencia_nodos == 0 & num_aristas_var <= 1:
        for i in Grafo_variable[Solucion[-1]]:
            if i == 0:
                Grafo_variable[Solucion[-1]][Grafo_variable[Solucion[-1]].index(i)] = Solucion[-2]
                break
        for i in Grafo_variable[Solucion[-2]]:
            if i == 0:
                Grafo_variable[Solucion[-2]][Grafo_variable[Solucion[-2]].index(i)] = Solucion[-1]
                break

        ultimo_nodo_borrado = Solucion.pop()
        num_aristas_var += 1
        valencia_nodos = 0

        for j in Grafo_variable[Solucion[-1]]:
            if j != 0:
                valencia_nodos += 1

        if valencia_nodos == 1:
            while valencia_nodos == 1:
                for i in Grafo_variable[Solucion[-1]]:
                    if i == 0:
                        Grafo_variable[Solucion[-1]][Grafo_variable[Solucion[-1]].index(i)] = Solucion[-2]
                        break
                for i in Grafo_variable[Solucion[-2]]:
                    if i == 0:
                        Grafo_variable[Solucion[-2]][Grafo_variable[Solucion[-2]].index(i)] = Solucion[-1]
                        break
                ultimo_nodo_borrado = Solucion.pop()

                num_aristas_var += 1
                valencia_nodos = 0

                for j in Grafo_variable[Solucion[-1]]:
                    if j != 0:
                        valencia_nodos += 1

            nodo_inicio = Solucion[-1]
            break

        else:
            nodo_inicio = Solucion[-1]
            break


    else:
        if i != 0 and i != ultimo_nodo_borrado:
            ultimo_nodo_borrado = 0

            for k in Grafo_variable[nodo]:
                if k == i:
                    Grafo_variable[nodo][Grafo_variable[nodo].index(k)] = 0

            for l in Grafo_variable[i]:
                if l == nodo:
                    Grafo_variable[i][Grafo_variable[i].index(l)] = 0

            num_aristas_var -= 1
            nodo_inicio = i
            valencia_nodos = 0
            Solucion.append(i)
            break

print
print('El circuito de EULER es:', Solucion)
print
print(Solucion)
print