# Predefined list of books
books = ["The Alchemist", "1984", "To Kill a Mockingbird", "The Great Gatsby", "Moby Dick"]

# Display original list
print("Original list of books:", books)

# a. Customer buys "1984" → remove it
books.remove("1984")
print("After selling '1984':", books)

# b. New shipment arrives → add two books
books.extend(["Pride and Prejudice", "The Catcher in the Rye"])
print("After adding new books:", books)

# c. Total number of books
print("Total number of books:", len(books))

# d. First and last book
print("First book:", books[0])
print("Last book:", books[-1])

# e. Sort books alphabetically
sorted_books = sorted(books)
print("Books sorted alphabetically:", sorted_books)

# f. Check if "Moby Dick" is still available
if "Moby Dick" in books:
    print("Yes, 'Moby Dick' is available in the store.")
else:
    print("Sorry, 'Moby Dick' is not available in the store.")
