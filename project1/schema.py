import graphene

import project1.api.schema

all_schemas = [
    project1.api.schema
]

# You won't have to modify this here or in the real codebase ;)
all_queries = []
all_types = []
for schema in all_schemas:
    if hasattr(schema, 'Query'):
        all_queries.append(schema.Query)

    for k, v in schema.__dict__.items():
        if k not in {'DjangoObjectType', 'Query'} and isinstance(v, type):
            if issubclass(v, graphene.ObjectType) or issubclass(v, graphene.Interface):
                if v != graphene.ObjectType and v != graphene.Interface:
                    all_types.append(v)


class Query(*all_queries, graphene.ObjectType):
    """
    This class will inherit from multiple other Query classes.
    As we expand the API, we will define more Query classes
    in different files and inherit them here
    """
    pass


# This is the global GraphQL schema which our API will serve
schema = graphene.Schema(query=Query, types=all_types)