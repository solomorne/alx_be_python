### library_system.py

# --- Base Class: Book ---
class Book:
    """
    Base class for all book types.
    """
    def __init__(self, title: str, author: str):
        """Initializes the title and author."""
        self.title = title
        self.author = author

    def __str__(self) -> str:
        """
        String Representation: Returns a user-friendly string with basic details.
        This is used when the object is printed.
        """
        return f"{self.title} by {self.author}"

# --- Derived Class: EBook (Inherits from Book) ---
class EBook(Book):
    """
    Represents a digital book, inheriting basic attributes and adding file_size.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """Initializes EBook attributes, calling the base class constructor."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self) -> str:
        """
        Overrides the base method to include EBook-specific details.
        """
        # Call the parent's __str__ for the base details and append specific info
        base_str = super().__str__()
        return f"{base_str} (EBook, Size: {self.file_size}MB)"

# --- Derived Class: PrintBook (Inherits from Book) ---
class PrintBook(Book):
    """
    Represents a physical book, inheriting basic attributes and adding page_count.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """Initializes PrintBook attributes, calling the base class constructor."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        """
        Overrides the base method to include PrintBook-specific details.
        """
        # Call the parent's __str__ for the base details and append specific info
        base_str = super().__str__()
        return f"{base_str} (PrintBook, Pages: {self.page_count})"

# --- Composition Class: Library ---
class Library:
    """
    Manages a collection of Book, EBook, and PrintBook instances using composition.
    """
    def __init__(self):
        """Initializes the library with an empty list of books."""
        self.books = [] 

    def add_book(self, book: Book):
        """
        Adds a Book instance (or derived EBook/PrintBook instance) to the collection.
        """
        if isinstance(book, Book):
            self.books.append(book)
            # Printing the book here automatically calls its __str__ method
            print(f"✅ Added: {book.title}")
        else:
            print("❌ Error: Item is not a valid Book type.")

    def list_books(self):
        """
        Prints details of each book in the library using the __str__ method.
        """
        if not self.books:
            print("\nThe library shelf is empty.")
            return

        print("\n📚 Current Library Collection:")
        for i, book in enumerate(self.books, 1):
            # When you use 'print(book)', Python automatically calls book.__str__().
            # This demonstrates polymorphism: the same method call produces different
            # output based on whether the object is a Book, EBook, or PrintBook.
            print(f"{i}. {book}")