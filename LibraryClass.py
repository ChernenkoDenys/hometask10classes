# Створіть клас Library, який зберігає книги (у вигляді списку екземплярів класу Book). 
# Реалізуйте __len__ 
# для повернення кількості книг 
# у бібліотеці та __getitem__ для доступу до книги за заданим індексом.


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
    
class Library:
    
    def __init__(self, book_list):
        self.book_list = book_list
    
    def __len__(self):
        return len(self.book_list)
    
    def __getitem__(self, key):
        if key > len(self.book_list)-1:
            raise IndexError("Cannot access element in this Index")
        else:
            return self.book_list[key]
    

b1 = Book("Title1", "Author1")

b2 = Book("Title2", "Author2")

b3 = Book("Title3", "Author3")

library = Library([b1, b2, b3])
print(len(library))
print(library[2])