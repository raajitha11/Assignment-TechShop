
from entity.Inventory import Inventory
from exception.exceptions import InvalidDataException
from util.DBConnUtil import DBConnUtil


class InventoryDao():
    def get_product(self, inventory_id):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = """
                        SELECT Products.ProductID, Products.ProductName, Products.Description, Products.Price
                        FROM Inventory
                        INNER JOIN Products ON Inventory.ProductID = Products.ProductID
                        WHERE Inventory.InventoryID = %s
                        """
            cursor.execute(sql_query, (inventory_id,))
            product_info = cursor.fetchone()
            if product_info:
                product_id, product_name, description, price = product_info
                return {"ProductID": product_id, "ProductName": product_name, "Description": description, "Price": price}
            return None
        except Exception as e:
            print("Error getting product:", e)
        finally:
            connection.close()

    def get_quantity_in_stock(self, inventory_id):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = "SELECT QuantityInStock FROM Inventory WHERE InventoryID = %s"
            cursor.execute(sql_query, (inventory_id,))
            quantity_in_stock = cursor.fetchone()
            if quantity_in_stock:
                return quantity_in_stock[0]
            else:
                return None
        except Exception as e:
            print("Error getting quantity in stock:", e)
        finally:
            connection.close()

    def remove_from_inventory(self, product_id, quantity):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            
            cursor.execute("SELECT QuantityInStock FROM Inventory WHERE productID = %s", (product_id,))
            current_quantity = cursor.fetchone()[0]
            
            new_quantity = current_quantity - quantity 
            new_quantity = new_quantity if new_quantity>0 else 0
            
            cursor.execute("UPDATE Inventory SET QuantityInStock = %s WHERE productID = %s", ( new_quantity, product_id,))
            
            connection.commit()
            print("Quantity removed from inventory successfully.")
        except Exception as e:
            print("Error removing quantity from inventory:", e)
        finally:
            connection.close()


    def update_stock_quantity(self, inventory_id, new_quantity):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            existing_inventory = self.get_product(inventory_id)
            if not existing_inventory:
                print("Inventory item not found.")
                return

            # if new_quantity == existing_inventory['QuantityInStock']:
            #     print("No updates provided.")
            #     return

            sql_query = "UPDATE Inventory SET QuantityInStock = %s WHERE InventoryID = %s"
            cursor.execute(sql_query, (new_quantity, inventory_id))
            connection.commit()
            print("Stock quantity updated successfully.")
        except Exception as e:
            print("Error updating stock quantity:", e)
        finally:
            connection.close()

    def is_product_available(self, inventory_id, quantity_to_check):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = "SELECT QuantityInStock FROM Inventory WHERE InventoryID = %s"
            cursor.execute(sql_query, (inventory_id,))
            quantity_in_stock = cursor.fetchone()
            if quantity_in_stock:
                return quantity_in_stock[0] >= quantity_to_check
            else:
                return False
        except Exception as e:
            print("Error checking product availability:", e)
        finally:
            connection.close()

    def get_inventory_value(self, inventory_id):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = """
                        SELECT Products.Price, Inventory.QuantityInStock
                        FROM Inventory
                        INNER JOIN Products ON Inventory.ProductID = Products.ProductID
                        WHERE Inventory.InventoryID = %s
                        """
            cursor.execute(sql_query, (inventory_id,))
            result = cursor.fetchone()

            if result:
                price, quantity_in_stock = result
                return price * quantity_in_stock
            else:
                # Handle case when no rows are returned
                print("No inventory found for the given ID.")
                return None  # Or raise an exception if necessary
        except Exception as e:
            print("Error getting inventory value:", e)
        finally:
            connection.close()

    def list_low_stock_products(self, threshold):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = """
                        SELECT Products.ProductName, Inventory.QuantityInStock
                        FROM Inventory
                        INNER JOIN Products ON Inventory.ProductID = Products.ProductID
                        WHERE Inventory.QuantityInStock < %s
                        """
            cursor.execute(sql_query, (threshold,))
            low_stock_products = cursor.fetchall()
            if low_stock_products:
                print("Low Stock Products:")
                for product_name, quantity_in_stock in low_stock_products:
                    print(f"Product: {product_name}, Quantity in Stock: {quantity_in_stock}")
            else:
                print("No low stock products found")
        except Exception as e:
            print("Error listing low stock products:", e)
        finally:
            connection.close()

    def list_out_of_stock_products(self):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = """
                        SELECT Products.ProductName
                        FROM Inventory
                        INNER JOIN Products ON Inventory.ProductID = Products.ProductID
                        WHERE Inventory.QuantityInStock = 0
                        """
            cursor.execute(sql_query)
            out_of_stock_products = cursor.fetchall()
            if out_of_stock_products:
                print("Out of Stock Products:")
                for product_name in out_of_stock_products:
                    print(product_name[0])
            else:
                print("No out of stock products found")
        except Exception as e:
            print("Error listing out of stock products:", e)
        finally:
            connection.close()

    def list_all_products(self):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = """
                        SELECT Products.ProductName, Inventory.QuantityInStock
                        FROM Inventory
                        INNER JOIN Products ON Inventory.ProductID = Products.ProductID
                        """
            cursor.execute(sql_query)
            all_products = cursor.fetchall()
            if all_products:
                print("All Products in Inventory:")
                for product_name, quantity_in_stock in all_products:
                    print(f"Product: {product_name}, Quantity in Stock: {quantity_in_stock}")
            else:
                print("No products found in inventory")
        except Exception as e:
            print("Error listing all products:", e)
        finally:
            connection.close()

    def insert_inventory(self, product_id, quantity_in_stock, last_stock_update):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            new_inventory = Inventory(None, product_id, quantity_in_stock, last_stock_update)
            sql_query = "INSERT INTO Inventory (ProductID, QuantityInStock, LastStockUpdate) VALUES (%s, %s, %s)"
            cursor.execute(sql_query, (new_inventory.product, new_inventory.quantity_in_stock, new_inventory.last_stock_update))
            connection.commit()
            print("Inventory item inserted successfully.")
        except Exception as e:
            print("Error inserting inventory item:", e)
        finally:
            connection.close()

