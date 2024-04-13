import os

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, file_path):
        self.file_path = file_path
        self.books = self.load_data()

    def load_data(self):
        books = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                for line in file:
                    title, author = line.strip().split(',')
                    books.append(Book(title, author))
        return books

    def save_data(self):
        with open(self.file_path, 'w') as file:
            for book in self.books:
                file.write(f"{book.title},{book.author}\n")

    def add_book(self):
        title = input("Enter title of the book: ")
        author = input("Enter author of the book: ")
        self.books.append(Book(title, author))
        print("Book added successfully!")

    def remove_book(self):
        title = input("Enter title of the book to remove: ")
        author = input("Enter author of the book to remove: ")
        for book in self.books:
            if book.title == title and book.author == author:
                self.books.remove(book)
                print("Book removed successfully!")
                return
        print("Book not found!")

    def display_books(self):
        if self.books:
            print("===== Books Available =====")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book.title} by {book.author}")
            print("==========================")
        else:
            print("No books available.")

    def display_menu(self):
        print("===== Library Management System =====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Exit")
        print("=====================================")

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.display_books()
            elif choice == '4':
                self.save_data()
                print("Thank you for using the Library Management System!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    library = Library("library_data.txt")
    library.main()
