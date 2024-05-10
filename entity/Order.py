from datetime import datetime

from entity.Customer import Customer

class Order:
    def __init__(self, order_id=None, customer=None, totalAmount=0, products=None):
        self.__order_id = order_id
        self.__customer = customer
        self.__order_date = datetime.now()
        self.__total_amount = totalAmount
        self.__products = products if products else []

        # self.__customer.orders.append(self)

    def calculate_total_amount(self):
        self.__total_amount = sum(product.price for product in self.__products)
        return self.__total_amount

    def get_order_details(self):
        # order_details = f"Order ID: {self.__order_id}\nCustomer: {self.__customer.first_name} {self.__customer.last_name}\nOrder Date: {self.__order_date}\nTotal Amount: ${self.calculate_total_amount()}\n"
        # for product in self.__products:
        #     order_details += f"\n{product.get_product_details()}"
        # return order_details
        pass

    def update_order_status(self, status):\
        pass

    def cancel_order(self):
        pass

    @property
    def order_id(self):
        return self.__order_id

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    @property
    def order_date(self):
        return self.__order_date

    @order_date.setter
    def order_date(self, order_date):
        if isinstance(order_date, datetime):
            self.__order_date = order_date
        else:
            raise ValueError("Order date must be a datetime object.")

    @property
    def total_amount(self):
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        if isinstance(total_amount, (int, float)):
            self.__total_amount = total_amount
        else:
            raise ValueError("Total amount must be a numeric value.")
