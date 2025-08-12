# creating a class on cart service
class CartService:
    def __init__(self):
        self.cart = []

# we are adding products on cart
    def add_product(self, product):
        self.cart.append(product)

# we are removing the products on top of that  we are using for loop to access the items
    def remove_product(self, product_id):
        self.cart = [product for product in self.cart if product.id != product_id]

# we can calcluate the amount of products it will add the amount of products
    def calculate_total(self):
        return sum(product.price for product in self.cart)

# we are proceeding to payment gateway
    def get_cart_items(self):
        return self.cart

# we are clearing the cart after the payment
    def clear_cart(self):
        self.cart = []
