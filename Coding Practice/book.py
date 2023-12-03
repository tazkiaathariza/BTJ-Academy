"""Class for making book data"""
class Book:
    """Represents books"""
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.genre = None
