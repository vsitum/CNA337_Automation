# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020

import os

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Vlado Situm")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    IpAddress = '13.59.54.144'
    responce = os.system('ping -n 4 ' + IpAddress)


    # TODO - Call Ping method and print the results
    if responce == 0:
        print()
        print(IpAddress, 'is up!')
    else:
        print(IpAddress, 'is down!')
