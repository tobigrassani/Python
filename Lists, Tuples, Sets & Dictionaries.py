# In this chapter I'll learn all abouy lists, tuples, sets & dictionaries on python.
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

# LISTS [ , , ]

thislist = [1, 2, 3, 4]
print(thislist.__len__())             # 4
print(thislist.__class__)             # <class 'list'>
print(thislist[0] + thislist[1])      # 3
print(thislist[1:3])                  # [2, 3] ( index 1 included, index 3 not includes )

# Test with input a value, and then an if statement check if the value is in thislist:
"""x = int(input("Fill with a number: "))
print ("The number inserted is:5",x)

if x in thislist:
    print(x, "Is in thislist")
else:
    print(x, "is not in thislist")
"""
print("Thislist is range:", thislist.__len__())
thislist.insert(2, 100)      # Insert a new index in the position/index number 2. The new range is range+1
print(thislist)
print("Thislist new is range:", thislist.__len__())
thislist.append("New item on list")     # Add new item at the end of the list, and also range is +1
thislist.extend(thislist)   # Append another list to a list, so the new range of the list appended is = range(thislist)
#   + range(anotherlist)
print(thislist)

thislist = [1, 2, 3]
thistuple = ("A", "B", "C")
thislist.extend(thistuple)
print(thislist)
thislist.remove("A")    # Removes the "A" element on the list
print(thislist)
thislist.pop(1)     # Pops (removes) the index "1" (position 2) of the list
print(thislist)
thislist.clear()    # Cleans all items of the list
print(thislist.__len__())
for i in range(5):
    thislist.append(i)
    i = i + 1
    print(thislist[i-1])
print(thislist)

for i in range(len(thislist)):
    thislist[i] = i*i
print(thislist)

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

newlist = [x.upper() for x in thislist]     # LIST COMPREHENSION
[print(x) for x in newlist]
newlist = [x if x != "apple" else "orange" for x in thislist]
[print(x) for x in newlist]

# TUPLES

thistuple = ("apple", "banana", "kiwi", "mango")
print("thistuple length: ", len(thistuple))
print("thistuple class: ", thistuple.__class__)
x = len(thistuple)-1        #this is the last item of the tuple
print(thistuple[x])
x = "banana"
if x in thistuple:
    print("Yes!", x, " is in thistuple")
else:
    print("No!", x, "is not in thistuple")

fruits = ("banana", "apple", "kiwi", "mango", "blueberry")

(yellow, red, green, orange, blue) = fruits     # Unpacking a tuple into variables

print(yellow, red, green, orange, blue)

for x in fruits:
    print(x)

fruits = ("banana", "apple", "kiwi", "mango", "blueberry")
i = 0
while i <= len(thistuple):
    print(fruits[i])
    i = i + 1

twotimesfruits = fruits * 2
print(twotimesfruits)
for x in twotimesfruits:
    print("item", x, ":", twotimesfruits)


# SETS

# DICTIONARIES : are used to store data in key:value pairs
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
# Example:
dictbrick = {"name": "Enrique",
        "lastName": "Havenstein",
        "bornDate": "14/4/1998",
        "age": 24
        }
print(dictbrick)            # {'name': 'Enrique', 'lastName': 'Havenstein', 'bornDate': '14/4/1998', 'age': 24}
print(dictbrick["age"])     # 24
print(len(dictbrick))       # 4
print(type(dictbrick))      # <class 'dict'>
age = dictbrick.get("age")
print(age)                  # 24
age = dictbrick["age"]
print(age)                  # 24
print(dictbrick.keys())     # dict_keys(['name', 'lastName', 'bornDate', 'age'])
x = dictbrick.keys()        # returns dict's keys
print(x)
dictbrick["nacionality"] = "Argentina"
print(x)
v = dictbrick.values()      # returns dict's values
print(v)

# To get all key:value pairs use > dict.items()
i = dictbrick.items()
print(i)

# Nested dictionaries are dictionaries inside dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily.items())

# end

