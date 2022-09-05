class Book:
    def __init__(self,name,date):
        self.name = name
        self.date = date
        self.author = None
    def addAuthor(self,autor):
        self.author=autor


class Author:
    def __init__(self, firstname,lastname,date):
        self.firstname=firstname
        self.lastname=lastname
        self.date=date





book = Book("Book","22.5.2022")
tekija = Author("Author", "lastname", "11.5.2022")


book.addAuthor(tekija)

print(book.author.lastname)
