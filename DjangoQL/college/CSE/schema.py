from graphene import ObjectType, Float, Field, Int, Mutation
from django.db.models import Avg, Max
from graphene.types.scalars import Boolean, String
from .models import Students
from graphene_django import DjangoObjectType

# Mention to print data in the Graphql server
class Student_avg_age(ObjectType):
    averageAGeStudent = Float()
    maxage = Int()

# Actual method implementation in class
class ShowAvgAge(ObjectType):

    showavg = Field(Student_avg_age)

    def resolve_showavg(self, info):
        get_avg_age = Students.objects.aggregate(Avg('age'))
        max_age = Students.objects.aggregate(Max('age'))
        return Student_avg_age(averageAGeStudent=get_avg_age.get('age__avg'), maxage = max_age.get('age__max'))

    
class TypeData(DjangoObjectType):
    class Meta:
        model = Students


class SaveStudentData(Mutation):
    class Arguments:
        name = String()
        age = Int()
        studentid = Int()
    
    ok = Boolean()

    def mutate(self, info, name, age, studentid):
        ok = False
        return SaveStudentData(ok=ok)