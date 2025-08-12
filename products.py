# creting a class with name product
class Product:
# In this we are creating function and intializing the objects
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
#  we are ceating child class to acess the objects from parent class
    def get_product_info(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }
## Create a product using the class method
    @classmethod
    def create_product(cls, id, name, price):
        return cls(id, name, price)
