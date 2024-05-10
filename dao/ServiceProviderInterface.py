import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def calculateTotalOrders(self):
        pass

    @abstractmethod
    def updateCustomerInfo(self):
        pass

    @abstractmethod
    def getCustomerDetails(self):
        pass

    @abstractmethod
    def getProductDetails(self):
        pass

    @abstractmethod
    def updateProductInfo(self):
        pass

    @abstractmethod
    def isProductInStock(self):
        pass

    @abstractmethod
    def calculateTotalAmount(self):
        pass

    @abstractmethod
    def getOrderDetails(self):
        pass

    @abstractmethod
    def updateOrderStatus(self):
        pass

    @abstractmethod
    def cancelOrder(self):
        pass

    @abstractmethod
    def calculateSubtotal(self):
        pass

    @abstractmethod
    def getOrderDetailInfo(self):
        pass

    @abstractmethod
    def updateQuantity(self):
        pass

    @abstractmethod
    def addDiscount(self):
        pass

    @abstractmethod
    def getProduct(self):
        pass

    @abstractmethod
    def updateStockQuantity(self):
        pass

    @abstractmethod
    def isProductAvailable(self):
        pass

    @abstractmethod
    def removeFromInventory(self):
        pass

    @abstractmethod
    def insertCustomer(self, cs):
        pass

    @abstractmethod
    def deleteCustomer(self, cs):
        pass

    @abstractmethod
    def getQuantityInStock(self):
        pass

    @abstractmethod
    def insertOrders(self, or_):
        pass

    @abstractmethod
    def insertProducts(self, pr):
        pass

    @abstractmethod
    def insertInventory(self, iv):
        pass

   



