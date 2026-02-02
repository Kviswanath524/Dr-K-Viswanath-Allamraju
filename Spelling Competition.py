# Predefined list of MSK words
msk_words = ["ankle", "patella", "rib", "femur", "sternocleidomastoid", 
             "tendon", "sternum", "abdominal external oblique", "muscle", 
             "scapula", "radius", "bone", "vertebra", "ligament", "ulna", 
             "skull", "clavicle"]

# a. Total number of words
total_words = len(msk_words)
print("Total number of words to learn:", total_words)

# b. Length of each word (including spaces)
print("Length of each word:")
for word in msk_words:
    print(f"{word}: {len(word)}")

# c. Short words (6 or fewer characters)
short = ["leg"]
for word in msk_words:
    if len(word) <= 6:
        short.append(word)
print("\nShort words list:", short)
print("Number of words in short list:", len(short))

# d. Intermediate words (7, 8, or 9 characters)
intermediate = ["cartilage"]
for word in msk_words:
    if 7 <= len(word) <= 9:
        intermediate.append(word)
print("\nIntermediate words list:", intermediate)
print("Number of words in intermediate list:", len(intermediate))

# e. Long words (10 or more characters)
long = ["pectoralis major"]
for word in msk_words:
    if len(word) >= 10:
        long.append(word)
print("\nLong words list:", long)
print("Number of words in long list:", len(long))
