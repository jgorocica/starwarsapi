# Graphene's tools
import graphene
# Schemas 
import api.schema

class Query(
    api.schema.Query, 
    graphene.ObjectType
    ):
    pass

class Mutation(
    api.schema.Mutation,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)