from graphene import ObjectType, String, Field, Schema
from graphql import GraphQLError
import graphene
import extraction
import requests


def extract(url):
    html = requests.get(url).text
    extracted = extraction.Extractor().extract(html, source_url=url)
    return extracted



class Website(ObjectType):
    url = String(required=True)
    title = String()
    description = String()
    image = String()


class Query(graphene.ObjectType):
    website = Field(Website, url=String())

    def resolve_website(self, info, url):
        extracted = extract(url)
        return Website(url=url,
                       title=extracted.title,
                       description=extracted.description,
                       image=extracted.image)

schema = Schema(query=Query)