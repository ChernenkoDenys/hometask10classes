# Розробіть клас Book, атрибутами якого є title та author. 
# Реалізуйте __eq__ для перевірки рівності на 
# основі назви та автора та __ne__ для перевірки нерівності.

class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __eq__(self, other):
        return (self.title == other.title) and (self.author == other.author)
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return f"Book with title: '{self.title}' and with authot: '{self.author}'"

        


book1 = Book("Title1", "Author1")
book2 = Book("Title2", "Author2")
book3 = Book("Title1", "Author1")

print(book1 != book2)

print(book1 == book2)

print(book1 == book3)