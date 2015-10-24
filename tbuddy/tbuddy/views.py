from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    # MyModel,
    Batch,
    Queue,
    Merge,
    )

from Merges.merges import recent
from stub import give_me_data

import time

@view_config(route_name='stub', renderer='templates/stub.jinja2')
def stub(request):
    return {}

@view_config(route_name='main', renderer='templates/main.jinja2')
def main(request):
    try:
        batches = DBSession.query(Batch).all()
        queue = DBSession.query(Queue).all()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'batches' : batches, 'queue' : queue, 'project' : 'tbuddy'}

@view_config(route_name='merges', renderer='templates/merges.jinja2')
def merges(request):
    recent_merges = recent()
    return { 'recent_merges' : recent_merges }

@view_config(route_name='giveData')
def giveData(request):
    data = give_me_data()
    return Response(data)

# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     try:
#         one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
#     except DBAPIError:
#         return Response(conn_err_msg, content_type='text/plain', status_int=500)
#     return {'one': one, 'project': 'tbuddy'}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_tbuddy_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

