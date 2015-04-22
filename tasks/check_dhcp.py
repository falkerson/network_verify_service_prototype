from tasks import base


class DHCPCheckTask(base.NetworkCheckTask):

    def run(self, *args, **kwargs):
        """
        Execute dhcp check on remote server
        """

        print 'DHCP check'
