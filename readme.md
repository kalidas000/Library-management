# 📚 Library Management System

A simple command-line Library Management System built with Python to practice Object-Oriented Programming (OOP) concepts.

## Features

- Add books
- Search books by title
- Borrow books
- Return books
- Delete books
- Track book availability
- Manage books using book IDs
- Basic input validation

## OOP Concepts Practiced

- Classes and objects
- Constructors (`__init__`)
- Instance attributes
- Instance methods
- `self`
- Object-to-object interaction
- Lists of objects
- `for` loops and `for...else`
- `enumerate()`
- Conditional statements
- Exception handling

## Classes

### Book

The `Book` class stores information about each book:

- Book ID
- Title
- Author
- Book type
- Location
- Availability status

It also handles borrowing and returning books.

### Library

The `Library` class manages the collection of books and provides functionality for:

- Adding books
- Searching books
- Borrowing books
- Returning books
- Deleting books

## Example Menu

```text
===== LIBRARY MANAGEMENT SYSTEM =====

1. Add Book
2. Search Book
3. Borrow Book
4. Return Book
5. Delete Book
6. Exit