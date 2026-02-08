from abc import ABC, abstractmethod

# ----------------------------------------
# Base Class: Member
# ----------------------------------------
class Member:
    def __init__(self, member_id, name, contact):
        self.member_id = member_id
        self.name = name
        self.contact = contact

    def display_member_details(self):
        print(f"ID: {self.member_id}")
        print(f"Name: {self.name}")
        print(f"Contact: {self.contact}")

# ----------------------------------------
# Inheritance: StudentMember and FacultyMember inherit from Member
# ----------------------------------------
class StudentMember(Member):
    def __init__(self, member_id, name, contact, college_name):
        super().__init__(member_id, name, contact)
        self.college_name = college_name

    def display_member_details(self):
        super().display_member_details()
        print(f"College: {self.college_name}")

class FacultyMember(Member):
    def __init__(self, member_id, name, contact, department):
        super().__init__(member_id, name, contact)
        self.department = department

    def display_member_details(self):
        super().display_member_details()
        print(f"Department: {self.department}")

# ----------------------------------------
# Encapsulation: Transaction class with private fields
# ----------------------------------------
class Transaction:
    def __init__(self, book_id, issue_date, return_date):
        self.__book_id = book_id
        self.__issue_date = issue_date
        self.__return_date = return_date

    def get_transaction_details(self):
        return f"Book ID: {self.__book_id}, Issued: {self.__issue_date}, Return: {self.__return_date}"

# ----------------------------------------
# Compile-Time Polymorphism: calculateFine
# ----------------------------------------
class FineCalculator:
    def calculate_fine(self, days_late=None, member_type=None):
        if member_type == "student":
            return 2 * days_late if days_late else 0
        elif member_type == "faculty":
            return 1 * days_late if days_late else 0
        else:
            return 0

# ----------------------------------------
# Abstraction: LibraryDepartment abstract class
# ----------------------------------------
class LibraryDepartment(ABC):
    @abstractmethod
    def manage_section(self):
        pass

class ScienceSection(LibraryDepartment):
    def manage_section(self):
        print("Managing the Science Books Section")

class ArtsSection(LibraryDepartment):
    def manage_section(self):
        print("Managing the Arts Books Section")

# ----------------------------------------
# Other Classes: Book and Library
# ----------------------------------------
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def get_book_info(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

# ----------------------------------------
# MAIN EXECUTION BLOCK
# ----------------------------------------
if __name__ == "__main__":
    # Books
    book1 = Book("Python 101", "John Smith", "123456")
    book2 = Book("Data Structures", "Alice Brown", "654321")

    # Members
    student = StudentMember("S001", "Ravi", "9876543210", "ABC College")
    faculty = FacultyMember("F001", "Dr. Meena", "9876512345", "Computer Science")

    # Transactions
    t1 = Transaction("123456", "2025-06-01", "2025-06-10")

    # Fine Calculation
    fine_calc = FineCalculator()
    print("\nFine for student (3 days late):", fine_calc.calculate_fine(3, "student"))
    print("Fine for faculty (3 days late):", fine_calc.calculate_fine(3, "faculty"))

    # Library Setup
    lib = Library()
    lib.add_book(book1)
    lib.add_book(book2)
    lib.add_member(student)
    lib.add_member(faculty)
    lib.add_transaction(t1)

    # Display Member Details
    print("\n--- Student Member ---")
    student.display_member_details()

    print("\n--- Faculty Member ---")
    faculty.display_member_details()

    # Display Book Info
    print("\n--- Books in Library ---")
    for book in lib.books:
        print(book.get_book_info())

    # Display Transactions
    print("\n--- Transactions ---")
    for transaction in lib.transactions:
        print(transaction.get_transaction_details())

    # Manage Departments
    print("\n--- Departments ---")
    sci = ScienceSection()
    art = ArtsSection()
    sci.manage_section()
    art.manage_section()
