Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: John
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: John

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. Did the hackers use the traceroute command on any websites? If so, list one.

128.8.120.43 csec.umiacs.umd.edu

I looked up how traceroute works: https://www.computerhope.com/unix/utracero.htm

>traceroute attempts to trace the route an IP packet would follow to some Internet host by launching probe packets with a small ttl (time to live) then listening for an ICMP "time exceeded" reply from a gateway. It start its probes with a ttl of one and increases this by one until it gets an ICMP "port unreachable" (or TCP reset), which means we got to the "host", or hit a max (which defaults to 30 hops).

Wireshark shows a bunch of ICMP and UDP traffic. I found packets saying  “destination unreachable” from 128.8.120.43 which is the host of the cybersecurity club website.


2. What are the names used by the hackers?

laz0rh4x and c0uchpot4doz

3.	What are the hackers' IP addresses, and where are they connecting from?

Laz0rh4x: 104.248.224.85

c0uchpot4doz: 142.93.118.186

They are using DigitalOcean servers in North Bergen, New Jersey.  

4. What port are they using to communicate on our server?

c0uchpot4doz sends a HTTP request to your server on port 80. The source port is 35020.

He also performs a traceroute to your server which uses many ports. Destination ports: 33434-33476.


5.	Did they mention their plans? When are they happening?

They mentioned their plans were saved in a file hosted on google drive. Tomorrow at 1500. 

The arrival time of one packet is Oct 24, 2018 22:42:39.699480000 Eastern Daylight Time. So they are planning for Oct 25, 2018 3:00pm EDT.


6. Did they send any files to each other? List any links or related information you found.

They sent a link to a file stored on google drive.

https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing 

7.	When do the hackers expect to see each other next?

Oct 25, 2018 3:00pm EDT.


![](https://i.imgur.com/txazKi0.png)


### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*

1.	When was update.fpff generated?

Unix timestamp: 1540428007

Wednesday, October 24, 2018 8:40:07 PM GMT-04:00 DST

2.	Who authored update.fpff?

laz0rh4x

3.	How many sections does update.fpff say it has? How many sections are there really?

The header says there are 9 sections. There are actually 11 sections.

4.	List each section, giving us the data in it and its type.

See below

5.	Report at least one flag hidden in update.fpff. Any other flag found will count as bonus points towards the competition portion of the syllabus.


Base64 decode Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9 gives the flag: CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}

Image stored in the custom file ![](https://i.imgur.com/6RpAKIc.png)

[(422) 537 - 7946](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

Flag hidden in text. If you have the source image, steganography is easy to detect. The same is true for text steganography. CMSC389R-{PlaIN_dIfF_LAG} https://i.imgur.com/2C5yA5C.png



````
------- HEADER -------
MAGIC: 0xdeadbeefL
VERSION: 1
TIMESTAMP: 1540428007
AUTHOR: laz0rh4x
SECTION COUNT: 9
-------  BODY  -------
section: 1
stype: 9
slength: 51
Call this number to get your flag: (422) 537 - 7946
type: SECTION_ASCII

section: 2
stype: 5
slength: 60
['\x03\x00\x00\x00', '\x01\x00\x00\x00', '\x04\x00\x00\x00', '\x01\x00\x00\x00', '\x05\x00\x00\x00', '\t\x00\x00\x00', '\x02\x00\x00\x00', '\x06\x00\x00\x00', '\x05\x00\x00\x00', '\x03\x00\x00\x00', '\x05\x00\x00\x00', '\x08\x00\x00\x00', '\t\x00\x00\x00', '\x07\x00\x00\x00', '\t\x00\x00\x00']
type: SECTION_WORDS

section: 3
stype: 6
slength: 16
lat: 38.991610, long: -77.027540
type: SECTION_COORD

section: 4
stype: 7
slength: 4
reference: 1
type: SECTION_REFERENCE

section: 5
stype: 9
slength: 60
The imfamous security pr0s at CMSC389R will never find this!
type: SECTION_ASCII

section: 6
stype: 9
slength: 991
The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}
type: SECTION_ASCII


section: 7
stype: 6
slength: 16
lat: 38.991094, long: -76.932802
type: SECTION_COORD

section: 8
stype: 1
slength: 245614
type: SECTION_PNG
https://i.imgur.com/6RpAKIc.png

section: 9
stype: 9
slength: 22
AF(saSAdf1AD)Snz**asd1
type: SECTION_ASCII

section: 10
stype: 9
slength: 45
Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9

type: SECTION_ASCII

section: 11
stype: 2
slength: 48
['\x04\x00\x00\x00\x00\x00\x00\x00', '\x08\x00\x00\x00\x00\x00\x00\x00', '\x0f\x00\x00\x00\x00\x00\x00\x00', '\x10\x00\x00\x00\x00\x00\x00\x00', '\x17\x00\x00\x00\x00\x00\x00\x00', '*\x00\x00\x00\x00\x00\x00\x00']
type: SECTION_DWORDS
````
