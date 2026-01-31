# Future Value Calculator (futval.py)

# Read inputs
principal = float(input())
rate = float(input())
years = int(input())

# Print table header
print("Year\tValue")

# Calculate and display value for each year
for year in range(years + 1):
    value = principal * ((1 + rate) ** year)
    print(f"{year}\t${value:.2f}")
