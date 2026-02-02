# Art Gallery Inventory Checker

# Predefined list of available paintings
paintings = [
    "Starry Night",
    "The Mona Lisa",
    "The Last Supper",
    "The Scream",
    "Girl with a Pearl Earring"
]

# Ask the customer for the painting they want to buy
requested_painting = input("Enter the painting you want to buy: ")

# Check if the painting is available
if requested_painting in paintings:
    print(f'Yes, we have "{requested_painting}" available for purchase!')
else:
    print(f'Sorry, "{requested_painting}" is currently unavailable.')
