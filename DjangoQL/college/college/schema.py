from graphene import Schema, ObjectType, AbstractType
from CSE.schema import ShowAvgAge, SaveStudentData

class Query(ShowAvgAge, ObjectType):
    pass

class Mutation(SaveStudentData, ObjectType):
    saveData = SaveStudentData.Field()

schema = Schema(query=Query, mutation=Mutation)