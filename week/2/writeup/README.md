Writeup 2 - OSINT (Open Source Intelligence)
======

Name: John 
Section: 0102

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: John

## Assignment 2 writeup

### Part 1 (45 pts)

1.  Fred Krueger. It is listed on his twitter and Instagram.


2. I used https://namechk.com/ to find registered social media accounts with the username kruegster1990. 
* https://twitter.com/kruegster1990
* https://www.instagram.com/kruegster1990/
* https://www.reddit.com/user/kruegster1990/

I found his email address on the about section of his website. kruegster1990@tutanota.com


3.  142.93.118.186
I looked up the dns records for cornerstoneairlines.co


4. I found this URL from the robots.txt file on his website.
http://cornerstoneairlines.co/secret/ CMSC389R-{fly_th3_sk1es_w1th_u5}


5. His website (cornerstoneairlines.co) has a link to an admin page. 142.93.117.193


6. I used iplocation.net to look up the location of the ip addressed I encountered.
* 142.93.117.193	United States  	New Jersey	North Bergen
* 142.93.118.186	United States  	New Jersey	North Bergen


7. Ubuntu
I looked at the HTTP response headers as they usually include system information. You could probably use nmap to find a more specific os version.

````
Server: Apache/2.4.18 (Ubuntu)
````

8. CMSC389R-{h1dden_fl4g_in_s0urce}  HTML source code comment http://cornerstoneairlines.co/ 

CMSC389R-{fly_th3_sk1es_w1th_u5} HTML source code comment http://cornerstoneairlines.co/secret/

CMSC389R-{dns-txt-rec0rd-ftw} DNS TXT record


### Part 2 (55 pts)


I used nmap to look for open ports on the ip addresses I encountered in part 1.

```` 
user@kali:~$ nmap -p - 142.93.117.193 -T5
Starting Nmap 7.70 ( https://nmap.org ) at 2018-09-09 10:32 EDT
Nmap scan report for 142.93.117.193
Host is up (0.044s latency).
Not shown: 65521 filtered ports
PORT      STATE  SERVICE
80/tcp    open   http
110/tcp   closed pop3
113/tcp   closed ident
139/tcp   closed netbios-ssn
199/tcp   closed smux
443/tcp   closed https
445/tcp   closed microsoft-ds
554/tcp   open   rtsp
995/tcp   closed pop3s
1723/tcp  closed pptp
2222/tcp  open   EtherNetIP-1
3306/tcp  closed mysql
7070/tcp  open   realserver
10010/tcp open   rxapi

Nmap done: 1 IP address (1 host up) scanned in 166.18 seconds
```` 

```` 
user@kali:~$ nmap -p - 142.93.118.186 -T5
Starting Nmap 7.70 ( https://nmap.org ) at 2018-09-09 10:32 EDT
Nmap scan report for 142.93.118.186
Host is up (0.039s latency).
Not shown: 65524 filtered ports
PORT     STATE  SERVICE
22/tcp   open   ssh
53/tcp   closed domain
80/tcp   open   http
110/tcp  closed pop3
113/tcp  closed ident
135/tcp  closed msrpc
143/tcp  closed imap
554/tcp  open   rtsp
1025/tcp closed NFS-or-IIS
7070/tcp open   realserver
8080/tcp closed http-proxy

Nmap done: 1 IP address (1 host up) scanned in 175.12 seconds
```` 

The stub shows connecting to TCP and the description says I will have access to a system shell. So, I looked for SSH services running on the servers.

```` 
142.93.117.193
2222/tcp  open   EtherNetIP-1

142.93.118.186
22/tcp   open   ssh
```` 

I tried to brute force these using hydra and multiple different usernames but I had no success.  

````
hydra -l kruegster1990 -P /usr/share/wordlists/rockyou.txt -s 2222 142.93.117.193 ssh
````

A few days later I revisted this project and tried again.


The open ports had changed so I am not sure if my first scan was incorrect or the servers had been reconfigured.

````
nmap -p - 142.93.117.193 -T5
Starting Nmap 7.70 ( https://nmap.org ) at 2018-09-11 16:48 Eastern Daylight Time
Nmap scan report for 142.93.117.193
Host is up (0.013s latency).
Not shown: 65527 closed ports
PORT      STATE    SERVICE
25/tcp    filtered smtp
80/tcp    open     http
554/tcp   open     rtsp
1337/tcp  open     waste
2222/tcp  open     EtherNetIP-1
7070/tcp  open     realserver
10010/tcp open     rxapi
11211/tcp filtered memcache

Nmap done: 1 IP address (1 host up) scanned in 15.87 seconds
````

````
nmap -p - 142.93.118.186 -T5
Starting Nmap 7.70 ( https://nmap.org ) at 2018-09-11 16:50 Eastern Daylight Time
Nmap scan report for 142.93.118.186
Host is up (0.014s latency).
Not shown: 65529 closed ports
PORT      STATE    SERVICE
22/tcp    open     ssh
25/tcp    filtered smtp
80/tcp    open     http
554/tcp   open     rtsp
7070/tcp  open     realserver
11211/tcp filtered memcache

Nmap done: 1 IP address (1 host up) scanned in 15.55 seconds
````


I used telnet to connect to all of the open ports and discovered a username prompt on port 1337 of the admin server.

I wrote a python script to brute force the login and gain access to the server. 


Once I had access to the server, I looked around for flags. I initially tried using grep but that did not help find the correct flag.

His Instagram page has his flight number and there is a text file with the same name.

CMSC389R-{c0rn3rstone-air-27670}

