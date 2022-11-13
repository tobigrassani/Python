def camino_euleriano():
    print("Introduzca cada entrada separada por coma (,) \n")
    print("Ejemplo: \nConjunto de vértices: a,b,c \nBordes: (a,b),(a,c),(b,a),(b,c) \n")

    sov = input("Conjunto de vértices: ")  # Obtener letras de vértice de entrada
    Ssov = sov.split(",")  # Obtener los vértices de entrada delimitados por comas y ponerlos en el array

    edg = input("Bordes: ")
    edg1 = edg.replace  (",", "")  # Borrar todas las comas (,) de la entrada Bordes
    edg2 = edg1.replace("(", "")  # Borrar todos los parentesis de apertura de la entrada Bordes
    edg3 = edg2.replace(")", "")  # Borrar todos los parentesis de cierre de la entrada Bordes

    outdeg = []  # Creación de lista de fuera de grado vacía
    indeg = []  # Creación de una lista en grados vacía

    odCounter = 0  # Declarar contador de-grado de salida igual a 0
    idCounter = 0  # Declarar contador fuera-de-grado de salida igual a 0

    equalDegrees = 0  # Variable para acumular cuando los grados en-grado y fuera-de-grado son iguales
    notEqualDegrees = 0

    EPEequalDegrees = 0  # Variable para acumular todos los vértices pares
    EPOequalDegrees = 0

    ECreason = 0  # Variable por la razón de no tener un motivo del circuito Euleriano
    EPreason = 0  # Variable por la razón de no tener una razón Camini Euleriano

    eulerPath = False
    ep1 = 0
    ep2 = 0

    eulerCircuit = False
    ec = 0

    forCounter = 0

    for j in Ssov:  ## Iterar a través de cada vértice

        ## Ver si el vértice es igual a outdegree

        ## Fuera-de-grado
        for i in range(0, len(edg3), 2):
            op, code = edg3[
                       i:i + 2]  ## Obtener Bordes 2 por 2 de la lista Bordes y asignar la primera letra a op y la segunda a code
            ## op comparará el grado de salida. El código se comparará en grado

            if j == op:  ## Si el vértice actual es igual a los primeros anuncios de ocurrencia de outdegree en el contador
                odCounter = odCounter + 1  ## Añadir un outdegree a un vértice

        outdeg.append(odCounter)  ## Añada la cantidad de ocurrencias de un vértice en la lista de salida
        odCounter = 0;  ## Establecer odCounter igual a 0

        ## En-grado
        ## Repetir todos los pasos desde En-grado hasta Fuera-de-grado
        for i in range(0, len(edg3), 2):
            op, code = edg3[i:i + 2]

            if j == code:
                odCounter = odCounter + 1

        indeg.append(odCounter)
        odCounter = 0;

    for j, o, i in zip(Ssov, outdeg, indeg):
        print(str('deg-('), j, str(')= '), o, str(', deg+('), j, str(')= '), i,
              str('\n'))  # Printing the values for every vertex letter and corresponding in and out degrees

        ## Chequear por circuito Euleriano

        if (o == i):
            equalDegrees = equalDegrees + 1  ## Cada vez que un En-grado y Fuera-de-grado sean iguales, anadir al contador
        else:
            notEqualDegrees = notEqualDegrees + 1  ## Cada vez que un vertice Fuera-de-grado y En-grado no sean iguales, anadir al contador

        if (notEqualDegrees == 0):  ## Si los vertices nunca fueron no iguales, entoces tenemos un circuito Euleriano
            eulerCircuit = True
        else:
            eulerCircuit = False
            ECreason = 2

        ## Chequear por un camino Euleriano
        if ((o - i) == 1):
            ep1 = ep1 + 1

        if ((i - o) == 1):
            ep2 = ep2 + 1

        ##  Verificar que uno si y uno no de cada vertex tenga En-grado =Fuera-de-grado
        if ((forCounter % 2) == 0):
            if (o == i):
                EPEequalDegrees = EPEequalDegrees + 1
        else:
            if (o == i):
                EPOequalDegrees = EPOequalDegrees + 1
        forCounter = forCounter + 1

    ## End for

    if (EPEequalDegrees >= 1 or EPOequalDegrees >= 1):
        if (ep1 == 1 and ep2 == 1):
            eulerPath = True
        else:
            eulerPath = False
            EPreason = 1
    else:
        EPreason = 2

    print(str('Circuito Euleriano: '), eulerCircuit)
    print(str('Camino Euleriano: '), eulerPath)

    if (eulerCircuit == True):
        print("La grafica no tiene un Circuito Euleriano")
    else:
        if (ECreason == 2):
            print(
                "La grafica no tiene un circuito euleriano porque el En-grado y Fuera-de-grado de cada vertice no son iguales")

    if (eulerPath == True):
        print("La grafica tiene un camino Euleriano")
    else:
        if (EPreason == 1):
            print(
                "La grafica no tiene un camino Euleriano porque ni a lo más un vértice tiene (fuera-de-grado) - (en-grado) = 1, tampoco tiene como mucho un vértice que tenga (en-grado) - (fuera-de-grado) = 1")
        elif (EPreason == 2):
            print("La grafica no tiene un camino Euleriano porque cada otro vértice no tiene en-grado = fuera-de-grado")


EulerianoCNN()

