# Average Word Length Calculator

sentence = input()

words = sentence.split()

total_characters = 0

for word in words:
    total_characters += len(word)

average_length = total_characters / len(words)

print(f"{average_length:.2f}")
