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

# Control Flow and Randomness

By default, code written in py5 is just executed line by line, starting with the very top of the sketch and ending at the bottom. This linear arrangement of code is perfectly acceptable for simple programs, but as your sketches begin to get more complex, you'll often find that laying out divergent paths and loops of behaviors is necessary. Laying out the rules and conditions for the computer to follow these different paths is called *control flow*. 

<img src="https://tabreturn.github.io/img/pitl03/intro-flowchart.svg">

Imagine that you wanted to fill the sketch window with circles. 

<img src="https://tabreturn.github.io/img/pitl03/intro-circles.svg">

Of course, to draw nine of these circles, you could simply manually write nine `ellipse()` functions, one after the other, telling the computer exactly where to place each one. However, if you wanted to draw eighty-one circles instead, this task becomes tedious and unproductive to perform manually. Using control flow, we can give py5 exactly the instructions and rules that it needs to place each circle for us, with a minimal amount of work on our end. In fact, it's easy enough to create more *dynamic* code that can be adapted to many different use cases - something that we can modify to account for any number of circles, or different sizes of circles, and let py5 do the hard stuff all by itself. 

In this lesson we will be discussing how to write these sorts of conditional statements to lead our code down different paths, and how to loop through tasks, running code repeatedly. Since we're discussing this code as dynamic and extensible, it's also useful to learn about randomness and how to utilize it, a powerful and exciting tool for the creative programmer. 

## conditional statements

A *conditional statement* is really just a fancy way of saying that if a condition is true, the program will do something. If you were communicating with a human, it would be helpful to think of this as a question-and-answer approach, where the answer will lead to some sort of action. If you had blocks of several different colors and several different boxes to put them in, the conditional statement might look like this: 

*A human is shown a colored block.*

*Question*: Is the block red?

*Answer*: Yes.

*Action*: Place it in the box labelled "red blocks".

The way the computerized brain works is similar, but simple conditional statements don't separate these three steps in the same way the human brain does. It's a little more like this: 

*A computer is shown a colored block.*

*Condition*: IF the block is red...

*Action*: ...place it in the box labeled "red blocks."

The question is, how do you communicate these sorts of concepts to the computer? Let's break down ways it can evaluate and store this sort of data.

## boolean data types

There are many simple types of data in py5 (and other programming languages). A single character of text is a *character*, many characters of text form a *string*, a whole number is an *integer*, and a number with a decimal point is a *float*. For comparing conditions to a target like this (*is the block red*), computers use a data type called a *boolean*. 

Strings can hold pretty much any text, and integers/floats pretty much any number. Booleans only have two possible states: `True` or `False`. Let's write some simple code together to demonstrate how this works.

```{code-cell} ipython3
# Setting up our size and background color, as always
size(600,400)
background('#004477')

# Declaring and assigning two variables...
block_is_red = True
block_is_blue = False

# What happens when you print these? 
print(block_is_red)
print(block_is_blue)
```

As you might expect, running the above code will print:

```
True
False
```

The capitalization here is important! true, TRUE, and tRuE will all be assumed to be strings, or variables that haven't been assigned properly. If you did need a string that stored the text "True" in it, you would include those quotation marks when you assign the variable - but this is likely to get confusing quickly.

## relational operators

In isolation, variables like this are not always useful. However, when you begin to compare the relationship variables have to each other, the decision-making capabilities of your programs become more powerful. As an example, consider this basic mathematical statement:

```
3 > 2
```

The integers 3 and 2 (our *operands*) are being compared by the greater-than sign (our *operator*). Reading this line, you can immediately tell that it's correct: 3 is larger than 2. To put it in the terms of a computer, 3 > 2 is *True*. You can ask py5 to use relational operators and give you the result of that operation.

```{code-cell} ipython3
# Setting up our size and background color, as always
size(600,400)
background('#004477')

# Declaring and assigning a variable...
x = 2

print( x > 1 )        # displays: True
print( x < 1 )        # displays: False
```

Just like our first code, running this will print:

```
True
False
```

Our py5 sketch has received these lines and returned a boolean - true or false - based on whether the comparison is correct. When we start to get into more complex comparisons, this is still the case. When we ask the computer a question to determine its control flow, it evaluates whatever we give it, decides if the answer is `True` or `False`, and moves onwards from there. 

There are a handful of different relational operators we can use in py5 (and Python in general):

```
>    greater-than
<    less-than
>=   greater-than-or-equal-to
<=   less-than-or-equal-to
==   equal-to
!=   not-equal-to
```

As you can imagine, checking if a variable is greater than or less than something else will only work on numbers, whether they're floats and integers. However, you can use `==` and `!=` on other variables, too, to quickly check for a match.

```{code-cell} ipython3
# Setting up our size and background color, as always
size(600,400)
background('#004477')

# Declaring and assigning a variable with a string in it...
name = 'Jo'

# Checking if that name is equal to various strings of text...
print( name == 'Jo' ) # displays: True
print( name == 'Em' ) # displays: False
print( name != 'Em' ) # displays: True
```

We've uncovered only part of the puzzle: evaluating statements and figuring out if they're `True` or `False`. The missing piece is instructing our program to take action based on this result.

## if statements

Think back on our colored block example, above.

*A computer is shown a colored block.*

*Condition*: IF the block is red...

*Action*: ...place it in the box labeled "red blocks."

We'll be writing our first simple *if statement* here, to give our program a way to logically decide on its next step. Let's imagine that we were writing a simple program to grade submissions in a university course. We'll do the hard part ourselves - marking the submission with a number out of 100. How can we ask the computer to provide us with a proper grade using that mark?

```{code-cell} ipython3
size(600,400)
background('#004477')

mark = 60

# If the mark is greater than or equal to fifty, it's a pass!
if mark >= 50:
    print('PASS')
```

This is almost exactly the same as our colored block example, but in the Python syntax!

*A computer is shown a mark.*

*Condition*: IF the mark is greater than, or equal to, 50...

*Action*: ...print the word PASS.

The indenting before the `print()` line is necessary. When we begin the if statement, py5 will look for indented lines following it as the action to take. It doesn't matter how far you indent this code - four spaces or two spaces are common, but it can be a single space or a dozen if you really want - as long as you are consistent and use the same indentation throughout. This means that you can have multiple lines included in the if statement, as long as they are all indented equally.

```{code-cell} ipython3
size(600,400)
background('#004477')

mark = 60

# If the mark is greater than or equal to fifty, it's a pass!
if mark >= 50:
    print('PASS')
    print('Well done!')
```

If you unindented that second `print()` line, the program would print "Well done!" regardless of the grade. Awkward, but optimistic. 

These if statements can be *nested* inside one another, like Russian nesting dolls. You have to be careful about the indentation, but this can be a powerful - if occasionally inefficient - way to have multiple branching paths in your code. For example, what if you needed to support both an English and Spanish language option in this marking program?

```{code-cell} ipython3
size(600,400)
background('#004477')

mark = 60

if mark >= 50:
    print('PASS')

    if language == 'EN':
        print('Well done!')

    if language == 'ES':
        print('Bien Hecho!')
```

As we know, booleans can only be `True` or `False`. This means that when you're just checking a boolean, you don't even have to compare it to anything. It's not more "correct" to use one or the other - leaving out the operator is efficient, but leaving it in is easy to read. You can also use a variation here, *if not*, to check if something is False without using a operator.

```{code-cell} ipython3
size(600,400)
background('#004477')

block_is_green = True
block_is_red = False

if block_is_green == True:
    print('The block is green')

# is the same as:

if block_is_green:
    print('The block is green')
    
if block_is_red == False:
    print('The block is NOT red')
    
# is the same as:

if not block_is_red:
    print('The block is NOT red')
```

Let's return to our assignment marking program. Currently, it will only tell you if your mark was a pass. If we instead want it to output letter grades, we'll need multiple if statements.

```{code-cell} ipython3
size(600,400)
background('#004477')

mark = 70

if mark >= 50:
    print('C')

if mark >= 65:
    print('B')
```

Does that code work? Yes, but with an unintended problem: if you changed your mark to 70, both of those if statements are true, and so the program returns both B and C. Luckily, with flow control, there's a way around this. In addition to regular *if* statements, we can use *else* statements and *else if* statements. Imagine if our computer had to sort quite a few colors of blocks:

*A computer is shown a colored block.*

*Condition*: IF the block is red...

*Action*: ...place it in the box labeled "red blocks."

*But what if the block was NOT red?*

*Condition*: ELSE, IF the block is green...

*Action*: ...place it in the box labeled "green blocks."

*What if you only taught the computer about red and green, but there were a handful of other colors?

*Condition*: ELSE...

*Action*: ...place the block in the box labeled "other colors."

Using Python syntax, *else if* becomes *elif*. This statement will only be evaluated if the preceding statement was false. For our structure to make sense, it's a good idea to start at higher marks, and contain lower marks in an elif statement. That way, the code will continue trying to run through these marks, only moving to the next statement if the current one fails.

```{code-cell} ipython3
size(600,400)
background('#004477')

mark = 70

if mark >= 80:
    print('A')

# The previous statement wasn't true, so let's move on...
elif mark >= 65:
    print('B')

# And so on, and so forth
elif mark >= 50:
    print('C')

# Actually, none of the previous statements were true!
else:
    print('FAIL')
```

Note that although this is a chain of IF, ELIF and ELSE statements, you don't necessarily need to use all three. Just combining IF and ELIF statements, or an IF statement and an ELSE statement, are completely valid ways to use control flow. It all depends on what you want your program to do. 

## logical operators

So far, each of our if/elif statements have only been evaluating one thing at a time. *Is the mark greater than 50?* For more complex logic, or even to streamline the statements we've already written, you might need to ask something like *is the mark greater than 50, AND less than 65?* For this, we can use logical operators. Actually, you've already taken a sneak peek at one of them, *not*, which checks for the opposite of something. There are three of these logical operators available to us in Python: 

```
and   returns True if both (or all) operands are true
or    returns True if at least one operand is true
not   reverses the boolean (True becomes False and vice-versa)
```

Let's incorporate *and* and *or* into our marking program to handle a few other cases. For example, if I incorrectly put in a mark as 152 or -52, it's better for the program to reject it than to mark it as an A or a FAIL. Plus, maybe if someone is in a certain range below a C, there's still a chance to retrieve their grade and ask them to resubmit. Changing the mark below, you can see the different results. That *or* operator means either condition being true will run the code, and that *and* means both must be true for the code to run.

```{code-cell} ipython3
size(600,400)
background('#004477')

mark = 152

if mark < 0 or mark > 100:
    print('INVALID MARK')

elif mark >= 80:
    print('A')

elif mark >= 65:
    print('B')

elif mark >= 50:
    print('C')

elif mark >= 45 and mark < 50:
    print('RESUBMIT')

else:
    print('FAIL')
```

## four-square task

It's time for a challenge. This marking program is completely non-visual, which is just not in the spirit of py5. Instead, your task is to create a simple program, using the statements and logical operators we've just discussed, that includes a bit of visual output. 

Let's start off with this code (and you will quickly understand the name of the task):

```{code-cell} ipython3
size(600,600)
no_fill()
no_stroke()

fill('#FF0000') # red quadrant
rect(width/2,0, width/2,height/2)

fill('#004477') # blue quadrant
rect(0,0, width/2,height/2)

fill('#6633FF') # violet quadrant
rect(0,height/2, width/2,height/2)

fill('#FF9900') # orange quadrant
rect(width/2,height/2, width/2,height/2)
```

<img src="https://tabreturn.github.io/img/pitl03/four-square-quadrants.png">

When run, this code will divide your sketch window into four colored quadrants. You can see we're using the built-in variables of *width* and *height* to easily make sure those quadrants are in the right place, and that they take up exactly one quarter of the window. (This means that your `size()` can be anything, of course.) Now, we'll create two variables for the x and y coordinate of a single character, and place the character at that location.

```{code-cell} ipython3
size(600,600)
no_fill()
no_stroke()

fill('#FF0000') # red quadrant
rect(width/2,0, width/2,height/2)

fill('#004477') # blue quadrant
rect(0,0, width/2,height/2)

fill('#6633FF') # violet quadrant
rect(0,height/2, width/2,height/2)

fill('#FF9900') # orange quadrant
rect(width/2,height/2, width/2,height/2)

x = 400
y = 100
txt = '?'

fill('#FFFFFF')
text_size(40)
text_align(CENTER, CENTER)
text(txt, x,y)
```

<img src="https://tabreturn.github.io/img/pitl03/four-square-qmark.png">

Your challenge is to write code that, depending on which quadrant the ? appears in, transforms it into a different character entirely: B for blue, R for red, P for purple or O for orange. If you can change x and y to any values and this works consistently, you've done well.

<img src="https://tabreturn.github.io/img/pitl03/four-square-four-up.png">

We'll run through the condition for red (R) together so that you can understand the principle. First, let's add a statement that checks if the character is on the right side of the screen. Of course, we can do this by checking the value of x and change the character accordingly.

```{code-cell} ipython3
size(600,600)
no_fill()
no_stroke()

fill('#FF0000') # red quadrant
rect(width/2,0, width/2,height/2)

fill('#004477') # blue quadrant
rect(0,0, width/2,height/2)

fill('#6633FF') # violet quadrant
rect(0,height/2, width/2,height/2)

fill('#FF9900') # orange quadrant
rect(width/2,height/2, width/2,height/2)

x = 400
y = 100
txt = '?'

if x >= width/2:
    txt = 'R'

fill('#FFFFFF')
text_size(40)
text_align(CENTER, CENTER)
text(txt, x,y)
```

This works because it checks our x value against `width/2`, the center point of the image's width. However, if you change the value of Y to 400, you'll have an R over the orange quadrant of the image. This is because we're only checking our X value, not our Y! Using a logical operator, you can check the values of X and Y simultaneously for a correct result.

```{code-cell} ipython3
size(600,600)
no_fill()
no_stroke()

fill('#FF0000') # red quadrant
rect(width/2,0, width/2,height/2)

fill('#004477') # blue quadrant
rect(0,0, width/2,height/2)

fill('#6633FF') # violet quadrant
rect(0,height/2, width/2,height/2)

fill('#FF9900') # orange quadrant
rect(width/2,height/2, width/2,height/2)

x = 400
y = 100
txt = '?'

if x >= width/2 and y < height/2:
    txt = 'R'

fill('#FFFFFF')
text_size(40)
text_align(CENTER, CENTER)
text(txt, x,y)
```

With that simple fix, our ? will change into an R only if it is in the top-right corner of the sketch window, and remain a ? in the other three corners. Now, write three more if statements to handle what happens in the other three corners. 

If you blaze through that, here's another question: how would you write a final if statement that checks to see if the character is off the edges of the screen, and places it at a position of `100, 100` if that's the case?

## iteration

If you were trying to tile a floor, it would make sense to start at one corner, placing a single tile. Then, you could move along the wall towards another corner, placing tiles as you go, until you reach the opposite wall. At that point, you would move along a row and place tiles on your way back. In this scenario, the placing of an individual tile is referred to as one *iteration* of the process. In many iterative processes, the result of a previous iteration defines the starting point of another – in this case, the position of each tile is advanced by the one laid before it.

Many iterative processes like this are a tedious task to the human mind, and boredom or inattention can lead to them being done imperfectly. Of course, these are exactly the sorts of tasks computers excel at.

As a fun aside, the term *computer* didn't refer to a machine when it was first used. Actually, a computer was the human being (usually a woman) who sat down and performed huge amounts of calculations by hand. Here's a photo of the High Speed Flight Station *computer room* (from 1949) at the National Advisory Committee for Aeronautics: 

<img src="https://upload.wikimedia.org/wikipedia/commons/0/06/Human_computers_-_Dryden.jpg">

*Human computers in the NACA High Speed Flight Station "Computer Room", Dryden Flight Research Center Facilities. Public domain, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Human_computers_-_Dryden.jpg)*

These human computers would usually spend their time calculating and putting together mathematical tables called logarithm tables. These are a lot like the multiplication tables many people memorize in school - they were your cheat sheet for looking up common calculations you may have been making frequently in your work. 

<img src="https://tabreturn.github.io/img/pitl03/wikimedia-backup/lossless-page1-789px-APN2002_Table_1%2C_1000-1500.agr.tiff.png">

*A logarithms table from American Practical Navigator. Nathaniel Bowditch, originally; National Imagery and Mapping Agency, U.S. Government. Public domain, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:APN2002_Table_1,_1000-1500.agr.tiff)*

Computing more efficiently (and without necessarily requiring the aid of humans) has been a problem itching to be solved for quite a long time. The very first iteration of the modern computer, the *Difference Machine*, was prototyped in the 1820s by Charles Babbage to automate the work of human computers. We've come a long way since then, and now many iteration tasks can be performed mechanically - including in Python. Let's begin exploring how we can automate tasks in py5.

```{code-cell} ipython3
size(500,500)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

# concentric circles
ellipse(width/2,height/2, 30,30)
ellipse(width/2,height/2, 60,60)
ellipse(width/2,height/2, 90,90)
```

<img src="https://tabreturn.github.io/img/pitl03/iteration-manual.png">

As you can imagine, we're thinking of filling the screen with these concentric circles here. Of course, you could simply do this all by hand, drawing an `ellipse()` each time with an expanding width and height. This would be pretty inefficient, so let's go over some ways we can get py5 to do it for us. 

## while loops

The *while* statement looks quite a lot like the if statement, which we explored earlier. The if statement executes code once, if the statement given is true. The while statement, on the other hand, executes its code as many times as necessarily *while* the statement is true. Let's write an example (and while we're here, I'll comment out our three ellipse functions; we won't be needing to draw them like that!)

```{code-cell} ipython3
size(500,500)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

# concentric circles
# ellipse(width/2,height/2, 30,30)
# ellipse(width/2,height/2, 60,60)
# ellipse(width/2,height/2, 90,90)

i = 0

while i < 24:
    print(i)
```

As you might imagine, running this code will fill your console area with printed zeroes... forever. That's because we've told this *while* loop to execute its code until our new integer *i* reaches a certain number - but we haven't done anything to actually increase *i*, so it will run forever. Try this instead:

```{code-cell} ipython3
size(500,500)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

# concentric circles
# ellipse(width/2,height/2, 30,30)
# ellipse(width/2,height/2, 60,60)
# ellipse(width/2,height/2, 90,90)

i = 0

while i < 24:
    print(i)
    i = i + 1
```

What's the difference? Well, each time the loop runs, it is telling you what number is assigned to i, and then *increasing i*, the missing step from before. Your console will print numbers one after the other, starting at 0 and reaching 23. At that point, increasing i means it is no longer less than 24, so the loop will not run again. Of course, i can be named anything, but these integers we create only for while loops are often just named i. Sometimes, you'll be using existing variables for your while loops instead, but for simple counters like this, it's sufficient to just create a new one. 

As an aside, that line `i = i + 1` can be written a few different ways and do the same thing. For example, `i += 1` is a common way to do the same thing, and in other coding languages (but not in Python) you might also see even shorter statements like `i++`. Other shorthand operators work similarly:

```
i -= 1 is equivalent to  i = i - 1
i *= 1 is equivalent to  i = i * 1
i /= 1 is equivalent to  i = i / 1
```

So how can we use all this to draw some circles? We can start by incorporating an `ellipse()` function, very similar to our first one, inside of our loop.

```{code-cell} ipython3
size(500,500)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

# concentric circles
# ellipse(width/2,height/2, 30,30)
# ellipse(width/2,height/2, 60,60)
# ellipse(width/2,height/2, 90,90)

i = 0

while i < 24:
    print(i)
    ellipse(width/2,height/2, 30,30)
    i = i + 1
```

<img src="https://tabreturn.github.io/img/pitl03/iteration-stacked-circles.png">

Your console will still print the numbers 0 to 23, so you can tell the loop is running. However, only a single circle will appear on the screen. Actually, this is 24 circles - but they're being drawn in exactly the same place, and their width and height are identical. To easily increase the size of our circle along with *i*, you can simply multiply the height and width of the circle by *i* each time. To make this a little easier to read and adjust, let's also store the size of our circle in a variable.

```{code-cell} ipython3
size(500,500)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

circle_size = 30
i = 0

while i < 24:
    print(i)
    ellipse(width/2,height/2, circle_size * i, circle_size * i)
    i = i + 1
```

<img src="https://tabreturn.github.io/img/pitl03/iteration-concentric-circles.png">

Because circle_size is now a variable, changing that 30 to a different number can give you more tightly clumped or spread out concentric circles. Notice that because this size is multiplied by i each time, and i starts at zero, we're actually only printing 23 visible circles - the very first circle is given a height and width of zero, so it's impossible to see. Of course, you could start i at 1 instead of at 0, or do some other trickery like `circle_size * (i + 1)` to get around this, but for the moment it's more than enough to just see it working.

## rows of circles task

Let's put our new knowledge of while loops to the test. You'll be recreating this image:

<img src="https://tabreturn.github.io/img/pitl03/rows-of-circles.png">

This code will start you off, placing a single `ellipse()` in the top left.

```{code-cell} ipython3
size(500,500)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)
ellipse(100,100, 80,80)
```

As with our concentric circles, your success will hinge on wrapping your `ellipse()` functions in a while loop. You need to draw 16 circles in total. There are a few possible approaches, and discussing them both in slightly more detail is worth doing.

One way to manage rows and columns would be to have variables for them, maybe named something like `row` and `column` (just to be explicit and un-creative). 

You could run your while loop sixteen times, drawing sixteen circles, and using `row` and `column` to determine their positions. 

Your `column` variable would increase each time a circle was drawn, and then when you'd drawn four circles, you would reset `column` and increase `row` by one instead. 

A good way to do this is using the modulo operator - this gives you the remainder of a division operation. 

For an *i* number of 4, 8, 12 and 16 (the numbers of the circles on the 'far right', or the final column), `i % 4 == 0` will be `True`.

This method is good to know, and it's worth trying before you continue. However, there's another, slightly easier way. In addition to *while* loops, you have access to something called a *for* loop. These are very similar, but the *for* loop is well suited to being nested (exactly like an if statement) with powerful results!

Above, we used the line `while i < 24:` to start off our while loop. The for loop would instead use `for i in range(24):` for the same results. One difference is that you don't have to declare i before using it - the for loop understands implicitly that it's created a new variable as its counter. And, unlike a while loop, you never have to manually increase i (or any other counter variable) - the for loop does this automatically. 

Combining this, an elegant way to draw your sixteen circles follows. 

```{code-cell} ipython3
size(500,500)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)
ellipse(100,100, 80,80)

# This whole for loop will run once for each column. 
for column in range(4):
    # This NESTED for loop will run once for each row INSIDE each column! 
    # So it will run four times... four times.
    for row in range(4):
        ellipse( (column + 1) * 100, (row + 1) * 100, 80, 80)
        # We don't have to increase column or row at all... it just works.
    
```

In the same way, our previous code for our concentric circles could be written like this:

```{code-cell} ipython3
size(500,500)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

circle_size = 30

for i in range(24):
    print(i)
    ellipse(width/2,height/2, circle_size * i, circle_size *i)
```

We've used `range()` above with just one argument, which is our "stopping point", equivalent to `while i > 24`. There are some optional arguments you can use, too. For example, providing `range()` with two arguments can define a stopping point and a starting point. For example, running this concentric circle code with `range(8,12)` instead will give this output: 

<img src="https://tabreturn.github.io/img/pitl03/iteration-for-loop-2-args.png">

You can even iterate through a range, but only take action every *x* steps, where *x* is your third argument. `range(0,12,3)` draws a circle at 0, 3, 6, and 9. 

## for loops task

For this task, you'll be recreating the following image:

<img src="https://tabreturn.github.io/img/pitl03/iteration-for-loops-task.png">

It may be a good idea to [save a copy](https://tabreturn.github.io/img/pitl03/iteration-for-loops-task.png) or keep it open to reference while you work on these tasks.

The pale blue lines at each point of this image are each the first step in a for loop, with their initial coordinates given. Placing the other white lines within a for loop will be your challenge! 

This code can start you off. The initial `line()` in each area of the screen has been commented out, but you can use it to begin your for loops.

```{code-cell} ipython3
size(600,600)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

# Top left
# line(75, 138, 228, 88)

# Top right
# line(370, 80, 522, 80)

# Bottom center
# line(225, 370, 300, 370)
```

For the top left pattern, the loop will be straightforward. You'll need to draw twelve lines in all.

For the top right pattern, it's useful to know that the spacing between the lines increases by 1.5 times each iteration.

For the bottom pattern, it may be helpful to remember that the result of `i % 2` can always determine whether i is odd or even. 

## randomness

The fact is, computers aren't great at behaving truly randomly. If you ask a computer to come up with a random number, it will inevitably end up doing some (non-random) calculations to give you a result, since all computers run on a series of instructions, no matter how complex. There have been many novel approaches to find a source of randomness in the world that can be fed into a computer - one fantastic solution was [Lavarand](https://en.wikipedia.org/wiki/Lavarand), a wall of lava lamps which were photographed and the results transformed into a series of numbers. This system is currently used by Cloudflare to assist in handling internet traffic.

<img src="https://upload.wikimedia.org/wikipedia/commons/b/bb/Lava_lamp_wall_at_Cloudflare_office_-2.jpg">

*A wall of lava lamps in the entrance area of the Cloudflare offices at 101 Townsend Street in San Francisco. Creative commons, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Lava_lamp_wall_at_Cloudflare_office_-2.jpg)*

Most programs (especially ones that don't need to rely on randomness for security reasons, like gambling or storing passwords) can get away with *pseudorandomness*. Essentially, a large enough series of numbers (possibly with modifications thrown in based on things like the current computer's time) will appear random to the human eye, and that's good enough. In addition, there are different types of randomness. Ken Perlin, in 1983, designed an algorithm for pseudorandomness that is usually called *Perlin noise*. If you compare true (pseudo)randomness and Perlin randomness in the image below, you can see it is especially suited to randomly generating smooth, somewhat organic sequences.

<img src="https://tabreturn.github.io/img/pitl03/random-random-v-noise.png">

This image was generated by picking random numbers with either algorithm (true pseudorandomness, or Perlin randomness) over time, and using it as the next point on a line. There are py5 functions for generating different types of noise (and even plugins which mimic the Perlin noise algorithm), but we'll be concentrating on two functions related to regular randomness: `random()` and `random_seed()`. 

`random()` can be used with a single argument - an upper bound - to get a number below that upper bound. You can also use it with two arguments, to get a number between the two. 

```{code-cell} ipython3
size(600,600)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

x = random(5)
print(x)
x = random(5,10)
print(x)
print( int(x) )
```

You'll quickly notice that the first two numbers are long decimal numbers rather than a whole number (a *float*, not an *integer*). If you'd like to instead get a whole number, you can use the `int()` function, seen above, to round it down. You'll also notice that - thanks to it being random - you get different results from repeatedly running the exact same sketch. 

Let's combine randomness with our previous understanding of for loops to draw a hundred random dots on the screen.

```{code-cell} ipython3
size(600,600)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

for i in range(100):
    point( random(width), height/2 )
```

<img src="https://tabreturn.github.io/img/pitl03/random-points-1d.png">

Broken down farther, in this range of 100 points, we're placing each one at the center of the screen vertically (`height/2`), and at a random point on the X-axis, between zero and `width`. This means they will never be placed off the right or left side of the screen. 

Let's edit our sketch to place a thousand points instead, and place them anywhere on the screen.

```{code-cell} ipython3
size(600,600)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

for i in range(1000):
    point( random(width), random(height) )
```

If you ran this code a hundred times, each result would look slightly different. However, this isn't always the result you want. If you've played any video game that uses randomized or procedurally generated elements, you may have heard of a *seed*. Essentially, the *seed* is a value that the game uses in its random calculations. In games that allow you to generate new worlds using a seed, you and your friend on another continent can put in the exact same seed and play through the exact same world, because all of these calculations have used their same starting value. 

In py5, you can use a function, `random_seed()`, to set this value manually. If `random_seed()` stays the same, running the sketch a hundred times will give the exact same results! 

```{code-cell} ipython3
size(600,600)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

random_seed(289212)

for i in range(1000):
    point( random(width), random(height) )
```

Run this sketch a few times. If you aren't certain, you can concentrate on a single corner to confirm the results. No matter how many times you run it, the placement of the points will be the same. 

## Truchet tiles

Sébastien Truchet (1657–1729), a French Dominican priest, was active in the fields of mathematics, hydraulics, graphics and typography. One of his contributions was a scheme for creating interesting patterns using tiles – which have since become known as Truchet tiles. The original Truchet tile is square, with two halves of color, divided diagonally. By rotating this tile, you can create four different variations.

<img src="https://tabreturn.github.io/img/pitl03/random-truchet-contrast-set.png">

Combining these tiles in different patterns (whether those patterns are carefully designed or completely random) has a variety of pleasing results:

<img src="https://tabreturn.github.io/img/pitl03/random-truchet-variants.png">

We'll be experimenting with a variation on the Truchet tile called the quarter-circle tile. This only has two possible rotations.

<img src="https://tabreturn.github.io/img/pitl03/random-truchet-quarter-circle-set.png">

To draw just a single quarter-circle Truchet tile, you would use the following code.

```{code-cell} ipython3
size(600,600)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

arc(0,0, 50,50, 0,PI/2)
arc(50,50, 50,50, PI,PI+PI/2)
```

Great - but just one truchet tile isn't going to cut it. Instead, let's try using one of those nifty nested for loops from before to fill the screen with these tiles.

```{code-cell} ipython3
size(600,600)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

for column in range(12):
    for row in range(12):
        arc(column * 50, row * 50, 50,50, 0,PI/2)
        arc(column * 50 +50, row * 50+50, 50,50, PI,PI+PI/2)
```

Great - but they're only being printed with one of our two possible rotations. Because there are only possibilities, we can essentially perform a coin flip each time a tile is placed. This means we need to use `random(2)` - and also wrap it in an `int()` function, since of course including the possibility for decimal numbers gives us way more than two options! Test out this coin flip by adding the appropriate `print()` command in your loop. The console will be filled with 1s and 0s, since our upper limit is 2 and our numbers are being rounded down each time.

```{code-cell} ipython3
size(600,600)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

for column in range(12):
    for row in range(12):
        print( int(random(2)) )
        arc(column * 50, row * 50, 50,50, 0,PI/2)
        arc(column * 50 +50, row * 50+50, 50,50, PI,PI+PI/2)
```

For the sake of streamlining our code, we can transform this into a True or False result by comparing the output to one of the two possible options. This change will fill the console with True and False output instead - a perfect coin flipper!

```{code-cell} ipython3
size(600,600)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

for column in range(12):
    for row in range(12):
        print( int(random(2)) == 1 )
        arc(column * 50, row * 50, 50,50, 0,PI/2)
        arc(column * 50 +50, row * 50+50, 50,50, PI,PI+PI/2)
```

All that's left is to figure out how to use this to rotate the tile. You won't have to do that manually - try including an if/else statement like this one.

```{code-cell} ipython3
size(600,600)
background('#004477')
no_fill()
stroke('#FFFFFF')
stroke_weight(3)

for column in range(12):
    for row in range(12):
        #print( int(random(2)) == 1 )
        if int(random(2)) == 1:
            arc(column * 50, row * 50, 50,50, 0,PI/2)
            arc(column * 50 + 50, row * 50+50, 50,50, PI,PI+PI/2)
        else:
            arc(column * 50 + 50, row * 50, 50,50, PI/2,PI)
            arc(column * 50, row * 50 + 50, 50,50, PI+PI/2,2*PI)
        
```

<img src="https://tabreturn.github.io/img/pitl03/random-truchet-quarter-circle-done.png">

Each time this code is run, you'll get a different randomized quarter-circle Truchet pattern.

It's important to mention at this point that your nested for loops can be even more efficient. You may notice a lot of the math above is offsetting the position of each tile by 50 pixels, so they don't all print on top of each other. This could be rewritten (with a small amount of effort) using three arguments in `range()` to define a starting point, ending point and how many steps between running our code, something like:

```
for column in range(0, width, 50):
    for row in range(0, height, 50):
```

Using this approach, complex grid shapes like tile placements can be easily scaled to any size of screen and any size of tile. 

## progressively-jittery quads task

This is the final challenge for this tutorial. It's an exercise adapted from Ira Greenberg’s *Processing: Creative Coding and Generative Art in Processing 2* (page 80), which teaches programming using Processing's Java mode (rather than the Python implementation we're using). You'll be recreating (using randomness, not manual labor) the following reference image:

<img src="https://tabreturn.github.io/img/pitl03/progressively-jittery-quads.png">

Let's place a small amount of code to start you off, and give you a few hints.

```{code-cell} ipython3
size(600,600)
background('#004477')
stroke('#FFFFFF')

# This variable will come in handy. Trust me.
jitter = 0

quad(50, 50, # top-left corner
     50, 100, # lower-left
     100, 100, # lower-right corner
     100, 50) # top-right corner
```

You'll be drawing a total of 64 `quad()`s - in eight rows and eight columns. So, consider that a good place to start might even be something like...

```
for column in range(8):
    for row in range(8):
```

Notice in the reference image that as quads are drawn across the page, there is an increasing amount of "jitter" - or randomness - nudging their corners, or vertices, up, down, left and right. Of course, since we're working with quads, we have a high amount of control over each one of their vertices, which makes them preferable to the visually similar `rect()`. 

If you wanted to make a set of quads that became linearly more distorted - instead of randomly - you could try adding a variable (like perhaps that variable above, `jitter`) to its corners, and increasing `jitter` each time your loop runs. Because you want this to happen randomly, you'll have to get a bit more clever. `random(jitter)` will return a random number up to the value of the `jitter` variable. Even more useful, `random(-jitter, jitter)` can also return negative values - which in this case might help you make sure those vertices can be distorted upwards and to the left, too. 

First, just work on placing each quad in your for loop, using the `column` and `row` variables generated by that loop. 

Next, try adding some random jitter to each corner... and increasing that jitter over time. Good luck!
