class PaymentRecord:
    def __init__(self, order_id, amount, status="Pending"):
        self.order_id = order_id
        self.amount = amount
        self.status = status

class PaymentRecordsList:
    def __init__(self):
        self.payment_records = []

    def record_payment(self, payment_record):
        """
        Record a payment for an order.
        """
        self.payment_records.append(payment_record)

    def update_payment_status(self, order_id, new_status):
        """
        Update payment status for a specific order.
        """
        for payment_record in self.payment_records:
            if payment_record.order_id == order_id:
                payment_record.status = new_status
                return
        # If order_id not found
        raise ValueError(f"No payment record found for order ID: {order_id}")

    def handle_payment_error(self, order_id, error_message):
        """
        Handle payment errors for a specific order.
        """
        for payment_record in self.payment_records:
            if payment_record.order_id == order_id:
                payment_record.status = "Error"
                payment_record.error_message = error_message
                return
        # If order_id not found
        raise ValueError(f"No payment record found for order ID: {order_id}")
