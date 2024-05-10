class Product:
    def __init__(self, product_id=None, product_name="", description="", price=0.00, in_stock=True):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.__price = price
        self.__in_stock = in_stock

    def get_product_details(self):
        return f"Product ID: {self.__product_id}\nName: {self.__product_name}\nDescription: {self.__description}\nPrice: ${self.__price}\nIn Stock: {'Yes' if self.__in_stock else 'No'}"

    def update_product_info(self, price=None, description=None, in_stock=None):
        if price is not None:
            self.price = price
        if description is not None:
            self.__description = description
        if in_stock is not None:
            self.__in_stock = in_stock

    def is_product_in_stock(self):
        return self.__in_stock

    @property
    def product_id(self):
        return self.__product_id

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, value):
        if isinstance(value, str):
            self.__product_name = value
        else:
            raise ValueError("Product name must be a string.")

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if isinstance(value, str):
            self.__description = value
        else:
            raise ValueError("Description must be a string.")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)):
            if value >= 0:  # Check if price is non-negative
                self.__price = value
            else:
                raise ValueError("Price must not be negative.")
        else:
            raise ValueError("Price must be a numeric value.")


# # Testing the corrected class
# product1 = Product(product_id=1, product_name="Laptop", description="A powerful laptop", price=999.99)

# print(product1.get_product_details())  # Should print product details
# product1.update_product_info(price=1099.99)  # Update price
# print(product1.get_product_details())  # Should print updated product details
# print(product1.is_product_in_stock())  # Should print True by default

# # Test property setters
# product1.product_name = "Gaming Laptop"
# product1.description = "A high-performance gaming laptop"
# product1.price = 1299.99

# # Print updated product details
# print(product1.get_product_details())
