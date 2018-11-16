Writeup 10 - Crypto II
=====

Name: John
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: John

## Assignment 10 Writeup

### Part 1 (70 Pts)

In this exercise we exploit MD5 to sign a message using a previously signed message. This is possible because the output of MD5 is the state of the internal variables. We can initialize MD5 with these variables and use it to hash a longer message. The result of the hash is ````hash(secret + original message + padding + extra message)```` By guessing the length of the secret, we can calculate the padding since we know the original message. This lets us “sign” a message without knowing the key. Alternatively, we could just brute force the key since MD5 fast and insecure.

To write the code for this assignment, I followed the comments. The only difficult part was calculating the padding, which I struggled with because I though 1 byte was equivalent to 4 bits, smh. Once I figured out that bug, it was easy to get working. I chose to use a socket to communicate with the server because copying and pasting was tiresome at the start. One ambiguous part of this assignment was if the key was allowed to not be a multiple of 8 bits. 
 

````
Now let me see...

Wow... I've never signed this data before!
This is crazy... I can't let anyone know that my service is broken!
Hey, if I give you this flag, you better keep quiet about this!
CMSC389R-{i_still_put_the_M_between_the_DV}
Made in Maryland - Substantial
````


### Part 2 (30 Pts)

I started by creating a message in ````msg.txt````. Then I reviewed the slides to see what commands I needed. The two commands I used are shown below.
````
gpg --import pgpassignment.key
gpg -e -r "UMD Cybersecurity Club <president@csec.umiacs.umd.edu>" msg.txt
mv msg.txt.gpg message.private
````

* generating keys

````gpg --gen-key````

* importing someone else's public key

````gpg --import pubkey.asc````

* encrypting a message for that someone else and dumping it to a file

````gpg --encrypt --output output.gpg -r "someone’s name" input_file.txt````




