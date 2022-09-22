# A variable its created when a value is assigned.
# Create & assign: (name) = (value)
x = 5
y = 2
z = "Josh"
if x > y:
    print(x, "is greater than", y)
    print(z, "born in New York.")

# Casting a variable means to assign a value & a data type once the variable its created
x = str(5)
y = int(5)
z = float(3.14)
print("x is string:",x)
print("y is integrer:",y)
print("z is float:",z,"and adding",y,"=",z+y)

# Get the data type of a variable with type()
print("x data type:", type(x))
print("y data type:", type(y))
print("z data type:", type(z))

