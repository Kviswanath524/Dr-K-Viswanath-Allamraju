# Predefined list of seasons
seasons = ["spring", "summer", "fall", "winter"]

# a. Seasons with at least 5 characters
seasons_at_least_5 = [season for season in seasons if len(season) >= 5]
print("Seasons with at least 5 characters:", seasons_at_least_5)

# b. Seasons with 4 or fewer characters
seasons_4_or_less = [season for season in seasons if len(season) <= 4]
print("Seasons with 4 or fewer characters:", seasons_4_or_less)

# c. Seasons whose position (index) is less than 2
seasons_index_less_2 = seasons[:2]  # slicing
print("Seasons with position less than 2:", seasons_index_less_2)

# d. Seasons whose position (index) is at least 2
seasons_index_at_least_2 = seasons[2:]  # slicing
print("Seasons with position at least 2:", seasons_index_at_least_2)
