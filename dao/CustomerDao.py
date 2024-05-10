
from entity.Customer import Customer
from exception.exceptions import InvalidDataException
from util.DBConnUtil import DBConnUtil

class CustomerDao():
    def calculateTotalOrders(self, customerId):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sqlQuery = "SELECT COUNT(*) FROM Orders WHERE CustomerID = %s"
            cursor.execute(sqlQuery, (customerId,))
            totalOrders = cursor.fetchone()[0]
            print("Total Orders:", totalOrders)
        except Exception as e:
            print("Error calculating total orders:", e)
        finally:
            connection.close()

    def getCustomerDetails(self, customerId):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sqlQuery = "SELECT * FROM Customers WHERE CustomerID = %s"
            cursor.execute(sqlQuery, (customerId,))
            customerData = cursor.fetchone()
            if customerData:
                print("Customer ID:", customerData[0])
                print("Name:", customerData[1], customerData[2])
                print("Email:", customerData[3])
                print("Phone:", customerData[4])
                print("Address:", customerData[5])
                return customerData
            else:
                print("Customer not found.")
        except Exception as e:
            print("Error getting customer details:", e)
        finally:
            connection.close()

    def updateCustomerInfo(self, customerId, email=None, phone=None, address=None):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sqlQuery = "SELECT * FROM Customers WHERE CustomerID = %s"
            cursor.execute(sqlQuery, (customerId,))
            customerData = cursor.fetchone()
            if not customerData:
                print("Customer not found.")
                return

            updates = {key: value for key, value in [("Email", email), ("Phone", phone), ("Address", address)] if value}
            if updates:
                sqlQuery = "UPDATE Customers SET "
                sqlQuery += ", ".join([f"{key} = %s" for key in updates.keys()])
                sqlQuery += " WHERE CustomerID = %s"
                params = list(updates.values()) + [customerId]
                cursor.execute(sqlQuery, params)
                connection.commit()
                print("Customer information updated successfully.")
            else:
                print("No updates provided.")
        except Exception as e:
            print("Error updating customer information:", e)
        finally:
            connection.close()

    def insertCustomer(self, firstName, lastName, email, phone, address):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            cust = Customer(first_name=firstName, last_name=lastName, email=email, phone=phone, address=address)
            sqlQuery = "INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sqlQuery, (cust.first_name, cust.last_name, cust.email, cust.phone, cust.address))
            connection.commit()
            print("Customer inserted successfully.")
        except InvalidDataException as e:
            print("Error: ", e)
        except Exception as e:
            print("Error inserting customer:", e)
        finally:
            connection.close()

    def deleteCustomer(self, customerId):
        try:
            connection = DBConnUtil.getConnection()
            cursor = connection.cursor()
            sqlQuery = "DELETE FROM Customers WHERE CustomerID = %s"
            cursor.execute(sqlQuery, (customerId,))
            connection.commit()
            print("Customer deleted successfully.")
        except Exception as e:
            print("Error deleting customer:", e)
        finally:
            connection.close()
