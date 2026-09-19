def show_menu():
    print('=' * 5 + " LIBRARY MANAGEMENT SYSTEM " + '=' * 5)
    print()
    print("1. Add Book")
    print("2. Search Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")

    try:
        choice = int(input("enter a the operation you want to perform: "))
        if 0 < choice <= 6:
            if 1 <= choice <= 5 :
                return choice
            else: 
                return choice
        else:
            print("Enter the choice that is in range")
    except ValueError:
        print("Invalid choice input! try again")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, search_text):
        search_text = search_text.strip()
        for book in self.books:
            if search_text in book.title and book.available:
                print(f"Book found titled {book.title}")
                return f"the location is: {book.location}"
            if search_text in book.title and not book.available:
                print("Book is currently borrowed")
                return
        else:
            print("Book not found")

    def borrow_book(self, book_id):
        for book in self.books:
            if book_id == book.book_id:
                book.borrow()
                break
        else:
            print("Book id not in range.")

    def return_book(self, book_id):
        for book in self.books:
            if book_id == book.book_id:
                book.return_book()
                break
        else:
            print("Book id not in range.")
                
    def delete_book(self, book_id):
        for idx,  book in enumerate(self.books):
            if book_id == book.book_id:
                deleted_book = self.books.pop(idx)
                print(f"Book with id:{deleted_book} titled {book.title} is deleted")
                return
        else:
            print("Book id not found")


class Book:
    def __init__(self, book_id, title, author, book_type, location):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.book_type = book_type
        self.location = location
        self.available = True
    def borrow(self):
        if self.available:
            self.available = False
            print(f"Book with id {self.book_id} is now borrowed")
        else:
            print("The book is already borrowed by other person")
    def return_book(self):
        if not self.available:
            self.available = True
            print("The book has returned to the library")

library = Library()

while True:
    choice = show_menu()
    if choice == 1:
        while True:
            try:
                book_id = int(input("Enter the book id: "))
                break
            except ValueError:
                print("Invalid input! book id must be a integer try again.")
        title = input("Enter the book title: ")
        author = input("Enter the author name: ")
        book_type = input("Enter the book type: ")
        location = input("Enter the location: ")
        book = Book(book_id, title, author, book_type, location)
        library.add_book(book)
        print("Book added successfully")

    elif choice == 2:
        search_text = input("Enter the name of the book you want: ").strip()
        result = library.search_book(search_text)
        print(result)
    elif choice == 3:
        book_id = int(input("Enter the book id you want: "))
        library.borrow_book(book_id)
    elif choice == 4:
        book_id = int(input("Enter the book id you want to return: "))
        library.return_book(book_id)
    elif choice == 5:
        book_id = int(input("Enter the book id you want to delete: "))
        library.delete_book(book_id)
    else:
        print("Thank you")
        break