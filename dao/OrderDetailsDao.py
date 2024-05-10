import decimal
from util.DBConnUtil import DBConnUtil


class OrderDetailsDao:

    def get_order_detail_info(self, order_detail_id):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = """
                        SELECT OrderDetails.OrderDetailID, Orders.OrderID, Products.ProductID, Products.ProductName, OrderDetails.Quantity
                        FROM OrderDetails
                        INNER JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
                        INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
                        WHERE OrderDetails.OrderDetailID = %s
                        """
            cursor.execute(sql_query, (order_detail_id,))
            order_detail_info = cursor.fetchone()
            if order_detail_info:
                order_detail_id, order_id, product_id, product_name, quantity = order_detail_info
                print(f"Order Detail ID: {order_detail_id}")
                print(f"Order ID: {order_id}")
                print(f"Product ID: {product_id}")
                print(f"Product Name: {product_name}")
                print(f"Quantity: {quantity}")
            else:
                print("Order detail not found.")
        except Exception as e:
            print("Error getting order detail info:", e)
        finally:
            connection.close()

    def update_quantity(self, order_detail_id, new_quantity):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()

            # Get the product price
            product_price_query = """
                                SELECT p.Price
                                FROM OrderDetails od
                                JOIN Products p ON od.ProductID = p.ProductID
                                WHERE od.OrderDetailID = %s
                                """
            cursor.execute(product_price_query, (order_detail_id,))
            product_price = cursor.fetchone()[0]

            # Update the quantity in OrderDetails
            update_quantity_query = "UPDATE OrderDetails SET Quantity = %s WHERE OrderDetailID = %s"
            cursor.execute(update_quantity_query, (new_quantity, order_detail_id))

            # Calculate the new total amount
            new_total_amount = product_price * new_quantity

            # Update the total amount in Orders
            update_total_amount_query = "UPDATE Orders SET TotalAmount = %s WHERE OrderID = (SELECT OrderID FROM OrderDetails WHERE OrderDetailID = %s)"
            cursor.execute(update_total_amount_query, (new_total_amount, order_detail_id))

            connection.commit()
            print("Quantity updated successfully.")
        except Exception as e:
            print("Error updating quantity:", e)
        finally:
            connection.close()


    def calculate_subtotal(self, order_detail_id):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = """
                        SELECT Products.Price, OrderDetails.Quantity
                        FROM OrderDetails
                        INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
                        WHERE OrderDetails.OrderDetailID = %s
                        """
            cursor.execute(sql_query, (order_detail_id,))
            result = cursor.fetchone()
            if result:
                price, quantity = result
                subtotal = price * quantity
                print("Subtotal:", subtotal)
            else:
                print("No order detail found for the given ID.")
        except Exception as e:
            print("Error calculating subtotal:", e)
        finally:
            connection.close()

    def add_discount(self, order_detail_id, discount_percentage):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = """
                        SELECT Quantity, p.Price
                        FROM OrderDetails od
                        JOIN Products p ON od.ProductID = p.ProductID
                        WHERE OrderDetailID = %s
                        """
            cursor.execute(sql_query, (order_detail_id,))
            rows = cursor.fetchone()
            if rows:
                quantity, price = rows
                total_before_discount = quantity * price
                discount_amount = total_before_discount * (decimal.Decimal(discount_percentage) / 100)
                total_after_discount = total_before_discount - discount_amount

                update_query = "UPDATE Orders SET TotalAmount = %s WHERE OrderID = %s"
                cursor.execute(update_query, (total_after_discount, order_detail_id))
                
                print("Discount applied successfully. New total price:", total_after_discount)
            else:
                print("Order detail ID not found.")
        except Exception as e:
            print("Error adding discount:", e)
        finally:
            connection.close()

    def insert_order_detail(self, order_id, product_id, quantity):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            
            # Insert order details into the OrderDetails table
            sql_query = "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (%s, %s, %s)"
            cursor.execute(sql_query, (order_id, product_id, quantity))
            
            connection.commit()  # Commit the transaction
            
            print("Order detail inserted successfully.")
        except Exception as e:
            connection.rollback()  # Rollback transaction in case of error
            print("Error inserting order detail:", e)
        finally:
            connection.close()
