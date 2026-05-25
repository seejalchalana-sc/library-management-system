# Library Management System
# Using Dictionary

library = {}

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    library[book_id] = {"title": title, "author": author, "status": "available"}
    print(f"Book '{title}' added successfully!")

def view_books():
    if not library:
        print("No books in library.")
    else:
        print("\n--- All Books ---")
        for book_id, details in library.items():
            print(f"ID: {book_id} | Title: {details['title']} | Author: {details['author']} | Status: {details['status']}")

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    if book_id in library:
        if library[book_id]["status"] == "available":
            library[book_id]["status"] = "issued"
            print("Book issued successfully!")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")

def return_book():
    book_id = input("Enter Book ID to return: ")
    if book_id in library:
        library[book_id]["status"] = "available"
        print("Book returned successfully!")
    else:
        print("Book not found.")

def delete_book():
    book_id = input("Enter Book ID to delete: ")
    if book_id in library:
        del library[book_id]
        print("Book deleted successfully!")
    else:
        print("Book not found.")

def view_issued_books():
    issued = False
    print("\n--- Issued Books ---")
    for book_id, details in library.items():
        if details["status"] == "issued":
            print(f"ID: {book_id} | Title: {details['title']} | Author: {details['author']}")
            issued = True
    if not issued:
        print("No books are currently issued.")

while True:
    print("\n=== Library Management System ===")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. View Issued Books")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        delete_book()
    elif choice == "6":
        view_issued_books()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")