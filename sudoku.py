n = int(input("Insert list size: "))
A = []

for i in range(0, n):
    x = int(input(f"Insert the {i+1}th element: "))
    A.append(x)

print("Matrix A: \n", A, "\nSize: ", len(A))

