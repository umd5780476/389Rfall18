#!/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version, timestamp, author, section_count = struct.unpack("<LLL8sL", data[0:24])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %d" % int(timestamp))
print("AUTHOR: %s" % author)
print("SECTION COUNT: %d" % int(section_count))
print("-------  BODY  -------")

	
i = 24
j = 1

while (i < len(data)):
	stype, slength = struct.unpack("<LL", data[i:i+8])
	svalue = data[i+8:i+8+slength]
	type = ""
	
	print("section: %d" % j)
	print("stype: %s" % stype)
	print("slength: %d" % int(slength))

	
	if stype == 0x1:
		type = "SECTION_PNG"
		with open("section %d.png" % j, "wb") as f:
			f.write(b'\211PNG\r\n\032\n')
			f.write(svalue)
	elif stype == 0x2:
		type = "SECTION_DWORDS"
		dwords = []
		for k in range(0, len(svalue)/8):
			dwords.append(svalue[k*8:k*8+8])
		print(dwords)
	elif stype == 0x3:
		type = "SECTION_UTF8"
	elif stype == 0x4:
		type = "SECTION_DOUBLES"
	elif stype == 0x5:
		type = "SECTION_WORDS"
		words = []
		for k in range(0, len(svalue)/4):
			words.append(svalue[k*4:k*4+4])
		print(words)
	elif stype == 0x6:
		type = "SECTION_COORD"
		lat, long = struct.unpack("<dd", svalue)
		print("lat: %f, long: %f" % (lat, long))
	elif stype == 0x7:
		type = "SECTION_REFERENCE"
		reference = struct.unpack("<L", svalue)
		print("reference: %d" % reference)
	elif stype == 0x9:
		type = "SECTION_ASCII"
		print(svalue)
	else:
		type = "???"
		
		
	f = open("section %d.%d" % (j, int(stype)), "w")
	f.write(svalue) 
	
	print("type: %s" % type)
	print("")
	
	i += 8 + slength
	j += 1



