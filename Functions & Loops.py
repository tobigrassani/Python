#>>>>>>> Conditions and Statements
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
b = 3301
print("A") if a > b else print("=") if a == b else print("B")
"""
STATEMENT 1:

print("A") if a > b else print("=") if a == b else print("B")

Its equal to
STATEMENT 2:

if a > b
    print("A")
else
    if a==b
        print("=")
    else
        print("B")
"""

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

#>>>>>>> LOOPS
i = 1
while i < 10:
    print(i)
    i += 1

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue    # jumps to the next iteration without ending the actual one
    print(i)

i = 0
j = 0
while i < 5:
    i += 1
    j += 1
    if i == 3:
        print(j , "is j")
        continue
    print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":      # strings are iterable with for loops
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break           # stops iterating with banana index
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue        # jumps the banana index
    print(x)

#>>>>>>>> FUNCTIONS


def myname(name):
    print(name + " is human")


myname("tobias")
myname("alex")

names = ["enrique", "marcos", "juan", "matias", "delin"]
for x in names:
    myname(x)


for x in names:
    if x == "juan":
        continue
    myname(x)

for x in names:
    if x == "juan":
        break
    myname(x)

i = 0
for x in names:
    if x == "juan":
        break
    myname(x)
    i += 1
print(i, "names where printed")

i = 0
for x in names:
    if x == "juan":
        continue
    myname(x)
    i += 1
print(i, "names where printed")

def arbitraryfunc(*people):   # pass data while indexing >>>> arbitrary arguments
    print("The selected person is", people[2])
arbitraryfunc("enrique", "marcos", "juan", "matias", "delin")







