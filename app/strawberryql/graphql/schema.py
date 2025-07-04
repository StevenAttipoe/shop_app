import strawberry
from .queries import Query
from strawberry_django.optimizer import DjangoOptimizerExtension

schema = strawberry.Schema(
    query=Query,
    extensions=[
        DjangoOptimizerExtension
    ]
)

