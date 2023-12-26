# Tips for Processing Java Users

**Welcome!**

We hope you enjoy using the Processing graphics vocabulary, now with Python 3.

## The slightly different *snake_case* names

The first thing you might notice is how the Processing function/method names you were used to followed the Java community's convention called *camelCase* and on py5 they use the Python community's *snake_case* convention: `mouseX` becomes `mouse_x`, and `noFill()` becomes `no_fill()`, etc.

Another thing you should know is that the global `mousePressed` variable becomes `is_mouse_pressed` and the event function we define for a "mouse pressed event", that in Java would be written `void mousePressed(){ ...`, should now be defined as `def mouse_pressed(): ...`.

This is because in Python the namespace for variable names and function names is the same. Note also that `keyPressed` becomes `is_key_pressed` for the variable, and `key_pressed()` for the event function.

Processing's `map(value, start, end, target_start, target_end)` is now [remap()](/reference/sketch_remap) because there is a Python built-in [`map(func, iterable)`](https://docs.python.org/3/library/functions.html#map). Likewise, `filter()` becomes [apply_filter()](/reference/sketch_apply_filter).

Processing's `get()` and `set()` functions to manipulate pixels become `get_pixels()` and `set_pixels()`, but you might want to read about `np_pixels` and [set_np_pixels()](/reference/sketch_set_np_pixels). That's because in Python, `set()` creates a [*set* data structure](https://docs.python.org/3/tutorial/datastructures.html#sets).

Instead of `frameRate`, use the [frame_rate()](/reference/sketch_frame_rate) function to set a target frame rate and the [get_frame_rate()](/reference/sketch_get_frame_rate) function to find out the current frame rate (an exponential moving average).

**Please have a look at the [py5 Reference Summary](/reference/summary), it will help you find any missing names**

## How about the P-Classes?

Most of Processing high-level objects, like `PFont` for typography fonts, or `PImage`, for image buffers, have an equivalent, a wrapper, in py5. So `Py5Font` does whatever `PFont` does, and `Py5Image` everything `PImage` does.

Then, there is some bonus stuff, `Py5Image` brings in a very helpful new [`numpy` interface for an "array of pixels"](/reference/py5image_np_pixels).

If you are used to `PVector`, please note that `Py5Vector` is a completely new implementation of vector objects, 2D, 3D and 4D, so it has some different method & attribute names, you won't regret reading the [Py5Vector](/reference/py5vector) documentation.

## About the libraries

No`import processing.pdf.*;` is needed for using the PDF features, same with the SVG export, but for other Processing Java libraries... it could be more complicated. Have a look at this [Camera3D tutorial](/how_tos/use_camera3D).

On the other hand, you can now import Python libraries with the `import` statement, you'll also need it to bring in functions and classes from other *modules* (files) if you split your sketch into several `.py` files.

## More tips for porting Processing Java code to py5

Maybe you want to port some existing Processing Java code to Python + py5?  The following tips should help you with the most common issues.

### Getting started on quick code conversions!

- As you probably know already, Python uses indentation to place code lines 'inside' a function definition and in many other code nesting structures. In Java the braces`{}` rule, but it is common for the indentation to also reflect the code hierarchy, even if this is not mandatory, so use the IDE auto-formatting tool before you start, and take care!

- The braces need to be removed, and you should replace each `{` with `:` at the beginning of an instruction block (this is not true for *array definitions*, which have braces but are not an instruction block, and will probably become a list or tuple with `[]` or `()`.

- Remove the `;` at the end of the lines.

- Comments with `//` in Java become comments with `#`. Multiline comments with `/*…*/` can be converted to *docstrings*, with triple quotes in Python, `""" … """`.

- Java is a *static typing language* and Python is a *dynamic typing language* that means we can remove all type declarations and everything should work fine, but, alternatively, one can keep the type information as [type annotations](https://docs.python.org/3/library/typing.html) that can then be used by a static type checking tool (like `mypy` or the checkers in some IDEs).

- For variables, you either simply remove the type `int`, `float`, `String`, `color`, `boolean` from variable declarations (for example, `int i = 0;` becomes `i = 0`), otherwise you can write `i : int = 0`, in this case `String` should be written `str`, `Boolean` will become `bool` and you might have to figure out a few other different class/type names. 

- On function definitions, we should remove `void` or any return type declaration, replacing it with Python's `def`. You can optionaly annotate the return type using `-> T:` as shown below. The type declaration of parameters should be removed or should follow the same pattern as the annotations for variables.

   **Java**
  
  ```java
  float average(float a, float b) {
    return (a + b) / 2;
  }
  ```

  **Python**
  
  ```python
  def average(a, b):
      return (a + b) / 2
  ```

**Type annotated Python**

  ```python
  def average(a: float, b: float) -> float:
      return (a + b) / 2
  ```

### A table with some equivalences for conversion

Boolean values in Java are named `true` and `false`, in Python they are `True` and `False`. Let's make a chart with the logical operators and some other equivalences.

| Java | Python |
| ------------------------------------------------ | ------------------------------------------ |
| `void func() {…}` | `def func():…` |
| **`true`** and **`false`** | **`True`** and **`False`** |
| <code>a <b>&&</b> b</code> (logical AND) | `a` **`and`** `b` |
| <code>a <b>&#x7C;&#x7C;</b> b</code> (logical OR) | `a` **`or`** `b` |
| <code><b>!</b>a</code> (logical NOT) | **`not`** `a` |
| `i++` (increment) | `i += 1` |
| `i--` (decrement) | `i -= 1` |
| `a <= b && b < c` | `a <= b < c` |
| `for (int i=0; i<limit; i++) { …` | `for i in range (limit): …` |
| `for (int i=start; i<limit; i+=step) { …` | `for i in range (start, limit, step): …` |
| `for (Ball b : arrayListOfBalls) { …` | `for b in list_of_balls: …` |
| `fill(#FFCC00) // hexadecimal color notation` | `fill('#FFCC00') # needs ' ' or " "` |

Similar to `null` in Java we have the special value `None` in Python, they are not totally equivalent but it is usually a good guess to make the substitution.

### Looping with `for`

The simplest case is a `for` based on a counter, such as `for (int i=0; i<limit; i++) { …` which translates into `for i in range(limit): …` and the so-called *for each* loop, shown in the chart, is also very straightforward.

But if you have a Java `for` loop with a *float* step, as the `range()` based `for` construct in Python works only with integers, you might want to define a 'special' non-int range generator, or convert it to a `while` loop like in the example below.

**Java**

```java
float angleStep = TWO_PI / 18
for (float angle=0; angle < TWO_PI; angle += angleStep){ 
    …
}
```

**Python**

Using a `while` loop

```python
angle_step = TWO_PI / 18
angle = 0
while angle < TWO_PI:
    …
    angle += angle_step
```

Another option would be to define a 'special' range generator:

```python
def frange(start, stop=None, step=1):
    if stop is None:
        stop, start = start, 0
    assert step != 0, "step can't be zero"
    invalid_limit_error_message =  (
        'start must be smaller than stop for positive step'
        if step > 0 else
        'stop must be smaller than start for negative step'
    )
    assert stop > start if step > 0 else stop < start, invalid_limit_error_message
    count = start
    while count < stop:
        yield count
        count += step

# and then frange in use...
step = TWO_PI / 18
for angle in frange(0, TWO_PI, step):
    …    
```

Now an example of a loop made just to get objects from a data structure:

```java
for (int i = 0; i < my_array.length; i ++) {
  something(my_array[i]);
}
```

**Python**

```python
for item in my_list:
    something(item)
```

or, if you need the index.

```python
for i, item in enumerate(my_list):
    something(i, item)
```

Here a reversed iteration for removing items from an *ArrayList* in Java, a list in Python:

**Java**

```java
for (int i = particles.size() - 1; i >= 0; i--) {
  Particle p = particles.get(i);
  p.run();
  if (p.isDead()) {
    particles.remove(p);
  }
}
```

**Python**

```python
for i, p in reversed(list(enumerate(particles))):
    p.run()
    if p.is_dead():
        del particles[i]
```

or maybe:

```python
for i in reversed(range(len(particles))):
    p = particles[i]
    p.run()
    if p.is_dead():
        del particles[i]
```

### `if`, `else` and their friends

Note that the `if` condition in Python does not require the parentheses as in Java. The combination of `else if`  becomes the `elif` contraction.

**Java**

```java
for (int i = 2; i < width-2; i += 2) {
  if ((i% 20) == 0) {
    stroke (255);
    line (i, 80, i, height / 2);
  } else if ((i% 10) == 0) {
    stroke (153);
    line (i, 20, i, 180);
  } else {
    stroke (102);
    line (i, height / 2, i, height-20);
  }
}
```

**Python**

```python
for i in range(2, width - 2, 2):
    # If 'i' divides by 20 with no remainder
    if i % 20 == 0:
        stroke(255)
        line(i, 80, i, height / 2)
    elif i % 10 == 0:
        stroke(153)
        line(i, 20, i, 180)
    else:
        stroke(102)
        line(i, height / 2, i, height - 20)
```

#### Ternary operator

**Java**

```java
result = cond ? a : b
```

**Python**

```python
result = a if cond else b
```

#### switch & case

Until recently there was nothing like Java's `switch / case` in Python, now from Python 3.10 onwards we get the [`match / case`](https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching) construct that could be used to translate that, but some people still frown upon it. You can arguably convert Java code with `switch / case` to a sequence of `if / elif` or, if just to call different functions, a function dictionary.

**Java**

```java
char letter = 'b';

switch(letter) {
  case 'a':
  case 'A': 
    println("Alpha");  // Does not execute in this example
    break;
  case 'b':
  case 'B': 
    println("Bravo");  // Prints "Bravo"
    break;
  default:            // default is optional
    println("Not found");  
    break;
}
```

**Python**

```python
letter = 'b'

if letter == 'a' or letter == 'A':
    println("Alpha")  # Does not execute in this example
elif letter in ('b', 'B'):
    println("Bravo")  # Prints "Bravo"
else:
    println("Not found")  
```

You might want to try a dictionary strategy.

```python
func = {
    'r': rect,
    'e': ellipse,
    't': (lambda x, y, w, h:
          triangle(x, y, x + w, y, x, y + h)),
    } 

def setup():
  size(400, 400)

def draw():
    func.get(key, func['r'])(100, 100, 200, 50)
```

### Global variables

If a variable is *declared and initialized* (type and value are defined) at the beginning of the sketch just remove the type declaration.

Since there is no way in Python to declare a variable without making an assignment, when the variable is just declared (a type is set without *initialization*) at the beginning of the sketch, we need to find where it is assigned for the first time and add the `global variable_name` statement at the beginning of that function.

In fact, every function that changes the assignment of global variables in its body needs the `global` statement with the names of the variables that are modified.

An example:

**Java**

```java
int rad = 60;       // Width of the shape
float xpos, ypos;   // Starting position of shape
float xspeed = 2.8; // Speed of the shape
yspeed float = 2.2; // Speed of the shape
int xdirection = 1; // Left or Right
int ydirection = 1; // Top to Bottom

void setup ()
{
  size (600, 300);
  // Set the starting position of the shape
  xpos = width / 2;
  ypos = height / 2;
}

void draw ()
{
  background (102);
  xpos = xpos + (xspeed * xdirection);
  ypos = ypos + (yspeed * ydirection);
    
  if (xpos > width-rad || xpos < rad) {
    xdirection * = -1;
  }
  if (ypos > height-rad || ypos < rad) {
    ydirection * = -1;
  }

  ellipse (xpos, ypos, rad * 2, rad * 2);
}
```

**Python**

```python
rad = 60; # Width of the shape
# The original had this here: float xpos, ypos; // Starting position of shape
xspeed = 2.8;   # Speed of the shape
yspeed = 2.2;   # Speed of the shape
xdirection = 1; # Left or Right
ydirection = 1; # Top to Bottom

def setup (): 
    size (600, 300)
    global xpos, ypos # xpos, ypos are assigned first here in setup
    noStroke ()
    xpos = width / 2
    ypos = height / 2

def draw ():
    global xpos, ypos, xdirection, ydirection # will be changed!
    background (102)
    xpos + = xspeed * xdirection
    ypos + = yspeed * ydirection
    
    if xpos < rad or width - rad < xpos: # note that rad is never changed
        xdirection * = -1
    if ypos < rad or height - rad < ypos:
        ydirection * = -1
    ellipse (xpos, ypos, rad * 2, rad * 2)
```

### Strings

**Type *char* in Java**

Java has a special type for characters, *char*, with literals written in code with single quotes `' '`, Python makes no such distinction, using single character *strings* (in `key`, for instance) and single or double quotes for *strings* in general.

To get a character at a certain position in a *string*, in Java, a special method is needed:

```Java
String word = "love";
char c = word.charAt(1); // c = 'o'
```

In Python the index notation `[i]` gets you a single character *string* from a *string*:

```Python
word = 'love'
c = word[1] # c = 'o'
```

**Comparing *strings* in Java**

```java
String str1 = "love";
String str2 = "love";
// Test if str1 is equal to str2
if (str1.equals(str2)) {
  println("equal"); } else {
  println("not equal"); 
}
```

**Comparing *strings* in Python**

```python
str1 = "love"
str2 = "love"
# Test if str1 is equal to str2
if str1 == str2:
  println("equal")
else:
  println("not equal")
```

### Importing libraries and using multiple tabs in your sketch

In Processing Java mode the libraries are imported with `import` but in Python mode this instruction is more often used to import *modules* from the *Python standard library*, and **.py** files in the same folder (which, unlike in Java mode, are not automatically a part of the sketch).

```python
from other_file import *  # everything from the file other.py
```

### Object Orientation

#### Getting an instance and access to its methods and attributes

Java needs the keyword **`new`** to create an instance of a class, just remove it! Access to methods and attributes is exactly the same.

**Java**

```java
import camera3D.Camera3D;

Camera3D camera3D;

void setup() {
  size(600, 600);
  camera3D = new VideoExport(this);
  camera3D.setBackgroundColor(192);
}
```

**Python**

``` python
from camera3D import Camera3D

def setup():
    global camera3D
    size(600, 600)
    this = get_current_sketch()    
    camera3D = Camera3D(this)
    camera3D.setBackgroundColor(192)
```

#### Declaring a class

Class declarations change slightly, roughly, the `def __init__(self …): …` method plays the same initialization role of the *constructor* method of a Java class (the method with the same name as the class). Strictly, the `__init__()` method, which we read like "dunder init", is not a constructor, but you don't have to worry about it. If you are curious, read more about Python's "data model" at the [Python docs](https://docs.python.org/3/reference/datamodel.html#basic-customization).

By convention, you'll add `self` as the first parameter of each method, and then use `self.` to access its members, any methods or attributes, of the class or instance.

Let's see the `MRect` class in the example **Basics > Objects > Objects** that comes with the Processing IDE.

**Java**

```java
class MRect 
{
  int w; // single bar width
  float xpos; // rect xposition
  float h; // rect height
  float ypos ; // rect yposition
  float d; // single bar distance
  float t; // number of bars
 
  MRect(int iw, float ixp, float ih, float iyp, float id, float it) {
    w = iw;
    xpos = ixp;
    h = ih;
    ypos = iyp;
    d = id;
    t = it;
  }
 
  void move (float posX, float posY, float damping) {
    float dif = ypos - posY;
    if (abs(dif) > 1) {
      ypos -= dif/damping;
    }
    dif = xpos - posX;
    if (abs(dif) > 1) {
      xpos -= dif/damping;
    }
  }
 
  void display() {
    for (int i=0; i<t; i++) {
      rect(xpos+(i*(d+w)), ypos, w, height*h);
    }
  }
}
```

**Python**

```python
class MRect:

    def __init__(self, iw, ixp, ih, iyp, id, it):
        self.w = iw  # single bar width
        self.xpos = ixp  # rect xposition
        self.h = ih  # rect height
        self.ypos = iyp  # rect yposition
        self.d = id  # single bar distance
        self.t = it  # number of bars

    def move(self, posX, posY, damping):
        self.dif = self.ypos - posY
        if abs(self.dif) > 1:
            self.ypos -= self.dif / damping

        self.dif = self.xpos - posX
        if abs(self.dif) > 1:
            self.xpos -= self.dif / damping

    def display(self):
        for i in range(self.t):
            rect(self.xpos + (i * (self.d + self.w)),
                 self.ypos, self.w, height * self.h)
```

`# TO DO:`

- How to deal with inheritance & method/function overloading.

### Data structures

Arrays like `int[]`, `float[]` or `PVector[]` usually become lists in Python (sometimes tuples if they are created and left alone). And a Java *ArrayList* is very much like a Python list:

**Java**

```java
ArrayList<Flag> flags; // a list of Flag de objetos

void setup() {
  size(400, 400); 
  flags = new ArrayList<Flag>();
  for (int i=0; i <50; i++) {
    flags.add(new Flag(100, 100, 12));
  }
}
```

**Python**

```python
flags = []  # a list of Flag de objetos

def setup():
    size(400, 400); 
    for i in range(50):
        flags.append(Flag(100, 100, 12))
```

Or you could use a *list comprehension*:

```python
def setup():
    global flags
    size(400, 400); 
    flags = [Flag(100, 100, 12) for i in range(50)]
```

#### 2D Arrays

**Java**

```java
int[][] board;
board = new int[grid_w][grid_h]
```

**Python**

```Python
board = [[0] * grid_w for _ in range(grid_h)]
```

Instead of `0` it could be a `None` placeholder or any calculated value if the structure will hold other things.

**Python with [numpy](https://numpy.org)**

```python
import numpy as np

board = np.zeros((2, 3))
print(board)
# array([[0., 0., 0.],
#        [0., 0., 0.]]
```

#### Other things (WIP)

- `HashMap` and `FloatDict`, are *mapping* data structures in Java, they become dictionaries (`dict`) in Python.

- If an *array* or an `ArrayList` is used to retain some kind of 'history', you might want to learn about `deque` (`from collections import deque`).

- Very simple classes in Java might suitably become just a *named tuple*.
