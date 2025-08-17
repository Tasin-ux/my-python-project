# Library Management System

class Library:
    def __init__(self):
        # Store books as a dictionary: {book_id: [book_name, author, available_copies, issued_copies]}
        self.books = {}
        # Store issued books as a dictionary: {member_name: [book_id, issued_date]}
        self.issued_books = {}

    def add_book(self, book_id, book_name, author, copies):
        if book_id in self.books:
            self.books[book_id][2] += copies  # Increase the available copies
        else:
            self.books[book_id] = [book_name, author, copies, 0]  # [name, author, available, issued]
        print(f"Book '{book_name}' by {author} added with {copies} copies.")

    def view_books(self):
        print("\nAvailable Books:")
        for book_id, details in self.books.items():
            print(f"ID: {book_id}, Title: {details[0]}, Author: {details[1]}, Available: {details[2]}")
        print()

    def issue_book(self, book_id, member_name):
        if book_id in self.books and self.books[book_id][2] > 0:
            self.books[book_id][2] -= 1  # Decrease available copies
            self.books[book_id][3] += 1  # Increase issued copies
            self.issued_books[member_name] = book_id
            print(f"Book '{self.books[book_id][0]}' issued to {member_name}.")
        else:
            print("Sorry, the book is not available for issue.")

    def return_book(self, member_name):
        if member_name in self.issued_books:
            book_id = self.issued_books[member_name]
            self.books[book_id][2] += 1  # Increase available copies
            self.books[book_id][3] -= 1  # Decrease issued copies
            del self.issued_books[member_name]
            print(f"Book '{self.books[book_id][0]}' returned by {member_name}.")
        else:
            print(f"{member_name} has not issued any book.")

    def view_issued_books(self):
        print("\nIssued Books:")
        if self.issued_books:
            for member, book_id in self.issued_books.items():
                print(f"Member: {member}, Book: {self.books[book_id][0]} by {self.books[book_id][1]}")
        else:
            print("No books have been issued.")
        print()

# Driver code
def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Available Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Issued Books")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            book_id = input("Enter book ID: ")
            book_name = input("Enter book name: ")
            author = input("Enter author: ")
            copies = int(input("Enter number of copies: "))
            library.add_book(book_id, book_name, author, copies)
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            book_id = input("Enter book ID to issue: ")
            member_name = input("Enter member name: ")
            library.issue_book(book_id, member_name)
        elif choice == "4":
            member_name = input("Enter member name to return book: ")
            library.return_book(member_name)
        elif choice == "5":
            library.view_issued_books()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
