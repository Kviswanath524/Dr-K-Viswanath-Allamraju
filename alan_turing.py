# Predefined list
alan_turing = ["Turing", "created", "an electromechanical machine", 
               "to crack", "the Nazi Navy's", "Enigma Code"]

# -------------------------------
# Using List Slicing
# -------------------------------

# Make a copy to preserve original
slicing_list = alan_turing[:]

# a. Replace "the Nazi Navy's" with "shortened the war"
slicing_list[4:5] = ["shortened the war"]

# b. Insert "by two years" in position 5 (6th element)
slicing_list[5:5] = ["by two years"]

# c. Replace "an electromechanical machine" with "his contribution"
slicing_list[2:3] = ["his contribution"]

# d. Add "saving millions of lives" to the end
slicing_list[len(slicing_list):] = ["saving millions of lives"]

# e. Replace "created" with "that"
slicing_list[1:2] = ["that"]

# f. Remove "to crack"
slicing_list[3:4] = []

# g. Replace "Turing" with "It is estimated"
slicing_list[0:1] = ["It is estimated"]

# h. Remove the element in position 5 (sixth element)
slicing_list[5:6] = []

print("After performing operations using list slicing:", slicing_list)

# -------------------------------
# Using List Methods
# -------------------------------

# Make a fresh copy of original
methods_list = alan_turing[:]

# a. Replace "the Nazi Navy's" with "shortened the war"
index = methods_list.index("the Nazi Navy's")
methods_list[index] = "shortened the war"

# b. Insert "by two years" in position 5
methods_list.insert(5, "by two years")

# c. Replace "an electromechanical machine" with "his contribution"
index = methods_list.index("an electromechanical machine")
methods_list[index] = "his contribution"

# d. Add "saving millions of lives" to the end
methods_list.append("saving millions of lives")

# e. Replace "created" with "that"
index = methods_list.index("created")
methods_list[index] = "that"

# f. Remove "to crack"
methods_list.remove("to crack")

# g. Replace "Turing" with "It is estimated"
index = methods_list.index("Turing")
methods_list[index] = "It is estimated"

# h. Remove element in position 5 (6th element)
methods_list.pop(5)

print("After performing operations using list methods:", methods_list)
