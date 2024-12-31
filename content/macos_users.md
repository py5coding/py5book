# Special Notes for macOS Users

Although much progress has been made getting py5 to work on macOS, there are a few
remaining issues and limitations, mostly related to Jupyter Notebooks. These
issues are minor and are in line with typical macOS experiences.

```{admonition} TL;DR

-   When using Jupyter Notebooks, start each notebook with the `%gui osx` magic
-   The [](/reference/sketch_run_sketch) method's `block` parameter is
    by necessity set to `False` when run through Jupyter Notebooks and set to
    `True` when run through a generic Python interpreter
-   The py5bot Jupyter kernel and some py5 magics cannot use the OpenGL renderers
-   The render helper tools cannot use the OpenGL renderers
-   When using Jupyter notebooks, the select methods
    [](/reference/sketch_select_folder), [](/reference/sketch_select_input), and
    [](/reference/sketch_select_output) will not work.
-   When using Jupyter notebooks, older macOS laptops (laptops with Intel CPUs?
    laptops with older macOS versions?) have an odd quirk where if the first
    Sketch you run uses the default renderer (JAVA2D), you cannot use the OpenGL
    renderers (P2D and P3D).
-   Ignore the warnings you see when exiting a Sketch ([Issue
    #6](https://github.com/py5coding/py5generator/issues/6))
```

None of these will stop you from using py5 productively on macOS.

## Jupyter Notebooks

Everything will work just fine after executing the following IPython magic at
the *start* of each notebook:

```ipython
%gui osx
```

This changes how Jupyter executes later notebook cells to allow GUI windows to
open and be usable. Do this *before* importing py5. If you import py5 without
doing this, py5 will run the magic for you after giving you a polite warning.

That magic command should not be run on non-macOS machines. If you need your
notebook code to run on multiple platforms, use the following code instead:

```python
import sys

if sys.platform == 'darwin':
        get_ipython().run_line_magic('gui', 'osx')
```

The `%gui osx` magic will enable macOS Cocoa event loop integration. Use of this
magic is not unique to py5; it is also used for other Python applications that
open interactive windows. It instructs Jupyter's Python kernel to share the main
thread with the window. On macOS, all GUIs are required to run on the main thread.
The Python kernel, however, also needs to use the main thread to execute cells.
Therefore, the main thread must be shared.

To see an example demonstrating the consequences of this sharing, try running
the following Sketch on macOS:

```python
import time


def setup():
    py5.size(200, 200, py5.P2D)


def draw():
    if py5.frame_count % 50 == 0:
        py5.println(py5.frame_count)
    py5.square(py5.random_int(py5.width), py5.random_int(py5.height), 10)


py5.run_sketch(block=False)

print('start pause')
time.sleep(3)
print('end pause')
```

When this code is run on a Linux or Windows computer, the output will be
similar to this:

```text
start pause
50
100
end pause
150
200
...
```

But when run on macOS, the output will be:

```text
start pause
end pause
50
100
150
200
...
```

Also, you'll notice the Sketch window does not open on the screen until after
"end pause" is printed. This will be the case for the OpenGL renderers `P2D` and
`P3D` as well as the default renderer `JAVA2D`.

Furthermore, if your Sketch uses the default renderer `JAVA2D` and you were to
later execute `time.sleep(3)` in another notebook cell, you would momentarily
see the Sketch stop animating. The Sketch actually is still running, but the new
frames are not being drawn to the screen. For the above Sketch this will be
apparent at the end of the 3 seconds when many new squares appear at the same
time. The Sketch really is running normally during this time, but because of
the shared main thread, the new frames are not being drawn to the screen. This
behavior only applies to the `JAVA2D` renderer and not the OpenGL
renderers `P2D` and `P3D`.

There are just a few more things macOS users need to know about using py5 in a
Jupyter notebook.

### Blocking

In Jupyter, the [](/reference/sketch_run_sketch) method will never "block",
which means that the method will return right away and let you execute lines of
code that appear after it or in other notebook cells. This shouldn't be a
problem for notebook users as this is most certainly what you would want to
happen anyway. If you want some code to run right when the Sketch exits,
implement an `exiting()` function, which will be called by py5 as the Sketch is
shutting down.

If you need to simultaneously run multiple Sketches in the same process on macOS,
running them through a Jupyter notebook (using class-mode) is your only option.

### Select Methods

When run through Jupyter, the select methods
[](/reference/sketch_select_folder), [](/reference/sketch_select_input), and
[](/reference/sketch_select_output) will not work. Consider using IPython
widgets instead.

### py5bot and py5 magics

On macOS, the Jupyter py5bot kernel and the py5 magic command
[](/reference/py5magics_py5bot) cannot use the OpenGL (P2D and P3D) renderers.
The [](/reference/py5magics_py5draw) magic also cannot use the OpenGL renderers,
and the [](/reference/py5magics_py5drawdxf) magic is not available.

A future version of py5 will address these issues.

## Generic Python Interpreter

Starting with py5 version 0.7.2, a Sketch can run through the generic Python
interpreter (outside of Jupyter). The limitations are that you can only run
one Sketch at a time and that exiting the Sketch will terminate the Python
process.

The [](/reference/sketch_run_sketch) command will always "block", which means
that the method will not return and allow you execute lines of code that appear
after it. Since exiting the Sketch will also terminate the Python process, the
call to [](/reference/sketch_run_sketch) will typically be the last line in your
Python script.

## Render Helper Tools

The render helper tools [](/reference/py5functions_render),
[](/reference/py5functions_render_frame),
[](/reference/py5functions_render_sequence), and
[](/reference/py5functions_render_frame_sequence) cannot use the OpenGL
(P2D and P3D) renderers.

A future version of py5 will address these issues.

## Jupyter Notebooks on Older Laptops

My old MacBook Pro laptop, with an Intel i7 CPU, runs macOS 12.7.6 (Monterey) and
cannot be upgraded to a newer macOS version. For reasons I cannot fathom, py5
has an odd limitation when run in a Jupyter Notebook on this machine. If the
first executed Sketch uses the default (JAVA2D) renderer, later executing a
Sketch that uses an OpenGL renderer will cause the IPython kernel to crash. If I
want to use an OpenGL renderer anywhere in the notebook, the first Sketch I run
must also use OpenGL.

I don't have this problem on my newer 2020 MacBook Pro with an M1 chip.
Everything worked just fine with macOS 14.7.2 (Sonoma). I upgraded it to
macOS 15.2 (Sequoia), and it works fine there too.

It's an unusual problem and right now I don't know if this is because of
something different with the Intel CPU or if it is because of the old (and no
longer supported) macOS version 12.7.6. Hopefully others from the py5 community
can provide feedback here so I can better understand what is going on.

To prevent a crash on machines that are potentially vulnerable to this problem,
py5 will detect the sequence of events that would lead to a crash and will instead
output a helpful message and throw an exception.

If you'd like to disable this safety check and test this for yourself, use the
following code in a Jupyter Notebook, with each line of code executed separately.

```python
from py5 import macos_problem, test

macos_problem.disable_safety_check()

# run a Sketch with the default renderer
test.test_java2d()

# run a Sketch with an opengl renderer
# does this cause a crash???
test.test_p2d()
```

If your laptop experiences the crashing problem and you'd like to quickly add a
Sketch to the beginning of your notebook that uses an OpenGL renderer, use the
below code. This will eliminate the problem entirely.

```python
import py5

from py5 import test
test.test_p2d()
```

This problem is an unfortunate side effect of a code change in py5 version 0.10.4
that actually improved a lot of things for all macOS users. This code change was
too important to leave out. The side effect is such an obscure edge case that it
likely won't impact very many users. Still, I don't want any py5 users to experience
frustration because of these kinds of crashes. That's why this is documented and
py5 has a safety check.

## Sketch Exit

When the Sketch exits you will see the following warning:

```text
NewtNSView::dealloc: softLock still hold @ dealloc!
```

Ignore that. That message comes from within native macOS code. Windows and Linux
users also get odd messages when exiting a Sketch. It's not a cause for concern.
