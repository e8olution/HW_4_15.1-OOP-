
#создание_класса
class Category:
    # атрибуты
    # типы_данных
    name: str
    description: str
    products: list
    count_categories = 0
    count_uniq_cat = 0

    # конструктор_класса
    # __init__
    def __init__(self,name,description,products):
        # self
        self.name = name
        self.description = description
        self.products = products
        Category.count_uniq_cat += len(set([product.name for product in products]))
        Category.count_categories += 1


#создание_класса
 # атрибуты
 #типы_данных
class Product:
    # атрибуты
    # типы_данных
    name: str
    description: str
    price: float
    quantity: int

# конструктор_класса
# __init__
    def __init__(self,name,description,price,quantity):
        # self
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

#    def __eq__(self, other):
#        if isinstance(other, Product):
#            return (self.name == other.name and
#                    self.description == other.description and
#                    self.price == other.price and
#                    self.quantity == other.quantity)
#        return False


def __repr__(self):
    return f'Product(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})'