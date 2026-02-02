# Bike Store - Change Bike Color

# Input initial bike features (comma-separated)
bike_features = input("Enter bike features: ").split(", ")

# Input new color
new_color = input("Enter the new color you want: ")

# Find the position of 'blue'
position = bike_features.index("blue")

# Remove 'blue'
bike_features.remove("blue")

# Insert new color at the same position
bike_features.insert(position, new_color)

# Display results
print("Position of 'blue' in the list:", position)
print("Updated bike features:", bike_features)
