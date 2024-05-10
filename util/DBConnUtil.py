import mysql.connector
from mysql.connector import Error
import time

from util.DBPropertyUtil import DBPropertyUtil

class DBConnUtil:
    __connection = None

    @staticmethod
    def getConnection():
        property_file = r"C:\Users\raaji\OneDrive\Documents\hexaware training\TechShop\db.properties"
        connection_string = DBPropertyUtil().get_connection_string(property_file)
        try:
            DBConnUtil.__connection = mysql.connector.connect(**connection_string)
            # print("Connected to MySQL database successfully.")
            return DBConnUtil.__connection
        except mysql.connector.Error as err:
            print("Error connecting to MySQL:", err)
            return None
        

    @staticmethod
    def close_connection():
        if DBConnUtil.__connection:
            DBConnUtil.__connection.close()
            print("Connection closed.")
            DBConnUtil.__connection = None
