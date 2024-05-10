from datetime import datetime
from exception.exceptions import InsufficientStockException, InvalidDataException

class Inventory:
    def __init__(self, inventory_id=None, product=None, quantity_in_stock=0, last_stock_update=None):
        self.__inventory_id = inventory_id
        self.__product = product
        self.__quantity_in_stock = quantity_in_stock if quantity_in_stock>0 else 0
        self.__last_stock_update = last_stock_update if last_stock_update else datetime.now()
    
    def get_product(self):
        return self.__product

    def get_quantity_in_stock(self):
        return self.__quantity_in_stock

    def add_to_inventory(self, quantity):
        self.__quantity_in_stock += quantity
        self.__last_stock_update = datetime.now()

    def remove_from_inventory(self, quantity):
        if self.__quantity_in_stock >= quantity:
            self.__quantity_in_stock -= quantity
            self.__last_stock_update = datetime.now()
        else:
            raise InsufficientStockException("Insufficient quantity in stock.")

    def update_stock_quantity(self, new_quantity):
        self.__quantity_in_stock = new_quantity
        self.__last_stock_update = datetime.now()

    def is_product_available(self, quantity_to_check):
        return self.__quantity_in_stock >= quantity_to_check

    def get_inventory_value(self):
        return self.__product.price * self.__quantity_in_stock

    def list_low_stock_products(self, threshold):
        if self.__quantity_in_stock < threshold:
            return self.__product

    def list_out_of_stock_products(self):
        if self.__quantity_in_stock == 0:
            return self.__product

    def list_all_products(self):
        return self.__product
    
    @property
    def inventory_id(self):
        return self.__inventory_id

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, product):
        # Add validation logic if needed
        self.__product = product

    @property
    def quantity_in_stock(self):
        return self.__quantity_in_stock

    @quantity_in_stock.setter
    def quantity_in_stock(self, quantity_in_stock):
        if isinstance(quantity_in_stock, int) and quantity_in_stock >= 0:
            self.__quantity_in_stock = quantity_in_stock
        else:
            raise InvalidDataException("Quantity in stock must be a non-negative integer.")

    @property
    def last_stock_update(self):
        return self.__last_stock_update

    @last_stock_update.setter
    def last_stock_update(self, last_stock_update):
        if isinstance(last_stock_update, datetime):
            self.__last_stock_update = last_stock_update
        else:
            raise InvalidDataException("Last stock update must be a datetime object.")
