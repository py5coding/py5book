# How Does py5 Work?

This document explains how py5 works

## How py5 Doesn't Work

Before diving into the details of how py5 actually works, let's first discuss how py5 doesn't work, and why.

You should know that py5 was not the first attempt at creating a Python 3 version of Processing that leveraged the Processing Jar files, as Processing.py does for Jython. The general approach of earlier attempts, as well the first few iterations of py5's architecture, looked very much like this:

1. py5 code calls the user's `settings()` function
2. py5 code calls Java code to initialize the Sketch window
3. py5 code calls the user's `setup()` function once
4. py5 code calls the user's `draw()` function in a loop

You can imagine writing the following pseudocode for the critical `run_sketch()` function that fits this general pattern:

```python
import time

def run_sketch(settings, setup, draw):
    call_users_settings_method(settings)
    create_sketch_window()
    call_users_setup_method(setup)
    while True:
        call_users_draw_method(draw)
        time.sleep(1 / frame_rate)
```

In fact, if you look at the [initial commit of the py5 project](https://github.com/py5coding/py5generator/blob/636712b1c786eee67a6e1cbec9d59d2a25afb0e8/packages/py5generator/py5generator/templates/py5_init_template.py), you can see this is very close to what py5 actually did. (Note that this early version of py5 also used modified Processing Library code that was not checked in.) Observe that with this approach, Python is managing the animation thread, not the Processing Library. This approach could in fact create runable py5 Sketches. There were, however, many problems. Two of the most critical were:

* There's no way to trigger mouse and keyboard events
* The OpenGL renderers `P2D` and `P3D` always crashed

The problem with the OpenGL renderers had to do with something called a "context thread". Bottom line, only one thread is allowed to make OpenGL calls, and that thread is not the Python thread this early version of py5 was using to call the user's `draw()` function in a loop. I tried everything I could think of to get OpenGL to work. As this work was done during the first month of COVID lockdowns, I had a lot of time to experiment. Nevertheless, this approach was not and could not be successful.

## How py5 Actually Works

The key insight behind py5 was to abandon the above approach and instead leverage JPype's ability to call Python from Java. Calling Java from Python is obviously important, but py5 wouldn't exist if JPype couldn't also make calls in the other direction, making calls *from* Java *to* Python.

With this approach, the Processing Library can manage the Sketch's animation thread and the various OpenGL complexities. In fact, as far as the Processing Library is concerned, every py5 user is running the exact same Java code: [Sketch.java](https://github.com/py5coding/py5generator/blob/main/py5_jar/src/main/java/py5/core/Sketch.java). This `py5.core.Sketch` class is an instance of the Processing Library's `processing.core.PApplet`.

The basic steps of a running py5 Sketch look like this:

1. py5 code creates an instance of the Java class `py5.core.Sketch`
2. py5 code uses JPype to pass the instance of `py5.core.Sketch` to the Processing Library's `runSketch()` method
3. The Processing Library launches the Sketch, opening the Sketch window and starting the animation thread
4. The Processing Library calls `py5.core.Sketch`'s `settings()`, `setup()`, and `draw()` methods, as well as mouse and keyboard event methods as needed
5. `py5.core.Sketch`'s `settings()`, `setup()`, and `draw()` methods make calls to Python, instructing it to call the user's `settings()`, `setup()`, and `draw()` functions
6. The user implemented functions use py5's API, making calls to methods such as `size()`, `begin_shape()`, etc.
7. Calls to py5's API methods that leverage the Processing Library code such as `size()`, `begin_shape()`, etc. make corresponding calls to the Processing Library methods `size()`, `beginShape()`, etc.
8. Calls to py5's API methods that are implemented in Python such as `convert_shape()`, `random()`, etc. execute their Python code without using the Processing Library

This approach is quite a bit more complicated, but the OpenGL renderers `P2D` and `P3D` work correctly, and the mouse and keyboard event functions are triggered at the appropriate times.

Let's review py5's code in more detail, examining each of the above steps to understand how they work.

### Create instance of the Java class `py5.core.Sketch`

### Pass `py5.core.Sketch` instance to the Processing Library's `runSketch()` method

### Open Sketch Window and Start Animation Thread

## Additional Complexity for OSX
