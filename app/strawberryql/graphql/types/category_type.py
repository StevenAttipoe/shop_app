import strawberry_django
from inventory.models import Category

@strawberry_django.type(
    Category, 
    fields=("id", "name", "slug"),
    description="A type representing a product category in the inventory."
)
class CategoryType:
    pass

# @strawberry_django.type
# class CategoryType:
#     id: strawberry.ID
#     parent_id: int | None
#     name: str
#     slug: str
#     is_active: bool
#     level: int