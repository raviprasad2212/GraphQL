from .models import Bike
import graphene
from graphene import ObjectType, List, String
from graphene_django import DjangoObjectType


class BikeType(DjangoObjectType):
    class Meta:
        model = Bike

class AllBikes(ObjectType):
    bikenames = List(BikeType)

    def resolve_bikenames(self, info):
        return Bike.objects.all()


