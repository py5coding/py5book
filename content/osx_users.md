# Special Notes for OSX Users

Although much progress has been made getting py5 to work on OSX, there are a few
remaining issues and limitations. The issues that are fixable will be addressed
in future py5 releases. The remaining issues are minor and in line with typical
OSX experiences.

```{admonition} TL;DR

-   When using Jupyter Notebooks, start each notebook with the `%gui osx` magic
-   The [](/reference/sketch_run_sketch) method's `block` parameter is
    by necessity set to `False` when run through Jupyter Notebooks and set to
    `True` when run through a generic Python interpreter
-   Apple Silicon is a mystery and will probably remain a mystery until I can
    get my hands on one to test
-   The py5bot Jupyter kernel and some py5 magics cannot use the OpenGL renderers
-   The render helper tools cannot use the OpenGL renderers
-   When using Jupyter notebooks, Sketches that use the default renderer will not
    appear as an icon on the dock at the bottom of the screen
-   Ignore the warnings you see when exiting a Sketch ([Issue
    #6](https://github.com/py5coding/py5generator/issues/6))
```

None of these will stop you from using py5 productively on OSX.

## Jupyter Notebooks

Everything will work just fine after executing the following IPython magic at
the *start* of each notebook:

```ipython
%gui osx
```

This changes how Jupyter executes later notebook cells to allow GUI windows to
open and be usable. Do this *before* importing py5. If you import py5 without
doing this, py5 will run the magic for you after giving you a polite warning.

That magic command should not be run on non-OSX machines. If you need your
notebook code to run on multiple platforms, use the following code instead:

```python
import sys

if sys.platform == 'darwin':
        get_ipython().run_line_magic('gui', 'osx')
```

The `%osx gui` magic will enable OSX Cocoa event loop integration. Use of this
magic is not unique to py5; it is also used for other Python applications that
open interactive windows. It instructs Jupyter's Python kernel to share the main
thread with the window. On OSX, all GUIs are required to run on the main thread.
The Python kernel, however, also needs to use the main thread to execute cells.
Therefore, the main thread must be shared.

To see an example demonstrating the consequences of this sharing, try running
the following Sketch on OSX:

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

But when run on OSX, the output will be:

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

There are just a few more things OSX users need to know about using py5 in a
Jupyter notebook.

### Blocking

In Jupyter, the [](/reference/sketch_run_sketch) method will never "block",
which means that the method will return right away and let you execute lines of
code that appear after it or in other notebook cells. This shouldn't be a
problem for notebook users as this is most certainly what you would want to
happen anyway. If you want some code to run right when the Sketch exits,
implement an `exiting()` function, which will be called by py5 as the Sketch is
shutting down.

If you need to simultaneously run multiple Sketches in the same process on OSX,
running them through a Jupyter notebook (using class-mode) is your only option.

### Dock Icon

When run through Jupyter, Sketches that use the default `JAVA2D` renderer will
not appear as an icon on the dock at the bottom of the screen. This does not
apply to Sketches that use the OpenGL renderers or Sketches run through the
generic Python interpreter.

### py5bot and py5 magics

On OSX, the Jupyter py5bot kernel and the py5 magic command
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

The render helper tools [](/reference/py5functions_render.rst),
[](/reference/py5functions_render_frame.rst),
[](/reference/py5functions_render_sequence.rst), and
[](/reference/py5functions_render_frame_sequence.rst) cannot use the OpenGL
(P2D and P3D) renderers.

A future version of py5 will address these issues.

## Apple Silicon

The Apple Silicon version of Processing (Java) is complete and py5 contains the
correct jars and native libraries. However, I don't have an Apple Silicon
machine to test with, so I don't know if it actually works correctly or not. If
you have such a machine available, please test and let me know. If it doesn't
work, know that I have a plan to get access to one in June and will be able to
test and debug any issues then.

## Sketch Exit

When the Sketch exits you will see the following warning:

```text
NewtNSView::dealloc: softLock still hold @ dealloc!
```

Ignore that. Windows and Linux users also get odd messages when exiting a Sketch.
