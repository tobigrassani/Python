n = int(input("Insert matrix size: "))
A = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input(f"Insert [{i}][{j}] value: ")))
    A.append(row)

print("Matrix A: \n", A, "\nSize: ", len(A))
print("Printing looped matrix: ")
for i in A:
    for j in i:
        print(j, end=" ")
    print()


