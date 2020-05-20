#!/usr/bin/env python3
# A simple DNS resolution script
#######################################################
# Usage Example:
# Import pyQueryDNS
# hosts = ['google.com','yahoo.com']
# x = get_address(hosts)
# print(x)
#
# ips = ['8.8.8.8', '7.7.7.7']
# z = get_hostname(ips)
# print(z)
#######################################################
import socket


def get_address(hosts):
    rtn_string = []
    for i in range(len(hosts)):
        rtn_string.append(hosts[i] + '|' + socket.gethostbyname(hosts[i]))
    return rtn_string


def get_hostname(address):
    rtn_string = []
    for i in range(len(address)):
        rtn_string.append(address[i] + '|' + socket.getfqdn(address[i]))
    return rtn_string
