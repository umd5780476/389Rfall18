Writeup 9 - Crypto I
=====

Name: John
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: John

## Assignment 9 Writeup

### Part 1 (60 Pts)

This part was very simple and straight forward. The assignment description details exactly what I had to do. Go through all the possible combinations of salt + password, hash them, and check if see if it is one of our known hashes. Even though it is not pretty or efficient, my code does work.

![](https://i.imgur.com/3QvV6V4.png)

````
mjordan c35eb97205dd1c1a251ad9ea824c384e5d0668899ce7fbf269f99f6457bd06055440fba178593b1f9d4bfbc7e968d48709bc03e7ff57056230a79bc6b85d92c8
uloveyou d39d933d91c3e4455beb4add6de0a48dafcf9cb7acd23e3c066542161dcc8a719cbac9ae1eb7c9e71a7530400795f574bd55df17a2d496089cd70f8ae34bf267
kneptune 9a23df618219099dae46ccb917fbc42ddf1bcf80583ec980d95eaab4ebee49c7a6e1bac13882cf5dd8d3850c137fdff378e53810e98f7e9508ca8516e883458e
ppizza 70a2fc11b142c8974c10a8935b218186e9ecdad4d1c4f28ec2e91553bd60cfff2cc9b5be07e206a2dae3906b75c83062e1afe28ebe0748a214307bcb03ad116f
````

### Part 2 (40 Pts)

I initial didn’t understand why the stub code was provided. I tried to complete the challenge by hand, but I was way too slow. So, I used the stub code to script it.

I started off by fighting with python regular expressions while trying to extract the hash method and value from the received data. To call the hash function in python, I looked up if python supported reflection and learned about the ```` getattr```` function. This prevented me from having to write out a bunch of if statements. Initially, I directly passed the input to ```` getattr````. However, I decided that since this is a security course, I should at least have some sort of input validation so the server can’t run arbitrary functions on my machine.

![](https://i.imgur.com/zaFr08u.png)

````
You win! CMSC389R-{H4sh-5l!ngInG-h@sH3r}
````
