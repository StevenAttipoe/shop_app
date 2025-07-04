import strawberry
from inventory.models import Product
import strawberry_django
from strawberryql.graphql.types.product_type import ProductType

@strawberry.type
class ProductQuery:
    @strawberry_django.field(description= "Returns a list of all products")
    def products(self) -> list[ProductType]:
        return Product.objects.only("id", "name", "slug", "description", "price", "is_active")
    
