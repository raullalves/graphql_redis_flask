import graphene

import flask
from flask_graphql import GraphQLView
from graphql_client.query import Query

def define_routes(app):
    @app.errorhandler(404)
    def not_found(error):
        return flask.make_response(flask.jsonfy({'success': False, 'error': error}), 404)

    @app.route('/')
    def root_flask_server():
        return 'Your flask server is running'

    schema_query = graphene.Schema(query=Query)

    app.add_url_rule('/graphql_client-query', view_func=GraphQLView.as_view(
        'graphql_client-query',
        schema=schema_query, graphiql=True
    ))
