class Book:
    """
    A Book class that demonstrates Python magic methods.
    
    This class models a book with title, author, and publication year,
    showcasing how magic methods control object behavior in Python.
    """
    
    def __init__(self, title, author, year):
        """
        Constructor method - called when creating a new Book instance.
        
        This magic method initializes the object's attributes when you write:
        my_book = Book("1984", "George Orwell", 1949)
        
        Args:
            title (str): The title of the book
            author (str): The author of the book  
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor method - called when the object is about to be destroyed.
        
        This magic method is invoked when the object is deleted from memory,
        either explicitly with 'del' or when it goes out of scope.
        Note: In CPython, this usually happens immediately, but in other 
        Python implementations, it might be delayed due to garbage collection.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        String representation method - called by str() and print().
        
        This magic method defines what gets displayed when you:
        - print(book_instance)
        - str(book_instance)
        - Use the object in string formatting
        
        This should return a human-readable, informal string representation.
        
        Returns:
            str: A formatted string showing book details for end users
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Official representation method - called by repr().
        
        This magic method defines the "official" string representation of the object.
        The goal is to return a string that, when passed to eval(), would 
        recreate the object (when possible).
        
        This is primarily used for:
        - repr(book_instance) 
        - Displaying objects in the Python interpreter
        - Debugging and development
        
        Returns:
            str: A string that could recreate this Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
