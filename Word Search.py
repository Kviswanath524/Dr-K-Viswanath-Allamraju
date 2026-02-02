# Predefined list of words
words = ["cards", "park", "pets", "football", "golf", "crosswords", "toys",
         "exercise", "hobbies", "riding", "biking", "games", "reading",
         "movies", "walking", "concerts"]

# a. Create title with number of words
title = len(words)
print(f"Word search with {title} words")

# b. Find all 5-letter words
words_5_letters = [word for word in words if len(word) == 5]
print("Words with 5 letters:", words_5_letters)
print("Number of 5-letter words:", len(words_5_letters))

# c. Words with fewer than 5 characters
print("Words with less than 5 letters:")
for idx, word in enumerate(words):
    if len(word) < 5:
        print(f"- '{word}' (position {idx}) has {len(word)} characters.")

# d. Words with more than 8 characters
print("Words with more than 8 characters:")
for idx, word in enumerate(words):
    if len(word) > 8:
        print(f"- '{word}' (position {idx}) has {len(word)} characters.")

# e. From second half, words whose length != 7
half_index = len(words) // 2
second_half = words[half_index:]
print("Words in the second half (different from 7 characters):")
for idx, word in enumerate(second_half, start=half_index):
    if len(word) != 7:
        print(f"- '{word}' (position {idx}) → {len(word)} characters")

# f. From first fourth, 4-letter words
quarter_index = len(words) // 4
first_quarter = words[:quarter_index]
print("4-letter words in the first fourth of the list:")
for idx, word in enumerate(first_quarter):
    if len(word) == 4:
        print(f"- '{word}' (position {idx})")
