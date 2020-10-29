import graphene
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations



class AuthMutation(graphene.ObjectType):

  register = mutations.Register.Field()


class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):

  pass


schema = graphene.Schema(query=Query, mutation=Mutation)
