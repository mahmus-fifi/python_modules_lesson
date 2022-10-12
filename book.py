# program to display info about a book 
class Book():
    """This Class is an example on Python Modules"""
    def __init__(self, book_name, author, sales):
        self.book_name = book_name
        self.author = author
        self.sales = sales 
        
    def __str__(self):
        print('Book Summary')
        return (f'Book Author: {self.author}, Book Name: {self.book_name}, Sales: {self.sales}')
    
    def AboutBook(self):
        print('An enchanting story about a young kid called Alex')
        
        
        