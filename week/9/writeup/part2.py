#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
	data = s.recv(1024)
	print(data)

	m = re.search(r'Find me the (\w+) hash of (\w+)', data)
	if not m:
		break
		
	hash, val = m.groups()

	# whitelisted input
	if hash not in ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']:
		break
	
	res = getattr(hashlib, hash)(val).hexdigest()

	print(res)
		
	s.send(res + '\n')
	
# close the connection
s.close()
