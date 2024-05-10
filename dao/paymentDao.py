from mysql.connector import Error

from util.DBConnUtil import DBConnUtil

class PaymentProcessingSystem:

    def record_payment(self, order_id, payment_method, amount):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sql_query = """
                        INSERT INTO payments (OrderID, PaymentMethod, Amount)
                        VALUES (%s, %s, %s)
                        """
            cursor.execute(sql_query, (order_id, payment_method, amount))
            connection.commit()

            print("Payment recorded successfully")
        except Error as e:
            print("Error recording payment:", e)
        finally:
            connection.close()

    def validate_payment(self, order_id, payment_method, amount):
        # Implement payment validation logic here
        # For example, check if payment method is valid, amount is greater than 0, etc.
        return True  # For demonstration purposes, always return True



