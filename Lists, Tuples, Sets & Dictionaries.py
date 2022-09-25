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
print(thislist)










# TUPLES

# SETS

# DICTIONARIES