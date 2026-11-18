class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._borrower = None

    def is_available(self):
        if not self._borrower:
            return True
        else:
            return False

    def lend_to(self, member):
        self._borrower = member

    def take_back(self):
        self._borrower = None

    def __str__(self):
        if self.is_available():
            return f"{self.title} by {self.author} (available)"
        else:
            return f"{self.title} by {self.author} (borrowed by {self._borrower.name})"


class Member:
    def __init__(self, name, limit=2):
        self.name = name
        self.limit = limit
        self._books = []

    def borrow(self, book):
        if len(self._books) >= self.limit or not book.is_available():
            return False
        else:
            self._books.append(book)
            book.lend_to(self)
            return True

    def give_back(self, book):
        if not book in self._books:
            return False
        else:
            book.take_back()
            self._books.remove(book)
            return True

    def get_books(self):
        return list(self._books)


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def lend(self, title, member):
        for book in self._books:
            if book.title == title:
                if member.borrow(book):
                    return f"{title} lent to {member.name}"
                else:
                    return "Cannot lend"
        return "No such book"

    def report(self):
        report = ""
        for book in self._books:
            report += str(book) + "\n"
        return report.rstrip("\n")


dune = Book("Dune", "Herbert")
emma = Book("Emma", "Austen")
ulysses = Book("Ulysses", "Joyce")

lib = Library()
lib.add_book(dune)
lib.add_book(emma)
lib.add_book(ulysses)

anna = Member("Anna")

print(lib.lend("Dune", anna))  # Dune lent to Anna
print(lib.lend("Dune", Member("Jan")))  # Cannot lend
print(lib.lend("Hamlet", anna))  # No such book
print(lib.lend("Emma", anna))  # Emma lent to Anna
print(lib.lend("Ulysses", anna))  # Cannot lend
print(dune)  # Dune by Herbert (borrowed by Anna)
print(anna.give_back(ulysses))  # False
print(anna.give_back(dune))  # True
print(dune)  # Dune by Herbert (available)
print(lib.report())
# Dune by Herbert (available)
# Emma by Austen (borrowed by Anna)
# Ulysses by Joyce (available)

books = anna.get_books()
books.clear()
print(len(anna.get_books()))  # 1
