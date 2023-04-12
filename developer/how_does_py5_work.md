# How Does py5 Work?

This document explains py5's basic architecture and how it is able to connect the Processing Library's Java code to Python 3 using JPype.

The intended audience is intermediate to advanced coders with some experience creating Sketches with the original Java version of Processing.

## How py5 Doesn't Work

Before diving into the details of how py5 actually works, let's first discuss how py5 doesn't work.

You should know that py5 was not the first open source project that attempted to create a Python 3 version of Processing that leveraged the Processing Jar files, as [Processing.py](https://py.processing.org/) does in Jython. The general approach of the other attempts, as well the first few iterations of py5's architecture, looked very much like this:

1. py5 code calls the user's `settings()` function
2. py5 code calls Java code to initialize the Sketch window
3. py5 code calls the user's `setup()` function once
4. py5 code calls the user's `draw()` function in a loop

You can imagine implementing the critical `run_sketch()` function with code that looks very much like this:

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

In fact, if you look at the [initial commit of the py5 project](https://github.com/py5coding/py5generator/blob/636712b1c786eee67a6e1cbec9d59d2a25afb0e8/packages/py5generator/py5generator/templates/py5_init_template.py), you can see this is very close to what py5 actually did. (Note that this early version of py5 also used modified Processing Library code that was never checked in.) Observe that with this approach, Python is managing the animation thread. This approach could in fact create runable py5 Sketches. There were, however, many problems. Two of the most critical were:

* There's no way to trigger mouse and keyboard events
* The OpenGL renderers `P2D` and `P3D` always crashed

The problem with the OpenGL renderers had to do with something called a "context thread." Bottom line, only one thread is allowed to make OpenGL calls, and there is no way to make that thread be the Python thread this early version of py5 was using to call the user's `draw()` function in a loop. I tried everything I could think of to get OpenGL to work. As this work was done during the first month of COVID lockdowns, I had a lot of time to experiment. Nevertheless, this approach was not and could not be successful.

## How py5 Actually Works

The key insight behind py5 was to abandon the above approach and instead leverage JPype's ability to call Python from Java. Calling Java from Python is obviously important, but py5 wouldn't exist if JPype couldn't also make calls in the other direction, making calls *from* Java *to* Python.

The basic idea of py5 is to provide a Processing Sketch in Java that makes calls to Python to execute the user's code, which will in turn makes calls back to Java to access Processing Library functionality. This approach lets the Processing Library manage the Sketch's animation thread and the various OpenGL complexities. As far as the Processing Library is concerned, every py5 user is running the exact same Java code, `py5.core.Sketch`, found in [Sketch.java](https://github.com/py5coding/py5generator/blob/main/py5_jar/src/main/java/py5/core/Sketch.java). This `py5.core.Sketch` class is an instance of the Processing Library's `processing.core.PApplet`. The `py5.core.Sketch` code makes calls to Python to execute the user's code.

The basic steps of a running py5 Sketch look like this:

1. Python code creates an instance of the Java class `py5.core.Sketch`
2. Python code uses JPype to pass the instance of `py5.core.Sketch` to the Processing Library's `runSketch()` method
3. The Processing Library's `runSketch()` method launches the Sketch, opening the Sketch window and starting the animation thread
4. The Processing Library animation thread calls `py5.core.Sketch`'s `settings()`, `setup()`, and `draw()` methods
5. `py5.core.Sketch`'s `settings()`, `setup()`, and `draw()` methods make calls from Java to Python, instructing it to call the user's `settings()`, `setup()`, and `draw()` functions
6. The user's `settings()`, `setup()`, and `draw()` functions use py5's API, making calls to methods such as `size()`, `begin_shape()`, `convert_shape()`, `random()`, etc.
7. Calls to py5's API methods that leverage the Processing Library code such as `size()` and `begin_shape()` make corresponding calls to the Processing Library methods `size()`, `beginShape()`, etc.
8. Calls to py5's API methods that are implemented in Python such as `convert_shape()` and `random()` provide their functionality without using the Processing Library

This approach is quite a bit more complicated than the initial approach. However, the OpenGL renderers `P2D` and `P3D` work correctly. The mouse and keyboard event functions can also be triggered at the appropriate times.

Let's review py5's code in more detail, examining each of the above steps to understand how they work.

### 1. Create Instance of the Java Class `py5.core.Sketch`

The JPype library lets Python create instances of Java classes. It can create an instance of `py5.core.Sketch` with [`jpype.JClass`](https://jpype.readthedocs.io/en/latest/api.html#jpype.JClass).

There is a Python class called `Sketch` that py5 uses to manage the interaction with the Java `py5.core.Sketch` instance. The Java class is created in the Python `Sketch` class's `__init__()` method.

### 2. Pass `py5.core.Sketch` Instance to the Processing Library's `runSketch()` Method

The Python class `Sketch` has a method `_run_sketch()` that calls `processing.core.PApplet`'s `runSketch()` method.

In addition, the `_run_sketch()` method builds a bridge between the Java class `py5.core.Sketch` and Python. This bridge is the mechanism through which `py5.core.Sketch` makes calls back to Python to run the user defined functions. The bridge will also inform the `py5.core.Sketch` instance which user functions are defined so it knows which calls to make to Python and which to skip.

The `_run_sketch()` method also has some special code needed to get py5 to run on OSX.

### 3. Open Sketch Window and Start Animation Thread

In `processing.core.PApplet`'s `runSketch()` method, the Processing Library opens the Sketch window and starts the animation thread. The mechanism behind this is exactly the same as it is for any ordinary Processing Sketch.

### 4. Call `py5.core.Sketch`'s User Methods

The Processing Library framework will make calls to `py5.core.Sketch`'s `settings()`, `setup()`, and `draw()` methods. It will also call its mouse and keyboard methods.

`py5.core.Sketch` implements every possible user function. When called, it will check if there is a corresponding user function Python that needs to be executed. It gets the set of registered events that require calls to Python when the bridge between Python and Java is first created in step 2.

The code in each of `py5.core.Sketch`'s user functions looks very much like this:

```java
    if (success) {
      if (py5RegisteredEvents.contains("draw")) {
        success = py5Bridge.run_method("draw");
      } else {
        // do nothing
      }
    }
```

The boolean `success` variable is a flag that is set to `false` if an exception is thrown in Python. Error handling in py5 is complex; Java and Python cannot throw or handle each other's exceptions. What actually happens a Python exception is thrown is py5 will pause the `py5.core.Sketch`, making it look like the Sketch has been stopped. Pausing the Sketch and not stopping it by throwing a second exception in Java is necessary to ensure py5 can shutdown the Sketch without also shutting down the Java Virtual Machine.

### 5. Call User's Python functions from Java

### 6. Execute User Implemented Functions

### 7. API Methods that Leverage the Processing Library Code

Almost all of the code for py5's methods that leverage the Processing Library are written dynamically using py5generator's custom code template engine. The code for a typical function, minus the docstring, is very simple:

```python
    def rect(self, *args):
        return self._instance.rect(*args)
```

The `self._instance` attribute is the Java `py5.core.Sketch` instance created in step 1. Most of py5's methods are really simple wrappers of their underlying Processing Library methods.

Code written with py5generator's template engine can be customized with decorators or overriden with Python code. How this works is explained in more detail in [](developer/understanding_py5generator).

### 8. API Methods that are Implemented in Python

Not all of py5's methods are implemented in Java. API methods that draw to the Sketch window in some way must be implemented in Java. Generally, API methods that do not draw to the Sketch window are implemented in Python. This is done for performance reasons. Noteable exceptions are the noise functions.

## Additional Complexity for OSX
