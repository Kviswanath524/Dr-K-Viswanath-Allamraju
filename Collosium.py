# Step 1: Create an initial dictionary with basic information
colosseum_info = {
    "Location": "Rome",
    "Construction Years": "70–80 AD",
    "Type": "Amphitheater"
}

# Display the initial dictionary
print("Initial Dictionary:")
print(colosseum_info)
print()

# Step 2: Update construction details based on new findings
# Remove the old key "Construction Years"
del colosseum_info["Construction Years"]

# Add new key "Construction Start Year" using direct assignment
colosseum_info["Construction Start Year"] = 72

# Add new key "Construction End Year" using .update() method
colosseum_info.update({"Construction End Year": 80})

# Display the updated dictionary
print("Updated Dictionary:")
print(colosseum_info)
print()

# Step 3(a): Calculate how many years it took to build the Colosseum
years_to_build = colosseum_info["Construction End Year"] - colosseum_info["Construction Start Year"]
print(f"It took {years_to_build} years to build the Colosseum.")

# Step 3(b): Calculate how many years have passed since construction started
current_year = 2026  # You can also use: from datetime import datetime; current_year = datetime.now().year
years_since_start = current_year - colosseum_info["Construction Start Year"]
print(f"{years_since_start} years have passed since construction began.")
