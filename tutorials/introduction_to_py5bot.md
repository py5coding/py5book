---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: py5bot
  language: python
  name: py5bot
---

# py5bot

This is py5bot. A simple and easy to use programming environment for teaching the very basics of Python programming and creative coding with py5.

If you are viewing this page from the py5 documentation website, see the Binder or Live Code options by hovering your mouse over the rocket ship icon at the top of this page.

Each cell in this notebook can contain a series of py5 drawing commands. The drawing commands will be executed to create a static image that will be embedded in the notebook.

The main design goal is to provide a simple programming environment that is suitable for beginners. Individual programming concepts can be explained in isolation from more complicated Python concepts like functions or modules.

When hosted on Jupyter Hub and paired with Jupyter Lab's "Show Contextual Help" feature, py5bot can become an easy to use programming environment for educators to teach Python to beginners.

Below is a simple example.

```{code-cell} ipython3
size(200, 200)
background(255, 255, 0)
rect(50, 50, 100, 100)
```

If you are familar with Processing, you might describe this as a static sketch.

Internally, py5 executes these commands inside of a `setup()` method to render a single frame.

+++

## py5bot rules

There are a few important rules that you should be aware of.

* The `size()` command should be the first line of Python code. Comments are ignored. If the `size()` command is omitted, the output size will be 100 by 100 pixels.
* When py5bot is run on Windows and Linux computers, you can use the `P2D` or `P3D` renderers. These OpenGL renderers are currently not supported on OSX.
* Each cell has its own local namespace. Variables and functions defined in one cell cannot be used in another cell.

There are some less important rules that should be mentioned but aren't that important:

* Calls to `smooth()` or `no_smooth()`, if desired, should be after `size()` and before other Python commands.
* A call to `pixel_density()` would also need to be after `size()` and before other Python commands, but since it just scales the size of the output, you probably shouldn't bother using it in py5bot.

That's basically it.

+++

## More examples

Let's see a more interesting example.

```{code-cell} ipython3
size(200, 200)
background(224)
no_stroke()
for _ in range(250):
    fill(random_int(255), random_int(255), random_int(255))
    rect(random_int(width), random_int(height), 10, 10)
```

If you like you can put `print` statements in the cell.

```{code-cell} ipython3
size(200, 200)
print('draw a red rectangle')
fill(255, 0, 0)
rect(50, 50, 100, 100)
```

You can define your own functions. Any functions will be local to only one cell, however.

```{code-cell} ipython3
size(200, 200)

def draw_random_circle():
    x = random_int(width)
    y = random_int(height)
    circle(x, y, random_int(25))
    
for _ in range(20):
    draw_random_circle()
```

## Error Message Reporting

No programming enviroment would be suitable for beginners without appropriate error messages. Observe that in all cases, the error message correctly points to the problem in the code.

Below is what syntax errors look like.

```{code-cell} ipython3
size(200, 200)
rect(10, 20, 30, 40))
```

This next example is a programming error:

```{code-cell} ipython3
size(200, 200)

impossible = 100 / 0
```

The next example shows the displayed error message for when a py5 drawing function is used incorrectly.

```{code-cell} ipython3
size(200, 200)

rect(1, 2, 3, 4, "extra param")
```

These error messages can be customized. That is a separate topic to be explained elsewhere.

+++

There are py5bot reserved words. You are not allowed to use a reserved word as a variable name.

Ideally py5bot would have syntax hightlighting to color the reserved words differently, but that hasn't been implemented yet. Let me know if you are interested in working on that.

```{code-cell} ipython3
size(200, 200)

red = 255, 0, 0
fill(*red)
rect(50, 50, 100, 100)
```

## Other Renderers

As previously stated, the P2D and P3D renderers only work on Linux and Windows. On OSX, py5bot will replace the P2D or P3D renderers with the default renderer after displaying a polite warning.

If you are running this through Jupyter Lab, the following cell will work just fine, without a warning. What matter is where the Jupyter server is running, not the Jupyter client.

```{code-cell} ipython3
size(200, 200, P2D)

circle(width / 2, height / 2, 150)
```

## Code Bypass

You can use `%%python` to bypass py5bot execution. Any variables or functions defined in such a cell will be available to all later cells. Python modules can be imported here as well.

The `%%python` bypass meta-command must be at the very beginning of the code cell.

```{code-cell} ipython3
%%python

import numpy as np

def draw_random_circle(x, y):
    fill(random_int(255), random_int(255), random_int(255))
    circle(x, y, random_int(25))

message = "py5bot is awesome"
```

The code in the previous cell will be available to regular py5bot cells.

```{code-cell} ipython3
size(200, 200)

no_stroke()

for _ in range(250):
    x = np.random.normal(width / 2, 40)
    y = np.random.normal(height / 2, 40)
    draw_random_circle(x, y)

    
fill(255, 196)
rect(0, 0, width, 30)

fill(255, 0, 0)
text_size(22)
text(message, 10, 20)
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
