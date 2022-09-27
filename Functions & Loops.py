#Conditions and Statements
"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

if  else
    elif  "if the previous conditions were not true, then try this condition"
while
for
"""
#   EXAMPLES
a = 2
b = 330
print("A") if a > b else print("B")     # reducing lines

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if (a > b) and (c > a):
    print("Both conditions are True")

#   NESTED IF
x = 17

if x > 10:
    print("Above ten,")
if x > 20:
    print("and also above 20!")
else:
    print("but not above 20.")


    #duplicadoooo

