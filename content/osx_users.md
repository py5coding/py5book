# Special Notes for OSX Users

There are some difficulties using py5 on Mac computers that still need
to be worked out.

```{admonition} TL;DR

-   Mac users must use Jupyter Notebooks with the `%gui osx` magic at
    the start of each notebook ([Issue
    #4](https://github.com/hx2A/py5generator/issues/4))
-   The [](/reference/sketch_run_sketch) method's `block`
    parameter is not available. This limits some py5 features that
    depend on it, such as py5bot.
-   When possible, prefer the `P2D` renderer over the default renderer
-   If using the default renderer, sometimes keyboard events will be
    captured by the Jupyter Notebook and not the Sketch window
-   Sketches that use the default renderer will not appear as an icon on
    the Dock at the bottom of the screen
-   Ignore the warnings you see when exiting a Sketch ([Issue
    #6](https://github.com/hx2A/py5generator/issues/6))
```

None of these will stop you from using py5 productively, but they might
annoy you a bit.

## JPype

The py5 library uses the Python library
[JPype](https://jpype.readthedocs.io/en/latest/) to create the
Java-Python bridge between the two languages. There is currently [a bug
in JPype that prevents Java GUI applications from running correctly on
Mac computers](https://github.com/jpype-project/jpype/issues/906).
JPype's core developer does not have a Mac computer to test and fix the
problem, and can't get access to one because of pandemic related
issues. This is a problem, but let's keep things in perspective: the
pandemic has taken a toll on all of us, with many people losing their
lives or jobs. Software bugs and delays aren't a real problem. I'd
like you to be patient with me while this gets worked out.

## Jupyter Notebooks

If you like Jupyter Notebooks, you're in luck! Everything will work
just fine after executing the following IPython magic at the
*start* of each notebook:

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell"><div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%</span><span class="k">gui</span> osx</pre></div>
</div></div></div></div>

This should be executed *before* importing py5. If you
forget to use the `%osx gui` magic, py5 will print a warning and
activate it for you.

OSX has some requirement that only allows GUI applications to run on the
main thread. That magic command configures things so that py5 can work.
I don't understand how or why it works. I know that it works, and I am
grateful.

The `%osx gui` magic should be executed before the `import py5`
statement. Running a script with the `%run` magic doesn't seem to work.
The py5 Jupyter Notebook Kernel will take care of the `%osx gui` magic
for you when run on a Mac computer.

If you like coding in an interactive terminal (I hope I'm not the only
one), you will need to use `jupyter console` and not `ipython`. The two
interactive terminal applications are not identical, with the `%gui osx`
magic working in the former but not the latter. The console can be
frustrating to use though. If a Sketch stops because of an error, no
error message will appear until after you hit the return key in the
console.

Mac users won't be able to use the generic `python` interpreter to run
py5, either interactively or to run a python program. If you need to run
a py5 application in a script, your best bet is to put your code in a
notebook with `%gui osx` at the top and execute the notebook, like so:

``` bash
$ jupyter nbconvert --execute --to notebook --inplace py5_code.ipynb
```

Of course you can always use a virtual machine or Docker, but those are
more complicated to get working. Still, these are valid choices that
might meet your needs.

I'm not an expert Mac user so it is very likely there is more to be
said about using py5 on Macs. Please experiment based on your own
knowledge and ideas. If you discover something useful, let me know and
I'll update the documentation. Feel free to comment on the [Github
Issue (#4)](https://github.com/hx2A/py5generator/issues/4) for this
problem.

## `Block` Parameter

The [](/reference/sketch_run_sketch) method's `block`
parameter is not available on OSX. This also limits some py5 features
that depend on it:

-   py5bot cannot use the `P2D` or `P3D` renderers. This includes the
    [](/reference/py5magics_py5bot) magic and the py5bot Jupyter
    Notebook Kernel.
-   The [](/reference/py5magics_py5draw) magic cannot use the
    `P2D` or `P3D` renderers.
-   The [](/reference/py5magics_py5drawdxf) magic is not
    available.
-   The render helper tools [](/reference/py5functions_render),
    [](/reference/py5functions_render_sequence),
    [](/reference/py5functions_render_frame), and
    [](/reference/py5functions_render_frame_sequence) cannot use the
    `P2D` or `P3D` renderers.

To undertand the cause of this issue, consider the following code:

``` python
import time

import py5

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

``` text
start pause
50
100
end pause
150
200
...
```

You can see that the Sketch is running at the same time as `time.sleep`.

When run on OSX, the output will look like this:

``` text
start pause
end pause
50
100
150
200
...
```

The Sketch is not able to run at the same time as `time.sleep`.

Additionally, the Sketch window will not appear until after the Notebook
cell with the [](/reference/sketch_run_sketch) call finishes
executing. The Sketch cannot start running until that cell's execution
completes. If the `block` parameter had been set to `True`, cell
execution would not complete because the [](/reference/sketch_run_sketch) method
blocks until the Sketch exits. But the Sketch would
not get the opportunity to start running because it needs to wait for
cell execution to complete. The Notebook would be stuck in limbo,
endlessly waiting for a Sketch to exit that cannot even start. The user
will need to interrupt the Kernel to break the deadlock.

If in the above code the Sketch had used the default renderer instead,
the printed output would be correct but the Sketch window would still
wait for cell completion before appearing. However, when the Sketch
window did become visible, it would have many squares drawn on it
already. In this case the animation is hidden when it starts running and
doesn't become visible to the user until after cell completion.
Furthermore, if one were to later run `time.sleep(3)` in a different
cell, the animation would appear to freeze until cell execution
completed, then resume with many new squares drawn on it. This has
nothing to do with `time.sleep`; the issue has to do with the fact that
the Notebook and the Sketch need to share the main thread, so any cell
that takes a long time to execute will prevent the Sketch from
simultaneously displaying changes to the drawing surface.

Sketches that use the OpenGL renderers `P2D` and `P3D` will not pause or
freeze once they open and start running. I recommend you use the OpenGL
renderers and not the default renderer when possible.

## Keyboard Events

When using the default renderer, sometimes keyboard events are captured
by the Jupyter Notebook and not the Sketch window. This seems to happen
for the first Sketch if the first Sketch also uses the default renderer.
This behavior will be confusing because the Sketch will be capturing
mouse events but not keyboard events.

While this behavior is occuring, hitting the `ESC` key to exit the
Sketch will cause the window to move behind other windows, making you
think the Sketch has stopped running. On OSX, Sketches that use the
default renderer will not appear as an icon on the Dock at the bottom of
the screen. If you try to run a new Sketch and get a message stating
that the current Sketch is already running, try first looking for the
Sketch window underneath the other windows on your screen.

## Sketch Exit

When the Sketch exits you will see the following warning:

``` 
NewtNSView::dealloc: softLock still hold @ dealloc!
```

Ignore that. Windows and Linux users also get odd messages when exiting.
