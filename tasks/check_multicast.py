from tasks import base


class MulticastCheckTask(base.NetworkCheckTask):

    def run():
        """
        Execute multicast check on remote server
        """

        print 'Multicast check'
