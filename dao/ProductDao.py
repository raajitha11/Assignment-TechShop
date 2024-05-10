
from entity.Product import Product
from exception.exceptions import InvalidDataException
from util.DBConnUtil import DBConnUtil

class ProductDao():

    def get_product_details(self, product_id):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = "SELECT * FROM Products WHERE ProductID = %s"
            cursor.execute(sql_query, (product_id,))
            product_data = cursor.fetchone()
            if product_data:
                print("Product ID:", product_data[0])
                print("Product Name:", product_data[1])
                print("Description:", product_data[2])
                print("Price:", product_data[3])
            else:
                print("Product not found.")
        except Exception as e:
            print("Error getting product details:", e)
        finally:
            connection.close()

    def update_product_info(self, product_id, price=None, description=None):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            # Retrieve existing product details from the database
            cursor.execute("SELECT * FROM Products WHERE ProductID = %s", (product_id,))
            product_data = cursor.fetchone()
            if not product_data:
                print("Product not found.")
                return

            # Prepare updates
            updates = {}
            if price is not None and price != product_data[3]:
                updates['Price'] = price
            if description and description != product_data[2]:
                updates['Description'] = description

            # Update product information if there are changes
            if updates:
                sql_query = "UPDATE Products SET "
                sql_query += ", ".join([f"{key} = %s" for key in updates.keys()])
                sql_query += " WHERE ProductID = %s"

                # Execute the update query with parameters
                params = list(updates.values()) + [product_id]
                cursor.execute(sql_query, params)
                connection.commit()
                print("Product information updated successfully.")
            else:
                print("No updates provided.")
        except Exception as e:
            print("Error updating product information:", e)
        finally:
            connection.close()

    def is_product_in_stock(self, product_id):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = "SELECT QuantityInStock FROM Inventory WHERE ProductID = %s"
            cursor.execute(sql_query, (product_id,))
            quantity = cursor.fetchone()
            if quantity and quantity[0] > 0:
                print("Product is in stock.")
            else:
                print("Product is out of stock.")
        except Exception as e:
            print("Error checking product stock:", e)
        finally:
            connection.close()

    def insert_product(self, product_name, description, price):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            new_product = Product(None, product_name, description, price)
            sql_query = "INSERT INTO Products (ProductName, Description, Price) VALUES (%s, %s, %s)"
            cursor.execute(sql_query, (new_product.product_name, new_product.description, new_product.price))
            connection.commit()
            print("Product inserted successfully.")
        except Exception as e:
            print("Error inserting product:", e)
        finally:
            connection.close()

    def search_product_by_name(self, keyword):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = """
                SELECT ProductID, ProductName, Description, Price
                FROM Products
                WHERE ProductName LIKE %s
            """
            cursor.execute(sql_query, ('%' + keyword + '%',))
            products = cursor.fetchall()
            if products:
                print("Search Results:")
                for product in products:
                    print(product)
            else:
                print("No products found matching the search criteria.")
        except Exception as e:
            print("Error searching for products:", e)
        finally:
            connection.close()

    def get_product_recommendations(self, category):
        try:
            # Get product recommendations based on the specified category
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = """
                SELECT ProductID, ProductName, Description, Price
                FROM Products
                WHERE Category = %s
                LIMIT 5
            """
            cursor.execute(sql_query, (category,))
            recommendations = cursor.fetchall()
            if recommendations:
                print("Product Recommendations:")
                for product in recommendations:
                    print(product)
            else:
                print("No recommendations found for the specified category.")
        except Exception as e:
            print("Error getting product recommendations:", e)
        finally:
            connection.close()
