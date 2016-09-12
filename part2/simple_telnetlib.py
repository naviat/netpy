#!/usr/bin/env python
'''
Script that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.
'''

import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6 

def send_command(remote_conn, cmd):
	'''
	Send a command dow telnet channel
	Return response
	'''
	cmd = cmd.rstrip()
	remote_conn.write(cmd + '\n')
	time.sleep(1)
	return remote_conn.read_very_eager()

def telnet_connect(ip_addr):
	'''
	Establish telnet connection
	'''
	try:
		return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
	except socket.timeout:
		sys.exit("Connection refused")


def main():
	'''
	Script that connects to router and runs 
	'show ip in brief.
	'''
	ip_addr = raw_input("IP address: ")
	ip_addr = ip_addr.strip()
	username = 'pyclass'
	password = getpass.getpass()

	remote_conn = telnet_connect(ip_addr)
	output = login(remote_conn, username, password)

	time.sleep(1)
	remote_conn.read_very_eager()
	disable_paging(remote_conn)

	output = send_command(remote_conn, 'show ip int brief')

	print "\n\n"
	print output
	print "\n\n"

	remote_conn.close()

if __name__ == "__main__":
	main()

