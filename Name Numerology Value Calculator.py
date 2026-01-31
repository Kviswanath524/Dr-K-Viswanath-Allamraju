# Name Numerology Value Calculator

name = input()

total = 0

for ch in name.lower():
    if ch.isalpha():
        total += ord(ch) - ord('a') + 1

print(total)
