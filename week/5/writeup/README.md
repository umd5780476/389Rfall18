Writeup 5 - Binaries I
======

Name: John
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: John

## Assignment 5 Writeup

My approach to part 1 was to write a function in assembly that would perform the required operation. I did not try to covert the C code into assembly. If the goal was to convert the C code to assembly, I might as well use a compiler. I chose to limit myself to the most basic instructions as I have never written x86 assembly before. I designed my code as if it was a “do while” loop. The condition was at the end, so to exit the loop, you just fall through. As the start, I jump directly to the condition as I want to check the condition before the first iteration of the loop. To keep track of the current iteration, I used the register rcx. I compare this value to the parameter to see if I should keep looping. The main problem I encountered was that I had difficulty understanding how to move just a single byte/character. I also did not know that both parameters to the mov instruction had to be the same size. The slides were not that helpful and it’s hard to know what to Google when I have such a basic understanding of this topic. To debug my program, I just looked at the output. I am not familiar with gdb and I did not need to complicate the task even further. One interesting output I encountered was “Hello zzzzz” There are the correct number of ‘z’ but there is no explanation point at the end. This was because I was copying the whole register instead of 1 byte. And the junk/zeros in the register were overwriting the explanation point. 

For the second part, I copied my code from part 1. I initially tried to move the character from memory directly to memory, but I encountered some errors and I had no idea how to limit it to one byte, so I used a register instead. I find the whole idea with specifying how many byte you want to move with slight changes in the register names to be confusing. I had to look up the special names for the r8 register and I found them here: https://cs.brown.edu/courses/cs033/docs/guides/x64_cheatsheet.pdf Luckily, that was the only problem I encountered in this part. 

What to do and what not to do when hand-writing assembly functions: The first rule to follow is: don’t write assembly. There is a reason why people write compilers. Unless you enjoy banging your head against a desk, I would recommend not trying to write assembly. At my internship there was a developer who was only halfway paying attention in a meeting and volunteered himself to work on a project no one else wanted to. Little did he know, the project required him to write assembly and debug someone else’s assembly code. People always joked about it and you could hear him getting frustrated. 


