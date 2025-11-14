from datetime import datetime, timedelta

# Starter data (moved here so no imports are needed)
library_books = [
    {
        "id": "B1",
        "title": "The Lightning Thief",
        "author": "Rick Riordan",
        "genre": "Fantasy",
        "available": True,
        "due_date": None,
        "checkouts": 2
    },
    {
        "id": "B2",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Historical",
        "available": False,
        "due_date": "2025-11-01",
        "checkouts": 5
    }
    # Add any additional books here
]


# Represents one book in the library
class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.author = data["author"]
        self.genre = data["genre"]
        self.available = data["available"]
        self.due_date = data["due_date"]
        self.checkouts = data["checkouts"]

    # Used in Level 3
    def checkout(self):
        self.available = False
        due = datetime.now() + timedelta(days=14)
        self.due_date = due.strftime("%Y-%m-%d")
        self.checkouts += 1


# Manages the book list
class Library:
    def __init__(self, book_list):
        self.books = [Book(b) for b in book_list]

    # LEVEL 1: View available books
    def view_available(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.available:
                print(f"{book.id} - {book.title} by {book.author}")

    # LEVEL 2: Search by author or genre
    def search(self, term):
        term = term.lower()
        print("\nSearch Results:")
        found = False

        for book in self.books:
            if term in book.author.lower() or term in book.genre.lower():
                print(f"{book.id} - {book.title} by {book.author}")
                found = True

        if not found:
            print("No matching books found.")

    # LEVEL 3: Checkout a book
    def checkout_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                if book.available:
                    book.checkout()
                    print(f"\n{book.title} has been checked out.")
                    print(f"Due Date: {book.due_date}")
                else:
                    print("\nThat book is already checked out.")
                return

        print("\nBook ID not found.")


# Main loop for librarian interaction
def main():
    library = Library(library_books)

    while True:
        print("\nLibrary Menu")
        print("1. View available books")
        print("2. Search by author or genre")
        print("3. Checkout a book")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            library.view_available()
        elif choice == "2":
            term = input("Enter author or genre: ").strip()
            library.search(term)
        elif choice == "3":
            book_id = input("Enter book ID to checkout: ").strip()
            library.checkout_book(book_id)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
