import strawberry_django
from strawberry import auto
from inventory.models import Product
from strawberryql.graphql.types.category_type import CategoryType

@strawberry_django.type(Product)
class ProductType:
    id: auto
    name: auto
    slug: auto
    description: auto
    price: auto
    is_active: auto
    category_id: auto
    category: CategoryType 