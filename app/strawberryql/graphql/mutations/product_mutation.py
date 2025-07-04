from strawberryql.graphql.types.product_type import ProductType
from strawberryql.graphql.inputs.product_inputs import ProductInput
from inventory.models import Category, Product
import strawberry

@strawberry.type
class ProductMutation:
    @strawberry.mutation(description="Create a new product")
    def create_product(self, input: ProductInput) -> ProductType:
        category = Category.objects.filter(id=input.category_id).first()
        
        if not category:
            raise ValueError("Category with the given ID does not exist.")

        product = Product.objects.create(
            name=input.name,
            slug=input.slug,
            description=input.description,
            price=input.price,
            category=category
        )
        return product

    @strawberry.mutation(description="Update an existing product")
    def update_product(self, id: int, input: ProductInput) -> ProductType:
        product = Product.objects.get(id=id)

        for attr, value in input.__dict__.items():
            setattr(product, attr, value)
            
        product.save()

        return product
