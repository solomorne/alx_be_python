### library_system.py

# --- Base Class: Book (The parent blueprint) ---
class Book:
    """
    Base class for all book types.
    """
    def __init__(self, title: str, author: str):
        """Initializes the title and author."""
        self.title = title
        self.author = author

    def get_details(self) -> str:
        """Returns basic book details."""
        return f"{self.title} by {self.author}"

# --- Derived Class: EBook (Inherits from Book) ---
class EBook(Book):
    """
    Represents a digital book, inheriting basic attributes and adding file_size.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """Initializes EBook attributes, calling the base class constructor."""
        # Call the parent's __init__ method
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self) -> str:
        """Overrides base method to include file size."""
        # Use the parent's get_details and add specific info
        base_details = super().get_details()
        return f"{base_details} (EBook, Size: {self.file_size}MB)"

# --- Derived Class: PrintBook (Inherits from Book) ---
class PrintBook(Book):
    """
    Represents a physical book, inheriting basic attributes and adding page_count.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """Initializes PrintBook attributes, calling the base class constructor."""
        # Call the parent's __init__ method
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self) -> str:
        """Overrides base method to include page count."""
        base_details = super().get_details()
        return f"{base_details} (PrintBook, Pages: {self.page_count})"

# --- Composition Class: Library (Manages a collection of books) ---
class Library:
    """
    Manages a collection of Book, EBook, and PrintBook instances using composition.
    """
    def __init__(self):
        """Initializes the library with an empty list of books."""
        # The 'books' list *is part of* the Library object (composition)
        self.books = [] 

    def add_book(self, book: Book):
        """
        Adds a Book instance (or derived EBook/PrintBook instance) to the collection.
        """
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added: {book.title}")
        else:
            print("Error: Item is not a valid Book type.")

    def list_books(self):
        """
        Prints the details for all books currently in the library collection.
        """
        if not self.books:
            print("\nThe library shelf is empty.")
            return

        print("\n📚 Current Library Collection:")
        for i, book in enumerate(self.books, 1):
            # Polymorphism in action: calling .get_details() executes the correct 
            # method based on the book's specific type (Book, EBook, or PrintBook).
            print(f"{i}. {book.get_details()}")