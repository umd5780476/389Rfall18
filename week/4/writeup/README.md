Writeup 3 - Pentesting I
======

Name: John
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: John

## Assignment 4 Writeup

### Part 1 (45 pts)
When faced with a command injection problem, I find it is best to go and try to do it yourself. So I executed the netcat command and played around with it for a bit. My initial attempts of trying to close quotes and insert commands failed, as the command was extremely simple and it did not use any quotes. With more attempts, I got a better understanding of how it works. From my understanding, the service listening to the socket literally just appends “ping ” to your input, executes it, and sends you back the result. After I discovered this, I started working on the shell in part 2.

After I had a working shell, I went on a hunt for the flag. Just like in previous assignments, the flag was store in the home directory. How convenient! With a simple “cat” command, I printed out the flag.

````
\week4>python shell.py
? shell
/>cd home
/home>ls
flag.txt
/home>cat flag.txt
Good! Here's your flag: CMSC389R-{p1ng_as_a_$erv1c3}
/home>
````

Fred should stop making these poorly designed services and instead use ssh. In the previous assignment, he should have used ssh instead of his own custom insecure shell. In this assignment, he should just use his local machine to ping a host or ssh into his server and do it there. If he really thinks “Ping as a Service” is the next billion dollar idea, then I would tell him to validate and sanitize his user input. Stop assuming the user is following your directions and is doing what you expect. An ever better idea would be to whitelist input so that only his expected servers can be pinged. That would prevent some nasty emails and men in suits from showing up if a user was to ping certain ip addresses.

I tried to find the program he is using but I was unsuccessful.  I couldn’t find what was listening to ports. I was unable to find which processes were running. I couldn't figure out how to list open network connections. The server is too locked down or I just doesn’t have many applications available. 

### Part 2 (55 pts)

To crate the shell, I first tried to inject commands to run bash. This was not successful because there is no way for me to input commands to bash. The program listening to the socket will not relay your input to the process or give you intermediate results. So I was stuck with running commands one at a time. This created a new challenge. I would have to keep track of the current directory in the python program, instead of letting bash handle it. So, added some code to keep track of the current directory. It works for simple commands but if the user tried to execute some more complex commands like: “echo ‘hello’ && cd /”, it would fail. I chose not to handle cases like this as they were out of the scope of this assignment.

To create the “pull” command, my implementation executes “cat” on the specified remote file and then saves it to a local file. One drawback is that this only works for text files. I tried to add support for binary files by using “base64” instead of “cat,” but I ran into problems. “base64” will encode a binary file in base64, and print it out in ascii. This can then be decode to the original binary format in python, and saved to the local file. There was some issue with my implementation of this.

