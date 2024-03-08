# User Functions

User Functions are the code you write to create your py5 Sketches. There are many such functions available, each called by the py5 framework for different purposes. This page documents all of the user functions py5 supports.

## Animated Sketches

The foundation of animated py5 Sketches are the `setup()` and `draw()` user functions. The `setup()` function is called once when the Sketch begins running and the `draw()` function gets called repeatedly at (ideally) regular intervals.

Here is a straightforward example:

```python
def setup():
    py5.size(500, 500)
    py5.frame_rate(30)
    py5.rect_mode(py5.CENTER)
    py5.fill(255, 0, 0)


def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)
```

Here, the `setup()` function executes py5 commands that only need to be executed once. The [](/reference/sketch_size) method creates the Sketch window and sets the window's width and height. The [](/reference/sketch_frame_rate) method tells py5 the speed at which to call the `draw()` method. In this case, it will be called 30 times a second. And finally, the [](/reference/sketch_fill) method sets the shape fill color to red.

Code that you want to be called once should be placed in the `setup()` function. Typically this code will do things like load image assets and set drawing styles.

Code that you want to be called repeatedly should be placed in the `draw()` method. Typically this will be the code that draws to the Sketch window, as well as supporting Python code that determines what should be drawn.

Within the `setup()` function, the [](/reference/sketch_frame_count) property will be zero. In the `draw()` function, it will be one or more.

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
```

This Sketch is similar to the previous one except it will draw 10 random rectangles and then stop drawing.

For static Sketches, code that you would typically see in the `draw()` function is placed in the `setup()` function. This technique is useful for creating static images.

This kind of Sketch is very similar, but not the same as, [Static Mode](/content/py5_modes) Sketches.

## Settings

There is a little bit of magic taking place within the `setup()` function. Before executing your Sketch, py5 will split the user's `setup()` function into its own `settings()` and `setup()` functions. For our previous example, the new code would be:

```python
def setttings():
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

This coding magic is a feature of py5 because it is also a feature in Processing. This reduces the cognitive load placed on beginners learning to use py5. Instead of needing to write `settings()`, `setup()`, and `draw()` functions, beginners only need to write `setup()` and `draw()`.

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
```

The extra vertical space you see in these `settings()` and `setup()` functions is there to ensure that any exceptions thrown by the executed code will point to the correct line numbers in the user's `setup()` function. This completes the illusion of the user's `setup()` function.

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
```

The `if` statement in that function would prevent py5 from creating `settings()` and `setup()` functions. Instead, you would need to write the following code:

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
```

Finally, py5's [Class Mode](/content/py5_modes) does not support this code transformation magic. When using py5 in Class Mode code, you must write a `settings()` method that makes the call to [](/reference/sketch_size).

## Keyboard Events

`key_pressed()`
`key_typed()`
`key_released()`

Mention `Py5KeyEvent` objects and also [](/reference/sketch_key) and [](/reference/sketch_key_code)

[](/reference/sketch_is_key_pressed)

## Mouse Events

`mouse_clicked()`
`mouse_dragged()`
`mouse_moved()`
`mouse_entered()`
`mouse_exited()`
`mouse_pressed()`
`mouse_released()`
`mouse_wheel()`

Mention `Py5MouseEvent` objects and also [](/reference/sketch_is_mouse_pressed)

[](/reference/sketch_mouse_button), other mouse properties, don't usually need `Py5MouseEvent` objects

## Sketch Exiting Event

`exiting()`

Close resources such as OpenCV webcam

## Window Events

`window_moved()`
`window_resized()`

## Movie Events

Processing supports a `movieEvent()` user function to best work with the [Processing Video Library](https://processing.org/reference/libraries/video/index.html). Similarly, py5 provides a `movie_event()` function to aid users who wish to use the Processing Video Library with py5. This event function is called when a new movie frame is available.

Here is a basic example, playing a movie found at `"/tmp/movie.mov"`.

```python
from processing.video import Movie


def setup():
    py5.size(500, 500)
    global movie_player
    movie_player = Movie(py5.get_current_sketch(), "/tmp/movie.mov")
    movie_player.loop()


def movie_event(m):
    m.read()


def draw():
    if movie_player.isPlaying():
        py5.image(movie_player, 0, 0)


def exiting():
    movie_player.stop()
```

Here, the `exiting()` event function shuts down the movie player resources when the Sketch exits.

## Update Function

The `predraw_update()` function is unique to py5. It offers an opportunity to make a small improvement in a Sketch's frame rate. The main idea is to allow users to execute code inbetween calls to `draw()`. It isn't clear from the design of py5 (or Processing) that `draw()` is not immediately called after the previous call completes. There is a small gap, usually just a few milliseconds. Due to technical reasons about how py5 works, the Python interpreter is idle during this gap. The `predraw_update()` function gives you an opportunity to do something useful during the time that would otherwise be idle.

For a Sketch with performance problems, use of the `predraw_update()` function will typically improve the frame rate by 5 to 10%. When performance tuning a Sketch, moving some code from `draw()` to `predraw_update()` can be an easy change to make to get a small speed boost.

The most important thing to know about the `predraw_update()` function is that you should not make any calls to py5 methods. Many of them will not work correctly, and it is difficult to know which are safe to call without being familiar with the source code of both py5 and Processing.

Here is an example that uses  `predraw_update()` function.

```python
import numpy as np


def setup():
    py5.size(500, 500)
    py5.rect_mode(py5.CENTER)


def predraw_update():
    global x, y
    # perform slow calculations for x and y
    x, y = 500 * np.random.rand(2)


def draw():
    def rect(x, y, 10, 10)
```

If `np.random.rand(2)` was sufficiently slow, the Sketch would perform better with the code in `predraw_update()` and not `draw()`.

There is a [GitHub Discussion thread](https://github.com/py5coding/py5generator/discussions/408) created during the development and testing of this feature. Most of what is discussed there is too tedious to include here.

## Camera3D Support Functions

And finally, the `pre_draw()` and `post_draw()` user functions. These functions are only for Sketches using the Processing library [Camera3D](https://ixora.io/projects/camera-3D/) with py5; without Camera3D, py5 will never call them.

Support for these user functions are a part of py5 because the author of py5, [@hx2A](https://github.com/hx2A/), is also the author of Camera3D.

Camera3D alters Processing execution in such a way that the user's `draw()` function is called multiple times. The `pre_draw()` and `post_draw()` user functions will be called once, regardless of how many times `draw()` is called. Code that you want to be called once per frame should be included here.

Here is an example that uses `pre_draw()`:

```python
from camera3D import Camera3D

rot_x, rot_y, rot_z = 0, 0, 0


def setup():
    py5.size(400, 400, py5.P3D)
    camera3D = Camera3D(py5.get_current_sketch())
    camera3D.renderDefaultAnaglyph().setDivergence(1)


def pre_draw():
    global rot_x, rot_y, rot_z
    rot_x += 0.8
    rot_y += 0.3
    rot_z += 0.5


def draw():
    py5.translate(py5.width / 2, py5.height / 2, -200)
    py5.rotate_x(py5.radians(rot_x))
    py5.rotate_y(py5.radians(rot_y))
    py5.rotate_z(py5.radians(rot_z))

    py5.box(250)
```

Here, the `pre_draw()` function is used to update the rotation angles. If the rotation angles were updated in the `draw()` function, the angles would change between the anaglyph's right and left frames, impeding the 3D effect.

Again, the `pre_draw()` and `post_draw()` user functions are only for Camera3D users. If you would like to learn more about py5 and Camera3D, read [](/how_tos/use_camera3D).
