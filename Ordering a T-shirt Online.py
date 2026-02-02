# Ordering a T-shirt Online

# Input T-shirt characteristics (comma-separated)
tshirt_features = input("Enter T-shirt features: ").split(", ")

# Input new text to print
new_text = input("Enter the text to print on the T-shirt: ")

# Find the position of 'add your text here'
position = tshirt_features.index("add your text here")

# Remove the old text
tshirt_features.remove("add your text here")

# Insert the new text at the same position
tshirt_features.insert(position, new_text)

# Display results
print("Position of 'add your text here' in the list:", position)
print("Updated T-shirt features:", tshirt_features)
