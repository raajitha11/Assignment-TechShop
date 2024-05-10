
from entity.Order import Order
from exception.exceptions import InvalidDataException


class OrderDetails:
    def __init__(self, order_detail_id=None, order=None, product=None, quantity=0):
        self.__order_detail_id = order_detail_id
        self.__order = order
        self.__product = product
        self.__quantity = quantity

        # self.__order.products.append(product)

    def calculate_subtotal(self):
        pass

    def get_order_detail_info(self):
        pass

    def update_quantity(self, new_quantity):
        pass

    def add_discount(self, discount):
        pass

    @property
    def order_detail_id(self):
        return self.__order_detail_id

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        self.__order = order

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, product):
        self.__product = product

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, int) and quantity >= 0:
            self.__quantity = quantity
        else:
            raise InvalidDataException("Quantity must be a non-negative integer.")
