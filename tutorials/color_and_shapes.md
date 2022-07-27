---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: py5bot
  language: python
  name: py5bot
---

# Your first py5 sketch

When we're instructing a computer to run code, we cannot use regular human language. Instead, code takes the form of an *algorithm* or a series of algorithms which are handed to the computer. Although the word algorithm has had a lot of complex recent use, at its simplest form, an algorithm is just a set of rules or instructions for a computer to follow. Unlike most humans, if a computer is given unclear instructions, it can't problem-solve its way out of the situation - it will simply stop in its tracks. This means that small errors in the syntax (grammatical structure) of your code will cause many of the problems you run into, and it will get easier as time goes on to anticipate and correct them.

Get familiar with the [py5 reference](https://py5.ixora.io/reference/sketch.html) and [py5 cheatsheet](https://raw.githubusercontent.com/tabreturn/processing.py-cheat-sheet/master/py5/py5_cc.pdf) - these will both serve as your glossary for the functions and methods we discuss here. When you're using the py5 reference pages, be aware that they use a slightly different mode, and slightly different syntax. We're using something called *static mode*, which is a simple way to get started with py5 (especially if you're using [py5bot](http://py5.ixora.io/tutorials/introduction_to_py5bot.html)). If the reference seems to be starting a lot of functions and arguments with `py5.`, or splits code up into blocks labeled with functions like `setup()` and `draw()`, you can safely omit that while using static mode. 

In this tutorial, you'll be walked through some basic functions in py5, including sizing your visual output, using color and drawing simple shapes.

## hello world

Let's make our first *sketch* in py5 (which is just what you call a program in this environment). If you're using an IDE (integrated development environment) of some kind on your computer, you'll want to start with creating a new file and saving it somewhere you can easily find again. If you're instead using this resource online, the easiest way to work with these sketches will be using the Binder or Live Code options, which you can see by hovering your mouse over the rocket ship icon at the top of this page.

Our first sketch will be a simple "hello world" sketch - a concept that is common across all sorts of programming languages and environments. We'll put in only two lines to start with:

```{code-cell} ipython3
size(500, 500)
print('hello world')
```

Run this code (either above using Live Code/Binder or in your own program) and two things will happen.
1. A window or square (your sketch) will open, with a size of 500 by 500 pixels.
2. Somewhere, the following text will be printed into the console: `hello world`.

You've just used your first two functions in py5! The name of the function, like *size* or *print*, is followed by two parenthesis, and inside of them you put the *arguments* that the function is working with. `size()` takes two arguments: the width and height of the window you want your sketch to be contained in. `print()` takes only one: the text you want to print in the console (which in other development environments might be called your shell, or your debug log - no matter, it's all the same thing!) 

When explaining arguments and what they do, it's common to use a format like `size(width, height)` - you can tell just by looking that if you run `size()`, the first argument will be your width, and the second your height. In fact, this format is used throughout the reference and cheatsheet I mentioned above. Look out for it! 

## comments

While writing code, it's very easy to end up with a big block of functions, one after the other. If something goes wrong, or if someone else is meant to be reading and understanding your code, it's essential to leave some notes. Comments are just that - lines of code that will not be run by the computer, so you can use them for noting things down, describing your functions, or even to temporarily disable parts of your code by "commenting them out". 

You can use # to comment out a single line, and flank sections of code with ''' to comment out multiple lines at once.

```{code-cell} ipython3

# This is a comment on a single line!

# Setting the size of our sketch
size(500, 500)

# Now let's print a message in the Shell
print('hello world')

'''
These are multi-line comments.
None of these lines are run as code.
print('Not even this one!')
'''
```

## whitespace

Python is sensitive to whitespace - that is, tapping the space bar to indent something a little, or using *tab* to move a whole block of code to the right. Because Python uses indents to differentiate between different blocks of code, using it in the wrong place can be catastrophic. If you indent the `size(500,500)` line in your first program, you can encounter an error. These errors will vary by program, but for example:

```
There is an indentation problem with your code on line 4:
--> 4        size(500, 500)
             ^
```
Many different development environments will do their best to point mistakes like this out to you. In this case, it tells you exactly what the problem is, where to find it in your code, and even (with that little carat, or upwards pointing arrow) exactly where on the line it stops understanding what's going on! You'll gain a better understanding of when whitespace is necessary when you begin working with more complex code.

We can force a different error by changing our `size(500,500)` line to `size(500,500` with a missing parenthesis. 

```
There is a problem with your code:
SyntaxError: '(' was never closed (<py5bot>, line 5)
    size(500, 500
        ^
```

Not every error is perfect, but at the very least, they will give you a clue that something is going wrong in the vicinity.

## colo(u)r

If you've done any work with graphics editing software like Photoshop or GIMP, you might be familiar with some of the different ways of digitally defining color. RGB (Red, Green, and Blue) values and HSB (Hue, Saturation, and Brightness) can both be used in py5 to great effect - for now, we're using RGB values, in particular represented by a *hex code* like #FF0000. 

In a hexadecimal (or hex for short) code like this, each pair of letters or numbers represents a color. So, we can tell #FF0000 will be red because the first two digits (R) are at their highest, while the G and B digits are at their lowest. Just like mixing light in a prism, #FFFFFF (RGB all at their highest value) is white, and #000000 is black.

When you're drawing a picture, you might do the linework and then fill it in with color afterwards. In py5, you do this in reverse - you tell the program what color something will be *before* you create it. As an example, let's create a red rectangle in our sketch. Here are our next two functions:

`fill(color)`

`rect(x_coordinate, y_coordinate, width, height)`

The function `fill()` will begin filling elements in your sketch with color if supplied with a color as its argument. `rect()` will draw a rectangle on your screen - the x coordinate is how far it is from the left edge of the screen, the y coordinate is how far it is from the top edge, and the width and height are simply its dimensions in pixels. (This system of positioning by coordinates is common in a lot of digital spaces, and you'll get your head around it quickly if you haven't already.) Put together, and with those arguments swapped out, your code might look something like this:

```{code-cell} ipython3
size(500,500)
fill('#FF0000')
rect(100, 150, 200, 300)
```

<img src="https://tabreturn.github.io/img/pitl01/colour-fill-rect.png">

The `fill()` function will last until you tell it to stop - no matter how many shapes you draw beneath it, all will have the color you specified. To end your `fill()`, you use a different function - `no_fill()`. It doesn't take any arguments at all.

```{code-cell} ipython3
size(500,500)

# red rectangles
fill('#FF0000')
rect(100,150, 200,300)
rect(10,15, 20,30)

# orange square
fill('#FF9900')
rect(50,100, 150,150)

# fill-less square
no_fill()
rect(250,100, 150,150)
```

<img src="https://tabreturn.github.io/img/pitl01/colour-fill-additional-rect.png">

By now you've probably noticed that all of these rectangles have a black outline. This outline can also be called a *stroke*, and that's what we call it in py5. Exactly like `fill()`, we can use `stroke()` with a color to change all subsequent outlines to that color. You can also change how big the outline is with `stroke_weight()` or entirely remove it with `no_stroke()`. Add a white stroke with a `stroke_weight()` of 3 above your rectangles to see how it works:

```{code-cell} ipython3
size(500,500)

# setting our stroke color and width!
stroke('#FFFFFF')
stroke_weight(3)

# red rectangles
fill('#FF0000')
rect(100,150, 200,300)
rect(10,15, 20,30)

# orange square
fill('#FF9900')
rect(50,100, 150,150)

# fill-less square
no_fill()
rect(250,100, 150,150)
```

<img src="https://tabreturn.github.io/img/pitl01/colour-stroke.png">

There's a few more ways to fine-tune those outlines... `stroke_cap()` can change these outlines to be sharper or to stick out, and `stroke_join()` changes how they connect at corners. 

*Reference pages: [stroke_cap()](http://py5.ixora.io/reference/sketch_stroke_cap.html) and [stroke_join()](http://py5.ixora.io/reference/sketch_stroke_join.html)*

## background colors

There's a `background()` function to define the color of your background in a sketch. Try adding this as the final line of your sketch:

```{code-cell} ipython3
size(500,500)

# setting our stroke color and width!
stroke('#FFFFFF')
stroke_weight(3)

# red rectangles
fill('#FF0000')
rect(100,150, 200,300)
rect(10,15, 20,30)

# orange square
fill('#FF9900')
rect(50,100, 150,150)

# fill-less square
no_fill()
rect(250,100, 150,150)

#dark blue background
background('#004477')
```

If you run the sketch, you'll notice everything has disappeared. This is because py5 draws from the top down, following the lines of your code, so the background is now hiding all the previous lines! Move that line to the top of the window, just after `size()`.

```{code-cell} ipython3
size(500,500)

#dark blue background
background('#004477')

# setting our stroke color and width!
stroke('#FFFFFF')
stroke_weight(3)

# red rectangles
fill('#FF0000')
rect(100,150, 200,300)
rect(10,15, 20,30)

# orange square
fill('#FF9900')
rect(50,100, 150,150)

# fill-less square
no_fill()
rect(250,100, 150,150)
```

<img src="https://tabreturn.github.io/img/pitl01/colour-blue-background.png">

## other color modes

Since a hexadecimal code is equivalent to using the RGB system, you can use straight RGB values for the same effect. By default, these values can go up to 255. For example, `fill('#FF0000')` (where FF represents the highest number possible) is equivalent to `fill(255, 0, 0)`. To get these sorts of values or convert from one to the other, remember you can utilize the *color selector* in Thonny's py5 mode. Why would you want to use one over the other? Well, if you had a program that had to change color, it would be a lot easier to simply add to the red, green or blue color value than to calculate the differences between hex codes. 

If you wanted to use HSB (hue, saturation, brightness) instead, you can use a function called `color_mode()` in your sketch, before you start coloring things in. In the *color selector*, you will quickly discover that the *hue* can be anywhere from 0 to 360 (like the degrees of a circle), and *saturation* and *brightness* can be anywhere from 0 to 100. This mimics the HSB system in many drawing programs. Making this system work in your code is pretty straightforward. To use `color_mode()` you need the following arguments: 

`color_mode(TYPE, maximum value, maximum value, maximum value)`

... which in this case means ...

`color_mode(HSB, 360, 100, 100)`

In HSB mode, that bright red color we represented as `fill(255, 0, 0)` would instead be `fill(0, 100, 100)` or `fill(360, 100, 100)` - since the hue range is "circular" and loops back in on itself, either will work. That's a color at the red point of the hue range, with maximum brightness and saturation. Why would you want to use HSB? Think again about a program that might have to change its colors while it runs. If you could simply add to the number representing hue and cycle through the rainbow that way, it would be a lot easier than manually working out how to do that with RGB values!

*Reference pages: [color_mode()](http://py5.ixora.io/reference/sketch_color_mode.html)*

# drawing functions

Let's take a look at some of the different functions py5 offers for drawing shapes. Start a new sketch with *File > New*, save it with *File > Save*, and name it **drawing**. Here's some code to start you off and help set up our sketch window:

```{code-cell} ipython3
size(500, 500)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)
```

If you hit the green play button now, a dark blue sketch will open, thanks to our `size()` and `background()` functions. You'll also notice that we've removed the color fill from our shapes, set our stroke or outline color to white, and made it 3 pixels wide. The following code examples will all be going under this block of setup code. Feel free to experiment with them and go off book a little!

`point(x coordinate, y coordinate)` creates a point, or a single dot, at the position you specify with your arguments. The size of the point will be dependent on your `stroke_weight()`. 

```
point(100, 25)
point(200, 25)
point(150, 75)
```

<img src="https://tabreturn.github.io/img/pitl01/drawing-point.png">

`triangle(x, y, second x, second y, third x, third y)` is a bit of a mouthful while you're explaining its arguments - but it will draw a triangle on the screen, with the three points of the triangle represented by these three pairs of x and y coordinates. 

```
triangle(100,25, 200,25, 150,75)
```

<img src="https://tabreturn.github.io/img/pitl01/drawing-triangle.png">

It's a good time to mention that in order to make your code easier to understand, there's no reason you can't use line breaks and indenting creatively. For example, to make those three pairs of x,y coordinates clearer, you could instead write it out like this, and it still runs:

```
triangle(100,25, # First corner
         200,25, # Second corner
         150,75) # Third corner
```

`ellipse(x, y, width, height)` creates an ellipse at the specified coordinates, with the width and height you choose. Giving the same width and height will create a perfect circle.

```
ellipse(100,100, 100,50)
```

<img src="https://tabreturn.github.io/img/pitl01/drawing-ellipse.png">

 Note that the x, y position here is the center of the ellipse, not one of the edges. When we were drawing with the `rect()` function, earlier, that position was the top-left corner of the rectangle. You can change this behavior if you want - by default, py5 uses `ellipse_mode(CENTER)` and `rect_mode(CORNER)`. 
 
 *Reference pages: [rect_mode()](http://py5.ixora.io/reference/sketch_rect_mode.html) and [ellipse_mode()](http://py5.ixora.io/reference/sketch_ellipse_mode.html)*

 `quad(x,y, x,y, x,y, x,y)` is a four-cornered or quadrilaterial shape, with each of those corners defined by a pair of x,y coordinates. It gives you more control over its shape than a `rect()` does.

 ```
 quad(250,250, # Remember, you can
      350,300, # break it up
      380,400, # to understand
      260,380) # what's happening!
```
<img src="https://tabreturn.github.io/img/pitl01/drawing-quad.png">

# rainbow task

Using what you've learned above, it's time to complete a task. Start a new sketch with *File > New*, save it with *File > Save*, and name it **rainbow**. Here's some code to start you off:

```
size(600, 600)
background('#004477')
noStroke()
```

Using what you've learned so far, create this rainbow image in py5. 

<img src="https://tabreturn.github.io/img/pitl01/drawing-rainbow.png">

Here's a hint: you don't have to figure out how to make half-circles, or to make gaps in your shapes. Just cover shapes with other shapes, and it'll look the same!

# Variables

Variables in programming are basically just placeholder names for information. It's a lot like using letters in algebra - you can name a variable and store pretty much anything you like in it, whether that's numerical values, hex codes, mathematical formulas or something else entirely. If you're using the same values over and over in your code, or you need to have more control over changing a value as your program runs, variables are the way to go. 

 Start a new sketch with *File > New*, save it with *File > Save*, and name it **variables**. We're going to be printing some data to the Shell tab in Thonny again. Start with this code:

```
size(600, 400)
background('#004477')

print(width)
print(height)
```

 <img src="https://i.imgur.com/qJLIAqp.png">

 We set the width and height of the window to 600 and 400 pixels using `size()`, and py5 has built-in variables for the width and height of the window. By printing those variables, we were able to quickly see what they were set to (or what information was stored in them). 

 You don't have to use the system's built-in variables. Creating your own variable is called *declaring* it. Storing information in that variable is called *assigning*. You can declare and assign a variable at the same time:

 ```
 x = 1
print(x) # displays 1 in the Shell tab
```

You can name variables anything you like, with some exceptions. Some variables, like `width` and `height`, are already taken by py5, and clashing with them will cause problems. Variable names cannot start with a number, or contain a space, hyphen or special symbol.

```
playerlives = 3  # correct
playerLives = 3  # correct
player_lives = 3 # correct
5playerlives = 3 # incorrect
player lives = 3 # incorrect
player-lives = 3 # incorrect 
player&live$ = 3 # incorrect
```

You'll see many variables in other development environments using camelCase, where the first letter is lowercase and subsequent words are capitalized. py5 (and much of Python coding) prefers to use underscores to separate words in functions and variables. Whatever method you use, use it consistently to avoid confusion. 

After you declare and assign variables, you can go ahead and use them as arguments for functions. Try adding three more variables, and using them to draw a `rect()`:

```
x = 1
print(x) # displays 1 in the console
y = 30
w = 20
h = w
rect(x,y, w,h)
```

<img src="https://i.imgur.com/mL2Ozc6.png">

We created a variable, *h*, and in the same line gave it the value we already assigned to *w* - so the width and height are the same, and we've drawn a square. Because we're using variables, if you wanted to change any of those arguments in your `rect()`, you could just change them in your variable assignments. This becomes really important when you re-use the same variables throughout your code! 

## doing maths with your variables

Variables that store a number can do all the things numbers do - like add, subtract, multiply and divide. Multiplication uses an asterisk (*), and division uses a forward slash (/). Try adding these lines to your code:

```
print(x + 2)       # displays 3
print(x - 2)       # displays -1
print(x * 5)       # displays 5
print(4 / 2)       # displays 2
```

What will this next code spit out?

```
print(1 + 2 * 3)   # displays ???
```

It displays a 7 (and not a 9, as you would expect, if you simply did each operation in order) because py5 follows the [order of operations](https://en.wikipedia.org/wiki/Order_of_operations) you may vaguely recall from previous schooling. Whether you call it BEDMAS, PEMDAS, or BODMAS, it works here, too. Since brackets/parenthesis are always checked first, if you need your maths to go a little differently you can cheat the system by adding some:

```
print(1 + 2 * 3)   # displays 7
print((1 + 2) * 3) # displays 9
```

These are all whole numbers, which in the world of programming are usually called *integers*. You'll also find references to *floating-point numbers* or *floats*, which are just numbers with a decimal point (like 1.5). In fact, Python used to always return an integer from dividing other integers, rounding down to the nearest whole number. You can see this old behavior by adding a second slash to your division:

```
print(3 / 2)   # prints 1.5
print(3 // 2)  # prints 1
```

And, of course, don't try to divide by zero... you'll get a special error for that. 

```
py5 encountered an error in your code:
    1    
    2    background('#004477')
    3    
--> 4    print(3 / 0)   

ZeroDivisionError: division by zero
```

## modulo

You may not have encountered the modulo operator before, but it's very useful in this course and deserves its own introduction. Modulo (represented by the percentage sign, %) calculates the *remainder* of a division operation. For example, 2 / 5 is 2.5 - but if we're just talking about how many times 5 can be divided into whole numbers, that's 2, and you will have a leftover (remainder) of 1 that can't be evenly divided among two people. Modulo is a shortcut to figuring out that remainder.

```
print(5.0 / 2)     # displays 2.5
print(5.0 % 2)     # displays 1
```

One way modulo can be useful is quickly determining if any number is odd or even, without having to have human eyes on it:

```
print(7 % 2)       # displays 1, therefore 7 is odd
print(6 % 2)       # displays 0, therefore 6 is even
```

If a modulo operation results in 0, you can know that something has been divided up perfectly. This will become very useful when you begin trying to draw things in rows and columns - using modulo will let you write instructions for py5 that can trigger every *x* steps, no matter what *x* is, since any multiple of a number will have the same modulo result as that number. 

# Image reveal task

Here's another challenge. Start a new sketch with *File > New*, save it with *File > Save*, and name it **symbol_reveal**. Let's give you a series of instructions and see if you can use them to draw a particular symbol. What is the symbol? You won't know until you try it out... Here's some code to start you off:

```
size(600, 740)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

xco = 400
yco = 440
```

You'll be given six steps, and following them will reveal the correct shape. To make things a little easier, the first step will also give you the code to use. You'll have to figure out the next five yourself!

1. Draw a line beginning at an x-coordinate of half the display window width, and y-coordinate of a third of the window height. The endpoint must have an x/y-coordinate equal to xco & yco.

```
line(width/2,height/3, xco,yco)
```

<img src="https://tabreturn.github.io/img/pitl01/arithmetic-operators-symbol-reveal.png">

*(See how that worked? To get half of width, you just use width/2, and so on. Break each instruction down into pieces and you'll figure it out quickly.)*

2. Draw a centred ellipse with a width that's an eleventh of the display window width, and a height that's a fourteenth of the window height. 

3. Draw a centred ellipse with a width that's a nineteenth of the display window width, and a height that's a twenty-second of the window height. 

4. Draw a line beginning at an x/y-coordinate equal to xco & yco respectively. The endpoint must have an x-coordinate of the display window width minus xco, and a y-coordinate equal to yco. 

5. Draw a line beginning at an x-coordinate of the display window width minus xco, and y-coordinate equal to yco. The endpoint must have an x-coordinate of half the display window width, and a y-coordinate of a third of the window height. 

6. Draw a centred ellipse with a width that's a fifth of the display window width, and height that's a twelfth of the display window height. 

*(A clue: if this seems like a conspiracy, you're on the right track.)*

# Disk space analyser task

This is the final challenge for this week. You'll be handing it in on Stream as your homework. Before we get to the task at hand, let's introduce the `arc()` function. This is used to draw elliptical arcs - and it's best to try it out to understand how it works. Start a new sketch with *File > New*, save it with *File > Save*, and name it **disk_space_analyser**. Here's your setup code:

```
size(600,700)
background('#004477')
stroke('#FFFFFF')
stroke_weight(3)
no_fill()
```

Breaking the `arc()` down across multiple lines will make it a little easier to examine its parts. Here are its required arguments. 

```
arc(
  x_coordinate, y_coordinate,
  width, height,
  start_angle, end_angle
)
```

If you take a look at the [py5 cheatsheet](https://raw.githubusercontent.com/tabreturn/processing.py-cheat-sheet/master/py5/py5_cc.pdf) (also accessible in the *py5* menu in Thonny), you'll see arcs on the lower right here. We use *radians* to measure where an arc ends and begins. Add an arc with a starting angle of zero radians and an ending angle of two radians:

```
arc(width/2,height/2, 200,200, 0,2)
```

<img src="https://tabreturn.github.io/img/pitl01/arithmetic-arc.png">

We started at zero radians, and our arc is being drawn clockwise. You may notice 2 radians is... well, a little more than a quarter of a way around the circle, which can feel quite unhelpful. Rather than trying to strictly remember exactly how much a single radian is, it can be better to remember that halfway around a circle is *pi* radians - that funny number starting with 3.1415. This animated diagram from Wikipedia is also helpful:

<img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Circle_radians.gif">

*Lucas V. Barbosa [Public domain], from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Circle_radians.gif)*

py5 actually has a built-in understanding of how much *pi* is. Anywhere you want to use pi, type `PI`. You can of course use this in mathematical operations too - a complete circle is PI*2 radians.

```
arc(width/2,height/2, 200,200, 0,2)
arc(width/2,height/2, 300,300, 0,PI)   # half-circle
arc(width/2,height/2, 400,400, 0,PI*2) # full-circle
```
<img src="https://tabreturn.github.io/img/pitl01/arithmetic-arcs.png">

Using variables, of course, means that if you wanted a variable to represent the radius of a complete circle, you could easily declare and assign one like this:

```
radius = PI * 2
```

...and instead of worrying about radians, you could just know `radius / 4` will always be a fourth of a circle, and so on. 

Many functions have optional arguments. In the case of `arc()`, there is a final MODE variable that can change the way the arc appears. If you want to close off the arc, so it looks like a slice of pie, you add one last argument called... PIE. 

```
arc(width/2,height/2, 200,200, 0,2)
arc(width/2,height/2, 300,300, 0,PI)   # half-circle
arc(width/2,height/2, 400,400, 0,PI*2) # full-circle
arc(width/2,height/2, 350,350, 3.4,(PI*2)-(PI/2), PIE)
```

<img src="https://tabreturn.github.io/img/pitl01/arithmetic-arc-pie.png">

This brings us to the weekly task. You may have seen *disk usage analysers* that break up the data on a hard drive into a funny pie charts or ring charts. One example is the Linux [GNOME Disk Usage Analyzer](https://en.wikipedia.org/wiki/Disk_Usage_Analyzer). Using what you know about arcs and drawing shapes in general, you'll be trying to recreate the image below:

<img src="https://tabreturn.github.io/img/pitl01/arithmetic-disk-space-analyser.png">

As with the rainbow task, remember that you can cover shapes with other shapes to create that ring shape, and don't worry about adding the text or even perfectly matching the colors.
