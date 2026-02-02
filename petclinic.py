# Step 1: Start with the initial list of pets
pets = [
    {"name": "Toby", "animal type": "dog", "age": 2},
    {"name": "Kitty", "animal type": "cat", "age": 5},
    {"name": "Tiki", "animal type": "parrot", "age": 1}
]

# Step 2: Add a new patient, a 4-year-old horse named Sugar
new_pet = {"name": "Sugar", "animal type": "horse", "age": 4}
pets.append(new_pet)

# Print the list after adding the new pet
print("List of pets after adding Sugar:")
for pet in pets:
    print(pet)
print()

# Step 3(a): Print all animal names using a for loop through elements
print("Pet names (using for loop through elements):")
for pet in pets:
    print(pet["name"])
print()

# Step 3(b): Print all animal names using a for loop through indices
print("Pet names (using for loop through indices):")
for i in range(len(pets)):
    print(pets[i]["name"])
print()

# Step 4: Add a new item indicating all animals are currently in the clinic
# We can add a boolean key 'in_clinic' to each pet dictionary
for pet in pets:
    pet["in_clinic"] = True

# Print the updated list
print("Updated list of pets showing all animals are in the clinic:")
for pet in pets:
    print(pet)
