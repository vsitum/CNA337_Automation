# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020

from Server import Server


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Vlado Situm")


# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    # TODO - Call Ping method and print the results

    my_server_ip = "52.14.212.224"
    my_rsa_key_file = "C:\\Users\\VladoPC\\.ssh\\id_rsa"
    username = "ubuntu"

    my_upgrade_command = 'sudo apt update && sudo apt upgrade -y'
    my_server = Server(my_server_ip, my_rsa_key_file, username, my_upgrade_command)

    print('Pinging server %s...' % my_server_ip)
    ping_result = my_server.ping()
    print(ping_result)
    if ping_result == 0:
        print("Pinging IP [%s] successful." % my_server_ip)
    else:
        print("Pinging IP [%s] Failed." % my_server_ip)

    print("\nUpdating server using ssh client from paramiko...")
    ssh_result = my_server.upgrade()
    print(''.join(ssh_result))

    print('Done.')
