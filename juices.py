# Step 1: Create a list of dictionaries for juice flavors
juices = [
    {"flavor": "orange", "price": 50, "color": "orange"},
    {"flavor": "lemon", "price": 40, "color": "yellow"},
    {"flavor": "pomegranate", "price": 60, "color": "red"}
]

# Step 2: Add "in shop" key to each juice (True if available, False if not)
for juice in juices:
    juice["in shop"] = True  # Let's assume all initial juices are available

# Print the list after adding "in shop" info
print("Juices after adding 'in shop' details:")
for juice in juices:
    print(juice)
print()

# Step 3: Add a new juice order "grape juice"
grape_juice = {"flavor": "grape", "price": 55, "color": "purple", "in shop": True}
juices.append(grape_juice)

# Print the updated list after adding grape juice
print("Updated list after adding grape juice:")
for juice in juices:
    print(juice)
print()

# Step 4: Calculate and print the average price of all juices
total_price = sum(juice["price"] for juice in juices)
average_price = total_price / len(juices)
print(f"The average price of all juices is: {average_price:.2f}")
