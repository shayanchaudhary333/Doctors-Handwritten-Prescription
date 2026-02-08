from abc import ABC, abstractmethod

# ----------------------------------------
# Base Class: Product
# ----------------------------------------
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.__stock_quantity = 0
        self.__supplier_info = None

    # Encapsulation with getters/setters
    def set_stock(self, quantity):
        self.__stock_quantity = quantity

    def get_stock(self):
        return self.__stock_quantity

    def set_supplier(self, supplier):
        self.__supplier_info = supplier

    def get_supplier(self):
        return self.__supplier_info

    def get_details(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: ₹{self.price}"

# ----------------------------------------
# Inheritance: Electronic & Furniture
# ----------------------------------------
class Electronic(Product):
    def __init__(self, product_id, name, price, warranty_period):
        super().__init__(product_id, name, price)
        self.warranty_period = warranty_period

    def get_details(self):
        return super().get_details() + f", Warranty: {self.warranty_period} year(s)"

class Furniture(Product):
    def __init__(self, product_id, name, price, material):
        super().__init__(product_id, name, price)
        self.material = material

    def get_details(self):
        return super().get_details() + f", Material: {self.material}"

# ----------------------------------------
# Polymorphism: Compile-Time (Simulated Overloading)
# ----------------------------------------
class Order:
    def place_order(self, product, quantity=1):
        total = product.price * quantity
        return f"Order placed for {quantity} x {product.name} = ₹{total}"

# ----------------------------------------
# Abstraction: Warehouse Base Class
# ----------------------------------------
class Warehouse(ABC):
    @abstractmethod
    def track_inventory(self):
        pass

class LocalWarehouse(Warehouse):
    def track_inventory(self):
        print("Tracking inventory in Local Warehouse")

class CentralWarehouse(Warehouse):
    def track_inventory(self):
        print("Tracking inventory in Central Warehouse")

# ----------------------------------------
# Supplier Class
# ----------------------------------------
class Supplier:
    def __init__(self, supplier_id, name, contact):
        self.supplier_id = supplier_id
        self.name = name
        self.contact = contact

    def get_supplier_info(self):
        return f"{self.name} (Contact: {self.contact})"

# ----------------------------------------
# MAIN EXECUTION BLOCK
# ----------------------------------------
if __name__ == "__main__":
    # Create Suppliers
    sup1 = Supplier("SUP101", "ElectroWorld", "9876543210")
    sup2 = Supplier("SUP102", "FurniDecor", "9876509876")

    # Create Products
    e1 = Electronic("E001", "Laptop", 50000, 2)
    f1 = Furniture("F001", "Sofa", 15000, "Leather")

    # Set stock and supplier (Encapsulation)
    e1.set_stock(10)
    e1.set_supplier(sup1.get_supplier_info())

    f1.set_stock(5)
    f1.set_supplier(sup2.get_supplier_info())

    # Display Product Details
    print("\n--- Product Details ---")
    print(e1.get_details())
    print(f"Stock: {e1.get_stock()} | Supplier: {e1.get_supplier()}")

    print("\n" + f1.get_details())
    print(f"Stock: {f1.get_stock()} | Supplier: {f1.get_supplier()}")

    # Place Orders (Polymorphism)
    print("\n--- Order Placement ---")
    order = Order()
    print(order.place_order(e1, 2))
    print(order.place_order(f1))

    # Warehouse Management (Abstraction)
    print("\n--- Warehouses ---")
    lw = LocalWarehouse()
    cw = CentralWarehouse()
    lw.track_inventory()
    cw.track_inventory()
