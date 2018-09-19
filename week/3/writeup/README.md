Writeup 3 - OSINT II, OpSec and RE
======

Name: John
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: John

## Assignment 3 Writeup

### Part 1 (100 pts)

The first major issue is Fred’s admin server is that he uses some simple TCP application for remotely accessing his server. Just using a socket leaves communications vulnerable to a man-in-the-middle attack. (evidence example: https://en.wikipedia.org/wiki/Man-in-the-middle_attack)  Additionally, it is not encrypted so it would be easy for someone to watch what he is doing. He already has ssh setup so he should just use that instead. 

Another issue is with his use of passwords. The password to his admin server was very simple and easy to brute force with a password list. He should use more secure passwords or use a password manager to pick and store strong passwords. If he decides to use ssh to connect to his server (which he should), he should use a ssh key instead of a password. I would advise him to disable password authentication all together or use fail2ban or some other program to monitor access attempts and ban bad actors. Moving ssh to a different port will not help in the long run. Learn about fail2ban: https://www.fail2ban.org/wiki/index.php/Main_Page

One less important issue was his attempt to use robot.txt to hide a “secret” page. It only prevents respectable crawlers from not accessing parts of a website. Malicious crawlers will ignore it or use it to find interesting pages. If he wants a “secret” page, he should use HTTPS and require some sort of authentication. Learn about HTTPS https://www.instantssl.com/ssl-certificate-products/https.html
