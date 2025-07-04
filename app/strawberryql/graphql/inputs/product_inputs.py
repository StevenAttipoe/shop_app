import strawberry_django
from strawberry import auto
from inventory.models import Product

@strawberry_django.input(Product)
class ProductInput:
    name: auto
    slug: auto
    description: auto
    price: auto
    is_active: auto
    category_id: int