from exception.exceptions import NotFoundException


class OrderManager:
    def __init__(self):
        self.__orders = []

    def add_order(self, order):
        self.__orders.append(order)

    def update_order_status(self, order_id, new_status):
        for order in self.__orders:
            if order.order_id == order_id:
                order.update_order_status(new_status)
                return
        raise NotFoundException("Order not found in the list.")

    def remove_canceled_orders(self):
        self.__orders = [order for order in self.__orders if order.status != "canceled"]

    def sort_orders_by_date(self, ascending=True):
        self.__orders.sort(key=lambda order: order.order_date, reverse=not ascending)

    def get_orders_in_date_range(self, start_date, end_date):
        return [order for order in self.__orders if start_date <= order.order_date <= end_date]

    def list_orders(self):
        return self.__orders
