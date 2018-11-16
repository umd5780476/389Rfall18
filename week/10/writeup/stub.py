#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import re
from time import sleep

#####################################
### STEP 1: Calculate forged hash ###
#####################################




message = 'message'    # original message here
malicious = 'malicious'  # put your malicious message here


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('142.93.118.186', 1234))

def recv():
	sleep(0.5)
	return s.recv(1024)
	
recv()
s.send('1\n')
recv()
s.send(message + '\n')
data = recv()

m = re.search(r'Your hash: (\w+)', data)
if not m:
	exit()
		
legit, = m.groups()
print('legit ' + legit)

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))


# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print('fake ' + fake_hash)


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits

def get_padding(secret_len):
	totalLength = 8*(secret_len + len(message))
	
	padding = '\x80'
	for i in range(totalLength + 8, 512 - 8*8, 8):
		padding = padding + '\x00'
	padding = padding + chr(totalLength) + '\x00\x00\x00\x00\x00\x00\x00'
	return padding
	
# payload is the message that corresponds to the hash in `fake_hash`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = fake_hash

for l in range(6,16):
	payload = message + get_padding(l)
	payload = payload + malicious

	s.send('2\n')
	recv()
	s.send(fake_hash + '\n')
	recv()
	s.send(payload + '\n')
	print(recv())
	
	# send `fake_hash` and `payload` to server (manually or with sockets)
	# REMEMBER: every time you sign new data, you will regenerate a new secret!

