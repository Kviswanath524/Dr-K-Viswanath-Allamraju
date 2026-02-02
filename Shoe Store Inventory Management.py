# Shoe Store Inventory Management

# Read initial list of shoes (comma-separated)
shoes = input("Enter initial shoe types: ").split(", ")

# Read shoe type to be added
shoe_to_add = input("Enter shoe type to add: ")

# Add the shoe to the list
shoes.append(shoe_to_add)

# Read shoe type to be removed
shoe_to_remove = input("Enter shoe type to remove: ")

# Remove the shoe if it exists
if shoe_to_remove in shoes:
    shoes.remove(shoe_to_remove)

# Display final list of shoes
print("Final list of shoes:", shoes)

# Read customer's requested shoe
requested_shoe = input("Enter the shoe type requested by the customer: ")

# Check availability
if requested_shoe in shoes:
    print(f'Yes, "{requested_shoe}" is available.')
else:
    print(f'Sorry, "{requested_shoe}" is not available.')
