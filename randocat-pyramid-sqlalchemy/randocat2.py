import logging
import sys

from pyramid.config import Configurator
from pyramid.response import Response
from sqlalchemy import create_engine
from wsgiref.simple_server import make_server


PAGE_HTML = '''
<img src="{image_url}">
'''
PORT = 8080

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

Engine = create_engine('postgresql://postgres:@database/postgres')


def view_random_cat(request):
    with Engine.connect() as con:
        rows = con.execute(
            'SELECT image FROM cat ORDER BY RANDOM() LIMIT 1')

    cat_url = rows.first()[0]
    return Response(PAGE_HTML.format(image_url=cat_url))


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(view_random_cat, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', PORT, app)
    logging.info('%s now running on port %s!', sys.argv[0], PORT)
    server.serve_forever()
