import abc

import six


@six.add_metaclass(abc.ABCMeta)
class NetworkCheckTask(object):

    @abc.abstractmethod
    def run(self, *args, **kwargs):
        """
        Execute some staff on remote server
        """
