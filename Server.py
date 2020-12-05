# Pinging AWS EC2 public IPv4.
# I worked with Abdi, Dorin and Igor, Mohammad and Saeid on this code.
# Liviu Patrasco (liviu_patrasco@hotmail.com) helped us to write the code.

import os
import paramiko


class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip, key_file, username, upgrade_command):
        # TODO -

        self.username = username
        self.command = upgrade_command
        self.key_file = key_file
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        result = os.system("ping -n 4 %s" % self.server_ip)
        return result

    def upgrade(self):
        # TODO - Use os module to ping the server

        # Create the ssh client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Make the connection to the server
        ssh_client.connect(hostname=self.server_ip, username=self.username, key_filename=self.key_file)

        # execute the command
        stdin, stdout, stderr = ssh_client.exec_command(self.command)

        # Return the result from both stdout and error
        result = stdout.readlines() + stderr.readlines()

        # Disconnect
        ssh_client.close()

        return result
