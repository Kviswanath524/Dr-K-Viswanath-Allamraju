# Acronym Generator

phrase = input()

words = phrase.split()
acronym = ""

for word in words:
    acronym += word[0].upper()

print(acronym)
