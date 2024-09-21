class OnlineShoppingPlatform:
    def __init__(self, products, customers):
        self.products = products
        self.customers = customers

    def add_product(self, product):
        # add a new product to the platform
        self.products.append(product)

    def remove_product(self, product_id):
        # remove a product from the platform
        self.products = [p for p in self.products if p.id != product_id]

class Customer:
    def __init__(self, customers):
        self.customers = customers

    def add_customer(self, customer):
        # add a new customer to the platform
        self.customers.append(customer)

    def remove_customer(self, customer_id):
        # remove a customer from the platform
        self.customers = [c for c in self.customers if c.id != customer_id]

class Payment_Processor:
    def process_payment(self, customer, product, amount):
        # process a payment for a customer
        print(f"Processing payment for {customer.name} for product {product.name}...")

class Send_Order_Confirmation:
    def send_order_confirmation(self, customer, product):
        # send an order confirmation to the customer
        print(f"Sending order confirmation to {customer.name} for product {product.name}...")

class Update_Product_Inventory:
    def update_product_inventory(self, product, quantity):
        # update the product inventory
        product.inventory -= quantity

class Update_Customer_Order_History:
    def update_customer_order_history(self, customer, product):
        # update the customer's order history
        customer.order_history.append(product)