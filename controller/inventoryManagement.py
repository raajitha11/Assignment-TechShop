from sortedcontainers import SortedList
from datetime import datetime


class InventoryManager:
    def __init__(self):
        self.inventory_list = SortedList()

    def add_inventory(self, inventory):
        self.inventory_list.add((inventory.product.product_id, inventory))

    def remove_inventory(self, product_id):
        index = self._find_index_by_product_id(product_id)
        if index is not None:
            del self.inventory_list[index]

    def update_inventory_quantity(self, product_id, new_quantity):
        index = self._find_index_by_product_id(product_id)
        if index is not None:
            self.inventory_list[index][1].quantity_in_stock = new_quantity

    def get_inventory_by_product_id(self, product_id):
        index = self._find_index_by_product_id(product_id)
        if index is not None:
            return self.inventory_list[index][1]
        return None

    def _find_index_by_product_id(self, product_id):
        for i, (key, inventory) in enumerate(self.inventory_list):
            if key == product_id:
                return i
        return None
