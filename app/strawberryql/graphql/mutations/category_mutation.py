from strawberryql.graphql.inputs.category_inputs import CategoryInput
from strawberryql.graphql.types.category_type import CategoryType
from inventory.models import Category
import strawberry

@strawberry.type
class CategoryMutation:
    @strawberry.mutation(description="Create a new category")
    def create_category(self, category_input: CategoryInput) -> CategoryType:
        category = Category.objects.create(
            name=category_input.name,
            slug=category_input.slug,
            parent_id=category_input.parent_id,
            is_active=category_input.is_active,
            level=category_input.level
        )
        return CategoryType.from_instance(category)

    @strawberry.mutation(description="Update an existing category")
    def update_category(self, id: int, category_input: CategoryInput) -> CategoryType:
        category = Category.objects.get(id=id)
        for attr, value in category_input.__dict__.items():
            setattr(category, attr, value)
        category.save()
        return CategoryType.from_instance(category)