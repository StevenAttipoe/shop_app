import strawberry
from strawberryql.graphql.mutations.product_mutation import ProductMutation
from strawberryql.graphql.mutations.category_mutation import CategoryMutation


@strawberry.type
class Mutation(
    ProductMutation,
    CategoryMutation,
):
    """
    Root mutation type for the GraphQL schema.
    
    This class aggregates all mutation types, allowing for the creation and modification of products and categories.
    """
    pass