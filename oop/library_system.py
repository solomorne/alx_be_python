### library_system.py

# --- Base Class: Book ---
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        """
        Modified to output: Book: [Title] by [Author]
        """
        return f"Book: {self.title} by {self.author}"

# --- Derived Class: EBook ---
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self) -> str:
        """
        Modified to output: EBook: [Title] by [Author], File Size: [size]KB
        """
        # Call the parent's __str__ to get the title and author details
        base_str_content = super().__str__().replace("Book: ", "") 
        # Remove the "Book: " prefix from the base string
        return f"EBook: {base_str_content}, File Size: {self.file_size}KB"

# --- Derived Class: PrintBook ---
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        """
        Modified to output: PrintBook: [Title] by [Author], Page Count: [pages]
        """
        # Call the parent's __str__ to get the title and author details
        base_str_content = super().__str__().replace("Book: ", "")
        # Remove the "Book: " prefix from the base string
        return f"PrintBook: {base_str_content}, Page Count: {self.page_count}"

# --- Composition Class: Library ---
class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self, book: Book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        if not self.books:
            print("\nThe library shelf is empty.")
            return

        print("\n📚 Current Library Collection:")
        for book in self.books:
            # Printing the book triggers the appropriate __str__ method
            print(book)