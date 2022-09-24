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


"""x = int(input("Fill with a number: "))
print ("The number inserted is:5",x)

if x in thislist:
    print(x, "Is in thislist")
else:
    print(x, "is not in thislist")
"""



# TUPLES

# SETS

# DICTIONARIES