def assignment():
    print("Object Oriented Programming")

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category

    @property
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price

    def get_info(self):
        return f"Product: {self.name}, Price: ${self.get_price}, Category: {self.category}"

    def apply_discount(self, discount):
        if discount < 0 or discount > 100:
            raise ValueError("Discount must be between 0 and 100")
        self.__price -= self.__price * (discount / 100)

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.get_price}, Category: {self.category}"
    
    def __add__(self, other):
        return self.get_price + other.get_price

def task1():
    print("\n -- task 1 - Create a Product class -- ")
    product1 = Product("Laptop", 999.99, "Electronics")
    print(product1.get_info())  
    product1.apply_discount(10)
    print("After applying discount:")   
    print(product1.get_info())

    product2 = Product("Camera", 999.99, "Electronics")
    print(product2.get_info())  
    product2.apply_discount(20)
    print("After applying discount:")   
    print(product2.get_info())


def task2():
    print("\n -- task 2 - Constructor and Encapsulation -- ")
    product3 = Product("Headphones", 199.99, "Electronics")
    print(product3.get_info())
    product3.set_price(249.99)
    print("After updating price:")
    print(product3.get_info())

class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Warranty: {self.warranty_years} years"
    


def task3():
    print("\n -- task 3 - Inheritance (Single level) -- ")
    electronic_product = ElectronicProduct("Smartphone", 799.99, "Electronics", 2)
    print(electronic_product.get_info())

class Laptop(Product):
    def __init__(self, name, price, category, ram):
        super().__init__(name, price, category)
        self.ram = ram

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, RAM: {self.ram} GB"
    
class Mobile(Product):
    def __init__(self, name, price, category, screen_size):
        super().__init__(name, price, category)
        self.screen_size = screen_size

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Screen Size: {self.screen_size} inches"
    
def task4():
    print("\n -- task 4 - Polimorphism (Method Overriding) -- ")
    laptop = Laptop("Gaming Laptop", 1499.99, "Electronics", 16)
    mobile = Mobile("Flagship Smartphone", 999.99, "Electronics", 6.5)
    # print(laptop.get_info())
    # print(mobile.get_info())
    # loop that iterate over objects of Laptop and Mobile and call get_info on each to show polimorphism
    products = [laptop, mobile]
    for product in products:
        print(product.get_info())   

from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass 

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ${amount}")

def task5():
    print("\n -- task 5 - Abstract Base Classes -- ")
    credit_card = CreditCardPayment()
    upi = UPIPayment()

    credit_card.process_payment(100)
    upi.process_payment(200)

def task6():
    print("\n -- task 6 - Magic Methods and Operator Overloading -- ")
    product_a = Product("Product A", 50, "Category A")
    product_b = Product("Product B", 30, "Category B")
    print(product_a)
    print(product_b)
    total_price = product_a + product_b
    print(f"Total price of {product_a.name} and {product_b.name} is: ${total_price}")


class Inventory:
    products = []
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.get_price
        return total
    
    def show_all_products(self):
        for product in self.products:
            print(product)

class Store:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def add_new_product(self, product):
        self.inventory.add_product(product)

    def show_summary(self):
        print(f"Store: {self.name}")
        print("Products in inventory:")
        self.inventory.show_all_products()
        print(f"Total inventory value: ${self.inventory.get_total_value()}")

    def __add__(self, other):
        return self.inventory.get_total_value() + other.inventory.get_total_value()
    
def task7():
    print("\n -- task 7 - Mini project : Store Inventory Management System -- ")
    inventory1 = Inventory([])
    store1 = Store("Tech Store", inventory1)

    product1 = Product("Laptop", 999.99, "Electronics")
    product2 = Product("Camera", 499.99, "Electronics")
    product3 = Product("Headphones", 199.99, "Electronics")

    store1.add_new_product(product1)
    store1.add_new_product(product2)
    store1.add_new_product(product3)

    store1.show_summary()

def main():
    assignment()
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()

if __name__ == "__main__":
    main()