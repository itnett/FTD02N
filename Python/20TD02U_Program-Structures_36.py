python
# domain/models.py
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# application/services.py
from domain.models import Product

class ProductService:
    def get_product_by_name(self, name):
        # Fetch product from database (using a repository)
        # ...

# presentation/views.py
from application.services import ProductService

def product_details(request, product_name):
    product_service = ProductService()
    product = product_service.get_product_by_name(product_name)
    # Render product details template...