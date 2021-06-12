from graphene import ObjectType, Schema

from Demo.schema import AllBikes

class Query(AllBikes, ObjectType):
    pass

schema = Schema(query=Query)