import strawberry
from strawberryql.graphql.mutations.mutation import Mutation
from strawberryql.graphql.queries.query import Query
from strawberry_django.optimizer import DjangoOptimizerExtension

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        DjangoOptimizerExtension
    ]
)

