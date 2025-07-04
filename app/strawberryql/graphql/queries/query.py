import strawberry
from strawberryql.graphql.queries.category_query import CategoryQuery
from strawberryql.graphql.queries.product_query import ProductQuery

@strawberry.type
class Query(
    CategoryQuery,
    ProductQuery,
):
    """
    Root query type for the GraphQL schema.

    This class aggregates all query types, allowing for the retrieval of products and categories.
    """
    pass