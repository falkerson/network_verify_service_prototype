from pecan import abort, expose, redirect
from stevedore import extension
from webob.exc import status_map


class TaskController(object):

    @expose(generic=True, template='json')
    def index(self):
        """Get all pluggable tasks
        """

        tasks = []
        mgr = extension.ExtensionManager(
            namespace='tasks',
            invoke_on_load=True
        )

        for i, ext in enumerate(mgr):
            tasks.append({
                'id': i,
                'name': ext.name
            })

        return {'tasks': tasks}

    @index.when(method='PUT')
    def index_PUT(self, id):
        return 'task {0} is running'.format(id)


class RootController(object):

    tasks = TaskController()
