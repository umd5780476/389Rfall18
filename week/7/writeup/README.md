Writeup 7 - Forensics I
======

Name: John
Section: 0102

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: John

## Assignment 7 writeup

### Part 1 (40 pts)

1.	What kind of file is it?

JPEG file 

2.	Where was this photo taken? Provide a city, state and the name of the building in your answer.

Regus - Illinois, Chicago - John Hancock Center
875 North Michigan Avenue, 31st Floor, Chicago, IL 60611

3.	When was this photo taken? Provide a timestamp in your answer.

August 22, 2018   11:33:24AM

4.	What kind of camera took this photo?

Apple iPhone 8

5.	How high up was this photo taken? Provide an answer in meters.

540 meters

6.	Provide any found flags in this file in standard flag format.

strings image.jpg | grep -C1 "CMSC389R"

You found the hidden message! CMSC389R-{look_I_f0und_a_str1ng}


Tried to used steghide to find more flags since it was hinted at during the lecture, but I didn’t know what password to use.
```
steghide.exe --extract -sf image
Enter passphrase:
steghide: could not extract any data with that passphrase!
```

![](https://i.imgur.com/FcDsZ4z.png)


### Part 2 (55 pts)

I ran the binary in my kali vm cause why not lol. It outputted some text but no flag. I knew I had to decompile it or run in in a debugger. I decided to try gdb as it is the only debugger I have used before and I couldn’t remember the name of the fancy one shown off in class. After consulting a gdb cheat sheet, I got the program debugging and stepping through statements. I set a brain point on the “main” function and stepped through until the end of the program. It was a very short program. Only 3 or so steps. I saw that it accessed a file called ```/tmp/.stego``` so I knew I had to analyze it.

First, I tried to figure out what type of file it was using the ```file``` command. It did not give me any useful results. It simply said it was ```”data”```. So I scrolled through the slides looking for something else to try. Next, I tried binwalk. It told me there was a JPEG image within the file. 

![](https://i.imgur.com/okPerFU.png)

I had a lot of trouble trying to actually get binwalk to extract the file. Nothing I found on google helped. I eventually resorted to using notepad++ to delete the first byte of the file. After that, I was able to open it as a valid JPEG image.

![](https://i.imgur.com/d36egVZ.jpg)

Since steghide was mentioned in class, I assumed it was the next step, but I still did not know a password. I tried the passwords Freddy Kruger used but to no avail. Like the Pokémon on his Instagram page, I used the image as a hint and it worked!

![]( https://i.imgur.com/AWsX7Bk.png)

```Congrats! Your flag is: CMSC389R-{dropping_files_is_fun}```



