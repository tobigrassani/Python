n = int(input("Insert matrix size: "))
A = []

for i in range(0, n):
    row = []
    for j in range(0, n):
        row.append(int(input(f"Insert [{i}][{j}] value: ")))
    A.append(row)

print("Matrix A: \n", A, "\nSize: ", len(A))

