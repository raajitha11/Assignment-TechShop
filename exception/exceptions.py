# exceptions.py

class InsufficientStockException(Exception):
    def __init__(self, message="Insufficient stock."):
        self.message = message
        super().__init__(self.message)


class InvalidDataException(Exception):
    def __init__(self, message="Invalid data provided."):
        self.message = message
        super().__init__(self.message)

class IncompleteOrderException(Exception):
    def __init__(self, message="Incomplete order details."):
        self.message = message
        super().__init__(self.message)


class PaymentFailedException(Exception):
    def __init__(self, message="Payment failed."):
        self.message = message
        super().__init__(self.message)



#product management
class DuplicateProductException(Exception):
    def __init__(self, message="Product already exists."):
        self.message = message
        super().__init__(self.message)

class NotFoundException(Exception):
    def __init__(self, message="Product not found."):
        self.message = message
        super().__init__(self.message)

class ProductHasOrdersException(Exception):
    def __init__(self, message="Product has existing orders and cannot be removed."):
        self.message = message
        super().__init__(self.message)

class FileIOException(Exception):
    def __init__(self, message="Error accessing or performing I/O operation on file."):
        self.message = message
        super().__init__(self.message)

class DatabaseOfflineException(Exception):
    def __init__(self, message="Error executing SQL query due to database offline."):
        self.message = message
        super().__init__(self.message)

class ConcurrencyException(Exception):
    def __init__(self, message="Concurrency issue occurred. Please retry."):
        self.message = message
        super().__init__(self.message)

class AuthenticationException(Exception):
    def __init__(self, message="Authentication failed. Invalid username or password."):
        self.message = message
        super().__init__(self.message)

class AuthorizationException(Exception):
    def __init__(self, message="Unauthorized access attempt."):
        self.message = message
        super().__init__(self.message)


