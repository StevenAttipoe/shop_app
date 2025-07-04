import strawberry
from inventory.models import Category
import strawberry_django
from strawberryql.graphql.types.category_type import CategoryType

@strawberry.type
class CategoryQuery:
    @strawberry_django.field(description= "Returns a list of all categories")
    def categories(self) -> list[CategoryType]:
        return Category.objects.only("id", "name", "slug")
    
