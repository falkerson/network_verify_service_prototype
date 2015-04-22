from pecan import abort, expose, redirect
from webob.exc import status_map


class TaskController(object):

    @expose(generic=True, template='json')
    def index(self):
        return {
            'tasks': [
                {
                    'id': '1',
                    'name': 'check_multicast'
                },
                {
                    'id': '2',
                    'name': 'check_dhcp'
                },
                {
                    'id': '3',
                    'name': 'check_connectivity'
                }
            ]
        }

    @index.when(method='PUT')
    def index_PUT(self, id):
        return 'task {0} is running'.format(id)


class RootController(object):

    tasks = TaskController()
