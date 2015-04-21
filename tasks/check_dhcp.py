from tasks import base


class DHCPCheckTask(base.NetworkCheckTask):

    def run():
        """
        Execute dhcp check on remote server
        """

        print 'DHCP check'
