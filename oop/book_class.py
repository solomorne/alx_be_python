class Book:

    """ Initialize a book instance with title, author and year."""
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):   # Create a destructor that prints a statement after deletion
        print(f"Deleting {self.title}")

    def __str__(self):   # Use a String Representation
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):  # USe an Official representation
        return f"Book('{self.title}', '{self.author}', {self.year})"
