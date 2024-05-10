import re
from exception.exceptions import InvalidDataException


class Customer:
    def __init__(self, customer_id=None, first_name="", last_name="", email="", phone="", address=""):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = self.__validate_email(email)
        self.__phone = phone
        self.__address = address
        self.orders = []

    def __validate_email(self, email):
        if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
            return email
        else:
            raise InvalidDataException("Invalid email address provided.")
        
    def calculate_total_orders(self):
        return len(self.orders)

    def get_customer_details(self):
        return f"Customer ID: {self.__customer_id}\nName: {self.__first_name} {self.__last_name}\nEmail: {self.__email}\nPhone: {self.__phone}\nAddress: {self.__address}\nTotal Orders: {self.calculate_total_orders()}"

    def update_customer_info(self, email=None, phone=None, address=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            raise InvalidDataException("First name must be a string.")

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            raise InvalidDataException("Last name must be a string.")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = self.__validate_email(email)

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        # Phone number validation: must be a string containing only digits
        if isinstance(phone, str) and phone.isdigit():
            self.__phone = phone
        else:
            raise InvalidDataException("Phone number must be a string containing only digits.")

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if isinstance(address, str):
            self.__address = address
        else:
            raise InvalidDataException("Address must be a string.")
        




# # Example usage:
# try:
#     customer = Customer(customer_id=1, first_name="John", last_name="Doe", email="invalid@mail.com", phone="1234567890", address="123 Main St")
#     print(customer.get_customer_details())
#     customer.phone = "A39899"
#     print(customer.phone)
# except InvalidDataException as e:
#     print(e.message)  # Output: Invalid email address provided.
