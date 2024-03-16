# User Functions

User Functions are the code you write to create your py5 Sketches. There are many such functions available, each called by the py5 framework for different purposes. This page documents all of the user functions py5 supports.

To execute each of the examples on this page, remember to first import py5.

```python
import py5
```

## Animated Sketches

The foundation of animated py5 Sketches are the `setup()` and `draw()` user functions. The `setup()` function is called once when the Sketch starts running and the `draw()` function gets called repeatedly at (ideally) regular intervals.

Here is a straightforward example:

```python
def setup():
    py5.size(500, 500)
    py5.frame_rate(30)
    py5.rect_mode(py5.CENTER)
    py5.fill(255, 0, 0)


def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)


py5.run_sketch()
```

Here, the `setup()` function executes py5 commands that only need to be executed once. The [](/reference/sketch_size) method creates the Sketch window and sets the window's width and height. The [](/reference/sketch_frame_rate) method tells py5 the speed at which to call the `draw()` method. In this case, it will be called 30 times a second. And finally, the [](/reference/sketch_fill) method sets the shape fill color to red.

Place code that you want to be called once in the `setup()` function. Typically this code will do things like load image assets and set drawing styles.

Code that you want to be called repeatedly should be placed in the `draw()` method. Typically this will be the code that draws to the Sketch window, as well as supporting Python code that determines what should be drawn.

Within the `setup()` function, the [](/reference/sketch_frame_count) property will be zero. In the `draw()` function, it will be one or more.

(content-user-functions-static-sketches)=
## Static Sketches

A py5 Sketch need not be animated; you can also create static Sketches by omitting the `draw()` function. For example:

```python
def setup():
    py5.size(500, 500)
    py5.frame_rate(30)
    py5.rect_mode(py5.CENTER)
    py5.fill(255, 0, 0)

    for _ in range(10):
        py5.rect(py5.random(500), py5.random(500), 10, 10)

    py5.save('/tmp/static_sketch.png')


py5.run_sketch()
```

This Sketch is similar to the previous one except it will draw 10 random rectangles and then stop drawing.

For static Sketches, code that you would typically see in the `draw()` function is placed in the `setup()` function. This technique is useful for creating static images.

This kind of Sketch is very similar, but not the same as, [Static Mode](content-py5-modes-static-mode) Sketches. With Static Mode Sketches, you write a series of py5 commands without a `setup()` function. Your Static Mode code is interpreted as if it was contained in a `setup()` function, and will achieve the same result as a Static Sketch described in this section.

And finally, there's a little bit of magic behind the `setup()` function that is being omitted here. If you are curious, find out more at [the bottom of this page](content-user_functions-settings-magic).

## Key Events

There are three key event functions that respond to inputs from a keyboard. The below list outlines the functions and their triggers.

* `key_pressed()` - after any key is pressed
* `key_typed()` - after any key is pressed and released
* `key_released()` - after any key is released

For each of these key event functions, py5 can pass a [](/reference/py5keyevent) object. If a key event function is defined with a single parameter, it will receive a `Py5KeyEvent` object; if defined with no parameters, the `Py5KeyEvent` object will be omitted.

The below example demonstrates all of the possible key event functions. One of the key event functions uses the `Py5KeyEvent` object to show you what that looks like.

Try running this example and experimenting with your keyboard to understand the events that trigger them.

```python
def setup():
    py5.size(500, 500, py5.P2D)


def key_pressed():
    py5.println("key pressed")


def key_typed(e):
    py5.println(f"key typed - key = {e.get_key()}")


def key_released():
    py5.println("key released")


py5.run_sketch()
```

Observe that this Sketch does not define a `draw()` user function. A `draw()` function is not necessary for key events to be triggered.

In addition to the above event functions, py5 also provides a few key-related properties for you to use. They are:

* [](/reference/sketch_is_key_pressed) - The `is_key_pressed` variable stores whether or not a keyboard button is currently being pressed.
* [](/reference/sketch_key) - The system variable `key` always contains the value of the most recent key on the keyboard that was used (either pressed or released). It will contain the constant `CODED` if it was a special key that can then be discriminated with `key_code`.
* [](/reference/sketch_key_code) - The variable `key_code` is used to detect special keys such as the arrow keys (`UP`, `DOWN`, `LEFT`, and `RIGHT`) as well as `ALT`, `CONTROL`, and `SHIFT`.

Between py5's key event functions, the `Py5KeyEvent` object, and the above properties, there are many ways for you to build a Sketch that responds to keyboard inputs.

## Mouse Events

There are many event functions that respond to inputs from a mouse. The complete list, and what triggers each of them, is below:

* `mouse_clicked()` - after any button is pressed and released
* `mouse_dragged()`- while the mouse is moving and any button is pressed
* `mouse_entered()` - when the mouse first enters the Sketch window area
* `mouse_exited()` - when the mouse exits the Sketch window area
* `mouse_moved()` - while the mouse is moving and no button is pressed
* `mouse_pressed()` - after any button is pressed and before it is released
* `mouse_released()` - after a pressed button is released
* `mouse_wheel()` - while the mouse wheel is rotating

Much like py5's key event functions, py5 can pass each of these mouse event functions a [](/reference/py5mouseevent) object. If a mouse event function is defined with a single parameter, it will receive the `Py5MouseEvent` object; if defined with no parameters, the `Py5MouseEvent` object will be omitted.

The example below demonstrates all of the supported mouse event functions. Some of the event functions use the `Py5MouseEvent` object and some do not, in an effort to show you both use cases.

Try running this example and experimenting with your mouse to understand the events that trigger them.

```python
def setup():
    py5.size(500, 500, py5.P2D)


def mouse_clicked(e):
    py5.println(f"mouse clicked - count = {e.get_count()}")


def mouse_dragged():
    py5.println("mouse dragged")


def mouse_moved():
    py5.println("mouse moved")


def mouse_entered(e):
    py5.println(f"mouse entered at time {e.get_millis()}")


def mouse_exited(e):
    py5.println(f"mouse exited at time {e.get_millis()}")


def mouse_pressed():
    py5.println("mouse pressed")


def mouse_released():
    py5.println("mouse released")


def mouse_wheel(e):
    direction = "down" if e.get_count() == 1 else "up"
    py5.println(f"mouse wheel rotating {direction}")


py5.run_sketch()
```

Like the previous example, this Sketch does not define a `draw()` user function. A `draw()` function is not necessary for mouse events to be triggered.

In addition to the above event functions, py5 also provides many mouse-related properties and methods for you to use. They are:

* [](/reference/sketch_is_mouse_pressed) - The `is_mouse_pressed` variable stores whether or not a mouse button is currently being pressed.
* [](/reference/sketch_mouse_button) - When a mouse button is pressed, the value of the system variable `mouse_button` is set to either `LEFT`, `RIGHT`, or `CENTER`, depending on which button is pressed.
* [](/reference/sketch_mouse_x) - The system variable `mouse_x` always contains the current horizontal coordinate of the mouse.
* [](/reference/sketch_mouse_y) - The system variable `mouse_y` always contains the current vertical coordinate of the mouse.
* [](/reference/sketch_pmouse_x) - The system variable `pmouse_x` always contains the horizontal position of the mouse in the frame previous to the current frame.
* [](/reference/sketch_pmouse_y) - The system variable `pmouse_y` always contains the vertical position of the mouse in the frame previous to the current frame.
* [](/reference/sketch_rmouse_x) - The current horizontal coordinate of the mouse after activating scale invariant drawing (activated with [](/reference/sketch_window_ratio)).
* [](/reference/sketch_rmouse_y) - The current vertical coordinate of the mouse after activating scale invariant drawing (activated with [](/reference/sketch_window_ratio)).

Using py5's mouse event functions, the `Py5MouseEvent` object, and the above properties and methods, you have many ways to create a Sketch that responds to mouse inputs.

## Sketch Exiting Event

The Sketch `exiting()` event function is called when the Sketch stops running and is shut down. This event is particularly useful for closing or releasing resources, such as a webcam.

```python
import cv2


def setup():
    global webcam
    py5.size(500, 500)
    py5.window_resizable(True)

    webcam = cv2.VideoCapture(0)


def draw():
    _, frame = webcam.read()
    img = py5.create_image_from_numpy(frame, bands="BGR")
    py5.image(img, 0, 0, py5.width, py5.height)


def exiting():
    webcam.release()


py5.run_sketch()
```

In the above example, the Sketch uses OpenCV to connect to a webcam. When py5 calls the `exiting()` event function, it will release the webcam and make it available to other processes.

## Window Events

The `window_moved()` and `window_resized()` event functions are called in response to changes to the Sketch window. If the user moves the Sketch window, the `window_moved()` event function will be called. If the Sketch window is resizable and the user resizes it, the `window_resized()` event function will be called.

Below is a basic example demonstrating both functions.

```python
def setup():
    py5.size(500, 500)
    py5.window_resizable(True)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text_size(50)
    py5.fill(0)


def window_moved():
    py5.println('Sketch window moved')


def window_resized():
    py5.println('Sketch window resized')


def draw():
    msg = f'({py5.width}, {py5.height})'
    py5.text(msg, py5.width / 2, py5.height / 2)


py5.run_sketch()
```

These `window_moved()` and `window_resized()` event functions will print messages when they are called.

## Movie Events

Processing supports a `movieEvent()` user function to best work with the [Processing Video Library](https://processing.org/reference/libraries/video/index.html). Similarly, py5 provides a `movie_event()` function to aid users who wish to use the Processing Video Library with py5. This event function is called when a new movie frame is available.

To use the [Processing Video Library](https://processing.org/reference/libraries/video/index.html) you must download it and make it available to py5. You can download the library by finding the [video.zip](https://github.com/processing/processing-video/releases/download/latest/video.zip) link on the library's [GitHub Releases](https://github.com/processing/processing-video/releases) page. Unzip the zip file and put the contents in a sub-directory called `jars`.

When the `movie_event()` function is called, it will always be passed the Processing Video Library Movie object as a parameter.

Here is a basic example, playing a video file `"movie.mov"`.

```python
from processing.video import Movie


def setup():
    py5.size(500, 500)
    global movie_player
    movie_player = Movie(py5.get_current_sketch(), "movie.mov")
    movie_player.loop()


def movie_event(m):
    m.read()


def draw():
    if movie_player.isPlaying():
        py5.image(movie_player, 0, 0)


def exiting():
    movie_player.stop()


py5.run_sketch()
```

Here, the `exiting()` event function shuts down the movie player resources when the Sketch exits.

(content-user-functions-update_functon)=
## Update Function

The `predraw_update()` function is unique to py5. It offers an opportunity to make a small improvement in a Sketch's frame rate. The main idea is to allow users to execute code in-between calls to `draw()`. It isn't clear from the design of py5 (or Processing) that `draw()` is not immediately called after the previous call completes. There is a small gap, usually just a few milliseconds. Due to technical reasons about how py5 works, the Python interpreter is idle during this gap. The `predraw_update()` function gives you an opportunity to do something useful during the time that Python would otherwise be idle. For most use cases, a few milliseconds is too trivial bother with. But for those situations where a few millisconds matters, the `predraw_update()` function can help.

For a Sketch with performance problems, use of the `predraw_update()` function will typically improve the frame rate by 5 to 10%. When performance tuning a Sketch, moving some code from `draw()` to `predraw_update()` can be an easy change to make that provides a small speed boost.

The most important thing to know about the `predraw_update()` function is that it should not make any calls to py5 methods. Many of them will not work correctly. It is difficult to know which are safe to call without being familiar with the source code of both py5 and Processing.

Here is an example that uses a `predraw_update()` function.

```python
import numpy as np


def setup():
    py5.size(500, 500)
    py5.rect_mode(py5.CENTER)


def predraw_update():
    global x, y
    # pretend this is a slow calculation for x and y
    x, y = 500 * np.random.rand(2)


def draw():
    def rect(x, y, 10, 10)


py5.run_sketch()
```

If `np.random.rand(2)` was sufficiently slow, the Sketch would perform better with that code in `predraw_update()` and not `draw()`.

There is a [GitHub Discussion thread](https://github.com/py5coding/py5generator/discussions/408) created during the development and testing of this feature. Most of what is discussed there is too tedious to include here.

## Camera3D Support Functions

And finally, the `pre_draw()` and `post_draw()` user functions. These functions are only for Sketches that use the Processing library [Camera3D](https://ixora.io/projects/camera-3D/) with py5; without Camera3D, py5 will never call them.

Support for these user functions are a part of py5 because the author of py5, [@hx2A](https://github.com/hx2A/), is also the author of Camera3D.

Like the [Processing Video Library](https://processing.org/reference/libraries/video/index.html), you must download Camera3D and make it available to py5. You can download the library from [https://ixora.io/downloads/camera3D/Camera3D.zip](https://ixora.io/downloads/camera3D/Camera3D.zip). Unzip the contents and put it in a `jars` sub-directory.

Camera3D alters Processing execution in such a way that the user's `draw()` function is called multiple times. The `pre_draw()` and `post_draw()` user functions will be called once, regardless of how many times `draw()` is called. Code that you want to be called once per frame should be included here.

Here is an example that uses both `pre_draw()` and `post_draw()`:

```python
from camera3D import Camera3D


rot_x, rot_y, rot_z = 0, 0, 0


def setup():
    py5.size(400, 400, py5.P3D)
    py5.stroke_weight(8)
    py5.text_size(16)
    camera3D = Camera3D(py5.get_current_sketch())
    camera3D.renderDefaultAnaglyph().setDivergence(2)


def pre_draw():
    global rot_x, rot_y, rot_z
    rot_x += 0.8
    rot_y += 0.3
    rot_z += 0.5


def draw():
    py5.fill(255)
    py5.translate(py5.width / 2, py5.height / 2, -200)
    py5.rotate_x(py5.radians(rot_x))
    py5.rotate_y(py5.radians(rot_y))
    py5.rotate_z(py5.radians(rot_z))
    py5.box(250)


def post_draw():
    py5.fill(0)
    py5.text("made with Camera3D", 225, 375)


py5.run_sketch()
```

Here, the `pre_draw()` function is used to update the rotation angles. If the rotation angles were updated in the `draw()` function, the angles would change between the anaglyph's right and left frames, interfering with the 3D effect. The `post_draw()` function adds a text label that is not altered by Camera3D's anaglyph algorithm, as the label would be if it were drawn in the `draw()` function.

Again, the `pre_draw()` and `post_draw()` user functions are only for Camera3D users. If you would like to learn more about py5 and Camera3D, read [](/how_tos/use_camera3D).

(content-user_functions-settings-magic)=
## Settings Magic

There is a little bit of magic taking place within the previously discussed `setup()` function. Before executing your Sketch, py5 will split the user's `setup()` function into its own `settings()` and `setup()` functions. To illustrate, consider this example `setup()` function from the [](content-user-functions-static-sketches) section of this page:

```python
def setup():
    py5.size(500, 500)
    py5.frame_rate(30)
    py5.rect_mode(py5.CENTER)
    py5.fill(255, 0, 0)

    for _ in range(10):
        py5.rect(py5.random(500), py5.random(500), 10, 10)

    py5.save('/tmp/static_sketch.png')
```

This `setup()` function will be split into this:

```python
def settings():
    py5.size(500, 500)


def setup():

    py5.frame_rate(30)
    py5.rect_mode(py5.CENTER)
    py5.fill(255, 0, 0)

    for _ in range(10):
        py5.rect(py5.random(500), py5.random(500), 10, 10)

    py5.save('/tmp/static_sketch.png')
```

The call to [](/reference/sketch_size) is moved to a separate `settings()` function. The rest of the code remained in `setup()`.

This coding magic is a feature of py5 because it is also a feature in Processing. This reduces the cognitive load placed on beginners learning to use py5. Instead of needing to write the three functions `settings()`, `setup()`, and `draw()`, beginners only need to define `setup()` and `draw()`.

This code transformation is facilitated by a few organizational rules about how the user must write their `setup()` function. The key rule is that the call to [](/reference/sketch_size) must be first, before the calls to methods like [](/reference/sketch_frame_rate) and [](/reference/sketch_fill). The other special methods that must be used at the beginning of `setup()`, before other code, are [](/reference/sketch_full_screen), [](/reference/sketch_smooth), [](/reference/sketch_no_smooth), and [](/reference/sketch_pixel_density). When the user's `setup()` function is organized in this way, py5 is able to reliably separate the code and divide it into two new functions.

The code separation process can manage the inclusion of global statements, comments, and docstrings. The recommended coding style for Python is to place global statements at the very beginning of a function or method, and py5 allows for that in user `setup()` functions. Here is an example that demonstrates this:

```python
def setup():
    # user setup function
    global shape
    py5.size(500, 500)
    py5.frame_rate(30)
    py5.rect_mode(py5.CENTER)
    shape = py5.create_shape(py5.RECT, 0, 0, 50, 50)


def draw():
    py5.background(204)
    py5.shape(shape, py5.mouse_x, py5.mouse_y)


py5.run_sketch()
```

For this example, the transformed code would be:

```python
def settings():
    # user setup function

    py5.size(500, 500)


def setup():

    global shape

    py5.frame_rate(30)
    py5.rect_mode(py5.CENTER)
    shape = py5.create_shape(py5.RECT, 0, 0, 50, 50)


def draw():
    py5.background(204)
    py5.shape(shape, py5.mouse_x, py5.mouse_y)


py5.run_sketch()
```

The transformed code is the actual code executed by py5, not the code as written by the user.

The extra vertical space you see in these `settings()` and `setup()` functions is there to ensure that any exceptions thrown by the executed code will point to the correct line numbers in the user's `setup()` function. This facilitates the illusion of the user's `setup()` function as the code that is actually executed by py5.

There are times when you might want to define the `settings()` function yourself and not rely on py5's transformation code. If your code would trip up py5's code transformation abilities, you will need to do this. For example, consider the following `setup()` function that optionally calls [](/reference/sketch_size) or [](/reference/sketch_full_screen).

```python
USE_FULL_SCREEN = True


def setup():
    if USE_FULL_SCREEN:
        py5.full_screen()
    else:
        py5.size(500, 500)

    py5.frame_rate(30)
    py5.rect_mode(py5.CENTER)
    py5.fill(255, 0, 0)


# do not run this code
# py5.run_sketch()
```

The `if` statement in that function would prevent py5 from properly creating `settings()` and `setup()` functions, and py5 would not execute the Sketch. Instead, you would need to write the following code:

```python
USE_FULL_SCREEN = True


def settings():
    if USE_FULL_SCREEN:
        py5.full_screen()
    else:
        py5.size(500, 500)


def setup():
    py5.frame_rate(30)
    py5.rect_mode(py5.CENTER)
    py5.fill(255, 0, 0)


py5.run_sketch()
```

Finally, py5's [Class Mode](content-py5-modes-class-mode) does not support this code transformation magic. When using py5 in Class Mode code, you must write a `settings()` method that makes the call to [](/reference/sketch_size).
