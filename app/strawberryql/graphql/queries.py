import strawberry
from inventory.models import Category
import strawberry_django
from .django_types import CategoryType

@strawberry.type
class Query:
    @strawberry_django.field
    def categories(self) -> list[CategoryType]:
        return Category.objects.only("id", "name", "slug")
    
    # fruits: strawberry_django.field()
