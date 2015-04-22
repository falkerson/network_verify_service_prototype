from tasks import base


class MulticastCheckTask(base.NetworkCheckTask):

    def run(self, *args, **kwargs):
        """
        Execute multicast check on remote server
        """

        print 'Multicast check'
