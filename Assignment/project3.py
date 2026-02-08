from abc import ABC, abstractmethod

# ----------------------------------------
# Base Class: Person
# ----------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_profile(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# ----------------------------------------
# Inheritance: Student inherits from Person
# ----------------------------------------
class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def display_profile(self):
        super().display_profile()
        print(f"Roll No: {self.roll_no}")
        print(f"Course: {self.course}")

# ----------------------------------------
# Inheritance: Teacher inherits from Person
# ----------------------------------------
class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def display_profile(self):
        super().display_profile()
        print(f"Employee ID: {self.employee_id}")
        print(f"Subject: {self.subject}")

# ----------------------------------------
# Encapsulation: Result class with private fields
# ----------------------------------------
class Result:
    def __init__(self, marks):
        self.__marks = marks
        self.__grade = self.__calculate_grade()

    def __calculate_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 60:
            return "C"
        else:
            return "D"

    def get_marks(self):
        return self.__marks

    def get_grade(self):
        return self.__grade

# ----------------------------------------
# Polymorphism: generateReport() - overloading (simulated)
# ----------------------------------------
class Report:
    def generate_report(self, student=None):
        if student:
            print(f"Generating report for {student.name}...")
        else:
            print("Generating report for all students...")

# ----------------------------------------
# Abstraction: Department base class
# ----------------------------------------
class Department(ABC):
    @abstractmethod
    def course_list(self):
        pass

class Science(Department):
    def course_list(self):
        print("Science Courses: Physics, Chemistry, Biology")

class Commerce(Department):
    def course_list(self):
        print("Commerce Courses: Accounts, Economics, Business Studies")

class Arts(Department):
    def course_list(self):
        print("Arts Courses: History, Geography, Political Science")

# ----------------------------------------
# MAIN EXECUTION
# ----------------------------------------
if __name__ == "__main__":
    # Creating student and teacher
    s1 = Student("Anjali", 20, "S101", "B.Sc")
    t1 = Teacher("Mr. Sharma", 45, "T001", "Physics")

    # Display profiles
    print("\n--- Student Profile ---")
    s1.display_profile()

    print("\n--- Teacher Profile ---")
    t1.display_profile()

    # Result
    print("\n--- Student Result ---")
    result1 = Result(87)
    print(f"Marks: {result1.get_marks()}")
    print(f"Grade: {result1.get_grade()}")

    # Report Generation
    print("\n--- Reports ---")
    report = Report()
    report.generate_report(s1)
    report.generate_report()

    # Departments
    print("\n--- Departments ---")
    sci = Science()
    com = Commerce()
    art = Arts()

    sci.course_list()
    com.course_list()
    art.course_list()
