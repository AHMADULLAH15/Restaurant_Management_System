from food_Item import FoodItem
from menu import Menu
from orders import Order
from restaurents import Restaurent
from users import Customer,Admin,Employee


mamar_restaurent = Restaurent("Mamar Restaurent")

def customer_menu():
    name = input("Enter your name : ")
    phone = input("Enter your phone number : ")
    email = input("Enter your Email : ")
    address = input("Enter your Address : ")
    customer = Customer(name=name,phone=phone,email=email,address=address)

    while True:
        print(f"Welcome {customer.name}")
        print("1. View Menu")
        print("2. add item to cart")
        print("3. view cart")
        print("4. paybill")
        print("5. Exit")

        choice = int(input("Enter your choice : "))
        if choice == 1:
            customer.view_menu(mamar_restaurent)
        elif choice == 2:
            item_name = input("Enter your item name : ") 
            quantity = input("Enter your  quantity : ") 
            customer.add_to_cart(mamar_restaurent,item_name=item_name,quantity=quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid choice")

def admin_menu():
    name = input("Enter your name : ")
    phone = input("Enter your phone number : ")
    email = input("Enter your Email : ")
    address = input("Enter your Address : ")
    admin = Admin(name=name,phone=phone,email=email,address=address)

    while True:
        print(f"Welcome Admin {admin.name}")
        print("1. Add new Item")
        print("2. add new employee")
        print("3. view employee")
        print("4. view item")
        print("5. delete item")
        print("6. Exit")

        choice = int(input("Enter your choice : "))
        if choice == 1:
            item_name = input("Enter your item name : ")
            item_price = int(input("Enter your item price : "))
            item_quantity = int(input("Enter your item quantity : "))
            item = FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_restaurent,item)
        elif choice == 2:
            name = input("Enter your Employee name : ")
            phone = input("Enter your Employee phone : ")
            email = input("Enter your Employee email : ")
            address = input("Enter your Employee address : ")
            age = input("Enter your Employee age : ")
            designation = input("Enter your Employee designation : ")
            salary = input("Enter your Employee salary : ")
            employee = Employee(name=name,phone=phone,email=email,address=address,age=age,designation=designation,salary=salary)
            admin.add_employee(mamar_restaurent,employee=employee)
            # admin.add_employee(name, phone, email, address,age,designation,salary)
        elif choice == 3:
            admin.view_employee(mamar_restaurent)
        elif choice == 4:
            admin.view_menu(mamar_restaurent)
        elif choice == 5:
            item_name = input("Enter your item name : ")
            admin.remove_item(mamar_restaurent,item=item_name)
            break
        elif choice == 6:
            break
        else:
            print("Invalid choice")

while True:
    print("Welcome to Mamar Restaurent")
    print("1. customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid choice")