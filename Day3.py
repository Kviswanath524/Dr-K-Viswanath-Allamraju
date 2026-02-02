#Lists are used to store multiple items in a single variable
'''thislist = ["apple", "banana", "cherry"]
print(thislist)'''
#List items are ordered, changeable, and allow duplicate values
#If you add new items to a list, the new items
#will be placed at the end of the list
'''thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)'''
'''thislist = ["apple", "banana", "cherry"]
print(len(thislist))'''
'''list1 = ["apple", "banana", "cherry"]
print(list1)
list2 = [1, 5, 7, 9, 3]
print(list2)
list3 = [True, False, False]
print(list3)'''
'''list1 = ["abc", 34, True, 40, "male"]
print(list1)
mylist = ["apple", "banana", "cherry"]
print(type(mylist))'''
#The list() Constructor
'''thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)'''
#Access Items
'''thislist = ["apple", "banana", "cherry"]
print(thislist[2])'''
#Negative indexing means start from the end
'''thislist = ["apple", "banana", "cherry"]
print(thislist[-3])'''
#Range of Indexes
'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])'''
'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])'''
'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])'''
'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])'''
'''thislist = ["apple", "banana", "cherry"]
if "mango" in thislist:
  print("Yes, 'apple' is in the fruits list")'''
#Change Item Value
'''thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)'''
#Change a Range of Item Values
'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)'''
#Change the second value by replacing it with two new values
'''thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)'''
#Change the second and third value by replacing it with one value
'''thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)'''
#Insert Items
'''thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)'''
# Python - Add List Items
'''thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)'''
#append elements from another list to the current list, use the extend() method
'''thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)'''
'''thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)'''
#Python - Remove List Items
'''thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)'''
'''thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)'''
'''thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)'''
'''thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)'''
'''thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)'''
'''thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)'''
#Python - Loop Lists
'''thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)'''
'''thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])'''
'''thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1'''
'''thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]'''
'''fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
    
print(newlist)'''
#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

'''newlist = [x for x in fruits if "a" in x]

print(newlist)
newlist = [x for x in fruits if x != "apple"]
print(newlist)'''
'''newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)'''
'''newlist = [x.upper() for x in fruits]
print(newlist)'''
'''newlist = ['hello' for x in fruits]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)'''
#Python - Sort Lists
'''thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)'''
'''thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)'''
#Sort the list based on how close the number is to 50
'''def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)'''
#sorting with capital letters
'''thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)'''
#Copy a List
'''thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)'''
#Join Two Lists
'''list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)'''
'''list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)
  print(list1)'''
'''list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)'''
#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable
'''thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Tuple items are ordered, unchangeable, and allow duplicate values.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)'''
'''thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
thistuple = ("apple",)
print(type(thistuple))'''

#NOT a tuple
'''thistuple = ("apple")
print(type(thistuple))'''
'''tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)'''
'''tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))'''
#The tuple() Constructor
'''thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)'''
'''thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")'''
#Python - Update Tuples
'''x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)'''
'''thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)'''
'''thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)'''
'''thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)'''
'''thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)'''
#Python - Unpack Tuples
'''fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)'''
'''fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)'''
'''fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)'''
#Python - Loop Tuples
'''thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1'''
#join tuples
'''tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 6, 7, 8, 9)

# Using set intersection
common_elements = tuple(set(tuple1) & set(tuple2))

print("Common Elements:", common_elements)'''













