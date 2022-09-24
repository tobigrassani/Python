""" Python Data Types:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
x = str("Hello World!")
print("This variable is a:", type(x), "and its value is:", x)
x = int(5)
print("This variable is a:", type(x), "and its value is:", x)
x = float(2.5)
print("This variable is a:", type(x), "and its value is:", x)
x = complex(3j)
print("This variable is a:", type(x), "and its value is:", x)


# String Data Handling
# Upper, Lower & Strip
a = "Hello, World!"
b = " Extra spaces "
print(a.upper())
print(a.lower())
print(b.strip(),"where removed")

a = a.upper()   # Returns upper case to the whole string
b = b.strip()   # Removes extra spaces from beginning and end of the string
print(a, b)

# Split & String Concatenation
a = a.split(",")    # Splits the string with the value between commas
print(a)
print(a[0] + a[1], "Here printed separetly")  # Prints the two parts of the list
a = a[0] + a[1]     # Concatenating the list parts
print(a, "Here we already concatenated")

# Format
# The format() method takes the passed arguments, formats them, and places them
# in the string where the placeholders {} are

age = 24
txt = "My name is Tobias, and I am {} actually"
print(txt.format(age))

age = [24, 1997, 30, 12]    # Test with a list
txt = "My name is Tobias, I was born the {} of the month number {} in {}. Actually, I am {}"
print(txt.format(age[2], age[3], age[1], age[0]))


print(isinstance(txt,str))  #Print > If txt is string: True else False



