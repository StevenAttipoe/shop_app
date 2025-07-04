import strawberry_django
from inventory.models import Category

@strawberry_django.input(Category)
class CategoryInput:
    name: str
    slug: str
    parent_id: int | None = None
    is_active: bool
    level: int | None = None