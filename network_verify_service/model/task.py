class Task(object):

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __json__(self):
        return dict(
            name=self.name,
            status=self.status
        )
