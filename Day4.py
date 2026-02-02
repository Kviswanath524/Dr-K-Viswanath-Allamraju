#Sets are used to store multiple items in a single variable
#A set is a collection which is unordered, unchangeable*, and unindexed
'''thisset = {"apple", "banana", "cherry"}
print(thisset)'''
#Set items are unordered, unchangeable, and do not allow duplicate values.
'''thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)'''
#True and 1 is considered the same value:
'''thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)'''
'''thisset = {"apple", "banana", "cherry"}

print(len(thisset))'''
'''set1 = {"abc", 34, True, 40, "male"}
print(set1)'''
'''myset = {"apple", "banana", "cherry"}
print(type(myset))'''
#The set() Constructor
'''thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)'''
#Python - Access Set Items
'''thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)'''

'''thisset = {"apple", "banana", "cherry"}
print("mango" in thisset)'''
'''thisset = {"apple", "banana", "cherry"}

print("mango" not in thisset)'''
#Python - Add Set Items
'''thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)'''
'''thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)'''
'''thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)'''
#Python - Remove Set Items
'''thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)'''
'''thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)'''
'''thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)'''
'''thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)'''
'''thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)'''
#Python - Loop Sets
'''thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)'''
#Python - Join Sets
'''set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)'''

'''set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)'''

'''set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)'''

'''set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)'''

'''x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)'''

'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)'''

'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)'''

'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)'''

'''set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)'''

'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)'''

'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)'''

'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)'''

'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)'''
# Python Dictionaries
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}'''
#Dictionaries are used to store data values in key:value pairs
#Dictionaries are written with curly brackets, and have keys and values
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)'''
#Dictionary Items
#Dictionary items are ordered, changeable, and do not allow duplicates.

#Dictionary items are presented in key:value pairs, and can be referred
#to by using the key name
''''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])'''
#Duplicates Not Allowed Dictionaries cannot have two items with the same key
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict))'''
#Dictionary Items - Data Types(any)
'''thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)'''
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))'''
#The dict() Constructor
'''thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)'''
#Accessing Items
'''thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("year")
print(x)
x = thisdict.keys()
print(x)'''
#The list of the keys is a view of the dictionary, meaning that any
#changes done to the dictionary will be reflected in the keys list.
'''car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change'''
'''car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
x = car.items()
print(x)'''
#Check if Key Exists
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "colour" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")'''
#Change Values
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
#Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)'''
#Removing Items
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)'''
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)'''
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict)'''
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)'''
#Python - Loop Dictionaries
#print all key values
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)'''
#print all values
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
for x in thisdict.keys():
  print(x)
for x in thisdict:
  print(thisdict[x])
for x, y in thisdict.items():
  print(x, y)'''
#Python - Copy Dictionaries
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)'''
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)'''
'''myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)'''
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
#print(child1)
#print(child2)
#print(child3)
#print(myfamily)
'''print(myfamily["child2"]["name"])
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])'''

'''sets = [
    {1, 2, 3},
    {3, 4, 5},
    {5, 6, 7}
]   # Efficient union using generator expressions
union_set = set().union(*sets)
print("Union of All Sets:", union_set)'''
'''set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {5, 6, 7, 8}

# Symmetric difference across multiple sets
result = set1 ^ set2 ^ set3

print("Symmetric Difference:", result)'''




















