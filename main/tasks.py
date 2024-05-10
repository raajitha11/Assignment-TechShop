import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from dao.paymentDao import PaymentProcessingSystem
from exception.exceptions import IncompleteOrderException
from dao.CustomerDao import CustomerDao
from dao.InventoryDao import InventoryDao
from dao.OrderDao import OrderDao
from dao.OrderDetailsDao import OrderDetailsDao
from dao.ProductDao import ProductDao



class Menu:
    def __init__(self):
        self.customer_obj = CustomerDao()
        self.product_obj = ProductDao()
        self.order_obj = OrderDao()
        self.orderdetails_obj = OrderDetailsDao()
        self.inventory_obj = InventoryDao()
        self.payment_obj = PaymentProcessingSystem()

    def display_menu(self):
        print("1. Customer Registration")
        print("2. Product Catalog Management")
        print("3. Place Orders")
        print("4. Track Order Status")
        print("5. Inventory Management")
        print("6. Sales Reports")
        print("7. Customer Account Updates")
        print("8. Payment Processing")
        print("9. Product Search and Recommendations")

    def handle_choice(self, choice):
        if choice == "1":
            self.customer_registration()
        elif choice == "2":
            self.product_catalog_management()
        elif choice == "3":
            self.place_orders()
        elif choice == "4":
            self.track_order_status()
        elif choice == "5":
            self.inventory_management()
        elif choice == "6":
            self.sales_reports()
        elif choice == "7":
            self.customer_account_updates()
        elif choice == "8":
            self.payment_processing()
        elif choice == "9":
            self.product_search_and_recommendations()
        else:
            print("Invalid choice")

    def customer_registration(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")
        self.customer_obj.insertCustomer(first_name, last_name, email, phone, address)

    def product_catalog_management(self):
        print(
            "\n1. Get Product Details\n2. Insert Product\n3. Update Product Info\n4. Check Product Stock\n"
        )
        choice_product = input("Enter your choice: ")
        if choice_product == "1":
            product_id = input("Enter Product ID: ")
            self.product_obj.get_product_details(product_id)
        elif choice_product == "2":
            product_name = input("Enter Product Name: ")
            description = input("Enter Product Description: ")
            price = input("Enter Product Price: ")
            self.product_obj.insert_product(product_name, description, price)
        elif choice_product == "3":
            product_id = input("Enter Product ID: ")
            price = input("Enter New Price: ")
            description = input("Enter New Description: ")
            self.product_obj.update_product_info(product_id, price, description)
        elif choice_product == "4":
            product_id = input("Enter Product ID: ")
            self.product_obj.is_product_in_stock(product_id)
        else:
            print("Invalid choice. Please try again.")


    def place_orders(self):
        try:
            product_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter quantity: "))
            customer_id = int(input("Enter Customer ID: "))

            if not self.inventory_obj.is_product_available(product_id, quantity):
                raise IncompleteOrderException("Selected product is not available in the required quantity.")
            
            order_id = self.order_obj.insert_order(customer_id)
            self.orderdetails_obj.insert_order_detail(order_id, product_id, quantity)
            self.inventory_obj.remove_from_inventory(product_id, quantity)
            self.order_obj.calculate_total_amount(order_id)
            print("Order placed successfully.")
        except IncompleteOrderException as e:
            print("Error placing order:", e)
        except Exception as ex:
            print("Error placing order:", ex)


    def track_order_status(self):
        order_id = input("Enter order ID: ")
        self.order_obj.get_order_details(order_id)

    def inventory_management(self):
        print(
            "1. Get Product\n"
            + "2. Get Quantity in Stock\n"
            + "3. Add To Inventory\n"
            + "4. Remove From Inventory\n"
            + "5. Update Stock Quantity\n"
            + "6. Product Available\n"
            + "7. Get Inventory Value\n"
            + "8. List Low Stock Products\n"
            + "9. List Out Of Stock Products\n"
            + "10. List All Products"
        )
        choice_inventory = input("Enter your choice: ")
        if choice_inventory == "1":
            inventory_id = int(input("Enter the inventory id: "))
            product = self.inventory_obj.get_product(inventory_id)
            print(product)
        elif choice_inventory == "2":
            inventory_id = int(input("Enter the inventory id: "))
            print(self.inventory_obj.get_quantity_in_stock(inventory_id))
        elif choice_inventory == "3":
            product_id = int(input("Enter the product id: "))
            quantity_in_stock = int(input("Enter the quantity in stock: "))
            last_stock_update = input("Enter the last stock update: ")
            self.inventory_obj.insert_inventory(
                product_id, quantity_in_stock, last_stock_update
            )
        elif choice_inventory == "4":
            product_id = int(input("Enter the product id: "))
            quantity = int(input("Enter the quantity: "))
            self.inventory_obj.remove_from_inventory(product_id, quantity)
        elif choice_inventory == "5":
            inventory_id = int(input("Enter the inventory id: "))
            new_quantity = int(input("Enter the new quantity: "))
            self.inventory_obj.update_stock_quantity(inventory_id, new_quantity)
        elif choice_inventory == "6":
            inventory_id = input("Enter Inventory ID: ")
            quantity_to_check = int(input("Enter Quantity to Check: "))
            if self.inventory_obj.is_product_available(inventory_id, quantity_to_check):
                print("Product is available in inventory.")
            else:
                print("Product is not available in inventory.")
        elif choice_inventory == "7":
            inventory_id = input("Enter Inventory ID: ")
            print(self.inventory_obj.get_inventory_value(inventory_id))
        elif choice_inventory == "8":
            threshold = int(input("Enter the threshold for low stock: "))
            self.inventory_obj.list_low_stock_products(threshold)
        elif choice_inventory == "9":
            self.inventory_obj.list_out_of_stock_products()
        elif choice_inventory == "10":
            self.inventory_obj.list_all_products()
        else:
            print("Invalid choice. Please try again.")

    def sales_reports(self):
        start_date = input("Enter Start Date: ")
        end_date = input("Enter end date: ")
        self.order_obj.fetch_sales_data(start_date=start_date, end_date=end_date)

    def customer_account_updates(self):
        customer_id = input("Enter Customer ID: ")
        email = input("Enter New Email: ")
        phone = input("Enter New Phone: ")
        address = input("Enter New Address: ")
        self.customer_obj.updateCustomerInfo(customer_id, email, phone, address)

    def payment_processing(self):
        order_id = int(input("Enter Order ID: "))
        payment_method = input("Enter Payment Method: ")
        amount = input("Enter amount: ")
        self.payment_obj.record_payment(order_id=order_id, payment_method=payment_method, amount=amount)

    def product_search_and_recommendations(self):
        print("1. Search for a product\n2. Get Recommendations\n")
        choice = input("Enter your choice: ")
        if choice == '1':
            keyword = input("Search for a product: ")
            self.product_obj.search_product_by_name(keyword=keyword)
        elif choice == '2':
            category = input("Enter a category: ")
            self.product_obj.get_product_recommendations(category=category)
        else:
            print("Invalid choice. Try again")



    def main(self):
        self.display_menu()
        choice = input("Enter your choice: ")
        self.handle_choice(choice)


if __name__ == "__main__":
    menu = Menu()
    menu.main()
