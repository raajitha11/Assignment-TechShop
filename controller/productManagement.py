from exception.exceptions import DuplicateProductException, ProductHasOrdersException, NotFoundException


class ProductManager:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if product not in self.__products:
            self.__products.append(product)
        else:
            raise DuplicateProductException("Product already exists in the list.")

    def update_product(self, product_id, new_product):
        for i, product in enumerate(self.__products):
            if product.product_id == product_id:
                self.__products[i] = new_product
                return
        raise NotFoundException("Product not found in the list.")

    def remove_product(self, product_id):
        for i, product in enumerate(self.__products):
            if product.product_id == product_id:
                # Check if the product has existing orders
                if product.has_orders():
                    raise ProductHasOrdersException("Product cannot be removed as it has existing orders.")
                del self.__products[i]
                return
        raise NotFoundException("Product not found in the list.")

    def list_products(self):
        return self.__products
