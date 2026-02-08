# Importing ABC and abstractmethod to create abstract classes
from abc import ABC, abstractmethod

# ----------------------------------------
# Base Class: Person
# ----------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name      # Public attribute
        self.age = age        # Public attribute

    def display_info(self):
        # Display common person details
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# ----------------------------------------
# Single Inheritance: Patient inherits from Person
# ----------------------------------------
class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)   # Call Person constructor
        self.disease = disease        # Patient-specific attribute

    def display_info(self):
        super().display_info()        # Call Person's method
        print(f"Disease: {self.disease}")

# ----------------------------------------
# Multilevel Inheritance: Doctor -> Surgeon
# ----------------------------------------
class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def display_info(self):
        super().display_info()
        print(f"Specialization: {self.specialization}")

class Surgeon(Doctor):  # Surgeon is a specialized Doctor
    def __init__(self, name, age, specialization, on_call_status):
        super().__init__(name, age, specialization)
        self.on_call_status = on_call_status

    def display_info(self):
        super().display_info()
        print(f"On Call Status: {self.on_call_status}")

# ----------------------------------------
# Hierarchical Inheritance: Staff also inherits from Person
# ----------------------------------------
class Staff(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")

# ----------------------------------------
# Encapsulation: Appointment class with private fields
# ----------------------------------------
class Appointment:
    def __init__(self, patient_name, doctor_name, appointment_time):
        self.__patient_name = patient_name        # Private field
        self.__doctor_name = doctor_name          # Private field
        self.__appointment_time = appointment_time  # Private field

    # Public method to access appointment details
    def get_details(self):
        return f"Appointment - Patient: {self.__patient_name}, Doctor: {self.__doctor_name}, Time: {self.__appointment_time}"

# ----------------------------------------
# Polymorphism: Compile-Time (Overloading simulated)
# ----------------------------------------
class Billing:
    def generate_bill(self, amount=None, days=None):
        if amount is not None and days is not None:
            return amount * days   # If both provided, multiply
        elif amount is not None:
            return amount          # Fixed amount
        else:
            return 0               # Default case

# ----------------------------------------
# Abstraction: Abstract base class and implementation
# ----------------------------------------
class Department(ABC):
    @abstractmethod
    def department_info(self):
        pass   # Abstract method; must be overridden

class Cardiology(Department):
    def department_info(self):
        print("Cardiology Department: Handles heart-related issues.")

class Neurology(Department):
    def department_info(self):
        print("Neurology Department: Handles nervous system issues.")

# ----------------------------------------
# MAIN EXECUTION BLOCK - Test all classes
# ----------------------------------------
if __name__ == "__main__":
    print("=== PATIENT ===")
    p = Patient("John Doe", 30, "Flu")  # Create Patient object
    p.display_info()                    # Show patient details

    print("\n=== DOCTOR ===")
    d = Doctor("Dr. Smith", 45, "Pediatrics")  # Create Doctor
    d.display_info()

    print("\n=== SURGEON ===")
    s = Surgeon("Dr. House", 50, "Cardiology", True)  # Create Surgeon
    s.display_info()

    print("\n=== STAFF ===")
    st = Staff("Anna", 28, "Receptionist")   # Create Staff
    st.display_info()

    print("\n=== APPOINTMENT ===")
    a = Appointment("John Doe", "Dr. Smith", "10:30 AM")  # Create Appointment
    print(a.get_details())                                # Show appointment

    print("\n=== BILLING ===")
    b = Billing()
    print("Total Bill (Fixed):", b.generate_bill(500))         # One-arg
    print("Total Bill (Per Day):", b.generate_bill(500, 3))    # Two-arg

    print("\n=== DEPARTMENTS ===")
    dept1 = Cardiology()
    dept1.department_info()  # Abstract method call

    dept2 = Neurology()
    dept2.department_info()
