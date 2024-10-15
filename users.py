from abc import ABC ,abstractmethod
from orders import Order
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self,restaurent):
        restaurent.menu.Show_menu()

    def add_to_cart(self,restaurent,item_name,quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if int(quantity) > int(item.quantity):
                print(f"Sorry, we don't have {quantity} quantity of this item.")
                print(f"We have {item.quantity} of this item")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item added Successfully")
        else:
            print("Item not found")

    def view_cart(self):
        print("*****View cart*****")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total price : {self.cart.total_price()}")

    def pay_bill(self):
        print(f"{self.cart.total_price()} paid successfully")
        self.cart.clear()


class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

emp = Employee('Karim',121212,'Karim@gmail.com','Anowara, Chittagong',22,'Chef',120000)
# print(emp.name,emp.phone,emp.email,emp.address,emp.age,emp.designation,emp.salary)

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)

    def view_employee(self,restaurent):
        restaurent.view_employee()

    def add_new_item(self,restaurent,item):
        # restaurent.add_new_item(item)
        restaurent.menu.add_menu_item(item)

    def remove_item(self,restaurent,item):
        restaurent.menu.remove_item(item)

    def view_menu(self,restaurent):
        restaurent.menu.Show_menu()



# ad = Admin('Ahmadullah',12121,'Ahmad@gmail.com','Anowara Chittagong')
# print(ad.name)
# # res = Restaurent("Karim Restaurent")
# emp = Employee('karim',32323,'Karim#@','ANoeadkf',22,'chef',2323)
# # ad.add_employee(res,emp)
# ad.add_employee(res,emp)
# # res.view_employee()
# ad.view_employee(res)
# mu = Menu()
# item = FoodItem('Biryani',120,10)
# item1 = FoodItem('kacci',120,10)
# ad.add_new_item(res,item)
# ad.add_new_item(res,item1)
# # res.menu.Show_menu()
# customer1 = Customer('chadni',1212,'Chadni@','sohore')
# customer1.view_menu(res)

# item_name = input("Enter item Name : ")
# item_quantity = int(input("Enter the quantity : "))
# customer1.add_to_cart(res,item_name,item_quantity)
# customer1.view_cart()